
import re

# 与えられた文字列のリスト
str_val_list = [
    'ItemA_001 50 OK',
    'ItemB_002 80 NG',
    'ItemC_003 90 OK'
]

# 正規表現パターン：'Item[任意の文字]_000' の後の数字を抽出
pattern = r'Item._\d{3}\s(\d+)'
# pattern = r'Item._(\d{3})\s(\d+)'

# 各文字列に対してパターンを適用し、数字の部分を抽出
# extracted_numbers = [re.search(pattern, s).group(1) for s in str_val_list if re.search(pattern, s)]
extracted_numbers = []
for val in str_val_list:
    ret = re.search(pattern, val)
    if ret!=None:
        buf = ret.group(1)
        extracted_numbers.append(buf)

print(extracted_numbers)

"""
groupメソッドについて
Pythonの正規表現で group() メソッドは、正規表現によってマッチした部分文字列を取得するために使用されます。正規表現パターン内でカッコ () によって指定された部分は「キャプチャグループ」と呼ばれ、これによりマッチした部分文字列を個別に取得することができます。

group(1) は、正規表現パターン内の最初のキャプチャグループにマッチした文字列を返します。例えば、正規表現 r'Item._\d{3}\s(\d+)' の中で、(\d+) は最初のキャプチャグループになります。これは、空白文字 \s の後に続く1つ以上の数字 \d+ にマッチします。

したがって、group(1) はこの数字部分を取得し、それを結果のリストに追加します。上記のコードでは、各文字列に対してこの正規表現パターンを適用し、group(1) を使用して各文字列の数字部分を抽出しています。
"""