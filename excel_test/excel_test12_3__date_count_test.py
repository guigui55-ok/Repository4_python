"""
表Aの日付データの出現回数をカウントして、 表Bに入力していく。
 作成時コード未整理

特定の日付を含むエクセル表A（列名：表番号、カテゴリA(日付)、カテゴリB(日付)）の日付をカウントしてdf_aとして読み込む。（データはセル値と番地を紐づけている）
 ある範囲の日付データと結果（columns=日付、結果）をdf_retにする
  日付と結果を列名に持つエクセルの表B（上記ret_dfと同じ）をdf_bとして読み込む。（データはセル値と番地を紐づけている）
    （df_bとdf_ret日付は異なっていてもよい） 
"""


from excel_data import ExcelSheetDataUtil
import excel_data
from pathlib import Path
import pandas as pd


# print('*書き込みシートをすべてクリア')
file_name = 'myworkbook.xlsx'
sheet_name = 'Write'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=True)
# clear_address = ex_data.reset_valid_cells()
# print('clear_address = {}'.format(clear_address))

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

print('*処理する日付のリストを作成')
import datetime
print(datetime.datetime.now().strftime('%Y-%m-%d'))
BEGIN_DATE = '2024-01-15'
begin_datetime = datetime.datetime.strptime(BEGIN_DATE, '%Y-%m-%d')
import calendar
y = begin_datetime.year
m = begin_datetime.month
d = calendar.monthrange(y, m)[1]
END_DATE = '{}-{}-{}'.format(y, m, d)
# END_DATE = '2023-01-20'
end_datetime = datetime.datetime.strptime(END_DATE, '%Y-%m-%d')
date_range = pd.date_range(BEGIN_DATE, END_DATE, freq='D')
# print(type(date_range))

print('*エクセルから読み取った日付データリストを文字列に変換する')
from excel_data import cnv_date_str_cell, cnv_date_str, cnv_date_str_yobi_cell
col_name_a = 'カテゴリA'
df_a[col_name_a] = df_a[col_name_a].map(cnv_date_str_cell)

print('*日付カウント格納用リストを用意する')
date_col_name = '日付'
df_ret = pd.DataFrame({date_col_name: date_range})
result_col_name = '結果数'
df_ret[result_col_name]=''
print('df_ret.head a')
print(df_ret.head())
print('*日付型を文字列に変換')
df_ret[date_col_name] = df_ret[date_col_name].map(cnv_date_str)


print('*特定の日付の出現回数をカウント')
print('*読み取った表Aから日付のdfに値をコピーする')
for date_val in date_range:
    target_date = date_val.strftime('%y/%m/%d')
    count = (df_a[col_name_a] == target_date).sum()
    print('    {} [{}] = {}'.format(col_name_a, target_date ,count))
    # buf_df = df_ret[df_ret[date_col_name] == target_date]
    buf_df = df_ret[df_ret[date_col_name].str.contains(target_date)]
    buf_df[result_col_name] = int(count)
    df_ret.update(buf_df)
df_ret[result_col_name] = df_ret[result_col_name].astype('Int64')
print('df_ret.head b')
print(df_ret.head())
print(df_ret.dtypes)



print('*結果貼り付け用、日付表Bの範囲を読み込み')
sheet_name = '日付Count'
ex_data.set_sheet(sheet_name)
keyword = '日付'
ex_data.set_address_by_find(keyword, 'H5', 'I50', debug=False)
print('begin_address = {}'.format(ex_data.cell.coordinate))
# ex_data.move_address(1,0)
ex_data.range_address = ex_data.get_range_address()
print('range_address = {}'.format(ex_data.range_address))

df_b = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=None)
print('df_b = ')
first_row_as_list = df_b.iloc[0].astype(str).tolist()
df_b.columns = first_row_as_list
print(df_b.columns)
print(df_b.shape)
print(df_b.head())
print('-------')

print('*日付カウント済みDFから、表Bにデータを入力していく')
print('df_bとdf_retは同じ想定')

