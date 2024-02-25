"""
pandas ファイル読み込み＋ソート
"""

import pandas as pd
path = "https://aiacademy.jp/dataset/sample_data.csv"
path = r'C:\Users\OK\source\repos\Repository4_python\pandas_test\related_data_japanese_updated.csv'
# df = pd.read_csv(
#     path,
#     encoding="cp932",
#     skiprows=1,) #1行読み飛ばす
df = pd.read_csv(
    path,
    encoding="utf-8",
    skiprows=0,) #1行読み飛ばす
print('### data.dtypes = ')
print(df.dtypes)


"""
エクセルの場合は下記のように使います。
.read_excel("任意のファイル名.xlsx",encoding='utf8')

例えば、Pandasでcsvファイルを読み込む場合は、「read_csv」を使い、
データの出力には「to_csv」や「to_excel」などが利用可能です。
csv以外にも、「read_json」や「read_excel」、「read_json」「read_sql」もあり、
それらの出力メソッドもあります。
TSVファイルの場合は、「read_table」を使うことで区切り文字がタブ\tのファイルを処理することが出来ます。
"""

df.sort_index(ascending=False)
# # df.sort_values(by=1)
# df = df.sort_values(by='名前')
# df = df.sort_values(by='給与')
# # 複数列を基準にソートできる。
# df = df.sort_values(['部署', '名前'])
# # 昇順・降順
# # それぞれの列に対して昇順・降順
# df = df.sort_values(['部署', '名前'], ascending=False)
# 昇順・降順の組み合わせは複数回実行する
# df = df.sort_values(by='給与', ascending=True)
# df = df.sort_values(by='管理職', ascending=False)

# # 文字列の長さ（文字数）でソートする例は以下の通り。
# df = df.sort_values('名前', key=lambda s: s.str.len())

# 行を基準に、列を入れ替え
# df = df.select_dtypes('number')
# df = df.sort_values('給与', axis=1) #Error
# df = df.sort_values(by=0, axis=1, ascending=False)

######
# data = {
#     'name':['A','B','C'],
#     'A': [3, 1, 2],
#     'B': [15, 16, 14],
#     'C': [27, 29, 18]
# }
# data = {
#     'A': [3, 1, 2],
#     'B': [15, 16, 14],
#     'C': [27, 29, 18]
# }
# df = pd.DataFrame(data)
# df = df.sort_values(by=1, axis=1, ascending=False)
######
# 元のオブジェクトを変更: 引数inplace
df = df.copy()
df.sort_values('部署', inplace=True)
# print(df_copy)

print('### type(data) = ')
print(type(df)) # <class 'pandas.core.frame.DataFrame'>
print('### data = ')
print(df)
