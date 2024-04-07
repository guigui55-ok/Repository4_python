"""
表を作成する
"""


import excel_data
from excel_data import ExcelSheetDataUtil
from pathlib import Path


# print('*書き込みシートをすべてクリア')
file_name = 'myworkbook.xlsx'
sheet_name = '日付Count'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=True)
# clear_address = ex_data.reset_valid_cells()
# print('clear_address = {}'.format(clear_address))

# print('*コピー元表Aの範囲を読み込み')
# sheet_name = '日付Count'
# ex_data.set_sheet(sheet_name)
# keyword = '行番号'
# ex_data.set_address_by_find(keyword, 'A1', 'I50', debug=False)
# print('begin_address = {}'.format(ex_data.cell.coordinate))
# # ex_data.move_address(1,0)
# ex_data.range_address = ex_data.get_range_address()
# print('range_address = {}'.format(ex_data.range_address))

print('日付データの用意')
import pandas as pd
# from pandas_test8_test_data import DF_TEST_DATA_B, DF_TEST_DATA_COLUMNS
# df = pd.DataFrame(DF_TEST_DATA_B, columns=DF_TEST_DATA_COLUMNS)
# # 'Date'列をdatetime型に変換
# df['Date'] = pd.to_datetime(df['Date'])
# # 日付範囲から1日ごとのDataFrameを作成する
# df_check_date = pd.date_range('2023-11-01', '2023-11-08', freq='D')
# # 元データを日付範囲のデータでフィルターを掛ける
# df_filtered = df[df['Date'].isin(df_check_date)]
# # 日付でソート
# df_sorted = df_filtered.sort_values(by='Date')
import datetime
print(datetime.datetime.now().strftime('%Y-%m-%d'))
BEGIN_DATE = '2023-01-15'
BEGIN_DATE = '2024-01-15'
begin_datetime = datetime.datetime.strptime(BEGIN_DATE, '%Y-%m-%d')
import calendar
y = begin_datetime.year
m = begin_datetime.month
d = calendar.monthrange(y, m)[1]
END_DATE = '{}-{}-{}'.format(y, m, d)
end_datetime = datetime.datetime.strptime(END_DATE, '%Y-%m-%d')
date_range = pd.date_range(BEGIN_DATE, END_DATE, freq='D')
print(type(date_range))

# # DataFrameを作成
# df_a = pd.DataFrame({
#     '日付': date_range,
#     '結果数': ['' for _ in range(len(date_range))]
# })

# DataFrameを作成
df_a = pd.DataFrame({'日付': date_range})
#列を追加
df_a['結果数'] = ''

print('df_a.shape')
print(df_a.shape)
# 結果の表示
print('df_a')
print(df_a)


print('書き込みのためにシートを読み直す（data_only=False)')
ex_data.reset_book_sheet(data_only=False)


print('*開始セルアドレスをセットして、dfの配列を順番に書き込んでいく')
dist_ex_data = ex_data.copy_self()
dist_ex_data.set_sheet('日付Count')
dist_ex_data.set_cell('I7')

print('コピーしたデータをWriteシートに張り付け（書式なし）')
from openpyxl.cell import Cell
# from excel_data import StrCell
from pandas import Series
import copy
from excel_data import copy_cell
# src_str_cell:StrCell=None
# src_cell:Cell = None
dist_cell:Cell = None
temp_begin_cell = None
temp_end_cell = None
is_write_column = True
if is_write_column:
    print('df_の見出しは出力されないので別途対応')
    for col_index, col_name in enumerate(df_a.columns):
        dist_cell = dist_ex_data.get_offset_cell(0, col_index)
        print('[{}, {}] = "{}" => {}'.format(
            0, col_index, col_name,  dist_cell.coordinate))
        dist_cell.value = col_name
    begin_row_indent = 1
else:
    print('columnsは書き込まない')
    begin_row_indent = 0

def strftime_youbi(timestamp:pd.Timestamp, format='%Y/%m/%d'):
    # 曜日を日本語表記に変換する辞書
    day_of_week_dict = {
        0: '月',
        1: '火',
        2: '水',
        3: '木',
        4: '金',
        5: '土',
        6: '日'
    }
    # Timestampオブジェクトを指定された形式の文字列に変換する
    formatted_date = f"{timestamp.strftime(format)}({day_of_week_dict[timestamp.day_of_week]})"
    return formatted_date
