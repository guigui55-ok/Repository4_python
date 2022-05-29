"""
"""
from input.input import input,input_init_new
input_init_new('rank_up_lesson3_input',1)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
h,w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ret_list = []
for y in range(h):
    for x in range(w):
        flag = False
        if x==0 and s[y][x+1]=="#":
            flag = True
        elif x==w-1 and s[y][x-1]=='#':
            flag = True
        elif s[y][x-1]=='#' and s[y][x+1]=="#":
            flag = True
        if flag:
            ret_list.append('{} {}'.format(y,x))

for ret in ret_list:
    print(ret)


h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        if x == 0 or s[y][x - 1] == "#":
            if x == w - 1 or s[y][x + 1] == "#":
                print(y, x)