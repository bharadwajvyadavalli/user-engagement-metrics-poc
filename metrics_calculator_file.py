"""
Metrics Calculator for User Engagement POC
"""

import pandas as pd
from datetime import timedelta
import config

class MetricsCalculator:
    def calculate_all_metrics(self, df):
        """Calculate all engagement metrics"""
        metrics = {}
        
        # DAU/MAU
        dau_data = df.groupby('Date')['User_ID'].nunique()
        mau_data = df.groupby('Month')['User_ID'].nunique()
        
        metrics['dau_data'] = dau_data
        metrics['mau_data'] = mau_data
        metrics['avg_dau'] = dau_data.mean()
        metrics['avg_mau'] = mau_data.mean()
        
        # Session Duration
        session_durations = []
        for thread_id in df['Thread_ID'].unique():
            thread_data = df[df['Thread_ID'] == thread_id]
            if len(thread_data) > 1:
                duration_minutes = (thread_data['Event_Date'].max() - 
                                  thread_data['Event_Date'].min()).total_seconds() / 60
                session_durations.append(duration_minutes)
        
        metrics['session_durations'] = session_durations
        metrics['avg_session_duration'] = sum(session_durations) / len(session_durations) if session_durations else 0
        
        # Session Frequency
        user_sessions = df.groupby('User_ID')['Thread_ID'].nunique()
        metrics['avg_sessions_per_user'] = user_sessions.mean()
        
        # Queries per Session
        human_messages = df[df['Role'] == 'human']
        queries_per_session = human_messages.groupby('Thread_ID').size()
        metrics['avg_queries_per_session'] = queries_per_session.mean()
        
        # Feature Usage
        feature_usage = {}
        for feature, keywords in config.FEATURE_KEYWORDS.items():
            count = 0
            for content in human_messages['Content']:
                if any(keyword.lower() in content.lower() for keyword in keywords):
                    count += 1
            feature_usage[feature] = count
        
        metrics['feature_usage'] = feature_usage
        
        # Retention Rate (simplified)
        first_dates = df.groupby('User_ID')['Date'].min()
        retention_rates = {}
        
        for period in config.RETENTION_PERIODS:
            retained_users = 0
            total_users = len(first_dates)
            
            for user_id, first_date in first_dates.items():
                target_date = first_date + timedelta(days=period)
                user_dates = df[df['User_ID'] == user_id]['Date'].unique()
                
                if any(date >= target_date for date in user_dates):
                    retained_users += 1
            
            retention_rates[f'{period}_day'] = retained_users / total_users if total_users > 0 else 0
        
        metrics['retention_rates'] = retention_rates
        
        # Churn Rate
        last_dates = df.groupby('User_ID')['Date'].max()
        latest_date = df['Date'].max()
        churn_threshold = latest_date - timedelta(days=config.CHURN_THRESHOLD_DAYS)
        
        churned_users = sum(1 for date in last_dates if date < churn_threshold)
        metrics['churn_rate'] = churned_users / len(last_dates) if len(last_dates) > 0 else 0
        
        return metrics