from openpyxl.cell import Cell
df_b_str_cell:excel_data.StrCell=None
buf_cell:Cell=None
for i, df_ret_val in enumerate(df_ret[date_col_name]):
    # print(type(df_ret_val))#str
    # print(df_ret_val)
    count = df_ret[result_col_name]
    if df_b_str_cell==date_col_name: continue
    # target_date = df_ret_val.strftime('%Y-%m-%d')
    # count = df_ret[df_ret[date_col_name] == target_date]
    target_date = df_ret_val
    buf_df_ret = df_ret[df_ret[date_col_name].str.contains(target_date)]
    # buf_df_ret >  DataFrame 日付 結果数 : 0  24/01/15
    count = buf_df_ret[result_col_name]
    # count_str = str(buf_df_ret[result_col_name][0])
    count_str = str(list(buf_df_ret[result_col_name].items())[0])
    if count_str.isdigit():
        count = int(count_str)
    else:
        count = 0
    buf_df = df_ret[df_ret[date_col_name].str.contains(target_date)]
    count = buf_df_ret[result_col_name]
    count = int(count)
    print('date = {},  ret = {}'.format(df_ret_val, count))
    # count : DataSeries  0  Name: 結果数, dtype: object
    # print(type(count))
    # buf_df_b = df_b[df_b[date_col_name].str.contains(target_date)]
    buf_df_b = df_b[df_b[date_col_name].str.contains(target_date)]
    if buf_df_b.shape[0]==0:
        print(' *nothing data(buf_df_b.shape={})'.format(buf_df_b.shape))
        continue
    for index, row in buf_df_b.iterrows():
        row[result_col_name].cell.value = count
        print('[{}] -> {}'.format(row[result_col_name].cell.coordinate, count))
        # 各列にアクセスするために、列名を使って値を取得します。
        # for col in buf_df_b.columns:
            # print(f"行{index}、列名[{col}]の値: {row[col]} ,type({type(row[col])})")
            # 行14、列名[日付]の値: 2024/01/28(日) ,type(<class 'excel_data.StrCell'>)
            # 行14、列名[結果数]の値: None ,type(<class 'excel_data.StrCell'>)
    #####
        
    # buf_df = df_ret[df_ret[date_col_name].str.contains(target_date)]
    # buf_df[result_col_name] = int(count)
    # df_ret.update(buf_df)
    # ##########
    # print('*****')
    # print(buf_df_b)
    # print(type(buf_df_b))
    # # buf_df_b >  DataFrame 日付 結果数 : 0  24/01/15
    # print(buf_df_b.shape)
    # # buf_ds_ret = buf_df_ret[result_col_name][0]
    # # buf_ds_ret = list(buf_df_ret[result_col_name].items())[0]
    # # buf_ds_ret = buf_df_ret[result_col_name] # <class 'pandas.core.series.Series'> Name: 結果数, dtype: object
    # # buf_ds_ret = buf_df_ret[result_col_name].items() #zip object
    # # buf_ds_ret = buf_df_ret[result_col_name].values #zip object
    # buf_ds_ret = buf_df_ret[result_col_name]
    # print(buf_ds_ret)
    # print(str(buf_ds_ret))
    # print(type(buf_ds_ret))
    # # # buf_df_b >  DataFrame 日付 結果数 : 0  24/01/15
    # # print(buf_df_b.shape)
    # # print(type(buf_ds_ret))
    # buf_ds_ret_b = list(buf_df_ret[result_col_name].items())[0]
    # # DataSeriesの各要素をループして更新します
    # for idx, val in buf_ds_ret.items():
    #     # object.cell.valueを更新します
    #     print(val)
    #     print(type(val))
    #     val.cell.value = count
    # buf_ds_ret_b.cell.value = count
    # # # DataSeriesの各要素をループして更新します（1つ目にStrCellが入っている想定）
    # # for idx, df_b_str_cell in buf_df_b.items():
    # #     # object.cell.valueを更新します
    # #     # buf_cell = df_b_str_cell.cell
    # #     # buf_cell.value = count
    # #     df_b_str_cell = buf_df_b[result_col_name]
    # #     df_b_str_cell.cell.value = count
    # #     break
    # # # 元の DataFrame に取得された DataSeries を更新します
    # # buf_df_b.update(buf_df_b)
    # ##########
####
# df_b_str_cell:excel_data.StrCell=None
# for i, df_b_str_cell in enumerate(df_b[date_col_name]):
#     # print(type(df_b_row))#StrCell
#     print(df_b_str_cell)
#     if df_b_str_cell==date_col_name: continue
#     # target_date = date_val.strftime('%y/%m/%d')
#     target_date = df_b_str_cell
#     count = df_ret[df_ret[date_col_name] == target_date]
#     print(type(count))
#     print(count)
#     df_b_str_cell.cell.value = count
    # count = (df_a[col_name_a] == target_date).sum()
    # print('    {} [{}] = {}'.format(col_name_a, target_date ,count))
    # df_ret[df_b[date_col_name] == target_date] = count
    # buf_df = df_ret[df_ret[date_col_name].str.contains(target_date)]

# date_col_name = 'col_name'
# target_date = '24/1/22'
# buf_df = df_ret[df_b[date_col_name] == target_date]
# # 結果格納用のDataFrameを作成
# df_c = pd.DataFrame()
#####
# print('書き込みのためにシートを読み直す（data_only=False)')
# ex_data.reset_book_sheet(data_only=False)

# print('コピーしたデータをWriteシートに張り付け（書式付き）')
# from openpyxl.cell import Cell
# from excel_data import StrCell
# from pandas import Series
# import copy
# from excel_data import copy_cell
# src_str_cell:StrCell=None
# src_cell:Cell = None
# dist_cell:Cell = None
# # インデックス指定で各行に対して処理を行う
# for row_index in df_a.index:
#     # インデックスラベルを使って行を取得
#     row:Series = df_a.loc[row_index]
#     # 取得した行のデータを1つずつ処理する
#     print(f"Processing {row_index}")
#     for col_index, src_str_cell in enumerate(row):
#         dist_cell = dist_ex_data.get_offset_cell(row_index, col_index)
#         src_cell = src_str_cell.cell
#         print('[{}, {}] = ({}){}  => {}'.format(
#             row_index, col_index, src_cell.value, src_cell.coordinate, dist_cell.coordinate))
#         copy_cell(src_cell, dist_cell, style=True)        
#     print("------")

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