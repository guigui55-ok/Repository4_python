import copy

lst1 = [1, [2, 3], 4]
lst2 = list(lst1)
lst3 = copy.deepcopy(lst1)
# lst3 = copy.copy(lst1)
lst1[1][0] = 'X'

print(id(lst1))
print(id(lst2))
print(id(lst3))
print(id(lst1[1]))
print(id(lst2[1]))
print(id(lst3[1]))

print(lst2[1][0], lst3[1][0])
# https://qiita.com/Kaz_K/items/a3d619b9e670e689b6db
