"""
pandas DataFrame作成方法、データ更新ex メモリ節約

"""

# https://note.nkmk.me/python-pandas-dataframe-values-columns-index/

import pandas as pd
import copy

s1 = pd.Series([1,2,3,5])
print('series = {}'.format(s1))

df = pd.DataFrame({
    '名前' :['田中', '山田', '高橋','多田野'],
    '役割' : ['営業部長', '広報部', '技術責任者','平社員'],
    '身長' : [178, 173, 120, 150]
    })
df_base = copy.copy(df)
print('df = ')
print(df)
print('df.dtypes = ')
print(df.dtypes)

buf = df.head() # 先頭から5件
print('head = ')
print(buf)
buf = df.tail()   # 末尾から5件
print('tail = ')
print(buf)



# https://qiita.com/141sksk/items/9883be05a3851c90d1d1
print('----------------')
# Better
def map_category(sintyo):
    if sintyo >= 170:
        return 'high'
    elif sintyo < 130:
        return 'low'
    else:
        return 'normal'

# rating_file = pd.read_csv('ratings.csv')
# rating_file["evalation"] = rating_file["rating"].apply(map_rating_category)
df["身長基準"] = df["身長"].apply(map_category)
print(df)



print('----------------')
import numpy as np

df = copy.copy(df_base)
def add_category(df_):
    return np.select(
        condlist=(
            df_["身長"] >= 170,
            df_["身長"] < 130,
        ),
        choicelist=("high", "low"),
        default="normal")

# rating_file = pd.read_csv('ratings.csv')
# rating_df = rating_file.assign(
#     evaluation = lambda df_: rating_category(df_)
# )
# df = df.assign(param = lambda df_: add_category(df_))
df = df.assign(身長基準=lambda df_: add_category(df_))
print(df)
df_b = copy.copy(df)

from pathlib import Path
dir_path = r'C:\Users\OK\source\repos\Repository4_python\pandas_test'
path = Path(dir_path).joinpath('related_data_japanese_updated2.csv')
df = pd.read_csv(path)
import sys

print('size = {}'.format(sys.getsizeof(df)/(1024**2)))


print('----------------')
print('DataFrame生成時にカラムの型(dtype)を指定する')
df = pd.read_csv(path)[['ID', '名前', '部署', '給与']]
print(df)
print('size = {}'.format(sys.getsizeof(df)/(1024**2)))
print(df.dtypes)



print('----------------')
print('DataFrame生成時にカラムの型(dtype)を指定する')
# pandasの主要なデータ型dtype一覧
# https://note.nkmk.me/python-pandas-dtype-astype/
dtyp = {
    'ID': 'uint16',
    '名前': 'object',
    '部署': 'object', 
    '給与': 'uint64'
}
df = pd.read_csv(path, dtype=dtyp)[['ID', '名前', '部署', '給与']]

print(df)
print('size = {}'.format(sys.getsizeof(df)/(1024**2)))
print(df.dtypes)


# 不要になったオブジェクトは削除 Better
import gc
del df
gc.collect()  


print('----------------')
print('データ更新')
# df_b[df_b['身長基準'] == 'high']['身長基準'] = 'Good'
# """
# c:\Users\OK\source\repos\Repository4_python\pandas_test\pandas_test1_3.py:115: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead

# See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#   df_b[df_b['身長基準'] == 'high']['身長基準'] = 'Good'
# """
# rating_df.loc[rating_df['evaluation'] == 'Average', 'evaluation'] = 'Good'
# df_b.loc[df_b['身長基準'] == 'high']['身長基準'] = 'Good'
# df_b.loc[df_b['身長基準'] == 'high'].loc['身長基準'] = 'Good'

df_b.loc[df_b['身長基準'] == 'high', '身長基準'] = 'Good' # OK
print(df_b)

###
# https://note.nkmk.me/python-pandas-dtype-astype/
# 欠損値NaNはisnull()で判定したり、dropna()で削除したりできる
###


print('----------------')
print('mutating(変異)とchaining(連鎖) データの更新・変更')
# NG
df_c = df_b.assign(身長基準=lambda df_: add_category(df_))

df_c = df_c.assign(
    身長基準=lambda df_: df_["身長基準"].astype("category"))
df_d = df_c.groupby('身長基準').get_group('high')
# print(df_d)


# Better
df_e = df_b.assign(
    身長基準 = lambda df_: add_category(df_)
).assign(
    evaluation=lambda df_: df_["身長基準"].astype("category")
).groupby('身長基準').get_group('high')
print(df_e)


"""
https://note.nkmk.me/python-pandas-assign-append/
列の追加、値の初期化　df['D'] = 0
assign()メソッドで追加・代入　列の追加
insert()メソッドで任意の位置に追加　行の追加
concat()関数でSeries, DataFrameを横に連結
concat()関数でSeries, DataFrameを縦に連結
"""