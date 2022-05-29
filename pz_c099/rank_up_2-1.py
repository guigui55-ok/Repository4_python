"""
"""
from input.input import input,input_init_new
input_init_new('rank_up_lesson5',1)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
h,w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ret_list = []
for y in range(h):
    for x in range(w):
        flag = False
        if s[y][x] == '#':
            flag = True
        if flag:
            ret_list.append('{} {}'.format(y,x))

for ret in ret_list:
    print(ret)


H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            print(y, x)