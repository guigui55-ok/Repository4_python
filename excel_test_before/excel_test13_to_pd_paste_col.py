"""
エクセルから読み込んで合計

データ集計加工
"""
"""

"""


from excel_data import ExcelSheetDataUtil
from pathlib import Path

import datetime
def cnv_date_str(value):
    buf = ExcelSheetDataUtil._cnv_datetime(value)
    if isinstance(buf , datetime.datetime):
        return buf.strftime('%y/%m/%d')
    else:
        return buf


print('*テーブルにデータ入力')
file_name = 'myworkbook.xlsx'
# file_name = 'myworkbook.xlsm'
### 書き込み処理するときは念のためバックアップ
import shutil
back_path = Path(__file__).parent.joinpath('back')
back_path.mkdir(exist_ok=True)
shutil.copy(file_name, back_path)
###
sheet_name = 'input_data'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=True)

keyword = 'PasteTable'
ex_data.set_address_by_find(keyword, 'A1', 'F10', debug=False,)
ex_data.move_address(1,0)
print('begin_address = {}'.format(ex_data.address))
buf_right_address = ex_data.get_end_address_to_end_horizon(ex_data.Direction.RIGHT)
print('buf_right_address = {}'.format(buf_right_address))
buf_bottom_address = ex_data.get_end_address_to_end_vertical(ex_data.Direction.DOWN)
print('buf_bottom_address = {}'.format(buf_bottom_address))
ex_data.set_range_address([buf_right_address, buf_bottom_address])
print('range_address = {}'.format(ex_data.range_address))
range_address_a = ex_data.range_address

df_a = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=1)


keyword = '■TestData'
ex_data.set_address_by_find(keyword, debug=False,)
ex_data.move_address(1,0)
print('begin_address = {}'.format(ex_data.address))
buf_right_address = ex_data.get_end_address_to_end_horizon(ex_data.Direction.RIGHT)
print('buf_right_address = {}'.format(buf_right_address))
buf_bottom_address = ex_data.get_end_address_to_end_vertical(ex_data.Direction.DOWN)
print('buf_bottom_address = {}'.format(buf_bottom_address))
ex_data.set_range_address([buf_right_address, buf_bottom_address])
print('range_address = {}'.format(ex_data.range_address))

df_b = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=1)

print('df_a = ')
print(df_a.columns)
print(df_a.values)

print('df_b = ')
print(df_b.columns)
print(df_b.values)

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

import pandas as pd
####
# df_aとdf_bをID列に基づいて結合
merged_df = pd.merge(df_a, df_b[['ID', 'Result']], on='ID', how='left')
# df_aのResult列をdf_bのResult列で更新
# df_a['Result'] = merged_df['Result']
df_a['Result'] = merged_df['Result_y']
####

# 結果を表示
print('df_a = ')
print(df_a)

ex_data.reset_book_sheet(data_only=False)
range_begin_address , range_end_address = range_address_a.split(':')
print('range_address_a = {}'.format(range_address_a))
ex_data.address = range_address_a
address_list = ex_data.find_value(
    ex_data.sheet,
    keyword='Result',
    find_begin_address=range_begin_address,
    find_end_address=range_end_address)
if len(address_list)<1:
    msg = 'Result is nothing(sheet={})'.format()
    raise Exception(msg)
begin_address = address_list[0]
begin_cell = ex_data._get_cell(begin_address)
end_cell = ex_data._get_cell(range_end_address)
begin_cell_buf = ex_data.find_entire_row_in_range(0, keyrowd='Result')
print('begin_cell_buf = {}'.format(begin_cell_buf))
# print('******')
# begin_cell_buf = ex_data.find_entire_col_in_range(0, keyrowd='A005')
# print(begin_cell_buf)
# ex_data.reset_book_sheet(data_only=False)
cells_2d = ex_data.get_entire_col_in_range_by_cell(begin_cell_buf)
from openpyxl.cell import Cell
cell:Cell=None
df = df_a['Result']
for i, row_cells in enumerate(cells_2d):
    # print('### {}'.format(i))
    # for (data, cell) in zip(df, row_cells):
    for j, cell in enumerate(row_cells):
        # if j==0:
        #     continue
        if j!=0:
            j-=1
            val = df.iloc[j]
            print('{}, {} = {}'.format(cell,j, val))
            cell.value = val
            row, col = ex_data._cnv_row_col_from_a1_address(cell.coordinate)
            ex_data.sheet.cell(row, col, val)
    # for cell in enumerate(row_cells):
    #     print(cell.coordinate)
    # for data in df_a['Result']:
    #     print(data)
print()


try:
    ex_data.save_book()
except PermissionError as e:
    msg = '[!]ERROR: ファイルアクセスエラーです。ファイルが開いていたらファイルを閉じてください。'
    print(msg)
    # raise e