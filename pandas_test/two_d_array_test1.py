# https://camp.trainocate.co.jp/magazine/python-two-dimensional-array/
# 2次元配列

print('1次元配列の追加')
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list2d_a = list()
list2d_a.append(list1)
list2d_a.append(list2)
print(list2d_a)

print('リテラルから')
list2d_b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(list2d_b)

print('リテラル省略形')
list2d_c = [[0]* 3]* 3
list2d_c[1][1] = 1
print(list2d_c)
for buf in list2d_c:
    print('id = {}'.format(id(buf)))

print('リスト内包表記')
list2d_d = [[0 for i in range(3)] for j in range(3)]
list2d_d[1][1] = 1
print(list2d_d)
for buf in list2d_d:
    print('id = {}'.format(id(buf)))

print('numpy')
import numpy as np

list2d_e = np.zeros((3, 3))
print(list2d_e)
print(list2d_e)
for buf in list2d_e:
    print('id = {}'.format(id(buf)))