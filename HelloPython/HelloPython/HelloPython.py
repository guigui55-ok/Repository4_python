import sys
from math import cos, radians
print("Hello Python!")

for i in range(360):
    print(cos(radians(i)))

import tkinter
frm = tkinter.Tk()
frm.geometry('600x400')
frm.mainloop()

#https://qiita.com/AI_Academy/items/b97b2178b4d10abe0adb

print(10) # 数値はクォーテーションで囲む必要はありません。
print(10 + 5) # 足している
print(5 - 2)  # 引いている
print(10 / 2)   # 割っている
print(10 % 5)   # あまりを求めている

# 優先順位の変更
# 通常は +と-よりも*や/の方が優先度が高いですが、()で囲むことで優先度を変えることができます。
print((20 - 5) // 3)  # 5 

var = "var"
Var = "Var"
print(var) # varと出力される
print(Var) # Varと出力される

# Pythonで変数名をつける際に２単語続ける場合
lowercase_underscore = "lowercase_underscore" # 推奨
lowercaseunderscore = "lowercase_underscore"  # 非推奨

hello_world = "Hello, World" # 推奨
helloworld  = "Hello, World" # 非推奨


# 上記のように変数名はすべて小文字で2つ以上の単語をつなげる場合は下線(_)を使うようにすることが推奨されています。
# また非推奨の書き方で、変数を定義することもできます。しかしプログラムにはエラーは出ませんが、推奨されている方法を使いましょう。


#予約語
"""
Python3.6系での予約語ですので、それらは変数名などに使用できません。

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue',
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']
"""

#データ型の全体像
"""
基本的なデータ型
　整数型
　Bool型
　コンテナ型
　　シーケンス型
　　　リスト型
　　　文字列型
　　集合型
　　　集合型
　　マップ型
　　　マップ型　
"""
