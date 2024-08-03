"""
Col順番入れ替え
"""

import pandas as pd

# サンプルDataFrameの作成
data = {'Column1': [1, 2, 3],
        'Column2': [4, 5, 6],
        'Column3': [7, 8, 9],
        'Column4': [10, 11, 12]}
index_labels = ['Row1', 'Row2', 'Row3']
df = pd.DataFrame(data, index=index_labels)

# カラムの順番を入れ替え
new_order = ['Column3', 'Column1', 'Column4', 'Column2']
df = df[new_order]

# 結果表示
print(df)