"""
エクセルから読み込んで合計

データ集計加工、外部参照テキストファイルと連携
"""

from excel_data import ExcelSheetDataUtil

from pathlib import Path
print('*外部データ連携済みのテキストを書き換え')
text_path = Path(__file__).parent.joinpath('test_ref.txt')
with open(str(text_path), 'r', encoding='utf-8')as f:
    lines = f.readlines()

# 2行目の数値を＋１カウントアップする。
# 2行目には数値のみしかない想定
lines[1] = str( int(lines[1].strip()) + 1 ) + '\n'
with open(str(text_path), 'w', encoding='utf-8')as f:
    f.writelines(lines)
print('write text value = {}'.format(lines[1]))

print('*セルを読み取って合計')
# file_name = 'myworkbook.xlsx'
file_name = 'myworkbook.xlsm'
### 書き込み処理するときは念のためバックアップ
import shutil
back_path = Path(__file__).parent.joinpath('back')
back_path.mkdir(exist_ok=True)
shutil.copy(file_name, back_path)
###
sheet_name = 'my sheet'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=False)

title = '■textファイル参照テスト'
ex_data.set_address_by_find(title, debug=False)
if not ex_data.address_is_valid(ex_data.address):
    raise Exception('Not found value(address={})'.format(ex_data.address))
print('begin_address = {}'.format(ex_data.address))

ex_data.move_address(1,0)
title = ex_data.get_value()
ex_data.move_address(1,0)
value = ex_data.get_value()
print('title, value = {}, {}'.format(title, value))

# print(ex_data.get_value('C1'))
