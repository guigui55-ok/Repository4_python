from input.input import input,input_init
input_init()
init_val = input()
print(init_val)


matrix = [
[11, 12, 13, 14],
[21, 22, 23, 24],
[31, 32, 33, 34],
]
print(str(matrix).replace('],','],\n'))
#https://python-academia.com/list-transpose/


# https://qiita.com/oyoshi0022/items/7475951f465d20ad4970
dp=[[0]*3 for i in range(5)]
print(dp)


def tow_dim_np_test():
    import numpy as np

    # 配列の宣言・初期化
    X = np.array([[1, 2, 3],
                [4, 5, 6]])
        
    # 参照    
    print(X[0][1]) # 2 (0行目1列目の要素)
    print(X[0,1])  # 2 (0行目1列目の要素)
    print(X[0:2, 0:2]) # [[1 2] (0～1行目,0～1列目の要素)
                    #  [4 5]]
        
    # 代入
    X[0:2, 0:2] = 10
    print(X)     # [[10 10  3]
                #  [10 10  6]]  

tow_dim_np_test()