


from excel_data import ExcelSheetDataUtil


"""
エクセル参照をしているとき、ほかのファイルをopenpyxlで実行するとどうなるか確認

data_only=True、式ではなくデータとして読み込んでSaveをすると式がすべて値になる
Falseなら式はそのままだが、値は読み込めない
式を保持したいなら、読み込み時と書き込み時で別にフラグを変更しないといけない
または、運用フローでopenpyxlでのエクセルファイルの扱いを読み込んだファイルは書き込まず、
別ファイルに出力するようにする。


openpyxl で書き込んだファイルは、ほかのファイルの参照しているセルが「0」となり、
それをopenpyxl で読み込むと、空文字となる
一度普通にエクセルファイルとして参照元ファイルを開き保存すると、
参照先のファイルでも普通に読み取れるようになる


セルの日付型について
　セル書式を"m月d日"にしても、 openpyxl+pandas では「 Timestamp('2022-08-06 00:00:00')」と認識される
"""


from pathlib import Path
print('*参照式の値変更')

print('*参照しているセルの値')
file_name = 'FileIO.xlsx'
import shutil
back_path = Path(__file__).parent.joinpath('back')
shutil.copy(file_name, back_path)
sheet_name = 'Sheet1'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=False)
ex_data.address = 'N16'

name = ex_data.get_value('N15')
val = ex_data.get_value('N16')
print('title, val = {}, {}'.format(name, val))
# 1つ右のセルを取得表示
ex_data.move_address(-1, 1)
name = ex_data.get_value()
ex_data.move_address(1, 0)
val = ex_data.get_value()
print('title, val = {}, {}'.format(name, val))
# 1つ右のセルを取得表示
ex_data.move_address(-1, 1)
name = ex_data.get_value()
ex_data.move_address(1, 0)
val = ex_data.get_value()
print('title, val = {}, {}'.format(name, val))


val = ex_data.get_value('N19')
val = int(val)+1
ex_data.set_value(val, 'N19')
ex_data.save_book()
print('save path  = {}'.format(ex_data.file_path))
# import os
# path = ex_data.file_path
# name, ext = os.path.splitext(path)
# ext = '.xlsx'
# new_path = Path(path).parent.joinpath(name + '_' + ext)
# ex_data.save_book(new_path)
# print('save path  = {}'.format(new_path))

print('~~~~~~~~~~~~~')
from pathlib import Path
# file_name = 'py_ref_test.xlsx'
file_name = 'FileIO.xlsx'
path = Path(__file__).parent.joinpath(file_name)
import shutil
back_path = Path(__file__).parent.joinpath('back')
shutil.copy(path, back_path)
sheet_name = 'Sheet1'
ex_data_b = ExcelSheetDataUtil(path, sheet_name, data_only=False)

val = ex_data_b.get_value('C5')
print('val = {}'.format(val))
val = int(val)+1
ex_data_b.set_value(val, 'C5')
ex_data_b.save_book()
print('save path  = {}'.format(ex_data_b.file_path))

print('~~~~~~~~~~~~~')
print('参照しているファイルで、参照しているセルのデータを読み込み')
from pathlib import Path
# file_name = 'py_ref_test.xlsx'
path = Path(__file__).parent.joinpath(file_name)
import shutil
back_path = Path(__file__).parent.joinpath('back')
shutil.copy(path, back_path)
sheet_name = 'TestData'
ex_data_b = ExcelSheetDataUtil(path, sheet_name, data_only=True)
ex_data_b.address = 'N6'
####
name = ex_data_b.get_value()
ex_data_b.move_address(1, 0)
val = ex_data_b.get_value()
print('val = {}'.format(val))
###
ex_data_b.move_address(-1, 1)
name = ex_data_b.get_value()
ex_data_b.move_address(1, 0)
val = ex_data_b.get_value()
print('val = {}'.format(val))
###
ex_data_b.move_address(-1, 1)
name = ex_data_b.get_value()
ex_data_b.move_address(1, 0)
val = ex_data_b.get_value()
print('val = {}'.format(val))
###

