import pandas as pd

# df_aとdf_bのデータをDataFrameオブジェクトとして作成
data_a = [
    ['A001', '01_A001', ''],
    ['A002', '01_A002', ''],
    ['A003', '01_A003', ''],
    ['A004', '01_A004', ''],
    ['A005', '01_A005', ''],
    ['A006', '02_A006', ''],
    ['A007', '02_A007', ''],
    ['A015', '03_A015', ''],
    ['A016', '03_A016', ''],
    ['A017', '03_A017', ''],
    ['A012', '04_A012', ''],
    ['A013', '04_A013', ''],
    ['A014', '04_A014', ''],
    ['A008', '05_A008', ''],
    ['A009', '05_A009', ''],
    ['A010', '05_A010', ''],
    ['A011', '05_A011', '']
]
df_a = pd.DataFrame(data_a, columns=['ID', 'Name', 'Result'])

data_b = [
    ['A001', '01_A001', 'OK', 'A001', 0],
    ['A002', '01_A002', 'NG', 'A002', 0],
    ['A003', '01_A003', 'OK', 'A003', 0],
    ['A004', '01_A004', 'OK', 'A004', 0],
    ['A005', '01_A005', 'OK', 'A005', 0],
    ['A006', '02_A006', 'OK', 'A006', 0],
    ['A007', '02_A007', 'NG', 'A007', 0],
    ['A008', '05_A008', 'OK', 'A008', 0],
    ['A009', '05_A009', 'OK', 'A009', 0],
    ['A010', '05_A010', 'NG', 'A010', 0],
    ['A011', '05_A011', 'OK', 'A011', 0],
    ['A012', '04_A012', '#N/A', 'A012', 0],
    ['A013', '04_A013', 'OK', 'A013', 0],
    ['A014', '04_A014', 'NG', 'A014', 0],
    ['A015', '03_A015', 'OK', 'A015', 0],
    ['A016', '03_A016', 'NG', 'A016', 0]
]
df_b = pd.DataFrame(data_b, columns=['ID', 'Name', 'Result', 'ID2', 'Result2'])

# df_bのResult列をdf_aのResult列にコピー
# df_a = df_a.set_index('ID').combine_first(df_b.set_index('ID')['Result']).reset_index()
# エラーの原因は combine_first メソッドを使用する際に、データフレームの軸（axis）の指定が適切でないことにあります。combine_first メソッドは、一方のデータフレームのnullまたは欠損値を他方のデータフレームの値で埋めるために使われますが、この場合は単に df_b の Result 列を df_a の Result 列にコピーするだけなので、他の方法を使う方が適切です。

####
# df_aとdf_bをID列に基づいて結合
merged_df = pd.merge(df_a, df_b[['ID', 'Result']], on='ID', how='left')
# df_aのResult列をdf_bのResult列で更新
# df_a['Result'] = merged_df['Result']
df_a['Result'] = merged_df['Result_y']
####

# ###
# # df_bのIDとResult列を辞書として抽出
# result_map = df_b.set_index('ID')['Result'].to_dict()
# # print(result_map) #{'A001': 'OK', 'A002': 'NG', 'A003': 'OK',
# # df_aのResult列をマッピングで更新
# df_a['Result'] = df_a['ID'].map(result_map)
# ###

# ###
# # df_bをID列をインデックスとして設定
# df_b_indexed = df_b.set_index('ID')
# # df_aと結合して必要な列を選択
# df_a = df_a.join(df_b_indexed['Result'], on='ID', how='left', rsuffix='_b')
# df_a['Result'] = df_a['Result_b']
# df_a.drop(columns=['Result_b'], inplace=True)
# ###

# 結果を表示
print(df_a)


from pathlib import Path
from excel_data import ExcelSheetDataUtil
print('*テーブルにデータ入力DataFrame')
file_name = 'myworkbook.xlsx'
# ### 書き込み処理するときは念のためバックアップ
# import shutil
# back_path = Path(__file__).parent.joinpath('back')
# back_path.mkdir(exist_ok=True)
# shutil.copy(file_name, back_path)
# ###
sheet_name = 'input_data'
file_path = Path(__file__).parent.joinpath(file_name)
ex_data = ExcelSheetDataUtil(file_path, sheet_name, data_only=True)