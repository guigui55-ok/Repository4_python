"""
エクセルから読み込んで合計

データ集計加工
表をの一部を読み込み、他の表にコピーする
"""
"""

"""


from excel_data import ExcelSheetDataUtil

from pathlib import Path
# text_path = Path(__file__).parent.joinpath('test_ref.txt')
# with open(str(text_path), 'r', encoding='utf-8')as f:
#     lines = f.readlines()

# # 2行目には数値のみしかない想定
# lines[1] = str( int(lines[1].strip()) + 1 ) + '\n'
# with open(str(text_path), 'w', encoding='utf-8')as f:
#     f.writelines(lines)
# print('write text value = {}'.format(lines[1]))

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
sheet_name = 'Copy'
ex_data = ExcelSheetDataUtil(file_path, sheet_name, data_only=True)


print('*セルをコピー元データ')
marker = 'Result'
begin_cell = ex_data.copy_self()
begin_cell.set_address_by_find(marker, 'B1','E10', debug=False,)
begin_cell.move_address(1,0)
end_address = begin_cell.get_end_address_to_end_vertical(
    begin_cell.Direction.DOWN)
print('end_address = {}'.format(begin_cell.address))
begin_cell.set_range_address(end_address)

copy_src_cells = begin_cell.copy_self()
copy_src_cells.get_end_address_to_end_horizon(begin_cell.Direction.RIGHT)
# コピー元開始セル
print('copy_src_address = {}'.format(copy_src_cells.range_address))
copy_src_cells.set_range_address(end_address)
copy_src_range_address = copy_src_cells.range_address
copy_src_cells.address = copy_src_cells.range_address

from openpyxl.cell import Cell
row, col = copy_src_cells._cnv_row_col_from_a1_address(copy_src_cells.address)
cell_a = Cell(worksheet=None, row=row, column=col)


#########
# 統合されたセルのアドレスを取得する
# sheet.merged_cells にシート内の統合セルの情報が格納されている
#########
# type = MultiCellRange 
from openpyxl.worksheet.cell_range import MultiCellRange
merged_cells:MultiCellRange = ex_data.sheet.merged_cells
# merged_cells:list[MultiCellRange] = ex_data.sheet.merged_cells
buf:list[MultiCellRange]  = merged_cells.ranges
# buf = ex_data._get_cells_address(merged_cells)
print('merged_cells = ')
print(buf)
print(type(merged_cells))# <class 'openpyxl.worksheet.cell_range.MultiCellRange'>
# from openpyxl.worksheet.merge import MultiCellRange
# from openpyxl.worksheet.merge import MultiCellRange as MultiCellRangeSingle
# range_val:MultiCellRangeSingle=None
from excel_data import _is_include_address
for cell_val in merged_cells.ranges:
    # buf = ex_data._get_cells_address(cell)
    # print(cell_val) # D2:E3
    # print(type(cell_val)) #<class 'openpyxl.worksheet.merge.MergedCellRange'>
    print(cell_val.coord)
    merge_address =cell_val.coord

    # 統合セルのアドレスを取得して、対象の範囲の中に含まれているか確認する
    # flag = _is_include_address(cell_a, merge_address)
    flag = _is_include_address(copy_src_range_address, merge_address)
    # print(flag)
    if flag:
        msg = '操作対象のセルに、統合セルが含まれている'
        msg += '(target_address={}, merge_address={})'.format(copy_src_range_address, merge_address)
        raise Exception(msg)
#########
#########

print('*セルをコピー、貼り付け')
marker = 'Result'
dist_begin_cell = ex_data.copy_self()
dist_begin_cell.set_address_by_find(marker, 'I3', debug=False,)
print('dist_begin_cell = {}'.format(dist_begin_cell.address))

print('　deta_only=Falseでファイルを開きなおす')
ex_data.close()
sheet_name = 'Copy'
ex_data = ExcelSheetDataUtil(file_path, sheet_name, data_only=False)

dist_begin_cell_old = dist_begin_cell.copy_self()
dist_cell = ex_data.copy_self()
dist_cell.copy_values_from_other_cell(dist_begin_cell)
# dist_begin_cell.get_end_address_to_end_horizon(ex_data.Direction.RIGHT)
# コピー先開始セル
dist_cell.move_address(1,0)
dist_begin_row, dist_begin_col = dist_cell._cnv_row_col_from_a1_address(dist_cell.address)
# 貼り付け
for row in copy_src_cells.get_rows_range():
    dist_cell.set_address_r1c1(col=dist_begin_col)
    for col in copy_src_cells.get_cols_range():
        # #コピー先に値をコピー。
        # if type(sheet[copySrcCoord]) != MergedCell :
        #     sheet[copyDstCoord].value = sheet[copySrcCoord].value;
        #     #書式があったら、書式もコピー。
        #     if sheet[copySrcCoord].has_style :
        #         sheet[copyDstCoord]._style = sheet[copySrcCoord]._style;
        src_cell:Cell = copy_src_cells.get_cell_r1c1(row, col)
        value = copy_src_cells.get_value_r1c1(row, col)
        dist_cell.copy_value(src_cell)
        d_row, d_col = dist_cell.get_row_and_col()
        print(' src_cell({},{}) >> dist_cell({},{})  [value={}]'.format(row, col, d_row, d_col, value))
        # dist_cell.move_address(row, col)
        dist_cell.move_address(0,1)
    dist_cell.move_address(1,0)

dist_cell.save_book()