


x = []
y1 = []
y2 = []
ylist = [y1,y2]
i = 0
datalist = ['3,30,100.txt','3,30,200.txt']
c1, c2 = 'blue','green'

for y in ylist:
 for l in datalist:
    # open(l).readlines()
    # data = l[:-1].split()  #なぜか'~~.txt'ではなく'~~.tx'と最後のtだけ読み込まれない。
    data = l.split()
    print('data={}'.format(data))
    # x += [i]
    # y += [float(data[0])]
    i += 1


text = 'aaa\n'
buf = text[:-1].split()
print(buf)