"""
Enhanced Data Processor for User Engagement Metrics
"""

import pandas as pd
import json
import numpy as np
import random
from datetime import datetime, timedelta


class DataProcessor:
    def process_csv(self, file_path):
        """Load and process the CSV file with enhanced features"""
        df = pd.read_csv(file_path)
        processed_data = []

        for _, row in df.iterrows():
            try:
                # Parse JSON message
                message = json.loads(row['Message'])
                event_date = pd.to_datetime(row['Event Date'])

                processed_row = {
                    'ID': row['ID'],
                    'Event_Date': event_date,
                    'User_ID': row['User ID'],
                    'Thread_ID': row['Thread ID'],
                    'Role': message.get('role', ''),
                    'Content': message.get('content', ''),
                    'Date': event_date.date(),
                    'Hour': event_date.hour,
                    'Month': event_date.to_period('M'),
                    'Weekday': event_date.weekday(),
                    'Is_Weekend': event_date.weekday() >= 5
                }

                # Extract feature from content
                processed_row['Feature'] = self._extract_feature(processed_row['Content'])

                processed_data.append(processed_row)
            except:
                continue  # Skip invalid rows

        df_processed = pd.DataFrame(processed_data)
        return df_processed.sort_values('Event_Date')

    def _extract_feature(self, content):
        """Extract feature type from message content"""
        content_lower = content.lower()

        feature_keywords = {
            'search': ['search', 'find', 'lookup', 'locate'],
            'analysis': ['analyze', 'analysis', 'report', 'trend', 'insight'],
            'export': ['export', 'download', 'save', 'pdf', 'excel'],
            'chat': ['hello', 'hi', 'chat', 'talk', 'conversation'],
            'help': ['help', 'support', 'assistance', 'guide', 'how'],
            'api': ['api', 'integration', 'endpoint'],
            'reporting': ['report', 'dashboard', 'kpi', 'summary'],
            'automation': ['automate', 'schedule', 'alert', 'workflow']
        }

        for feature, keywords in feature_keywords.items():
            if any(keyword in content_lower for keyword in keywords):
                return feature

        return 'other'


class DataGenerator:
    """Simple data generator for realistic chatbot interactions"""

    def __init__(self):
        self.user_types = {
            'new': {'weight': 0.3, 'sessions': (1, 3), 'queries': (1, 4)},
            'casual': {'weight': 0.4, 'sessions': (2, 6), 'queries': (1, 6)},
            'power': {'weight': 0.3, 'sessions': (3, 10), 'queries': (2, 12)}
        }

        self.messages = {
            'help': ["How do I get started?", "I need help with this feature", "Can you guide me?"],
            'search': ["Find my documents", "Search for quarterly reports", "Locate customer data"],
            'analysis': ["Analyze sales trends", "Generate insights", "Show me patterns"],
            'export': ["Export to PDF", "Download this report", "Save as Excel"],
            'chat': ["Hello there!", "Good morning", "Quick question"],
            'api': ["API documentation please", "How to integrate?", "Rate limits info"],
            'reporting': ["Monthly dashboard", "Generate KPI report", "Executive summary"],
            'automation': ["Automate this workflow", "Schedule reports", "Set up alerts"]
        }

    def generate_data(self, num_users=500, num_days=60):
        """Generate realistic chatbot interaction data"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=num_days)

        interactions = []
        msg_id = 1

        # Generate users
        users = []
        for i in range(num_users):
            user_type = np.random.choice(list(self.user_types.keys()),
                                         p=[ut['weight'] for ut in self.user_types.values()])
            users.append({
                'id': f"user_{i + 1:04d}",
                'type': user_type,
                'join_date': start_date + timedelta(days=random.randint(0, num_days // 2))
            })

        # Generate interactions day by day
        for current_date in pd.date_range(start_date, end_date, freq='D'):
            for user in users:
                # Skip if user hasn't joined yet
                if current_date.date() < user['join_date'].date():
                    continue

                # Determine if user is active (decreasing probability over time)
                days_since_join = (current_date.date() - user['join_date'].date()).days
                activity_prob = 0.7 * (0.995 ** days_since_join)

                # Reduce activity on weekends
                if current_date.weekday() >= 5:
                    activity_prob *= 0.3

                if random.random() < activity_prob:
                    # User is active today - generate sessions
                    num_sessions = random.randint(0, 2)

                    for session in range(num_sessions):
                        thread_id = f"thread_{msg_id}_{session}"

                        # Random time (biased toward business hours)
                        if random.random() < 0.7:
                            hour = random.randint(9, 17)
                        else:
                            hour = random.choice(list(range(0, 9)) + list(range(18, 24)))

                        session_time = current_date.replace(
                            hour=hour,
                            minute=random.randint(0, 59),
                            second=random.randint(0, 59)
                        )

                        # Generate conversation
                        user_config = self.user_types[user['type']]
                        num_queries = random.randint(*user_config['queries'])

                        for q in range(num_queries):
                            feature = random.choice(list(self.messages.keys()))

                            # Human message
                            interactions.append({
                                'ID': msg_id,
                                'Event Date': session_time.strftime('%Y-%m-%d %H:%M:%S'),
                                'User ID': user['id'],
                                'Thread ID': thread_id,
                                'Message': json.dumps({
                                    'role': 'human',
                                    'content': random.choice(self.messages[feature])
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
                                    'content': f"I can help you with {feature}. Here's what you need to know."
                                })
                            })
                            msg_id += 1
                            session_time += timedelta(seconds=random.randint(30, 180))

        return pd.DataFrame(interactions)