"""
エクセルの表に値を書き込む
 特定の列、特定の値の条件に合致したところのみ
   作成中
"""

import excel_data
from excel_data import ExcelSheetDataUtil
from pathlib import Path
import pandas as pd


# print('*書き込みシートをすべてクリア')
file_name = 'myworkbook.xlsx'
sheet_name = 'my sheet1'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=True)

print('データの用意')
keyword = 'ItemL'
ex_data.set_address_by_find(keyword, 'A1', 'P13', debug=False,)
print('begin_address = {}'.format(ex_data.address))
ex_data.range_address = ex_data.get_range_address()
print('range_address = {}'.format(ex_data.range_address))

df_a = ex_data.get_values_from_range_address_pd(
    ex_data.range_address, columns=None)
# first_row_as_list = df_a.iloc[0].astype(str).tolist()
# df_a.columns = first_row_as_list
print('df_a = ')
print(df_a.columns)
print(df_a.shape)
print(df_a)




try:
    ex_data.save_book()
except PermissionError as e:
    msg = '[!]ERROR: ファイルアクセスエラーです。ファイルが開いていたらファイルを閉じてください。'
    print(msg)
    # raise e