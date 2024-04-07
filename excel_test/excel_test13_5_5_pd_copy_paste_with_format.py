"""
表をコピペする
 （連続したセルの表を読み取り、他のシートにコピーする）
    書き込み前に、書き込み先のシートの有効範囲をすべて削除する
     DataFrame、StrCellを使用、書式もコピーする
"""


from excel_data import ExcelSheetDataUtil
from pathlib import Path


print('*書き込みシートをすべてクリア')
file_name = 'myworkbook.xlsx'
sheet_name = 'Write'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=True)
ex_data.reset_valid_cells()

print('*コピー元範囲を読み込み')
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
print(df_a.values)


# keyword = '■TestData'
# ex_data.set_address_by_find(keyword, debug=False,)
# ex_data.move_address(1,0)
# print('begin_address = {}'.format(ex_data.address))
# buf_right_address = ex_data.get_end_address_to_end_horizon(ex_data.Direction.RIGHT)
# print('buf_right_address = {}'.format(buf_right_address))
# buf_bottom_address = ex_data.get_end_address_to_end_vertical(ex_data.Direction.DOWN)
# print('buf_bottom_address = {}'.format(buf_bottom_address))
# ex_data.set_range_address([buf_right_address, buf_bottom_address])
# print('range_address = {}'.format(ex_data.range_address))

# df_b = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=1)

# print('df_b = ')
# print(df_b.columns)
# print(df_b.values)

# col_index_b = list(df_b.columns).index('Result')
# col_index_a = list(df_a.columns).index('Result')
# for i, key in enumerate(df_b['ID']):
#     # val = df_b['ID' == key]['Result']
#     # df_buf = df_b.query('ID == "{}"'.format(key))
#     if i==0:
#         df_buf = df_b.loc[df_b.ID == key]['Result']
#         print(type(df_buf))
#         # print(df_buf.info())
#         print(df_buf.shape)
#         print(df_buf.values[0])
#         # val = df_buf['Result'].T
#         pass
#     # val = df_buf.iloc[0,2]
#     # val = df_b.at[key, 'Result'] #xx
#     val = df_b.iloc[i, col_index_b]
#     val = df_b.loc[df_b.ID == key]['Result'].values[0]
#     print('ID[{}] = {}'.format(key, val))

# import pandas as pd
# ####
# # df_aとdf_bをID列に基づいて結合
# merged_df = pd.merge(df_a, df_b[['ID', 'Result']], on='ID', how='left')
# # df_aのResult列をdf_bのResult列で更新
# # df_a['Result'] = merged_df['Result']
# df_a['Result'] = merged_df['Result_y']
# ####

# # 結果を表示
# print('df_a = ')
# print(df_a)

print('書き込みのためにシートを読み直す（data_only=False)')
ex_data.reset_book_sheet(data_only=False)

dist_ex_data = ex_data.copy_self()
dist_ex_data.set_sheet('Write')
dist_ex_data.set_cell('C3')
print('コピーしたデータをWriteシートに張り付け（書式付き）')
from openpyxl.cell import Cell
from excel_data import StrCell
from pandas import Series
import copy
from excel_data import copy_cell
src_str_cell:StrCell=None
src_cell:Cell = None
dist_cell:Cell = None
# インデックス指定で各行に対して処理を行う
for row_index in df_a.index:
    # インデックスラベルを使って行を取得
    row:Series = df_a.loc[row_index]
    # 取得した行のデータを1つずつ処理する
    print(f"Processing {row_index}")
    for col_index, src_str_cell in enumerate(row):
        dist_cell = dist_ex_data.get_offset_cell(row_index, col_index)
        src_cell = src_str_cell.cell
        print('[{}, {}] = ({}){}  => {}'.format(
            row_index, col_index, src_cell.value, src_cell.coordinate, dist_cell.coordinate))
        copy_cell(src_cell, dist_cell, style=True)        
    print("------")

# df = df_a['Result']
# for num , row_cells in enumerate(cells_2d):
#     # print('### {}'.format(i))
#     # for (data, cell) in zip(df, row_cells):
#     for j, cell in enumerate(row_cells):
#         # if j==0:
#         #     continue
#         if j!=0:
#             j-=1
#             val = df.iloc[j]
#             print('{}, {} = {}'.format(cell,j, val))
#             cell.value = val
#             row, col = ex_data._cnv_row_col_from_a1_address(cell.coordinate)
#             ex_data.sheet.cell(row, col, val)
#     # for cell in enumerate(row_cells):
#     #     print(cell.coordinate)
#     # for data in df_a['Result']:
#     #     print(data)
# print()


try:
    ex_data.save_book()
except PermissionError as e:
    msg = '[!]ERROR: ファイルアクセスエラーです。ファイルが開いていたらファイルを閉じてください。'
    print(msg)
    # raise e