
from input.input import input,input_init_new
input_init_new('c095',1)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s = input()
t = input()

flag = False

if s==t:
    #完全一致するものはNG
    flag = False
elif len(s)!=len(t):
    #文字列の数が一致しないものもNG
    flag = False
else:
    #1文字ずつ確認して、一致したものを消す。消していった結果が空文字であればflag=Trueとする
    temp_s:str = s
    for i in range(len(t)):
        t_char = t[i]
        pos = temp_s.find(t_char)
        if pos>=0 and len(temp_s)==1:
            #pos>=0 and 残り1文字ならすべて合致とする
            flag=True
            break
        if pos==0:
            temp_s = temp_s[pos+1:]
        elif pos==len(temp_s)-1:
            temp_s = temp_s[:-1]
        elif pos>=0:
            temp_s = temp_s[:pos] + temp_s[pos+1:]
        else:
            #存在しない文字が1つでもあればNGとする
            flag =False
            break

#結果を出力する
if flag:
    ret = 'YES'
else:
    ret = 'NO'
print(ret)
