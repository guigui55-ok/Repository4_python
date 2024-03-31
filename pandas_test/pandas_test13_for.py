import pandas as pd

# サンプルDataFrameの作成
data = {'Column1': [1, 2, 3],
        'Column2': [4, 5, 6],
        'Column3': [7, 8, 9]}
index_labels = ['Row1', 'Row2', 'Row3']
df = pd.DataFrame(data, index=index_labels)

# インデックス指定で各行に対して処理を行う
for index_label in df.index:
    # インデックスラベルを使って行を取得
    row = df.loc[index_label]
    
    # 取得した行のデータを表示
    print(f"Processing {index_label}")
    print(row)
    print("------")

print("##########################")
# 行と列のインデックスを使って各セルに対して処理を行う
for row_index in df.index:
    # インデックスラベルを使って行を取得
    row = df.loc[row_index]
    # 取得した行のデータを表示
    print(f"Processing {row_index}")
    for col_index in row.index:
        # 各セルの値を取得
        cell_value = df.loc[row_index, col_index]
        # 取得したセルのデータを表示
        print(f"    {col_index}: {cell_value}")