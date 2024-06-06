"""
pandas DataFrame列追加、
時間計算
時間の型変換
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Initial setup for DataFrame
data = {
    'number': [1, 2, 3, 4, 5, 6],
    'begin_time': [None] * 6,
    'end_time': [None] * 6
}

df = pd.DataFrame(data)

# Update begin_time and end_time to satisfy the conditions
# Starting with a random datetime for the first row
initial_datetime = datetime.now() - timedelta(days=np.random.randint(1, 10))
df.at[0, 'begin_time'] = initial_datetime
df.at[0, 'end_time'] = initial_datetime + timedelta(minutes=np.random.randint(30, 121))

# Subsequent rows: begin_time is random 0 to 60 minutes after previous end_time
for i in range(1, 6):
    next_begin_time = df.at[i-1, 'end_time'] + timedelta(minutes=np.random.randint(0, 61))
    df.at[i, 'begin_time'] = next_begin_time
    df.at[i, 'end_time'] = next_begin_time + timedelta(minutes=np.random.randint(30, 121))

####
# Ensure begin_time is in ascending order
# inplace: ブール値で、True に設定すると元のDataFrameが直接更新され、何も返されません。
df.sort_values('begin_time', inplace=True)

# Add a new column 'diff_long' initialized to False
df['diff_long'] = False

# Compute the time difference for rows from the second one onwards
for i in range(1, len(df)):
    time_diff = df.iloc[i]['begin_time'] - df.iloc[i-1]['end_time']
    df.at[i, 'diff_long'] = time_diff >= timedelta(minutes=30)

df.reset_index(drop=True, inplace=True)  # Reset index after sorting

# Add a new column 'time_gap' to calculate the time between the previous end_time and the current begin_time
df['time_gap'] = df['begin_time'] - df['end_time'].shift(1)
df['time_gap'] = df['time_gap'].fillna(pd.Timedelta(seconds=0))  # Fill the NaN values for the first row

# Compute the average of 'time_gap'
average_time_gap = df['time_gap'].mean()

# Add a new column 'diff_time' that stores the duration between end_time and begin_time
df['diff_time'] = df['end_time'] - df['begin_time']

###
# Correctly update 'diff_long' by shifting end_time
# df['diff_long'] = (df['begin_time'] - df['end_time'].shift(1).fillna(df['begin_time'])) <= timedelta(minutes=30)

# Calculate total duration in 'diff_time'
total_duration = df['diff_time'].sum()

# Check if total duration is 4 hours or more
duration_over_four_hours = total_duration >= timedelta(hours=6)

# Count the number of True in 'diff_long'
true_count = df['diff_long'].sum()

# Ensure 'begin_time' and 'end_time' are datetime objects
df['begin_time'] = pd.to_datetime(df['begin_time'])
df['end_time'] = pd.to_datetime(df['end_time'])

# Format 'begin_time' and 'end_time' to 'yy/mm/dd hh:mm:ss'
df['begin_time'] = df['begin_time'].dt.strftime('%y/%m/%d %H:%M:%S')
df['end_time'] = df['end_time'].dt.strftime('%y/%m/%d %H:%M:%S')

# Convert 'time_gap' to 'yy:dd:mm' format
# Note: This format might be a bit unusual as it implies years:days:minutes, which is not a standard. Assuming you wanted days:hours:minutes.
# df['time_gap'] = df['time_gap'].apply(lambda x: f"{x.days}:{x.components.hours:02}:{x.components.minutes:02}")
# Convert 'time_gap' to 'HHh MMm SSs' format
# df['time_gap'] = df['time_gap'].apply(lambda x: f"{x.components.hours:02}h {x.components.minutes:02}m {x.components.seconds:02}s")

def change_time_format(x):
    ret = f"{x.days * 24 + x.components.hours:02}:{x.components.minutes:02}:{x.components.seconds:02}"
    return ret

# df['time_gap'] = df['time_gap'].apply(
#     lambda x: f"{x.days * 24 + x.components.hours:02}:{x.components.minutes:02}:{x.components.seconds:02}"
# )
df['time_gap'] = df['time_gap'].apply(change_time_format)



# Output the required information
df, duration_over_four_hours, true_count
# Display the DataFrame
print(df)
print('duration_over_four_hours = {}'.format(duration_over_four_hours))
print('true_count = {}'.format(true_count))
print(df['time_gap'].dtype)