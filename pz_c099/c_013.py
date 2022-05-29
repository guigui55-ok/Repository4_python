
from input.input import input,input_init_new
input_init_new('c013',1)



"""
・1行目に嫌いな数字 n (0から9までの1桁の数字)
・2行目に病室の総数 m
・3行目以降に各病室の部屋番号を表す整数 r_i (1 <= i <= m)

"""

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = input()
count = int(input())
room_list = [input() for _ in range(count)]

#嫌いな番号が含まれないもののみをリストに追加する
ret_list=[]
for room_num_str in room_list:
    if room_num_str.find(n)<0:
        ret_list.append(room_num_str)

#結果出力する
if len(ret_list)>0:
    for ret in ret_list:
        print(ret)
else:
    print('none')


"""
入力例1
4
5
101
204
301
401
501
出力例1
101
301
501
入力例2
9
3
409
509
109
出力例2
none
入力例3
1
6
101
102
205
224
231
314
出力例3
205
224"""