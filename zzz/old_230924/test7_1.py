
# import keras
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Activation
# from keras.optimizers import RMSprop
# from keras.layers import LSTM
# from keras.models import Model
# from keras import Input
# from keras.preprocessing.image import ImageDataGenerator
# from keras.preprocessing import image
# from keras.callbacks import TensorBoard, ModelCheckpoint
# from sklearn.metrics import mean_squared_error
# from keras.models import load_model
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import math
import csv
import matplotlib.patheffects as path_effects
import os
import sys

x = []
y = []
y1 = []
y2 = []
ylist = [y1,y2]
# i = 0
datalist = ['3,10,100.txt','1,30,200.txt']
c1, c2 = 'blue','green'

# datalist = ['1,10,100.txt','3,30,200.txt','5,50,200.txt']
# c = ['blue','green','red']


import numpy as np
x_list = []
y_list = []

for y in ylist:
 for l in datalist:
    # open (l).readlines()
    data = l.split(',')  #なぜか'~~.txt'ではなく'~~.tx'と最後のtだけ読み込まれない。
    # print(data)
    # x += data[i]
    # y += [float(data[0])]
    # i += 1
    x_list.append(float(data[0]))
    y_list.append(float(data[1]))

# データ生成
# x = np.linspace(0, 10, 100)
# y = x + np.random.randn(100) 
plt.title("data")
plt.xlabel("x")
plt.ylabel("y")
# 上記で配列に格納されているx座標、y座標にファイル名を色を指定して描画する。
# for i in range(len(datalist)):
#     buf_x, buf_y, buf_c = x[i], y[i], c[i]
#     print('x={}, y={}, c={}'.format(buf_x, buf_y, buf_c))
#     plt.plot(buf_x,buf_y,color=buf_c)
#     plt.scatter(buf_x, buf_y, c=buf_c)
#     plt.text(buf_x, buf_y, s=datalist[i], c=buf_c)

plt.plot(x_list, y_list, c=c1)
plt.plot(y_list, x_list, c=c2)

plt.savefig("3,30,x.png")
