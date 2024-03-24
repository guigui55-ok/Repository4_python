"""
pandas その他

テーブルを結合、追加

データをマージ、特定の列を複数抽出、
 条件に合う列データ（ＩＤ）を指定して絞り込み
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

df3 = pd.DataFrame(['Sapporo','Tokyo','London'] ,columns=['City'])

# https://machine-learning-skill-up.com/knowledge/pandas%E3%81%A7%E3%83%A6%E3%83%8B%E3%83%BC%E3%82%AF%E3%81%AA%E7%B5%84%E3%81%BF%E5%90%88%E3%82%8F%E3%81%9B%E3%82%92%E6%8A%BD%E5%87%BA%E3%81%99%E3%82%8B
# Pandasでユニークな組み合わせを抽出する


print("★★★★")
print('#')
print("外部結合：how='outer'")
df = pd.merge(df_a, df_b, how='outer')
print(df)

print('#')
print('結合列の明示的な指定（※左側のみ）')

# 'ID'列を文字列型に変換
df_a['ID'] = df_a['ID'].astype(str)
df_b['ID'] = df_b['ID'].astype(str)

# df_aとdf_bを'ID'列を基にして結合
df = pd.merge(df_a, df_b, on='ID', how='left')
print('df = ')
print(df)

# 特定の列名の条件に合致する行のみを抽出
#https://note.nkmk.me/python-pandas-query/
print('df_a = ')
print(df_a)
df_a = df.query('ID == "002"')


#任意の列を抽出する
columns = ['ItemName_x', 'Amount', 'Memo']
df_b = df_a[columns]
print('df_b = ')
print(df_b)

# https://note.nkmk.me/python-pandas-index-row-column/
# 列名のスライス
# print(df.loc[:, 'col_1':'col_3'])
# print(df.iloc[:, 2])














