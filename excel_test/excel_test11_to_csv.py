"""
エクセルから読み込んで合計

データ集計加工
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

print('*セルをコピー、貼り付け')
file_name = 'myworkbook.xlsx'
# file_name = 'myworkbook.xlsm'
### 書き込み処理するときは念のためバックアップ
import shutil
back_path = Path(__file__).parent.joinpath('back')
back_path.mkdir(exist_ok=True)
shutil.copy(file_name, back_path)
###
sheet_name = 'Copy'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=False)

title = 'ID'
ex_data.set_address_by_find(title, 'I3', debug=False,)
print('begin_address = {}'.format(ex_data.address))

# right_end_cell:ExcelSheetDataUtil = ex_data.copy_self()
right_end_cell = ex_data.copy_self()
right_end_cell.get_end_address_to_end_horizon(ex_data.Direction.RIGHT)
# コピー先開始セル
right_end_cell.move_address(0,1)
value = ex_data.get_value()
print('title, value = {}, {}'.format(title, value))

# print(ex_data.get_value('C1'))

# ex_data.move_address()