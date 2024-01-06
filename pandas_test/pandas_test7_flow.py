"""
pandas その他

numpyでデータを作成、DataFrameに変換、条件を指定して値を取得、一連の流れ

値の取得, loc iloc at iat
"""
# https://www.yutaka-note.com/entry/pandas_index_setting

import pandas as pd
import numpy as np

# print('numpy 空配列')
# buf = ['' for s in range(3)]
# buf = list('' for s in range(3))
# df = pd.DataFrame(buf)
# df = pd.DataFrame(buf, dtype=object)
# # ary = np.empty(3)
# print(df)


row_begin, row_end = 0, 5
col_begin, col_end = 10, 15
col_amount = abs(col_end - col_begin)
test_data = ['●', '', '●', '', '●']
# data_all = pd.DataFrame(buf)
data_all = np.ndarray(0)
for j, row in enumerate(range(row_begin, row_end)):
    row += 1
    # numpy 初期化時に型が勝手に追加される
    # data_rows = np.zeros(col_amount) #とすると数値型となり'1_10'を渡すとint(110)になる
    data_rows = np.zeros(col_amount, dtype=object)
    for i, col in enumerate(range(col_begin, col_end)):
        # 特定の列はvalueを置き換え
        if i==4:
            val = test_data[j]
        else:
            val = str(row) + '_' + str(col)
        # 値を行のバッファに追加する
        # data_rows = np.append(data_rows, [val])
        np.put(data_rows, [i], val)
    # data_rowsをdata_allに追加する
    if data_all.size < 1:
        data_all = data_rows
    else:
        data_all = np.vstack((data_all, data_rows))
# print('data_all')
# print(data_all)

import pandas as pd
cell_values_np = data_all
# if columns!=None:
#     columns = cell_values_np[0]
#     cell_values_np = cell_values_np[1:]
# if index!=None:
#     index = cell_values_np[:, 0]
#     cell_values_np = cell_values_np[:, 1:]
index = None
columns = ['ColA', 'ColB', 'ColC', 'ColD', 'ColE']
df = pd.DataFrame(
    cell_values_np,
    columns=columns, index=index)
print('### df = ')
print(df)
print('### df = ')
df = df[df['ColE']=='●']
print(df)
# https://note.nkmk.me/python-pandas-list-as-value/


print('# to str')
# buf = df.at['0', 'ColA']
buf = df.at[0, 'ColA']
print(buf)
print(type(buf))

print('# to list')
buf = list(df['ColA'])
print(buf)
print(type(buf))

print('*************')
print('値の取得, loc iloc at iat')
print('loc[]の使用例:')
data = df.loc[0, 'ColA']  # 0行目と'ColA'列のデータを取得する
# data = df.loc[0, 0] # raise KeyError(key) from err
print(data)

print('iloc[]の使用例:')
data = df.iloc[0, 1]  # 0行目と1列目（2番目の列）のデータを取得する
# data = df.iloc[0, 'ColA']  #ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types
print(data)

print('at[]の使用例:')
data = df.at[0, 'ColA']  # 0行目と'ColA'列の単一データを高速に取得する
print(data)

print('iat[]の使用例:')
data = df.iat[0, 1]  # 0行目と1列目（2番目の列）の単一データを高速に取得する
print(data)

"""
Pandasにおける loc[]、iloc[]、at[]、iat[] の違いは主に次のようになります：

loc[]: ラベルベースのインデックス指定で、DataFrameからデータを選択します。行と列のラベル（名前）を使用してデータにアクセスします。スライスやブール配列を使用して複数の行や列を選択することができます。

iloc[]: 位置ベースのインデックス指定で、DataFrameからデータを選択します。行と列の数値インデックス（0から始まる）を使用してデータにアクセスします。スライスや整数のリストを使用して複数の行や列を選択することができます。

at[]: ラベルベースのインデックス指定で、単一の要素を選択します。loc[]よりも高速ですが、一度に一つの要素のみを取得または設定するために使用されます。

iat[]: 位置ベースのインデックス指定で、単一の要素を選択します。iloc[]よりも高速ですが、同様に一度に一つの要素のみを取得または設定するために使用されます。

要するに、loc[] と iloc[] は複数の要素を選択するために使用され、at[] と iat[] は単一の要素を高速にアクセスするために使用されます。また、loc[] と at[] はラベル（行や列の名前）を基に動作し、iloc[] と iat[] は位置（インデックスの数値）を基に動作します。

"""