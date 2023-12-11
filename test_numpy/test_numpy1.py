import numpy as np


print()
print('*****')
### numpy 
list2d_a = np.zeros((3, 3))
print('list2d_a=\n{}'.format(list2d_a))
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]
#  [ 0.  0.  0.]]

list2d_a[1][1] = 1
print('list2d_a=\n{}'.format(list2d_a))
# [
#     [0. 0. 0.],
#     [0. 1. 0.],
#     [0. 0. 0.]
#

### search value
list_b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print('list_b=\n{}'.format(list_b))
# インデックス1の値が2のリストはどこか検索
print(np.where(list_b[:,1]==2)[0])
# [0]

### sort
list_c = np.array([
    [5, 6, 4],
    [9, 8, 7],
    [3, 1, 2]
])
print(np.sort(list_c))
# [[4 5 6]
#  [7 8 9]
#  [1 2 3]]
print('list_c 1=\n{}'.format(list_c))

print(np.sort(list_c, axis=0))# 列のソート（0列目がソートされる
# [[3 1 2]
#  [5 6 4]
#  [9 8 7]]
print('list_c 2=\n{}'.format(list_c))

print(np.sort(list_c, axis=1))# 行のソート、1行目がソートされる
# [[4 5 6]
#  [7 8 9]
#  [1 2 3]]
print('list_c 3=\n{}'.format(list_c))

# 1次元配列を2次元配列に変換
buf = [x for x in range(9)]
list_d = np.array(buf)
print('list_d 1=\n{}'.format(list_d))

# print(list_d.reshape(3, 2))
# ぴったり合わないとエラーになる
#ValueError: cannot reshape array of size 9 into shape (3,2)
#cannot reshape array of size 9 into shape (3,2)

list_d2 = list_d.reshape(3, 3)
print('list_d 2=\n{}'.format(list_d2))


# 2次元配列の転置
lidt_e = np.array(list_d2).T
print('lidt_e 1=\n{}'.format(lidt_e))


# https://camp.trainocate.co.jp/magazine/python-two-dimensional-array/