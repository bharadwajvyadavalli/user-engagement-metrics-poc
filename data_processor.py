"""
Data Processor and Generator for User Engagement Metrics
"""

import pandas as pd
import json
import numpy as np
import random
from datetime import datetime, timedelta

class DataProcessor:
    def process_csv(self, file_path):
        """Load and process CSV file"""
        df = pd.read_csv(file_path)
        processed_data = []

        for _, row in df.iterrows():
            try:
                message = json.loads(row['Message'])
                event_date = pd.to_datetime(row['Event Date'])

                processed_data.append({
                    'ID': row['ID'],
                    'Event_Date': event_date,
                    'User_ID': row['User ID'],
                    'Thread_ID': row['Thread ID'],
                    'Role': message.get('role', ''),
                    'Content': message.get('content', ''),
                    'Date': event_date.date(),
                    'Hour': event_date.hour,
                    'Month': event_date.to_period('M'),
                    'Feature': self._extract_feature(message.get('content', ''))
                })
            except:
                continue

        return pd.DataFrame(processed_data).sort_values('Event_Date')

    def _extract_feature(self, content):
        """Extract feature from content"""
        content_lower = content.lower()
        keywords = {
            'search': ['search', 'find', 'lookup', 'locate'],
            'analysis': ['analyze', 'analysis', 'report', 'trend', 'insight'],
            'export': ['export', 'download', 'save', 'pdf', 'excel'],
            'chat': ['hello', 'hi', 'chat', 'talk', 'conversation'],
            'help': ['help', 'support', 'assistance', 'guide', 'how'],
            'api': ['api', 'integration', 'endpoint'],
            'reporting': ['report', 'dashboard', 'kpi', 'summary'],
            'automation': ['automate', 'schedule', 'alert', 'workflow']
        }

        for feature, words in keywords.items():
            if any(word in content_lower for word in words):
                return feature
        return 'other'

class DataGenerator:
    def __init__(self):
        self.user_types = {
            'new': {'weight': 0.3, 'sessions': (1, 3), 'queries': (1, 4), 'retention': 0.6},
            'casual': {'weight': 0.4, 'sessions': (2, 6), 'queries': (1, 6), 'retention': 0.7},
            'power': {'weight': 0.3, 'sessions': (3, 10), 'queries': (2, 12), 'retention': 0.85}
        }

        self.templates = {
            'help': ["How do I get started?", "I need help", "Can you guide me?"],
            'search': ["Find my documents", "Search for reports", "Locate data"],
            'analysis': ["Analyze trends", "Generate insights", "Show patterns"],
            'export': ["Export to PDF", "Download report", "Save as Excel"],
            'chat': ["Hello there!", "Good morning", "Quick question"],
            'api': ["API documentation", "How to integrate?", "Rate limits"],
            'reporting': ["Monthly dashboard", "Generate report", "KPI summary"],
            'automation': ["Automate workflow", "Schedule reports", "Set alerts"]
        }

    def generate(self, users=500, days=90, scenario='standard'):
        """Generate realistic chatbot data with different scenarios"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        # Adjust parameters based on scenario
        params = self._get_scenario_params(scenario)

        # Create users
        user_list = []
        for i in range(users):
            user_type = np.random.choice(list(self.user_types.keys()),
                                       p=[ut['weight'] for ut in self.user_types.values()])
            join_date = start_date + timedelta(days=int(np.random.exponential(days/4)))
            user_list.append({
                'id': f"user_{i+1:04d}",
                'type': user_type,
                'join_date': max(join_date, start_date),
                'activity': random.uniform(0.5, 1.0) * params['activity_boost']
            })

        # Generate interactions
        interactions = []
        msg_id = 1

        for current_date in pd.date_range(start_date, end_date, freq='D'):
            for user in user_list:
                if current_date.date() < user['join_date'].date():
                    continue

                # Activity probability with scenario modifiers
                days_since_join = (current_date.date() - user['join_date'].date()).days
                base_prob = self.user_types[user['type']]['retention']
                decay = params['decay_rate'] ** days_since_join
                weekend_factor = 0.3 if current_date.weekday() >= 5 else 1.0

                activity_prob = base_prob * decay * user['activity'] * weekend_factor

                if random.random() < activity_prob:
                    sessions = random.randint(0, params['max_sessions'])

                    for session in range(sessions):
                        thread_id = f"thread_{msg_id}_{session}"
                        session_time = self._get_session_time(current_date, params)

                        queries = random.randint(*self.user_types[user['type']]['queries'])
                        for q in range(queries):
                            feature = self._select_feature(user['type'], params)

                            # Human message
                            interactions.append({
                                'ID': msg_id,
                                'Event Date': session_time.strftime('%Y-%m-%d %H:%M:%S'),
                                'User ID': user['id'],
                                'Thread ID': thread_id,
                                'Message': json.dumps({
                                    'role': 'human',
                                    'content': random.choice(self.templates[feature])
                                })
                            })
                            msg_id += 1
                            session_time += timedelta(seconds=random.randint(5, 60))

                            # AI response
                            interactions.append({
                                'ID': msg_id,
                                'Event Date': session_time.strftime('%Y-%m-%d %H:%M:%S'),
                                'User ID': user['id'],
                                'Thread ID': thread_id,
                                'Message': json.dumps({
                                    'role': 'ai',
                                    'content': f"I can help you with {feature}. Here's the information you need."
                                })
                            })
                            msg_id += 1
                            session_time += timedelta(seconds=random.randint(30, 180))

        return pd.DataFrame(interactions)

    def _get_scenario_params(self, scenario):
        """Get parameters for different data scenarios"""
        scenarios = {
            'standard': {
                'activity_boost': 1.0,
                'decay_rate': 0.995,
                'max_sessions': 2,
                'business_hours_weight': 0.7,
                'feature_distribution': 'balanced'
            },
            'high_engagement': {
                'activity_boost': 1.5,
                'decay_rate': 0.998,
                'max_sessions': 4,
                'business_hours_weight': 0.6,
                'feature_distribution': 'power_features'
            },
            'low_retention': {
                'activity_boost': 0.7,
                'decay_rate': 0.990,
                'max_sessions': 1,
                'business_hours_weight': 0.8,
                'feature_distribution': 'basic_features'
            },
            'rapid_growth': {
                'activity_boost': 1.2,
                'decay_rate': 0.997,
                'max_sessions': 3,
                'business_hours_weight': 0.5,
                'feature_distribution': 'diverse'
            }
        }
        return scenarios.get(scenario, scenarios['standard'])

    def _get_session_time(self, date, params):
        """Generate session time based on scenario"""
        if random.random() < params['business_hours_weight']:
            hour = random.randint(9, 17)
        else:
            hour = random.choice(list(range(0, 9)) + list(range(18, 24)))

        return date.replace(hour=hour, minute=random.randint(0, 59), second=random.randint(0, 59))

    def _select_feature(self, user_type, params):
        """Select feature based on user type and scenario"""
        distribution = params['feature_distribution']

        if distribution == 'power_features' and user_type == 'power':
            return random.choice(['analysis', 'api', 'automation', 'reporting'])
        elif distribution == 'basic_features':
            return random.choice(['help', 'chat', 'search'])
        else:
            return random.choice(list(self.templates.keys()))