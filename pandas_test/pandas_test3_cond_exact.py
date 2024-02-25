"""
pandas
データ数取得、計算、条件抽出テスト
"""

import pandas as pd
path = r'C:\Users\OK\source\repos\Repository4_python\pandas_test\related_data_japanese_updated1.csv'

from pathlib import Path
dir_path = r'C:\Users\OK\source\repos\Repository4_python\pandas_test'
# path = Path(dir_path).joinpath('related_data_japanese_updated2.csv')
path = Path(dir_path).joinpath('related_data_japanese_updated2.csv')

df_a = pd.read_csv(
    str(path),
    encoding="utf-8",
    skiprows=0,) #1行読み飛ばす
print('### data.dtypes = ')
print(df_a.dtypes)
#https://note.nkmk.me/python-pandas-len-shape-size/


#####
# 行数・列数
print('df_a.shape = {}'.format(df_a.shape)) #row,col
print('len(df_a) = {}'.format(len(df_a)))
print('df_a.columns = {}'.format(df_a.columns))
# df.shape[0] * df.shape[1]
print('df_a.size = {}'.format(df_a.size))
print('##### df = ')
df = df_a


#####
#  計算
calc_ret = df.groupby(by='部署')['給与'].sum()
print('df.calc_ret = ')
print(calc_ret)
df_sum = pd.DataFrame(list(calc_ret.index), columns=['部署'])
df_sum['給与'] = calc_ret.values
print('df_sum = ')
print(df_sum)
# print('df_sum.values = ')
# print(df_sum.values)


#####
# 条件よりデータを抽出
# df = df[df['年齢'] < 25]

# df = df[df['名前'].str.endswith('e')]
# df = df[df['名前'].str.startswith('C')]
# &、|、~ == and or not
# df = df[df['管理職']==1]
# df = df[ (df['年齢']<40) & (df['管理職']==True) ]
# df = df[ (df['年齢']<40) | (df['管理職']==True) ]
# df = df[ (df['年齢']<40) & ~(df['管理職']==True) ]
# isin 指定した複数の文字列のいずれかと完全一致する要素
# df = df[ df['部署'].isin(['IT部', '営業部']) ]
# 部分一致
# df = df[ df['名前'].str.contains('n') ]
# 3個以上の条件では演算子の優先順位に注意

df = df[ df['ID'] == 12 ]

print(df)


