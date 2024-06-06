

import pandas as pd
import datetime
import random

columns = ['time_a', 'time_b', 'time_diff']
data = []

now_time = datetime.datetime(2024,5,1,0,0,0)
time_a = now_time
max = 10
for i in range(max):
    add_time_int = random.randint(5,100)
    add_time = datetime.timedelta(minutes=add_time_int)
    time_b = time_a + add_time
    time_diff = (time_b - time_a).total_seconds() / 60  # time_diff in minutes
    # 列を追加
    add_row = [time_a, time_b, time_diff]
    data.append([time_a, time_b, time_diff])
    #
    add_time_int = random.randint(5,100)
    add_time = datetime.timedelta(minutes=add_time_int)
    time_a = time_b + datetime.timedelta(minutes=add_time_int)
    # 5列ごとに区切りを入れる
    if i == max-1: break
    if i==0:continue
    if (i+1)%5==0:
        # add_row = [None,None,None]
        add_row = ['','','']
        data.append(add_row)

#CSVに出力する
file_name = '__test_file.csv'

# Create DataFrame
df = pd.DataFrame(data, columns=columns)
print('*****')
print(df)
print('*****')

# Output to CSV
file_name = '__test_file.csv'
df.to_csv(file_name, index=False)
print('file_name = {}'.format(file_name))