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

# https://machine-learning-skill-up.com/knowledge/pandas%E3%81%A7%E3%83%A6%E3%83%8B%E3%83%BC%E3%82%AF%E3%81%AA%E7%B5%84%E3%81%BF%E5%90%88%E3%82%8F%E3%81%9B%E3%82%92%E6%8A%BD%E5%87%BA%E3%81%99%E3%82%8B
# Pandasでユニークな組み合わせを抽出する

print('# concat =')
print('異なるカラムを持つ要素同士を結合')
print('下側に追記される（行が追加される、存在しないデータはNaNとなる）')
df = pd.concat([df_a, df_b])
print(df)

print('# concat =')
df3 = pd.DataFrame(['Sapporo','Tokyo','London'] ,columns=['City'])
df = pd.concat([df_a, df3], axis=1)
# ???
# df = pd.concat([df_a, df3], axis=2)#Errror
# df = pd.concat([df_a, df3], axis=0)
# df = pd.concat([df_a, df3])
print('axis指定で横方向結合')
print('右側に追記される（City列が増える）')
print(df)



print('#####')
print('#')
print('一方でもデータがないものは削除する')
print('同じカラム名、ID、ItemNameなども重複する')
df = pd.concat([df_a, df_b], axis=1, join='inner')
print(df)

print('#')
print('結合軸（インデックス）以外は同名でも別物として扱う')
print('上と変わらない')
df = pd.concat([df_a, df_b], axis=1)
print(df)


print('#####')
print('# merge')
print('データが結合される、重複カラムは除外される')
print('片方しかないデータはすべて除外される')
df = df_a.merge(df_b)
print(df)

print('#')
df = pd.merge(df_a, df_b)
print(df)

# mergeの重要な特徴として、1度に結合できるのは2つまでという点です。
# concatは3つ以上の結合が可能です
# 　例）pd.concat([df1, df2, df3])

print("★★★★")
print('#')
print("外部結合：how='outer'")
# df = pd.merge(df_a, df3, how='outer')
# MergeError 
#No common columns to perform merge on. Merge options: left_on=None, right_on=None, left_index=False, right_index=False
df = pd.merge(df_a, df_b, how='outer')
print(df)


print('#')
print("左結合：how='left'")
print('df_a にないものは除外される')
df = pd.merge(df_a, df_b, how='left')
print(df)

print('#')
print("左結合：how='right'")
df = pd.merge(df_a, df_b, how='right')
print(df)


print('###')
print('join')
# df = df_a.join(df_b)
# olumns overlap but no suffix specified: Index(['ID', 'ItemName'], dtype='object')
# 同じ列名があるとNG
print('右に追加される（1列増える）')
df = df_a.join(df3) #OK
print(df)
df = df3.join(df_a) #OK
print(df)

print('#')
print('結合列の明示的な指定（※左側のみ）')
# df = df_a.join(df_b, on="ItemName")
# You are trying to merge on object and int64 columns. If you wish to proceed you should use pd.concat
# df = df_a.join(df_b, on=['ID', 'ItemName'])
# df = df_b.join(df_a, on=['ID', 'ItemName'])
# 例外が発生しました: ValueError
# len(left_on) must equal the number of levels in the index of "right"
# df = df_a.join(df3, on="ItemName")
# ValueError: You are trying to merge on object and int64 columns. If you wish to proceed you should use pd.conca
# print(df)
# df = df_a.join(df_b, on=['ID'])
# 1番目の型があっていなければならない？
# df_a = [ID=str, ItemName=str ...]
# df_b = [order=int, ID=str, ItemName=str ...]
# となっているので、1番目をIDでそろえる

# ##########
# # columns = df_b.columns.values #これを直接編集すると、df内のcolumnsも変わってしまう
# import copy
# columns = copy.copy(df_b.columns.values)
# buf_a = columns[0]
# buf_b = columns[1]
# buf_c = columns[2]
# columns[0] = buf_b
# columns[1] = buf_c
# columns[2] = buf_a

# print('columns')
# print(columns)
# # df_b2 = df_b.reindex(columns, axis=0)
# df_b2 = df_b.reindex(columns=columns)
# # 列の入れかえ
# # df_b2 = df_b.reindex(index=[5,4,3])
# # df_b2 = df_b.reindex(index=[3,2,1])
# df_b2["Order"] = df_b2["Order"].astype(str)
# print(df_b2)
# print(df_b2.dtypes)
# df = df_a.join(df_b2, on=['ID'])
#########

# 'ID'列を文字列型に変換
df_a['ID'] = df_a['ID'].astype(str)
df_b['ID'] = df_b['ID'].astype(str)

# df_aとdf_bを'ID'列を基にして結合
df = pd.merge(df_a, df_b, on='ID', how='left')
print(df)















