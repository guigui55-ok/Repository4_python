str_val_list = [
    'ItemA 55',
    'ItemB 66',
    'ItemC 80',
]

str_val_list_ret = [
    'ItemA ,55',
    'ItemB ,66',
    'ItemC ,80',
]


# [
#     'ItemA ,55',
#     'ItemB ,66',
#     'ItemC ,80'
# ]
# ``` &#8203;``【oaicite:0】``&#8203;

# str_val_list_ret = []
# for str_val in str_val_list:
#     # str_valのpattern1 'Item[アルファベット]' pattern2'[数値]'
#     # buf = pattern1 +  ',' + pattern2
#     str_val_list_ret.append(buf)

import re
# 元のリスト
str_val_list = [
    'ItemA 55',
    'ItemB 66',
    'ItemC 80',
]

# 変換処理
str_val_list_ret = []
for str_val in str_val_list:
    # 正規表現でpattern1とpattern2を分割
    pattern1, pattern2 = re.match(r'(Item[A-Z]+) (\d+)', str_val).groups()
    # buf = pattern1 + ',' + pattern2
    buf = pattern1 + ' ,' + pattern2
    str_val_list_ret.append(buf)

print(str_val_list_ret)