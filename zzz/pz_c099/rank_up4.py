"""
"""
from input.input import input,input_init_new
input_init_new('rank_up_lesson4',1)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
h,w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ret_list = []
for y in range(h):
    for x in range(w):
        flag = False
        if y==0 and s[y+1][x]=="#":
            flag = True
        elif y==h-1 and s[y-1][x]=='#':
            flag = True
        elif s[y-1][x]=='#' and s[y+1][x]=="#":
            flag = True
        if flag:
            ret_list.append('{} {}'.format(y,x))

for ret in ret_list:
    print(ret)


h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        if y == 0 or s[y - 1][x] == "#":
            if y == h - 1 or s[y + 1][x] == "#":
                print(y, x)