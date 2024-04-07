"""
表のAとBを比較して、差分を表示させる（新たにDataFrameの表を作成して、別の場所に書き込み）
    差分あり〇、削除された×、新しく追加されたNew、変わらない＞空白
 （差分は別のシートに出力される）
    書き込み前に、書き込み先のシートの有効範囲をすべて削除する
     ** 別テーブルMerge版（異なる行、異なる列のテーブル）
     DataFrame、StrCellを使用、書式はなし
"""


from excel_data import ExcelSheetDataUtil
from pathlib import Path


print('*書き込みシートをすべてクリア')
file_name = 'myworkbook.xlsx'
sheet_name = 'Write'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=True)
clear_address = ex_data.reset_valid_cells()
print('clear_address = {}'.format(clear_address))

print('*コピー元表Aの範囲を読み込み')
sheet_name = 'Copy'
ex_data.set_sheet(sheet_name)
keyword = '■DF抽出_and_書式コピー表A'
ex_data.set_address_by_find(keyword, 'A35', 'I50', debug=False)
print('begin_address = {}'.format(ex_data.cell.coordinate))
ex_data.move_address(1,0)
ex_data.range_address = ex_data.get_range_address()
print('range_address = {}'.format(ex_data.range_address))

df_a = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=None)
print('df_a = ')
first_row_as_list = df_a.iloc[0].astype(str).tolist()
df_a.columns = first_row_as_list
print(df_a.columns)
# print(df_a.values)
print(df_a.shape)


print('*マージする表Bの範囲を読み込み')
sheet_name = 'Copy'
ex_data.set_sheet(sheet_name)
keyword = '■DF抽出_and_書式コピー表B'
ex_data.set_address_by_find(keyword, 'L34', 'P46', debug=False)
print('begin_address = {}'.format(ex_data.cell.coordinate))
ex_data.move_address(1,0)
ex_data.range_address = ex_data.get_range_address()
print('range_address = {}'.format(ex_data.range_address))

df_b = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=None)
print('df_b = ')
first_row_as_list = df_b.iloc[0].astype(str).tolist()
df_b.columns = first_row_as_list
print(df_b.columns)
# print(df_b.values)
print(df_b.shape)

# 異なる部分のみを表示、アドレス（df_a,df_b、row,col）、差異内容


import pandas as pd
###
# 同じ列名のみを抽出
same_columns = []
for df_a_column in df_a.columns:
    is_match = False
    for df_b_column in df_b.columns:
        if df_a_column == df_b_column:
            same_columns.append(df_b_column)
            is_match = True
            break
# 統合に使用する列は、df_aの一番左とする。この列は比較・更新の対象外とする。
id_column = df_a.columns[0]
same_columns.remove(id_column)
###
# 結合処理
# df_aにdf_bを結合して、df_bの値で更新
# 重複しない列は含める
# df_merged = pd.merge(df_a, df_b, on=['番号', '分類'], how='outer', suffixes=('', '_b'))
df_merged = pd.merge(df_a, df_b, on=[id_column], how='outer', suffixes=('', '_b'))

print('df_merged.columns = ')
print(df_merged.columns)

# 結果格納用のDataFrameを作成
df_c = pd.DataFrame()
import math
def apply_proc(row):
    """
    DataFrameの各値の差分を比較して、その比較結果文字列（〇、×、New）を出力する。
        A==Bは空白、A!=Bは〇、AがあってBがないものは×、AがなくてBにある場合はNew
    
    Memo:
        Cellで値がないときは 空白''かNoneとなり、
        DataFrameで新規に行列を追加した場合は float(nan)となるので、すべてに対応している。
    """
    ### Inner Method BEGIN
    def is_nan(value):
        try:
            return math.isnan(value)
        except ValueError as e:
            return False
        except TypeError: #TypeError: must be real number, not str
            return False
        except Exception as e:
            print(str(e))
            return False
    ### Inner Method END
    if row[original_col] != row[original_col + '_b']:
        print('{}, {}'.format(row[original_col], row[original_col + '_b']))
        if str(row[original_col])=='' or row[original_col]==None or is_nan(row[original_col]):
            return "New"
        elif is_nan(row[original_col + '_b']):
            return "×"
        else:
            return "〇"
    else:
        return ""

