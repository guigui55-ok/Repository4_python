"""
pandas DataFrame作成方法、データ取得1

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

buf = df.head() # 先頭から5件
print('head = ')
print(buf)
buf = df.tail()   # 末尾から5件
print('tail = ')
print(buf)


print('----------------')
# 行、列、範囲を指定して抽出する
df = pd.DataFrame([[10, 20], [25, 50]], index=["1行", "2行"], columns=["1列", "2列"])
buf = df.loc["1行", :]
print('df = {}'.format(df))
print('df.loc = ')
print(buf)

buf = df.iloc[1:2]# index指定が可能
print('df.iloc = ')
print(buf)

buf = df.iat[0,1]# index指定が可能
print('df.iat = ')
print(buf)

# 単独の要素を選択したい場合はloc[]でもよいが、at[]のほうがより高速。
np_buf = df.at['1行','2列']
print('df.at = ')
print(np_buf)


print('----------------')
# 条件による行の抽出(query)
df = pd.DataFrame([[10, 20,30, 30], [25, 50,65, 80]], index=["1行", "2行"], columns=["A", "B", "C", "D"])
print(df)
buf = df.query('A >= 5 and C < 50')
print('df.query = ')
print(buf)
