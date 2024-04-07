"""
pandas その他

日付ごとの計算
 データをプリントする
  日付文字列をDate型に変換

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
# print(df.head())
print(df)
print('-----------')
print(df.dtypes)

"""
     ID ItemName  Status Enable  Amount       Date
0   001    ItemA       1      ●      50 2022-09-27
1   002    ItemB       2             20 2021-07-20
2   003    ItemC       3             80 2022-04-30
3   004    ItemD       1             90 2023-11-02
4   005    ItemE       2      ●      30 2023-01-25
5   006    ItemF       3             20 2021-10-24
6   007    ItemG       1             60 2022-05-13
7   008    ItemA       2             30 2022-03-06
8   009    ItemB       3             70 2023-05-14
9   010    ItemC       1      ●       0 2022-09-03
10  011    ItemD       2             20 2021-11-19
11  012    ItemA       3             60 2022-10-06
12  013    ItemB       1              0 2022-08-15
13  014    ItemC       2             20 2022-06-30
14  015    ItemD       3      ●      60 2022-07-19
"""