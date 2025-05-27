"""
Simple Metrics Calculator for User Engagement
"""

import pandas as pd
from datetime import timedelta

class MetricsCalculator:
    def __init__(self):
        self.feature_keywords = {
            "search": ["search", "find", "lookup"],
            "analysis": ["analyze", "analysis", "report"], 
            "export": ["export", "download", "save"],
            "chat": ["chat", "conversation", "talk"],
            "help": ["help", "support", "assistance"]
        }
    
    def calculate_all_metrics(self, df):
        """Calculate all engagement metrics"""
        metrics = {}
        
        # 1. Daily Active Users (DAU)
        dau_data = df.groupby('Date')['User_ID'].nunique()
        metrics['avg_dau'] = dau_data.mean()
        metrics['dau_data'] = {str(k): v for k, v in dau_data.to_dict().items()}
        
        # 2. Monthly Active Users (MAU)
        mau_data = df.groupby('Month')['User_ID'].nunique()
        metrics['avg_mau'] = mau_data.mean()
        metrics['mau_data'] = {str(k): v for k, v in mau_data.to_dict().items()}
        
        # 3. Session Duration
        session_durations = []
        for thread_id in df['Thread_ID'].unique():
            thread_data = df[df['Thread_ID'] == thread_id]
            if len(thread_data) > 1:
                duration = (thread_data['Event_Date'].max() - 
                           thread_data['Event_Date'].min()).total_seconds() / 60
                session_durations.append(duration)
        
        metrics['session_durations'] = session_durations
        metrics['avg_session_duration'] = sum(session_durations) / len(session_durations) if session_durations else 0
        
        # 4. Session Frequency (Sessions per User)
        sessions_per_user = df.groupby('User_ID')['Thread_ID'].nunique()
        metrics['avg_sessions_per_user'] = sessions_per_user.mean()
        
        # 5. Queries per Session
        human_messages = df[df['Role'] == 'human']
        queries_per_session = human_messages.groupby('Thread_ID').size()
        metrics['avg_queries_per_session'] = queries_per_session.mean()
        
        # 6. Feature Usage
        feature_usage = {}
        for feature, keywords in self.feature_keywords.items():
            count = 0
            for content in human_messages['Content']:
                if any(keyword.lower() in content.lower() for keyword in keywords):
                    count += 1
            feature_usage[feature] = count
        metrics['feature_usage'] = feature_usage
        
        # 7. Retention Rate
        first_dates = df.groupby('User_ID')['Date'].min()
        all_dates = df.groupby('User_ID')['Date'].apply(set)
        
        retention_rates = {}
        for period in [1, 7, 30]:
            retained = 0
            total = len(first_dates)
            
            for user_id, first_date in first_dates.items():
                target_date = first_date + timedelta(days=period)
                if any(date >= target_date for date in all_dates[user_id]):
                    retained += 1
            
            retention_rates[f'{period}_day'] = retained / total if total > 0 else 0
        
        metrics['retention_rates'] = retention_rates
        
        # 8. Churn Rate
        last_dates = df.groupby('User_ID')['Date'].max()
        latest_date = df['Date'].max()
        churn_threshold = latest_date - timedelta(days=30)
        
        churned = (last_dates < churn_threshold).sum()
        metrics['churn_rate'] = churned / len(last_dates) if len(last_dates) > 0 else 0
        
        return metrics
