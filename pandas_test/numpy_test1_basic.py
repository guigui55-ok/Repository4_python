

# https://note.nkmk.me/python-numpy-insert/
import numpy as np

print('numpy.insert()で一次元配列に要素を挿入、追加')
ary = np.arange(4)
print(ary)

np.insert(ary, 2, 100)
ary = np.insert(ary, 2, 100)
print(ary)

ary = np.insert(ary, 1, [100, 101, 102])
print(ary)

ary = np.insert(ary, [0, 2, 4], [100, 101, 102])
print(ary)

print('一次元配列の要素を置換')
ary_b= ary.copy()
ary_b[1] = 100
print(ary_b)

ary_b = ary.copy()
ary_b[1:3] = [100, 101]
print(ary_b)
print(ary)

print('一次元配列の要素を削除')
ary_b = np.delete(ary_b, 4)


print('numpy.insert()で二次元配列に行を挿入、追加')
ary = np.arange(12).reshape((3, 4))
print(ary)

print('引数axis=None（デフォルト）とすると、元のndarrayが多次元配列の場合でも平坦化された一次元配列が返される。')
ary = np.insert(ary, 2, 100)
print(ary)

print('axisが設定されていると、その行すべてにvalueが適用される。1次元にはならない')
ary = np.arange(12).reshape((3, 4))
ary = np.insert(ary, 2, 100, axis=0)
print(ary)

print('一次元配列ndarrayを挿入')
ary_b = np.arange(100, 104)
print(ary_b)

print('ary_b を 2列目に（index=1）,列の0番目から')
ary_c = np.insert(ary, 1, ary_b, axis=0)
print(ary_c)
print('ary_b を 3列目に（index=3）,列の0番目から')
ary_c = np.insert(ary, 3, ary_b, axis=0)
print(ary_c)
print('ary_b を 1と2列目に（index=0,2,列の0番目から')
ary_c = np.insert(ary, [0, 2], ary_b, axis=0)
print(ary_c)

print('ary_b を 4列目に（index=5),列の1番目から')
ary_d = np.arange(100, 102)
ary_c = np.insert(ary, [4], ary_b, axis=1)
print(ary_c)


print('二次元配列ndarrayを挿入')
ary = np.arange(16).reshape((4, 4))
ary = np.arange(20).reshape((5, 4))
ary_c = np.arange(100, 112).reshape((3, 4))
print(ary_c)

print('ary の3列目に ary_c を挿入')
ary_d = np.insert(ary, 2, ary_c, axis=0)
print(ary_d)
# [[  0   1   2   3]
#  [  4   5   6   7]
#  [100 101 102 103]
#  [104 105 106 107]
#  [108 109 110 111]
#  [  8   9  10  11]]

# せんたくもの

print('ary に 1列だけ ary_c を挿入')
ary_d = np.insert(ary, 2, ary_c[2], axis=0)
print(ary_d)
# [[  0   1   2   3]
#  [  4   5   6   7]
#  [108 109 110 111]
#  [  8   9  10  11]]

print('ary の 0，2，3列目に それぞれ ary_cを追加')
print(ary)
ary_d = np.insert(ary, [0, 2, 3], ary_c, axis=0)
print(ary_d)
# [[100 101 102 103]
#  [  0   1   2   3]
#  [  4   5   6   7]
#  [104 105 106 107]
#  [  8   9  10  11]
#  [108 109 110 111]]

# print('ary の 0，2列目に それぞれ ary_cを追加')
# print(ary)
# ary_d = np.insert(ary, [0, 2], ary_c, axis=0)
# print(ary_d)
# ValueError
# shape mismatch: value array of shape (3,4) could not be broadcast to indexing result of shape (2,4)
# 列数とリストの数があっていないとError

print('range イテレータを使って挿入  [0,1,2] と同じ')
ary_d = np.insert(ary, range(3), ary_c, axis=0)
print(ary_d)
# [[100 101 102 103]
#  [  0   1   2   3]
#  [104 105 106 107]
#  [  4   5   6   7]
#  [108 109 110 111]
#  [  8   9  10  11]]


print('numpy.vstack()で二次元配列の先頭・末尾に行を追加')
print('vstack 1 aryの末尾')
ary_d = np.vstack((ary, ary_b))
print(ary_d)

print('vstack 2 aryの先頭')
ary_d = np.vstack((ary_b, ary))
print(ary_d)

