"""
Simple Data Processor for User Engagement Metrics
"""

import pandas as pd
import json
from datetime import datetime

class DataProcessor:
    def process_csv(self, file_path):
        """Load and process the CSV file"""
        df = pd.read_csv(file_path)
        processed_data = []
        
        for _, row in df.iterrows():
            try:
                # Parse JSON message
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
                    'Month': event_date.to_period('M')
                })
            except:
                continue  # Skip invalid rows
        
        df_processed = pd.DataFrame(processed_data)
        return df_processed.sort_values('Event_Date')
