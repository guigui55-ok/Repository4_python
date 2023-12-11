

for i in range(4,6):
    print(i)

# l = []
# print(max(l))

l = [buf for buf in range(100)]

for i in l:
    if i % 5 == 0:
        l.remove(i)
print(l)

l = [1,2,3,4]
for i, val in enumerate(l):
    if len(l) < i+2 :break
    print(i+1)