import numpy as np

x = np.array([1])
print(x) 
yi = np.array([0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,1,0,0,0,1,1,0])
print(yi)
#出力
#[0 0 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 1 1 0 1 1 0 0 0 1 1 0]
#[array([ 2,  5, 14, 17, 19, 20, 22, 23, 27, 28])]

m=30

flag=np.where(x==1)
print(flag)

flag = np.any(x==1)
print(flag)

# for i in range(m): 
#   if i in yi.any():
#     print("ある")
#   else:
#     print("ない")