# 列ごとに処理
for col in df_merged.columns:
    if '_b' in col:
        # 元の列名を取得（接尾辞を除去）
        original_col = col.rstrip('_a').rstrip('_b')
        # if original_col + '_a' in df_merged and original_col + '_b' in df_merged:
        # columna_nameとcolumna_name_bがあるcolumn配下の処理
        if (original_col in df_merged) and (original_col + '_b' in df_merged):
            # 前の値が空なら、Newにする
            
            # 値が異なる場合は "〇"、同じ場合は "" をセット
            # apply_proc = lambda row: "〇" if row[original_col] != row[original_col + '_b'] else ""
            buf_data = df_merged.apply(apply_proc, axis=1)
            df_c[original_col] = buf_data
        elif original_col in df_merged:
            df_c[original_col] = ""
    else:
        # '番号' と '分類' 列はそのままコピー
        df_c[col] = df_merged[col]

    # df_bにのみ存在する列は "New" をセット
    for col in df_b.columns:
        if not col in df_a.columns:
            df_c.loc[1:, col] = "New"


#列を入れ替え（備考が2番目に来るので）
# 順番を入れ替えたい列を保持
target_col = "備考"
df_target = df_c[target_col]
buf_index = [i for i, x in enumerate(df_c.columns) if x==target_col]
index = buf_index[0]
# 入れ替え対称の列を削除
df_d = df_c.drop(target_col, axis=index)
# 任意の場所に対象の列を挿入
df_d.insert(len(df_d.columns), target_col, df_target)


print('****************')
print('df_c = ')
df_c = df_d
print(df_c)


print('*開始セルアドレスをセットして、dfの配列を順番に書き込んでいく')
dist_ex_data = ex_data.copy_self()
dist_ex_data.set_sheet('Write')
dist_ex_data.set_cell('C3')

from openpyxl.cell import Cell
w_df = df_c
# df_aの1行目のデータをdf_bの1行目にコピー
# 共通の列にのみ値をコピーする
common_columns = [col for col in df_a.columns if col in df_c.columns]
df_c.loc[0, common_columns] = df_a.iloc[0][common_columns].values
# 
print('*DataFrameをエクセルに書き込む')
for i , column_name in enumerate(w_df.columns):
    print('Processing {}'.format(i))
    for j, data_series_value in enumerate(w_df[column_name]):
        value = data_series_value
        cell:Cell = dist_ex_data.get_offset_cell(j, i)
        dist_ex_data.set_value(value, cell.coordinate)
        print('[i ,j] = [{}, {}] = ({}){}'.format(i, j, cell.coordinate, value))
        cell.value = value
    print('-------')
print()
ex_data = dist_ex_data


# # 'ID'列を文字列型に変換
# df_a['ID'] = df_a['ID'].astype(str)
# df_b['ID'] = df_b['ID'].astype(str)

