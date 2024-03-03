# リスト内包表記

print('buf_a')
buf_a = [i for i in range(3)]
print(buf_a)

print('buf_b')
buf_b = [i**2 for i in range(5)]
print(buf_b)

print('buf_c')
buf_c = [i for i in range(10) if i % 2 == 1]
print(buf_c)

print('buf_d')
buf_d = ['odd' if i % 2 == 1 else 'even' for i in range(10)]
print(buf_d)


print('リスト内包表記で0-9の2次元配列を作るA')
n = -1
def plus_one(i):
    global n
    n += 1
    return n
list2d_d = [[plus_one(i) for i in range(3)] for j in range(3)]
print(list2d_d)


print('リスト内包表記で0-9の2次元配列を作るB')
list2d_d = [[(j*3)+i for i in range(3)] for j in range(3)]
print(list2d_d)


print('zip')
l_str1 = ['a', 'b', 'c']
l_str2 = ['x', 'y', 'z']

l_zip = [(s1, s2) for s1, s2 in zip(l_str1, l_str2)]
print(l_zip)