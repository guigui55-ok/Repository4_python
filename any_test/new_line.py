print('abc')
print('a\na')
buf = 'b\nb'
print(buf)
with open('test.txt','w', encoding='utf-8') as f:
    f.write(buf)
