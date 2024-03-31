"""
シートの有効範囲をすべて削除する
"""


import excel_data
from excel_data import ExcelSheetDataUtil
from pathlib import Path


print('*テーブルにデータ入力')
file_name = 'myworkbook.xlsx'
sheet_name = 'Write'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=True)

# keyword = '■DF抽出_and_書式コピー表A'
# ex_data.set_address_by_find(keyword, 'A35', 'I50', debug=False,)
# ex_data.move_address(1,0)
begin_address = ex_data.valid_cells.begin_cell.coordinate
print('begin_address = {}'.format(begin_address))
# buf_right_address = ex_data.get_end_address_to_end_horizon(ex_data.Direction.RIGHT)
end_address = ex_data.valid_cells.end_cell.coordinate
print('end_address = {}'.format(end_address))
# buf_bottom_address = ex_data.get_end_address_to_end_vertical(ex_data.Direction.DOWN)
# print('buf_bottom_address = {}'.format(buf_bottom_address))
ex_data.set_range_address([begin_address, end_address])
print('range_address = {}'.format(ex_data.range_address))
range_address_a = ex_data.range_address

# df_a = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=1)


# print('df_a = ')
# print(df_a.columns)
# print(df_a.values)


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

cells = ex_data.sheet[begin_address : end_address]
from openpyxl.cell import Cell
cell:Cell=None
for rows in cells:
    for cell in rows:
        print(cell.coordinate)
        cell.value = None
        cell.style = excel_data.ConstExcel.STYLE_NORMAL


try:
    ex_data.save_book()
except PermissionError as e:
    msg = '[!]ERROR: ファイルアクセスエラーです。ファイルが開いていたらファイルを閉じてください。'
    print(msg)
    # raise e