print('二次元配列の行を置換')
ary_e = ary.copy()
ary_e = np.arange(0,20).reshape((5,4))
print(ary_e)
# ary_d = np.arange(200, 212).reshape((3, 4))
# ary_d = np.arange(200).reshape((3, 4))
# ary_d = np.arange(200, 212)
# 
# ary_d = np.arange(200, 204)
# ary_d = np.arange(200, 204).reshape((1,4))
ary_d = np.arange(200, 208).reshape((2,4))
print(ary_d)
print('##')
ary_e[2] = ary_d[1]
print(ary_e)


print('*************')
print('二次元配列の行を置換 2')
ary_e = np.arange(0,20).reshape((5,4))
# ary_d = np.arange(200, 208).reshape((2,4))
# print(ary_d[0, 2])
# ary_e[1:] = ary_d[0, 2]
ary_d = np.arange(100, 112).reshape((3, 4))
print(ary_d[[0, 2]])
# ary_e[1:] = ary_d[[0, 2]] #ValueError: could not broadcast input array from shape (2,4) into shape (4,4)
ary_e[3:] = ary_d[[0, 2]] #とにかく左辺と右辺の形状が同じならOK
print(ary_e)
# ary_d の各行を ary_e の特定の行にコピーする
ary_e[1, :] = ary_d[0, :]
ary_e[2, :] = ary_d[1, :]
print(ary_e)


print('*************')
print('numpy.insert()で二次元配列に ”列” を挿入、追加')
# 二次元配列ndarrayに列を挿入したい場合はaxis=1とする
print('ary_aa')
ary_aa = np.arange(0,12).reshape((3,4))
print(ary_aa)

print('2列目すべてに100を挿入')
ary_ac = np.insert(ary_aa, 1, 100, axis=1)
print(ary_ac)

print('ary_ab')
ary_ab = np.arange(100, 103)
print(ary_ab)

print('2列目に挿入')
ary_ac = np.insert(ary_aa, 1, ary_ab, axis=1)
print(ary_ac)
# ary_ac = np.insert(ary_aa, 1, ary_ab) # [  0 100 101 102   1   2   3   4   5   6   7   8   9  10  11]

print('4列目に挿入')
ary_ac = np.insert(ary_aa, 3, ary_ab, axis=1)
print(ary_ac)


print('*************')
print('numpy.insert()で二次元配列に ”列” を挿入、追加 part2')
print('ary_aa')
ary_aa = np.arange(0,12).reshape((3,4))
print(ary_aa)

print('ary_ad')
ary_ad = np.arange(300, 303)
print(ary_ad)

print('2列目にary_adを追加')
ary_ae = np.insert(ary_aa, 1, ary_ad, axis=1)
print(ary_ae)

print('2列目にary_ad ”すべて” を追加')
ary_ae = np.insert(ary_aa, [1], ary_ad, axis=1)
print(ary_ae)

print('2列目にary_ad ”すべて” を追加')
ary_ae = np.insert(ary_aa, [1, 3, 4], ary_ad, axis=1)
print(ary_ae)

print('ary_ae の1列目')
# ary_af = ary_aa.reshape((1, 3))
ary_ae = np.arange(500,503).reshape((1,3))
ary_ae = np.arange(500,503)
print(ary_ae)

print('ary_aa の1列目から ary_aeのすべてを追加')
ary_af = np.insert(ary_aa, 1, ary_ae, axis=1)
print(ary_af)


print('ary_aa の1列目から ary_aeの 2列目 を追加')
ary_af = np.insert(ary_aa, [1], ary_ae, axis=1)
print(ary_af)

print('ary_aa の1,3,4列目に ary_aeのすべて を追加')
ary_af = np.insert(ary_aa, [1, 3, 4], ary_ae, axis=1)
print(ary_af)


print('*************')
print('numpy.hstack()で二次元配列の先頭・末尾に列を追加')
print('ary_aa')
ary_aa = np.arange(0,12).reshape((3,4))
print(ary_aa)

print('ary_ad')
ary_ad = np.arange(300, 303).reshape((3,1))
print(ary_ad)

print('ary_ad2')
ary_ad2 = np.arange(300, 306).reshape((3,2))
print(ary_ad2)

print('末尾に追加')
ary_ae = np.hstack((ary_aa, ary_ad))
print(ary_ae)

print('先頭に追加')
ary_ae = np.hstack((ary_ad, ary_aa))
print(ary_ae)

print('末尾に追加 すべて')
ary_ae = np.hstack((ary_aa, ary_ad2))
print(ary_ae)

print('先頭に追加 すべて')
ary_ae = np.hstack((ary_ad2, ary_aa))
print(ary_ae)


# https://tech-lab.sios.jp/archives/21127
# https://qiita.com/tttmurakami/items/677655725853f1b5a429
# https://ai-trend.jp/programming/python/what-is-numpy/