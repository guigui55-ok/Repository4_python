


range_a = range(10)
range_b = range(4)
#エラーは出ず小さい方に合わせられる（はみ出た部分は無視される）
print('****')
for i,j in zip(range_a, range_b):
    buf = (i,j)
    print(buf)

print('****')
for i,j in zip(range_b, range_a):
    buf = (i,j)
    print(buf)