# import pandas as pd
# # df_aとdf_bを'ID'列を基にして結合
# # df = pd.merge(df_a, df_b, on='番号', how='left')
# # df = df_a.join(df_b) #OK
# ###
# # 同じ列名のみを抽出
# same_columns = []
# for df_a_column in df_a.columns:
#     is_match = False
#     for df_b_column in df_b.columns:
#         if df_a_column == df_b_column:
#             same_columns.append(df_b_column)
#             is_match = True
#             break
# # 統合に使用する列は、df_aの一番左とする。この列は比較・更新の対象外とする。
# id_column = df_a.columns[0]
# same_columns.remove(id_column)
# ###
# # 結合処理
# # df_aにdf_bを結合して、df_bの値で更新
# # 重複しない列は含める
# # df_merged = pd.merge(df_a, df_b, on=['番号', '分類'], how='outer', suffixes=('', '_b'))
# df_merged = pd.merge(df_a, df_b, on=[id_column], how='outer', suffixes=('', '_b'))
# print()
# print('******')
# print(df_merged)
# # df_bの値でdf_aの同じ列の値を更新
# for col in same_columns:
#     df_merged[col] = df_merged[col + '_b'].combine_first(df_merged[col])
# # 不要な列を削除
# # del_columns = [col + '_b' for col in df_b.columns if '_b' in col]
# del_columns = [col for col in df_merged.columns if '_b' in col]
# df_merged.drop(columns=del_columns, inplace=True)
# df = df_merged
# ###
# # 欠損値NaNを共通の値で一律に置換
# # df.fillna(StrCell('')) #
# print('##########')
# print('marged df = ')
# print(df)
# print('##########')
# print()
# # col_index_b = list(df_b.columns).index('Result')
# # col_index_a = list(df_a.columns).index('Result')
# # for i, key in enumerate(df_b['ID']):
# #     # val = df_b['ID' == key]['Result']
# #     # df_buf = df_b.query('ID == "{}"'.format(key))
# #     if i==0:
# #         df_buf = df_b.loc[df_b.ID == key]['Result']
# #         print(type(df_buf))
# #         # print(df_buf.info())
# #         print(df_buf.shape)
# #         print(df_buf.values[0])
# #         # val = df_buf['Result'].T
# #         pass
# #     # val = df_buf.iloc[0,2]
# #     # val = df_b.at[key, 'Result'] #xx
# #     val = df_b.iloc[i, col_index_b]
# #     val = df_b.loc[df_b.ID == key]['Result'].values[0]
# #     print('ID[{}] = {}'.format(key, val))

# # import pandas as pd
# # ####
# # # df_aとdf_bをID列に基づいて結合
# # merged_df = pd.merge(df_a, df_b[['ID', 'Result']], on='ID', how='left')
# # # df_aのResult列をdf_bのResult列で更新
# # # df_a['Result'] = merged_df['Result']
# # df_a['Result'] = merged_df['Result_y']
# # ####

# # # 結果を表示
# # print('df_a = ')
# # print(df_a)
# df = df_c
# print('書き込みのためにシートを読み直す（data_only=False)')
# ex_data.reset_book_sheet(data_only=False)

# dist_ex_data = ex_data.copy_self()
# dist_ex_data.set_sheet('Write')
# dist_ex_data.set_cell('C3')
# print('作成したしたデータをWriteシートに張り付け（書式付き,StrCell）')
# from openpyxl.cell import Cell
# from excel_data import StrCell
# from pandas import Series
# import copy
# from excel_data import copy_cell
# src_str_cell:StrCell=None
# src_cell:Cell = None
# dist_cell:Cell = None
# import numpy as np
# import math
# # インデックス指定で各行に対して処理を行う
# for row_index in df.index:
#     # インデックスラベルを使って行を取得
#     row:Series = df.loc[row_index]
#     # 取得した行のデータを1つずつ処理する
#     print(f"Processing {row_index}")
#     for col_index, src_str_cell in enumerate(row):
#         dist_cell = dist_ex_data.get_offset_cell(row_index, col_index)
#         if isinstance(src_str_cell, float):
#             if math.isnan(src_str_cell):
#                 src_address = 'nan'
#         else:
#             src_cell = src_str_cell.cell
#             src_address = src_cell.coordinate
#             copy_cell(src_cell, dist_cell, style=True)        
#         print('[{}, {}] = ({}){}  => {}'.format(
#             row_index, col_index, src_cell.value, src_address, dist_cell.coordinate))
#     print("------")


try:
    ex_data.save_book()
except PermissionError as e:
    msg = '[!]ERROR: ファイルアクセスエラーです。ファイルが開いていたらファイルを閉じてください。'
    print(msg)
    # raise e