"""
pandas DataFrame作成
csv連携

"""



import pandas as pd
import copy

from pathlib import Path
dir_path = r'C:\Users\OK\source\repos\Repository4_python\pandas_test'
path = Path(dir_path).joinpath('related_data_japanese_updated2.csv')
df = pd.read_csv(path)
import sys
print('size = {}'.format(sys.getsizeof(df)/(1024**2)))


with open(str(path), 'r', encoding='utf-8')as f:
    lines = f.readlines()
# ID,名前,年齢,給与,部署,経験年数,管理職
columns = lines[0].strip().split(',')
print('columns = ')
print(columns)

print('----------------')
print('csvを読み込みdfにする。')
df = pd.read_csv(path, skiprows=1) 
# df = pd.read_csv(path, skiprows=1,columns=columns) #TypeError: read_csv() got an unexpected keyword argument 'columns'
df.columns = columns
print('df = ')
print(df)
print('size = {}'.format(sys.getsizeof(df)/(1024**2)))
print(df.dtypes)



# print('----------------')
# print('DataFrame生成時にカラムの型(dtype)を指定する')
# # pandasの主要なデータ型dtype一覧
# # https://note.nkmk.me/python-pandas-dtype-astype/
# dtyp = {
#     'ID': 'uint16',
#     '名前': 'object',
#     '部署': 'object', 
#     '給与': 'uint64'
# }
# df = pd.read_csv(path, dtype=dtyp)[['ID', '名前', '部署', '給与']]

# print(df)
# print('size = {}'.format(sys.getsizeof(df)/(1024**2)))
# print(df.dtypes)

