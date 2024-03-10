"""
エクセルから読み込んでデータ加工

表を読み込んで、別のところにコピーする（ファイル書き込み）
 DataFrame
"""

from excel_data import ExcelSheetDataUtil
from pathlib import Path

print('*ファイル読み込み')
# file_name = 'myworkbook.xlsx'
file_path = 'myworkbook.xlsx'
### 書き込み処理するときは念のためバックアップ
import shutil
back_path = Path(__file__).parent.joinpath('back')
back_path.mkdir(exist_ok=True)
shutil.copy(file_path, back_path)
print('* backup ok = {}'.format(Path(back_path).name + '/' + file_path))
###
src_sheet_name = 'DailyTest'
ex_data = ExcelSheetDataUtil(file_path, src_sheet_name, data_only=True)

print('*コピー先を用意（書式の設定）')
marker = '日付'
src_cell_ex = ex_data.copy_self()
src_cell_ex.set_address_by_find(marker, debug=False)
print('begin_address = {}'.format(src_cell_ex.address))
# src_cell_ex.set_address_entire(opt=src_cell_ex.ConstExcel.COL)
# print('src_address = {}'.format(src_cell_ex.address))
src_address = src_cell_ex.get_range_address()
print('src_address = {}'.format(src_address))

dist_cell_ex = ex_data.copy_self()
# marker = 'ID'
# dist_cell_ex.set_address_by_find(marker, 'I3', debug=False,)
# dist_cell_ex.set_end_address_to_end_horizon(dist_cell_ex.Direction.RIGHT)
# dist_cell_ex.move_address(0, 1)
# dist_cell_ex.set_address_r1c1(row=1)
dist_sheet_name = 'Write'
dist_cell_ex.set_sheet(dist_sheet_name)
dist_cell_ex.set_address_a1('C3')
print('dist_begin_address = {}'.format(dist_cell_ex.address))


print('*セルをコピー、貼り付け')
print('　deta_only=Falseでファイルを開きなおす')
ex_data.close()
ex_data.reset_book_sheet(data_only=False)
dist_cell_ex.reset_book_sheet(data_only=False)

# col = dist_cell_ex.get_col()
# from excel_data import get_column_letter
# col_str = get_column_letter(col)
print('+ insert_col = {}'.format(dist_cell_ex.cell.column_letter))
dist_cell_ex.sheet.insert_cols(dist_cell_ex.cell.column, amount=1)


# # コピー先開始セル
dist_begin_cell_ex = dist_cell_ex.copy_self()
src_begin_row, src_begin_col = src_cell_ex._cnv_row_col_from_a1_address(src_address)
# src_cells = src_cell_ex.sheet[src_cell_ex.address]
src_cells = src_cell_ex.sheet[src_address]
from openpyxl.cell import Cell
src_cell_temp:Cell=None
# print(type(src_cells))
dist_begin_cell_ex.copy_range_address(src_cell_ex, src_cells, debug=True)
# # 2次元の場合と、1次元の場合がある
# for crc_cell in src_cells:
#     if isinstance(crc_cell, tuple):
#         #2次元の場合
#         for src_cell_b in crc_cell:
#             src_cell_temp = src_cell_b
#             offset_row, offset_col = src_cell_ex.get_diff_row_and_col(src_cell_temp.row, src_cell_temp.column)
#             dist_now_cell_ex = dist_begin_cell_ex.get_offset_cell_ex(offset_row, offset_col)
#             dist_now_cell_ex.copy_value(src_cell_temp, style=True)
#             ### log
#             value = src_cell_temp.value
#             print(' src_cell({},{}) >> dist_cell({},{})  [value={}]'.format(
#                 src_cell_temp.row, src_cell_temp.column, dist_now_cell_ex.cell.row, dist_now_cell_ex.cell.column, value))
#     else:
#         #1次元の場合
#         src_cell_temp = crc_cell[0]
#         offset_row, offset_col = src_cell_ex.get_diff_row_and_col(src_cell_temp.row, src_cell_temp.column)
#         dist_now_cell_ex = dist_begin_cell_ex.get_offset_cell_ex(offset_row, offset_col)
#         dist_now_cell_ex.copy_value(src_cell_temp, style=True)
#         ### log
#         value = src_cell_temp.value
#         print(' src_cell({},{}) >> dist_cell({},{})  [value={}]'.format(
#             src_cell_temp.row, src_cell_temp.column, dist_now_cell_ex.cell.row, dist_now_cell_ex.cell.column, value))
#     ###

try:
    dist_cell_ex.save_book()
except PermissionError as e:
    msg = '[!]ERROR: ファイルアクセスエラーです。ファイルが開いていたらファイルを閉じてください。'
    print(msg)
    # raise e