from excel_data import cnv_date_str_cell, cnv_date_str, cnv_date_str_yobi_cell
df_a['日付'] = df_a['日付'].map(cnv_date_str_yobi_cell)

print('----')
# インデックス指定で各行に対して処理を行う
for row_index in df_a.index:
    # インデックスラベルを使って行を取得
    row:Series = df_a.loc[row_index]
    # 取得した行のデータを1つずつ処理する
    print(f"row_index {row_index}")
    for col_index, src_str in enumerate(row):
        dist_cell = dist_ex_data.get_offset_cell(row_index+begin_row_indent, col_index)
        if temp_begin_cell==None:
            temp_begin_cell = dist_cell
        # src_cell = src_str_cell.cell
        # copy_cell(src_cell, dist_cell, style=True)
        # if '日付' in df_a.columns[col_index]:
        if isinstance(src_str, pd.Timestamp):
            src_str_b = strftime_youbi(src_str)
        else:
            src_str_b = src_str
        print('[{}, {}] = "{}" => {}'.format(
            row_index, col_index, src_str_b,  dist_cell.coordinate))
        dist_cell.value = src_str_b

temp_end_cell = dist_cell

######
print('colの幅を文字数に合わせて調整する')
col_begin = temp_begin_cell.column
col_end = temp_end_cell.column
for buf_col in range(col_begin, col_end+1):
    begin_cell = dist_ex_data.valid_cells.begin_cell
    begin_row = begin_cell.row
    end_cell = dist_ex_data.valid_cells.end_cell
    end_row = end_cell.row
    col_name = excel_data.get_column_letter(buf_col)
    now_width = dist_ex_data.sheet.column_dimensions[col_name].width
    value_list = []
    for buf_row in range(begin_row, end_row+1):
        buf_cell = dist_ex_data.get_cell_r1c1(buf_row, buf_col)
        buf_val = buf_cell.value
        if buf_val == None: buf_val = ''
        len_val = len(str(buf_val))
        len_val =  len_val* buf_cell.font.sz /10
        value_list.append(len_val)
    # 行全体をチェックして一番長いものに合わせる
    max_str_count = max(value_list)
    adjusted_width = max_str_count
    print('  *calc adjusted_width = {}'.format(adjusted_width))
    if now_width < adjusted_width:
        dist_ex_data.sheet.column_dimensions[col_name].width = adjusted_width
        w = dist_ex_data.sheet.column_dimensions[col_name].width
        print('  *ajusted width = {}'.format(w))
    else:
        w = dist_ex_data.sheet.column_dimensions[col_name].width
        print('  *not ajusted width = {}'.format(w))

    print("------")
ex_data = dist_ex_data




# df_a = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=None)
# print('df_a = ')
# first_row_as_list = df_a.iloc[0].astype(str).tolist()
# df_a.columns = first_row_as_list
# print(df_a.columns)
# # print(df_a.values)
# print(df_a.shape)

# BEGIN_DATE = '2024/1/1'
# import datetime
# begin_datetime = datetime.datetime.strptime(BEGIN_DATE, '%Y%m%d')
# import calendar
# end_datetime = begin_datetime
# end_datetime.day = calendar.monthrange(begin_datetime.year, begin_datetime.month)[1]

# from excel_data import cnv_date_str_cell, cnv_date_str
# df = df_a
# data = df['カテゴリA'].loc[0]
# print('data.cell.coordinate = ')
# print(data.cell.coordinate)

# df['カテゴリA'] = df['カテゴリA'].map(cnv_date_str_cell)
# df['カテゴリB'] = df['カテゴリB'].map(cnv_date_str_cell)
# print(df.values)

# data = df['カテゴリA'].loc[0]
# print('data.cell.coordinate = ')
# print(data.cell.coordinate)

# target_date = datetime.datetime(year=2024, month=1, day=19).strftime('%y/%m/%d')
# # target_date = '24/1/19' # KeyError
# df_cat_a = df['カテゴリA'].value_counts()
# print('df_cat_a = ')
# print(df_cat_a)
# count = df_cat_a[target_date]
# print('カテゴリA [{}] = {}'.format(target_date ,count))
#####

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