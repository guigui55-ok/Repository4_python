# https://qiita.com/sho11hei12-1998/items/2458aa0822cc6e7268fa


import numpy as np
print('\n######')
a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print('\n-------')
#条件を満たす箇所がTrue,満たさない箇所がFalseとなるnumpy arrayが返される。
print(a > 5)
# [[False False False False]
#  [False False  True  True]
#  [ True  True  True  True]]

print('\n-------')
#条件を満たす箇所の値が返される。
print( a[a > 5] )
# [ 6  7  8  9 10 11]