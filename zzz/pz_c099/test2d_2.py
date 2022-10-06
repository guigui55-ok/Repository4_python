from input.input import input,input_init
input_init()
init_val = input()
# print(init_val)


def two_dim_test1():

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

    print('-----')
    val = input()
    ary = val.split(' ')
    dp.append(ary)
    print(dp)
    print(dp[5][0])


#######################################
def tow_dim_np_test4():
    import numpy as np
    print('********** ')
    # 配列の宣言・初期化
    row,col  = 2,3
    np_ary = np.zeros((row, col))
    print(np_ary)
#  [[0. 0. 0.]
#  [0. 0. 0.]]
    ##
    row,col  = 2,0
    np_ary = np.zeros((row, col))
    print(np_ary)
    np_ary = np.append(np_ary,0)

    ##
    row,col  = 2,3
    np_ary = np.zeros((row, col))
    np_ary_ex = np.array([10,11,12])
    # print(np.append(np_ary, np_ary_ex, axis=0))
    #all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)

    # print(np.append(np_ary, np_ary_ex, axis=1))
    #ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
    
    ##
    row,col  = 2,3
    np_ary = np.zeros((row, col))
    np_ary_ex = np.arange(6).reshape(2, 3) * 10 #OK
    np_ary_ex = [np.array([10,11,12])] #OK
    # np_ary_ex = np.array([10,11,12]) #NG
    print(np.append(np_ary, np_ary_ex, axis=0))
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 0 10 20]
#  [30 40 50]]
#######################################
def tow_dim_np_test4_0():
    import numpy as np
    print('********** ')
    # 配列の宣言・初期化
    np_ary = np.array([])
    print(np_ary)
    np_ary = np.append(np_ary,[[4, 5, 6]])
    print(np_ary)
    add_ary = [np.array([1,2,3])]
    np_ary = np.append(np_ary,add_ary)
    print(np_ary)


#######################################
def tow_dim_np_test3():
    import numpy as np
    class NpTest():
        pass
    # 配列の宣言・初期化
    X = np.array([[NpTest(), 2, 3],
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

# two_dim_test1()
tow_dim_np_test4()
# tow_dim_np_test3()