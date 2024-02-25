"""
numpy 初期化
"""

import numpy as np

# https://www.headboost.jp/how-to-create-an-array/
print(' np.linspace: 指定の要素数の等差数列を作成')
#  デフォルトでは要素数は50
np.linspace(1, 50)

#  第三引数で生成する配列の要素数を指定
np.linspace(1, 50, 5)
# 逆順
np.linspace(50, 0, 5)
# 多次元
np.linspace(0, 10, 8).reshape(4, 2)

print('初期化')
# 1次元配列を生成
np.zeros(5)