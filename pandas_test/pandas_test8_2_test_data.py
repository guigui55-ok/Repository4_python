"""
文字列や時間の処理テスト

dfをprintしたものをコピペして、ソース上で扱う時ののデータ処理（検討中）
"""

import re

# 元の文字列
data_a = """
 ['001' 'ItemA' 1 '●' 50 Timestamp('2022-09-27 00:00:00')]
 ['002' 'ItemB' 2 '' 20 Timestamp('2021-07-20 00:00:00')]
"""

# Timestampの表現を変換
data_b = re.sub(r"Timestamp\('([^']+)'\)", r"'\1'", data_a)

# クォート内の要素間の空白をカンマに置換
data_b = re.sub(r"'\s+'", "', '", data_b)

# 数値と文字列の間、または記号と数値の間の空白をカンマに置換
data_b = re.sub(r"(\d)\s+'", r"\1, '", data_b)
data_b = re.sub(r"'\s+(\d)", r"', \1", data_b)

# 行の先頭と末尾の不要なスペースやクォートを除去し、適切なインデントを追加
data_b = re.sub(r"\n\s+'\[", "\n    ['", data_b)
data_b = re.sub(r"\]'\n", "']", data_b)

# 結果の文字列
result = "[\n" + data_b.strip() + "\n]"

print(result)