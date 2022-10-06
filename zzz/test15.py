#https://teratail.com/questions/rpmha3057g8s2b


import numpy as np

a = np.array([[1, 2, 3],  [4, 5, 6]])
a = np.array([[1, 2, 3]])
print(a)
a = np.array([1, 2, 3]) * 1
print(a)
a = np.array([1, 2, 3] * 1)
print(a)
a = np.array([[1, 2, 3], 1])
print(a)

a = [1, 2, 3]
print(a)
b = [1, 2, 3] * 1
print(b)
print(a==b)
c = [1, 2, 3] * 2
print(c)

import torch

# x = torch.rand([10, 1, 128, 128],  requires_grad=True)
x = torch.rand([2, 1, 2, 3],  requires_grad=True)
y1 = x  # ➠ y=x*1 にすれば、エラーを引き起こす⚡
print('*****')
print(type(y1)) #<class 'torch.Tensor'>
print(len(y1))
print(y1)
y2 = x*1
y2 = torch.rand([2, 1, 2, 3],  requires_grad=True) * 1
y2.requires_grad=True
print('*****')
print(type(y2))
print(len(y2))
print(y2)
print( y1==y2 )
loss = torch.abs(y1).sum()
loss.backward()
y_grad = y1.grad.data   # ⚡エラー発生❣　


loss = torch.abs(y2).sum()
loss.backward()
y_grad = y2.grad.data   # ⚡エラー発生❣　