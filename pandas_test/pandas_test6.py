"""
pandas その他

データ作成時 行列を変更
"""
# https://www.yutaka-note.com/entry/pandas_index_setting

import pandas as pd

d = {'Data0':[1, 2],
     'Data1':[3, 4],
     'Data2':[5, 6]}
 
print('基本的な作成方法｜{key:values} ⇒ df')
df = pd.DataFrame(d)
print(df)

print('キーをカラム名に設定｜orient="columns"')
df = pd.DataFrame.from_dict(d, orient="columns")
# df = pd.DataFrame.from_dict(d) # デフォルト値なのでorient="columns"は省略可能
# df = pd.DataFrame(d) # pd.DataFrame()でも同じ結果
print(df)

print('キーをインデックス名に設定｜orient="index"')
df = pd.DataFrame.from_dict(d, orient="index")
print(df)