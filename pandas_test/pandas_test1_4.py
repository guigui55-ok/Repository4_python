"""
pandas DataFrame作成方法、データ更新2

"""
# https://www.delftstack.com/ja/howto/python-pandas/pandas-replace-values-in-column/
import pandas as pd

import numpy as np

data = {
    "name": ["michael", "louis", "jack", "jasmine"],
    "city": ["berlin", "paris", "roma", np.nan],
}
df = pd.DataFrame(data, columns=["name", "city"])

print('Pandas DataFrame で列の値をコレクションに置き換える')
print('Pandas DataFrame の関数で列の値を置き換える')
# replace column values with function
new_dict = {"berlin": "dubai", "paris": "moscow", "roma": "milan", np.nan: "NY"}

df["city"] = df["city"].map(new_dict, na_action=None,)

# print(df)
func = "I am from {}".format
df["city"] = df["city"].map(func)

print(df)

print('Pandas で列値を置換するには loc メソッドを使用する')
print('Pandas の DataFrame で列の値を条件付きで置き換える')
data = {
    "name": ["michael", "louis", "jack", "jasmine"],
    "grades": [30, 70, 40, 80],
    "result": ["N/A", "N/A", "N/A", "N/A"],
    "salary": [700, 800, 1000, 1200],
}

df = pd.DataFrame(data, columns=["name", "grades", "result", "salary"])

df.loc[df.grades > 50, "result"] = "success"
df.loc[df.grades < 50, "result"] = "fail"
print(df)

print('replace() メソッドを使用して値を変更する')
df['name'] = df['name'].replace([30, 30, 30], 100)
df['grades'] = df['grades'].replace([30, 30, 30], 100)

print('Pandas DataFrame で列の値を 1つの値に置き換える')
df["salary"] = df["salary"].replace([700], 750)
print(df)