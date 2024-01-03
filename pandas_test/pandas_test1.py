"""
pandas DataFrame作成方法

ループ処理
 データ取得1列ずつ、1行ずつ
"""

# https://note.nkmk.me/python-pandas-dataframe-values-columns-index/

import pandas as pd

s1 = pd.Series([1,2,3,5])
print('series = {}'.format(s1))

df = pd.DataFrame({
    '名前' :['田中', '山田', '高橋'],
    '役割' : ['営業部長', '広報部', '技術責任者'],
    '身長' : [178, 173, 169]
    })
print('df = ')
print(df)
print('df.dtypes = ')
print(df.dtypes)


# https://note.nkmk.me/python-pandas-dataframe-values-columns-index/
import numpy as np

ary = np.arange(9).reshape(3, 3)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

df_b = pd.DataFrame(
    ary,
    columns=['col_0', 'col_1', 'col_2'],
    index=['row_0', 'row_1', 'row_2'])
#        col_0  col_1  col_2
# row_0      0      1      2
# row_1      3      4      5
# row_2      6      7      8
print('df_b = ')
print(df_b)

# 列データの取得
df_c = df_b['col_0']
print('df_c = ')
print(df_c)

# 行データの取得
# df_d = df_b['row_0'] #KeyError: 'row_0'
df_d = df_b.loc['row_0']
print('df_d = ')
print(df_d)


print('column_name = ' )
buf = [column_name for column_name in df]
print(buf)


"""
iterrows()は各行をSeriesに変換するのでかなり遅い
itertuples()はiterrows()よりも速い
列を指定する方法が最も高速。
forループなしで実現できる処理はforループを使わないのが一番良い。
"""

print('=====')
print('1列ずつ取り出す: items() = ' )
for column_name, item in df.items():
    print('{}:'.format(column_name), end='')
    # print(type(item))#<class 'pandas.core.series.Series'>
    buf = [x for x in item]
    print(buf)

print('=====')
print('## 1列ずつ取り出す: iterrows() = ' )
for index, row in df.iterrows():
    print('{}:'.format(index), end='')
    # print(type(row))# <class 'pandas.core.series.Series'>
    buf = [x for x in row]
    print(buf)




msg = """
# https://note.nkmk.me/python-pandas-at-iat-loc-iloc/
locやilocで一行を選択してpandas.Seriesで取得する場合、元のpandas.DataFrameの各列のデータ型dtypeが異なっていると暗黙の型変換が行われる。
"""
print(msg)

print('=====')
print('1列ずつ取り出す2' )
df_mix = pd.DataFrame({'col_int': [0, 1, 2], 'col_float': [0.1, 0.2, 0.3]}, index=['A', 'B', 'C'])
buf = df_mix.loc['B']
print(buf)
print(type(buf))
# <class 'pandas.core.series.Series'>


print('=====')
msg = """
なお、locやilocにおいてリストやスライスで一行を選択した場合は、pandas.Seriesではなくpandas.DataFrameが返される。この場合は元のデータ型dtypeが保持される。
"""
print(msg)
buf = df_mix.loc[['B']]
print(buf)
print(type(buf))
# <class 'pandas.core.frame.DataFrame'>

# https://note.nkmk.me/python-pandas-dataframe-for-iteration/
print('=====')
# obj.attribute のように使用できる。
# 1行の値rowが他の任意のオブジェクトと同じインターフェースを持つときに使用可能
def buf_for_method(row):
    print(type(row))
    print(row)
    print(row[0], row[1], row[2], row[3])
    print(row.名前, row.役割, row.身長)
    print('======')

for row in df.itertuples():
    # この場合、返されるnamedtupleには行のインデックスが含まれます。
    # つまり、DataFrameに3つの列がある場合でも、
    # 返されるnamedtupleはインデックスを含めて4つの要素を持つことになります。
    buf_for_method(row)
    # <class 'pandas.core.frame.Pandas'>

print('引数indexをFalseにすると行名は要素に含まれない。また、引数nameでnamedtupleの名前を指定できる。')
for row in df.itertuples(index=False, name='名前'):
    # buf_for_method(row)
    print(type(row))
    print(row)
    print(row[0], row[1], row[2])
    print(row.名前, row.役割, row.身長)
    
print('引数nameをNoneにするとノーマルのタプルを返す。')
for row in df.itertuples(index=False, name=None):
    print(type(row))
    print(row)
    print(row[0], row[1], row[2])
exit(0)

print('=====')
print('=====')
print('pandasで値の更新と警告 SettingWithCopyWarningについて')
print('## id check row = ' )
df_e = df.loc[0]
# df_e[2] = 110 # SettingWithCopyWarning
# df.loc[0][2] = 110
# df.loc[0, 2] = 110 # 列が追加されてしまう＞, 178, 110.0
# df.loc[0, 1] = 110 # 列が追加されてしまう＞, 178, 110.0
# Key名を指定しなければならない
df.loc[0, '身長'] = 110
# または、ilocでindexを指定する
df.iloc[0, 2] = 120
"""

C:\Program Files\Python\Python310\lib\site-packages\pandas\core\series.py:1056: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  cacher_needs_updating = self._check_is_chained_assignment_possible()
# データフレームからのスライスのコピーに値を設定しようとしています
ドキュメントの注意事項を参照してください: 

# https://qiita.com/FukuharaYohei/items/b3aa7113d08858676910
"""
print('df_e id = ')
buf = [x for x in df_e]
print(buf)
buf = [id(x) for x in df_e]
print(buf)

print('=====')
print('## id check all = ' )
for index, row in df.iterrows():
    print('{}:'.format(index), end='')
    buf = [x for x in row]
    print(buf)
    buf = [id(x) for x in row]
    print(buf)

# print('=====')
# print('## id check all2 = ' )
# for index, row in df.iterrows():
#     print('{}:'.format(index), end='')
#     buf = [x for x in row]
#     print(buf)
#     buf = [id(x) for x in row]
#     print(buf)


"""
df_e[2] と df[0][2] が同じことを確認するときidを使用することについて。


df_e[2] と df[0][2] が同じメモリ位置を参照していない可能性があります。特にPandasのDataFrameでは、内部的にデータがどのように格納されているかによって、同じ値でも異なるメモリアドレスに存在することがあります。

DataFrameの場合、特に数値データは内部的にNumPy配列として格納され、これらの値はDataFrameから単独でアクセスされた際、新しいPythonオブジェクトとしてインスタンス化されることがあります。このため、元のDataFrameのセルの値と、その値を別の変数に代入した場合、異なるメモリアドレスを持つことがあります。

DataFrameのコードの信頼性の確認に id を使うことは推奨されません。DataFrame内の値の一致を確認する際は、値自体の比較を行うのが一般的です。例えば、次のように値が等しいかどうかを確認できます：

python
Copy code
if df.iloc[0, 2] == df_e[2]:
    print("値は等しい")
else:
    print("値は等しくない")
この方法は、値自体が等しいかどうかを正確に評価するため、DataFrameの検証に適しています。DataFrame内のデータの整合性や一貫性を確認する際には、このような値の比較を利用することをお勧めします。
"""