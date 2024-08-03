import pandas as pd

# サンプルデータを作成
data = {'dir': ['path1', 'path3', 'path2', 'path3', 'path1', 'path4'],
        'value': [10, 40, 20, 50, 30, 60]}
df = pd.DataFrame(data)

# 'dir'列でソートする
df_sorted = df.sort_values(by='dir')

# 'dir'列の値が重複する行を除外する
df_unique = df_sorted.drop_duplicates(subset='dir')

print("ソート後のデータフレーム:")
print(df_sorted)
print("\n重複を除外した後のデータフレーム:")
print(df_unique)