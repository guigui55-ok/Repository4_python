"""
エクセルの表を読み込む
    指定した文字列を探す（見つかったセルからオフセット分移動）
    連続したセル（右、下）を取得し、範囲指定
    DFで読み込み
"""

from excel_data import ExcelSheetDataUtil
import excel_data
from pathlib import Path
import pandas as pd


file_name = 'myworkbook.xlsx'
sheet_name = 'my sheet1'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=True)

print('データの用意')
keyword = '■テスト表'
ex_data.set_address_by_find(keyword, 'A1', 'H14', debug=False,)
ex_data.move_address(1,0)
print('begin_address = {}'.format(ex_data.address))
ex_data.range_address = ex_data.get_range_address()
print('range_address = {}'.format(ex_data.range_address))

df_a = ex_data.get_values_from_range_address_pd(
    ex_data.range_address, columns=None)
print('df_a = ')
print(df_a.columns)
print(df_a.shape)
print(df_a)


try:
    # ex_data.save_book()
    pass
except PermissionError as e:
    msg = '[!]ERROR: ファイルアクセスエラーです。ファイルが開いていたらファイルを閉じてください。'
    print(msg)
    # raise e