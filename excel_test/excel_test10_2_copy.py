"""
エクセルから読み込んでデータ加工

列全体をほかの列にコピーする、書式ごと
 
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
sheet_name = 'Copy2'
ex_data = ExcelSheetDataUtil(file_path, sheet_name, data_only=True)


print('*コピー先を用意（書式の設定）')
marker = '※コピー用'
src_cell_ex = ex_data.copy_self()
src_cell_ex.set_address_by_find(marker, debug=False,)
src_cell_ex.set_address_entire(opt=src_cell_ex.ConstExcel.COL)
print('src_address = {}'.format(src_cell_ex.address))

marker = 'ID'
dist_cell_ex = ex_data.copy_self()
dist_cell_ex.set_address_by_find(marker, 'I3', debug=False,)
dist_cell_ex.set_end_address_to_end_horizon(dist_cell_ex.Direction.RIGHT)
dist_cell_ex.move_address(0, 1)
dist_cell_ex.set_address_r1c1(row=1)
print('dist_begin_address = {}'.format(dist_cell_ex.address))


print('*セルをコピー、貼り付け')
print('　deta_only=Falseでファイルを開きなおす')
ex_data.close()
sheet_name = 'Copy2'
ex_data = ExcelSheetDataUtil(file_path, sheet_name, data_only=False)

dist_cell_ex_old = dist_cell_ex.copy_self()
dist_cell_ex = ex_data.copy_self()
dist_cell_ex.copy_values_from_other_cell(dist_cell_ex_old)

# コピー先開始セル
dist_begin_row, dist_begin_col = dist_cell_ex.get_row_and_col()
# 貼り付け
for row in src_cell_ex.get_rows_range():
    dist_cell_ex.set_address_r1c1(col=dist_begin_col)
    for col in src_cell_ex.get_cols_range():
        # コピー先に値をコピー。
        dist_cell_ex.copy_value(src_cell_ex.get_cell_r1c1(row, col), style=True)
        ### log
        d_row, d_col = dist_cell_ex.get_row_and_col()
        value = src_cell_ex.get_value_r1c1(row, col)
        print(' src_cell({},{}) >> dist_cell({},{})  [value={}]'.format(row, col, d_row, d_col, value))
        ###
        dist_cell_ex.move_address(0,1)
    dist_cell_ex.move_address(1,0)

try:
    dist_cell_ex.save_book()
except PermissionError as e:
    msg = '[!]ERROR: ファイルアクセスエラーです。ファイルが開いていたらファイルを閉じてください。'
    print(msg)
    # raise e