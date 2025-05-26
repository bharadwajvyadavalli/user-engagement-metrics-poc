"""
Data Processor for User Engagement Metrics POC
"""

import pandas as pd
import json
from datetime import datetime

class DataProcessor:
    def process_csv(self, file_path):
        """Load and process the CSV file"""
        # Load CSV
        df = pd.read_csv(file_path)
        
        # Parse JSON messages and extract role/content
        processed_data = []
        
        for _, row in df.iterrows():
            try:
                message = json.loads(row['Message'])
                processed_data.append({
                    'ID': row['ID'],
                    'Event_Date': pd.to_datetime(row['Event Date']),
                    'User_ID': row['User ID'],
                    'Thread_ID': row['Thread ID'],
                    'Role': message.get('role', ''),
                    'Content': message.get('content', '')
                })
            except (json.JSONDecodeError, KeyError):
                continue  # Skip invalid rows
        
        df_processed = pd.DataFrame(processed_data)
        
        # Add derived columns
        df_processed['Date'] = df_processed['Event_Date'].dt.date
        df_processed['Hour'] = df_processed['Event_Date'].dt.hour
        df_processed['Month'] = df_processed['Event_Date'].dt.to_period('M')
        
        # Sort by date
        df_processed = df_processed.sort_values('Event_Date')
        
        return df_processed