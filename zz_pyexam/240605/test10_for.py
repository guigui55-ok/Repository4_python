buf = [x*2 for x in [i**2 for i in range(4)]]
print(buf)

i=0
buf = [i*2 for x in [i**2 for i in range(4)]]
print(buf)

buf = [x*2 for x in [i**2 for i in range(3)]]
print(buf)

x2 =0
i2 =0
buf = [x2 for x in [i2 for i in range(4)]]
print(buf)