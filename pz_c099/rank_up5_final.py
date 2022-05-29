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
        horizon = False
        vertical = False
        if x==0 and s[y][x+1]=="#":
            horizon = True
        elif x==w-1 and s[y][x-1]=='#':
            horizon = True
        elif s[y][x-1]=='#' and s[y][x+1]=="#":
            horizon = True
        
        if y==0 and s[y+1][x]=="#":
            vertical = True
        elif y==h-1 and s[y-1][x]=='#':
            vertical = True
        elif s[y-1][x]=='#' and s[y+1][x]=="#":
            vertical = True
        if vertical and horizon:
            ret_list.append('{} {}'.format(y,x))

for ret in ret_list:
    print(ret)


# h, w = map(int, input().split())
# s = [list(input()) for _ in range(h)]

# for y in range(h):
#     for x in range(w):
#         flag_row = False
#         flag_column = False

#         if x == 0 or s[y][x - 1] == "#":
#             if x == w - 1 or s[y][x + 1] == "#":
#                 flag_row = True

#         if y == 0 or s[y - 1][x] == "#":
#             if y == h - 1 or s[y + 1][x] == "#":
#                 flag_column = True

#         if flag_column and flag_row:
#             print(y, x)