"""
pandas その他

日付
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
"""

print('合計用の別のDataFrameを作成（日付ごとに計算）')
print('毎日のデータを、日付範囲を指定する')
from pandas_test8_test_data import DF_TEST_DATA_B, DF_TEST_DATA_COLUMNS

df = pd.DataFrame(DF_TEST_DATA_B, columns=DF_TEST_DATA_COLUMNS)
df 
df['Date'] = pd.date_range('2023-11-01', '2023-11-15', freq='D')
import datetime
today = datetime.datetime.now()
df = df['Date']
df_sum = df.set_index('Date').resample('D')['Amount'].sum()
df_d = pd.DataFrame(list(df_sum.index), columns=['DateB'])
df_d['SUM'] = df_sum.values
print(df_d)
