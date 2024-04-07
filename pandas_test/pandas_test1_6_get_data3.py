
import pandas as pd

# 例として、DataFrameを作成します
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

# DataFrameのインデックスを設定します
index_names = ['row1', 'row2', 'row3']

df = pd.DataFrame(data, index=index_names)
print(df)
print('----')

# 特定の行名と列名に値を設定します
# ここでは、行名が'row1'で列名が'B'の位置に値を設定しています
df_b = df.at['row1', 'B'] = 10
print('df_c')
print(df_b)
# df_b = df.at[df.loc['row1'] == 4]
# df_b = df.at[df['B'] == 4]
# df_b = df.at[df['B'] == '4']
df_c = df[df['B'] == '4']
df_c = df[df['B'] == '10']
df_c = df[df['B'] == 5]
# df_b = df[df['B'] == 10]
df_c['C'] = 22
print('df_c')
print(df_c)

print('****')
print('df')
print(df)