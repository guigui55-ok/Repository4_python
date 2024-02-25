"""
pandas その他

テーブルを結合、追加
"""
import pandas as pd

DF_TEST_DATA_COLUMNS_A = ['ID', 'ItemName', 'Status', 'Enable', 'Amount', 'Date']

DF_DATA_A = [
 ['001', 'ItemA', 1, '●', 50, '2022-08-06 00:00:00'],
 ['002', 'ItemB', 2, '', 20, '2021-12-07 00:00:00'],
 ['005', 'ItemE', 5, '', 220, '2022-12-07 00:00:00'],
 ['003', 'ItemC', 3, '', 80, '2023-02-25 00:00:00']]


DF_TEST_DATA_COLUMNS_B = ['ID', 'ItemName', 'Name', 'Memo']
DF_DATA_B =[
['001', 'ItemA', 'Andy', 'memo:aaa' ],
 ['002', 'ItemB', 'Billy', 'memo:bbb' ],
 ['003', 'ItemC', 'Cyndy', '']]

DF_TEST_DATA_COLUMNS_B = ['Order', 'ID', 'ItemName', 'Name', 'Memo']
DF_DATA_B =[
[3, '001', 'ItemA', 'Andy', 'memo:aaa' ],
 [4, '002', 'ItemB', 'Billy', 'memo:bbb' ],
 [4, '004', 'ItemD', 'Debian', 'memo:dd' ],
 [5, '003', 'ItemC', 'Cyndy', '']]

df_a = pd.DataFrame(DF_DATA_A, columns=DF_TEST_DATA_COLUMNS_A)

print('df_a =')
print(df_a)
print(df_a.dtypes)


df_b = pd.DataFrame(DF_DATA_B, columns=DF_TEST_DATA_COLUMNS_B)
print('df_b =')
print(df_b)
print(df_b.dtypes)

# DataFrameの作成
df_a = pd.DataFrame(DF_DATA_A, columns=DF_TEST_DATA_COLUMNS_A)
df_b = pd.DataFrame(DF_DATA_B, columns=DF_TEST_DATA_COLUMNS_B)

# 'ID'列を文字列型に変換
df_a['ID'] = df_a['ID'].astype(str)
df_b['ID'] = df_b['ID'].astype(str)

# df_aとdf_bを'ID'列を基にして結合
df = pd.merge(df_a, df_b, on='ID', how='left')

print(df)















