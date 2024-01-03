


buf_a = 123
id('buf_a id = ')
print(id(buf_a))
buf_b = buf_a
id('buf_b id = ')
print(id(buf_b))
buf_c = 123
id('buf_c id = ')
print(id(buf_c))

print('------')
buf_a = 12345
id('buf_a id = ')
print(id(buf_a))
buf_b = buf_a
id('buf_b id = ')
print(id(buf_b))
buf_c = 12345
id('buf_c id = ')
print(id(buf_c))
# print(id(buf_a),id(buf_b),id(buf_c))
print('------')
buf_a = 1234567
id('buf_a id = ')
print(id(buf_a))
buf_b = buf_a
id('buf_b id = ')
print(id(buf_b))
buf_c = 1234567
id('buf_c id = ')
print(id(buf_c))