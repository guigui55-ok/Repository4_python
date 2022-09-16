
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sympy import *
from sympy.abc import *

init_printing()

# 単位ベクトルとか角度の定義
angles = symbols("phi_0 phi_1 phi_2")# 原点から肩部への方向を表す角度
thetas = symbols("theta_0 theta_1 theta_2")# モーターの角度(±90deg)
unit_vectors = [Matrix([cos(angles[i]),sin(angles[i]),0]) for i in range(3)]
ez = Matrix([0,0,1])

# パラメータ(実数)
params = [(A,130.0),(B,200.0),(C,400.0),(D,130.0)]
params.append((angles[0],2.0*np.pi/3.0*0))
params.append((angles[1],2.0*np.pi/3.0*1))
params.append((angles[2],2.0*np.pi/3.0*2))
params.append((x,0))
params.append((y,0))
params.append((z,400))

# 各座標の計算
# A_vectors = map(lambda x: A*x, unit_vectors) #修正前
A_vectors = [(lambda x: A*x)(unit_vectors[i]) for i in range(3)]
B_vectors = [A_vectors[i] + B*(unit_vectors[i] * cos(thetas[i])-ez*sin(thetas[i]) ) for i in range(3)]

for val in B_vectors:
    print(val) #確認用

##########
# パターン2
A_vectors = []
for i in range(3):
    A_vectors.append(A*unit_vectors[i])

B_vectors = []
for i in range(3):
    B_dush_vector = B*(unit_vectors[i] * cos(thetas[i])-ez*sin(thetas[i]))
    B_vectors.append(A_vectors[i] + B_dush_vector)

print('*****')
for val in B_vectors:
    print(val) #確認用
##########

D_vector = Matrix([x,y,z])
C_vectors = [D_vector + D * unit_vectors[i] for i in range(3)]