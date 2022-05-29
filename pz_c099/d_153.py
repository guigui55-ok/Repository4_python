
from input.input import input,input_init_new
input_init_new('d_153',1)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
# price_list = map(int, input().split())
# print(type(price_list)) #<class 'map'>
price_list = list(map(int, input().split()))
print(type(price_list))
exit(0)
a,b,c = map(int, input().split())
price_list:list = [a,b,c]
remove_list = [max(price_list),min(price_list)]
for rm_val in remove_list:
    price_list.remove(rm_val)
for price in price_list:
    print(price)