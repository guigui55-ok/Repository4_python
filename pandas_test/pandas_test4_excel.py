"""
pandas エクセル読み込み
"""
# https://note.nkmk.me/python-pandas-read-excel/
"""
pandas.read_excel()では内部でopenpyxlとxlrdというライブラリを使っている。

$ pip install openpyxl
$ pip install xlrd
"""
# https://pyhoo.jp/pandas-read-excel
# https://machine-learning-skill-up.com/knowledge/pandas%E3%81%A7%E3%82%A8%E3%82%AF%E3%82%BB%E3%83%AB%E3%82%92%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%82%80%E9%9A%9B%E3%81%AB%E5%88%97%E3%82%92%E6%8C%87%E5%AE%9A%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95%EF%BC%9A



from pathlib import Path
path = r'C:\Users\OK\source\repos\Repository4_python\excel_test'
path = Path(path).joinpath('FileIO.xlsm')
path = str(path)

import pandas as pd

# df = pd.read_excel(path, index_col=0)
# df = pd.read_excel(path)
# df = pd.read_excel(path, sheet_name='TestData')
# data_frame = pd.read_excel(path, sheet_name='TestData' ,header=5)
# data_frame = pd.read_excel(path, sheet_name='TestData' ,header=5, index_col='B')#NG ValueError: Index B invalid
# data_frame = pd.read_excel(path, sheet_name='TestData' ,header=5, index_col='ID')#NG ValueError: Index ID invalid
# df = pd.read_excel(path, sheet_name='TestData', header=5, usecols=['ID','ItemName','Status']) #NG
# df = pd.read_excel(path, sheet_name='TestData', usecols=['ID','ItemName','Status']) #NG
# ValueError: Usecols do not match columns, columns expected but not found: ['ID', 'ItemName']
# df = pd.read_excel(path, sheet_name='TestData', usecols=['ID']) #ValueError: Usecols do not match columns, columns expected but not found: ['ID']

# df = pd.read_excel(path, sheet_name='TestData' ,header=5, index_col=2)
# df = pd.read_excel(path, sheet_name='TestData' ,header=5, index_col='ID')#ValueError: Index ID invalid
# df = pd.read_excel(path, sheet_name='TestData' , index_col='■TableA')
# df = pd.read_excel(path, sheet_name='TestData' ,header=4, index_col=2, usecols='B:D')
df = pd.read_excel(path, sheet_name='TestData' ,header=4, index_col=2, usecols=['ID','ItemName','Status'])

# 行数・列数
print('df_a.shape = {}'.format(df.shape)) #row,col
print('len(df_a) = {}'.format(len(df)))
print('df_a.columns = {}'.format(df.columns))
# df.shape[0] * df.shape[1]
print('df_a.size = {}'.format(df.size))
print('df = ')
print(df)