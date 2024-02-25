

# https://qiita.com/juri_engineer/items/f641870b0644d2f8d667#ndarray%E9%85%8D%E5%88%97%E3%81%AE%E4%BD%9C%E3%82%8A%E6%96%B9
# https://note.nkmk.me/python-numpy-ndarray-ndim-shape-size/

import numpy as np

# https://note.nkmk.me/python-numpy-empty-empty-like/
print('numpy 空配列')
ary = np.empty(3)
print(ary)

print('2次元配列、値を1つずつ追加する')
ary = np.arange(1,21).reshape(4,5)
print(ary)

col_begin, col_end = 10, 15
col_amount = abs(col_end - col_begin)
# data_all = np.arange(0, col_amount)
data_all = np.arange(0)
for row in range(5):
    row += 1
    # numpy 初期化時に型が勝手に追加される
    # data_rows = np.zeros(col_amount) #とすると数値型となり'1_10'を渡すとint(110)になる
    data_rows = np.zeros(col_amount, dtype=object)
    for i, col in enumerate(range(10,15)):
        val = str(row) + '_' + str(col)
        # 値を行のバッファに追加する
        # data_rows = np.append(data_rows, [val])
        np.put(data_rows, [i], val)
    # data_rowsをdata_allに追加する
    if data_all.size < 1:
        data_all = data_rows
    else:
        data_all = np.vstack((data_all, data_rows))

print('data_all')
print(data_all)