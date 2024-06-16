import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

class DataFrameGenerator:
    def __init__(self, num_records, id_range, start_date_str, end_date_str, min_duration, max_duration, now_time_str):
        self.num_records = num_records
        self.id_range = id_range
        self.start_date = datetime.strptime(start_date_str, '%Y/%m/%d %H:%M:%S')
        self.end_date = datetime.strptime(end_date_str, '%Y/%m/%d %H:%M:%S')
        self.min_duration = min_duration
        self.max_duration = max_duration
        self.now_time = datetime.strptime(now_time_str, '%Y/%m/%d %H:%M:%S')

    def generate_data(self):
        data = []
        for _ in range(self.num_records):
            start_time = self.start_date + (self.end_date - self.start_date) * random.random()
            duration = self.min_duration + (self.max_duration - self.min_duration) * random.random()
            end_time = start_time + duration
            record = {
                "ID": random.choice(self.id_range),
                "start_time": start_time,
                "end_time": end_time
            }
            data.append(record)
        return pd.DataFrame(data)

    def process_data(self, df):
        # Filter by start_time < now_time
        df_filtered = df[df['start_time'] < self.now_time].copy()
        
        # Adjust end_time for records where end_time > now_time
        df_filtered.loc[df_filtered['end_time'] > self.now_time, 'end_time'] = self.now_time
        
        # Add 'interval' column
        df_filtered['interval'] = df_filtered['end_time'] - df_filtered['start_time']
        
        # Sort by start_time
        df_sorted = df_filtered.sort_values(by="start_time").reset_index(drop=True)
        
        return df_sorted

if __name__ == '__main__':
    # Parameters
    num_records = 20
    id_range = range(100, 200)
    start_date_str = '2022/08/01 00:00:00'
    end_date_str = '2022/08/01 12:00:00'
    min_duration = timedelta(minutes=30)
    max_duration = timedelta(hours=3)
    now_time_str = '2022/08/01 10:11:00'
    # now_time_str = '2022/08/02 10:00:00'

    generator = DataFrameGenerator(num_records, id_range, start_date_str, end_date_str, min_duration, max_duration, now_time_str)
    df = generator.generate_data()
    df_processed = generator.process_data(df)
    
    # Display the processed DataFrame
    print(df_processed)
