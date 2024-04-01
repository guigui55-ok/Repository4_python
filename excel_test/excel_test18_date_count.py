"""
表をコピペする
 （連続したセルの表を読み取り、他のシートにコピーする）
    書き込み前に、書き込み先のシートの有効範囲をすべて削除する
     ** 別テーブルMerge版（異なる行、異なる列のテーブル）
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
sheet_name = '日付Count'
ex_data.set_sheet(sheet_name)
keyword = '行番号'
ex_data.set_address_by_find(keyword, 'A1', 'I50', debug=False)
print('begin_address = {}'.format(ex_data.cell.coordinate))
# ex_data.move_address(1,0)
ex_data.range_address = ex_data.get_range_address()
print('range_address = {}'.format(ex_data.range_address))

df_a = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=None)
print('df_a = ')
first_row_as_list = df_a.iloc[0].astype(str).tolist()
df_a.columns = first_row_as_list
print(df_a.columns)
# print(df_a.values)
print(df_a.shape)

BEGIN_DATE = '2024/1/1'
import datetime
begin_datetime = datetime.datetime.strptime(BEGIN_DATE, '%Y%m%d')
import calendar
end_datetime = begin_datetime
end_datetime.day = calendar.monthrange(begin_datetime.year, begin_datetime.month)[1]

from excel_data import cnv_date_str_cell, cnv_date_str
df = df_a
data = df['カテゴリA'].loc[0]
print('data.cell.coordinate = ')
print(data.cell.coordinate)

df['カテゴリA'] = df['カテゴリA'].map(cnv_date_str_cell)
df['カテゴリB'] = df['カテゴリB'].map(cnv_date_str_cell)
print(df.values)

data = df['カテゴリA'].loc[0]
print('data.cell.coordinate = ')
print(data.cell.coordinate)

target_date = datetime.datetime(year=2024, month=1, day=19).strftime('%y/%m/%d')
# target_date = '24/1/19' # KeyError
df_cat_a = df['カテゴリA'].value_counts()
print('df_cat_a = ')
print(df_cat_a)
count = df_cat_a[target_date]
print('カテゴリA [{}] = {}'.format(target_date ,count))

# # 結果格納用のDataFrameを作成
# df_c = pd.DataFrame()
# import math
# def apply_proc(row):
#     def is_nan(value):
#         try:
#             return math.isnan(value)
#         except ValueError as e:
#             return False
#         except TypeError: #TypeError: must be real number, not str
#             return False
#         except Exception as e:
#             print(str(e))
#             return False
#     if row[original_col] != row[original_col + '_b']:
#         print('{}, {}'.format(row[original_col], row[original_col + '_b']))
#         if str(row[original_col])=='' or row[original_col]==None or is_nan(row[original_col]):
#             return "New"
#         elif is_nan(row[original_col + '_b']):
#             return "×"
#         else:
#             return "〇"
#     else:
#         return ""


# print('書き込みのためにシートを読み直す（data_only=False)')
# ex_data.reset_book_sheet(data_only=False)
# # 列ごとに処理
# for col in df_merged.columns:
#     if '_b' in col:
#         # 元の列名を取得（接尾辞を除去）
#         original_col = col.rstrip('_a').rstrip('_b')
#         # if original_col + '_a' in df_merged and original_col + '_b' in df_merged:
#         # columna_nameとcolumna_name_bがあるcolumn配下の処理
#         if (original_col in df_merged) and (original_col + '_b' in df_merged):
#             # 前の値が空なら、Newにする
            
#             # 値が異なる場合は "〇"、同じ場合は "" をセット
#             # apply_proc = lambda row: "〇" if row[original_col] != row[original_col + '_b'] else ""
#             buf_data = df_merged.apply(apply_proc, axis=1)
#             df_c[original_col] = buf_data
#         elif original_col in df_merged:
#             df_c[original_col] = ""
#     else:
#         # '番号' と '分類' 列はそのままコピー
#         df_c[col] = df_merged[col]

#     # df_bにのみ存在する列は "New" をセット
#     for col in df_b.columns:
#         if not col in df_a.columns:
#             df_c.loc[1:, col] = "New"


# #######################
# print('****************')
# print('df_c = ')
# print(df_c)

# print('*開始セルアドレスをセットして、dfの配列を順番に書き込んでいく')
# dist_ex_data = ex_data.copy_self()
# dist_ex_data.set_sheet('Write')
# dist_ex_data.set_cell('C3')

# from openpyxl.cell import Cell
# w_df = df_c
# # df_aの1行目のデータをdf_bの1行目にコピー
# # 共通の列にのみ値をコピーする
# common_columns = [col for col in df_a.columns if col in df_c.columns]
# df_c.loc[0, common_columns] = df_a.iloc[0][common_columns].values
# print('*DataFrameをエクセルに書き込む')
# for i , column_name in enumerate(w_df.columns):
#     print('Processing {}'.format(i))
#     for j, data_series_value in enumerate(w_df[column_name]):
#         value = data_series_value
#         cell:Cell = dist_ex_data.get_offset_cell(j, i)
#         dist_ex_data.set_value(value, cell.coordinate)
#         print('[i ,j] = [{}, {}] = ({}){}'.format(i, j, cell.coordinate, value))
#         cell.value = value
#     print('-------')
# print()
# ex_data = dist_ex_data



try:
    ex_data.save_book()
except PermissionError as e:
    msg = '[!]ERROR: ファイルアクセスエラーです。ファイルが開いていたらファイルを閉じてください。'
    print(msg)
    # raise e