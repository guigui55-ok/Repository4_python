# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
H, W, N = map(int, input().split())
S = [list(input()) for _ in range(H)]
for _ in range(N):
  y, x = map(int, input().split())
  S[y][x] = '#'

ret = ''
for s in S:
    for buf in s:
        ret += buf
    else:
        ret += '\n'
print(ret)


###################
h, w, n = map(int, input().split())
s = [list(input()) for _ in range(h)]

for _ in range(n):
    y, x = map(int, input().split())
    s[y][x] = "#"

for y in range(h):
    print("".join(s[y]))