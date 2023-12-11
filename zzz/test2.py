
# for i in range(1):
#     print(i)



buf = ''
for i in range(1000):
    if i==0:continue
    buf = ['2']*i
    buf = ''.join(buf)
    buf = int(buf)
    print(buf)
print()
print('*****')
print(buf + 1)