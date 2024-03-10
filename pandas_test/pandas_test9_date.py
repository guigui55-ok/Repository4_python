"""
pandas その他

日付ごとの計算

"""
import pandas as pd
from pandas_test8_test_data import DF_TEST_DATA, DF_TEST_DATA_COLUMNS

df = pd.DataFrame(DF_TEST_DATA, columns=DF_TEST_DATA_COLUMNS)

print('df =')
print(df.dtypes)
print(df)

# https://note.nkmk.me/python-pandas-datetime-timestamp/
print('日付に変換')
df['Date'] = pd.to_datetime(df['Date'])
print(df.head())
print(df.dtypes)

# 元の書式が違っていても指し示す日時が同じであればdatetime64[ns]型の値は等価。
# print(pd.to_datetime(df['A']) == pd.to_datetime(df['B'], format='%Y年%m月%d日 %H時%M分'))
# Timestamp型はPythonの標準ライブラリdatetimeのdatetime型を継承し拡張した型。

print('合計用の別のDataFrameを作成（日付間隔ごとに計算）')
print('Mは月末ごと')
df_sum = df.set_index('Date').resample('M')['Amount'].sum()
df_d = pd.DataFrame(list(df_sum.index), columns=['DateB'])
df_d['SUM'] = df_sum.values
print('df_d[SUM]')
print(df_d)

"""
# https://note.nkmk.me/python-pandas-time-series-resample-asfreq/
D: 毎日
B: 毎営業日（月曜 - 金曜）
W: 毎週（日曜始まり）
M: 月末ごと
SM: 15日と月末ごと
Q: 四半期末ごと
AまたはY: 年末ごと

SM（15日と月末ごと）についてはSMS（月初と15日ごと）が指定可能。営業日は指定できない。
W（週次）は毎日曜日が対象となるが、W-MONのように任意の曜日を指定可能。
四半期Q、年次AまたはYでは終了月あるいは開始月をQ-FEBのように指定できる。
毎月の第何週目の曜日を指定できる。WOM-4FRIのようにWOM-<第何週かの数値><曜日>で指定する。
100Dは100日ごと、100Bは100営業日ごと、10Wは10週ごとの日曜日、10W-WEDは10週ごとの水曜日、2Mは隔月、90Tは90分ごととなる。


#http://ailaby.com/date_range/


"""


# MをそのままD（Date）にするとエラーとなる
# TypeError: Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex, but got an instance of 'Index'
# df_sum = df.set_index('Date').resample('D')['Amount'].sum()
# df_d = pd.DataFrame(list(df_sum.index), columns=['DateB'])
# df_d['SUM'] = df_sum.values
# print('df_d[SUM] Date')
# print(df_d)


print('合計用の別のDataFrameを作成（日付ごとに計算）')
print('毎日のデータを、日付範囲を指定する')
from pandas_test8_test_data import DF_TEST_DATA_B, DF_TEST_DATA_COLUMNS

df = pd.DataFrame(DF_TEST_DATA_B, columns=DF_TEST_DATA_COLUMNS)
# 上記dfのDate列に以下の日付をれていく（元ある値を入れ替えてしまう）
# df['Date'] = pd.date_range('2023-11-01', '2023-11-15', freq='D')
# df_check_date = pd.date_range('2023-11-01', '2023-11-15', freq='D')
# import datetime
# today = datetime.datetime.now()
# df = df['Date'] #'pandas.core.series.Series
# df_sum = df.set_index('Date').resample('D')['Amount'].sum()
# df_d = pd.DataFrame(list(df_sum.index), columns=['DateB'])
# df_d['SUM'] = df_sum.values
# print(df_d)

# 'Date'列をdatetime型に変換
df['Date'] = pd.to_datetime(df['Date'])

# 日付範囲から1日ごとのDataFrameを作成する
df_check_date = pd.date_range('2023-11-01', '2023-11-08', freq='D')

# 元データを日付範囲のデータでフィルターを掛ける
df_filtered = df[df['Date'].isin(df_check_date)]

# 日付でソート
df_sorted = df_filtered.sort_values(by='Date')

# 結果の表示
print('df_sorted')
print(df_sorted)


print('-------------')

# 'Date'列をdatetime型に変換
df['Date'] = pd.to_datetime(df['Date'])

# 日付範囲DataFrameの作成
date_df = pd.date_range(start='2023-11-01', end='2023-11-08', freq='D')
df_date_range = pd.DataFrame({'Date': date_df})

# 元のデータと日付範囲DataFrameの結合
df_merged = pd.merge(df_date_range, df, on='Date', how='left')

# https://note.nkmk.me/python-pandas-nan-dropna-fillna/
# Nanを空白に
df_merged = df_merged.fillna('')

# 結果の表示
print(df_merged)