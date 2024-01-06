"""
pandas DataFrame作成方法、データ取得3

"""
# https://www.delftstack.com/ja/howto/python-pandas/pandas-replace-values-in-column/
import pandas as pd
import numpy as np
# https://note.nkmk.me/python-pandas-dataframe-for-iteration/
data = {
    "name": ["michael", "louis", "jack", "jasmine"],
    "city": ["berlin", "paris", "roma", np.nan],
    "age": [32, 64, 46, 11],
    "state":['NY', 'CA', 'NY', 'OH'],
    "point":[46, 55, 99, 11]
}
df = pd.DataFrame(data, columns=["name", "city", "age", "state", "point"])

print('zip()を使うと、複数列の値をまとめて取得することも可能。')
for age, point in zip(df['age'], df['point']):
    print(age, point)

print('行名（インデックス）を取得したい場合はindex属性を使う。')
for index, state in zip(df.index, df['state']):
    print(index, state)
print(type(index))
print(type(df.index))