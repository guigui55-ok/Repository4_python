
x = 800
n = 1
ret = ''
for i in range(8):
    n = n * 2
    if x - n == 0:
        ret = 'OK'
        break
else:
    ret = 'NG'
print(ret)

