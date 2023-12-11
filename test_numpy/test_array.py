# https://qiita.com/sho11hei12-1998/items/2458aa0822cc6e7268fa

def print_(value, name=''):
    bef = '\n'
    if name!=None:
        name += '=' + '\n'
    buf = bef + name + str(value)
    print(buf)

print()
print('#####')

# 1. リスト内包表記を使って二次元配列を作る
# ex1.py
a = [[0 for j in range(3)] for i in range(2)]
print('a = \n{}'.format(a))

import numpy as np
listb = np.arange(12).reshape(3, 4)
print_(listb, 'listb')
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]