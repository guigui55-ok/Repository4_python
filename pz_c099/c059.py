
from input.input import input,input_init_new
input_init_new('c059',1)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input())
parity_list = [list(list(input())) for _ in range(n)]

#読み込んだ文字列を2次元配列にして、行と列を変換し、変換後の行に1が1つ以上がるか判定する
import numpy as np
cnv_parity_list = np.array(parity_list).T.tolist()

ret = ''
for temp_list in cnv_parity_list:
    flag = False
    value_a = temp_list[0]
    if value_a == '1':
        value_a_flag = True
    else:
        value_a_flag = False
    for i in range(1,len(temp_list)):
        value_b = temp_list[i]
        if value_b == '1':
            value_b_flag = True
        else:
            value_b_flag = False
        if (value_a_flag and (not value_b_flag)) or ((not value_a_flag) and value_b_flag):
            flag = True
    if flag:
        ret += '1'
    else:
        ret += '0'

print(ret)
    

"""
入力例1
2
0011
0110
出力例1
0101
入力例2
4
0001
0010
0100
1000
出力例2
1111

"""