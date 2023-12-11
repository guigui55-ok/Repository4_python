# https://py-memo.com/python/numpy-access/
import numpy as np

print('\n#####')
buf = [0, 1, 2, 3, 4]
buf = [x for x in range(10, 15)]

a = np.array(buf)

print(buf)
print(a[0]) #先頭から３番目
print(a[2]) #先頭から３番目
print(a[4])
print(a[-1]) #最後から１番目

print('\n#####')
a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

print(a[1][2])
print(a[1, 2])

print('\n#####')
a = np.array([2, 3, 1, 8, 4, 3, 6, 1, 3, 5])

print(a[a>=4])


print('\n#####')
b = np.array([2, 3, 1, 8, 4, 3, 6, 1, 3, 5])
b[b%2==0] = 0
print(b)
# b[b%2==0] = True
b[b%2==0] = False
print(b)

print(int(True))
print(int(False))

