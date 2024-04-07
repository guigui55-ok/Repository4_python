"""
エクセルの表に値を書き込む
 特定の列、特定の値の条件に合致したところのみ
"""

import excel_data
from excel_data import ExcelSheetDataUtil
from pathlib import Path
import pandas as pd


# print('*書き込みシートをすべてクリア')
file_name = 'myworkbook.xlsx'
file_name = Path(__file__).parent.joinpath(file_name)
sheet_name = 'my sheet1'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=True)

print('データの用意')
keyword = '■条件一致書き込みテスト表'
ex_data.set_address_by_find(keyword, 'A1', 'P22', debug=False,)
ex_data.move_address(1, 0)
print('sheet={}, keyword={}'.format(ex_data.sheet.title, keyword))
print('begin_address = {}'.format(ex_data.address))
ex_data.range_address = ex_data.get_range_address()
print('range_address = {}'.format(ex_data.range_address))

df_a = ex_data.get_values_from_range_address_pd(
    ex_data.range_address, columns=0)
# first_row_as_list = df_a.iloc[0].astype(str).tolist()
# df_a.columns = first_row_as_list
print('df_a = ')
print(df_a.columns)
print(df_a.shape)
print(df_a)

print('*設定する値をセットする')
set_values_dict = {}
d = {'項目2':'22'}
set_values_dict.update(d)
print('set_values_dict')
print(set_values_dict)

print('書き込みのためにシートを読み直す（data_only=False)')
ex_data.reset_book_sheet(data_only=False)

print('*表にデータを入力していく')

from openpyxl.cell import Cell
str_cell:excel_data.StrCell=None
buf_cell:Cell=None
df_a_col_name_find = df_a.columns[0]
df_a_col_name_write = df_a.columns[1]
#結果の日付列をfor文で処理する
for i, col_name_key in enumerate(set_values_dict.keys()):
    update_value = set_values_dict[col_name_key]
    # df_a 対象の項目名データ(StrCell)を取得（含まれる文字列を検索）
    buf_df = df_a[df_a[df_a_col_name_find].str.contains(col_name_key)]
    # buf_df = df_a[df_a[col_name_key] == target_col_value)#完全一致
    # 書き込み先の表Bの該当する日付のデータ（とCell）を取得する
    if buf_df.shape[0]==0:
        print(' *nothing data(buf_df.shape={})'.format(buf_df.shape))
        print('[{}] -> {}, col_name_key={}'.format(
            None, update_value, col_name_key))
        continue
    #buf_df_b はDataFrame型が返る
    # 見つかった値はStrCellでアドレスデータを持っているので、そのセルに書き込む
    for index, row in buf_df.iterrows():
        # row[df_a_col_name_write].cell.value = str(update_value)
        # df_aのStrCellに書き込んでも、そのCellをex_dataの方に上書きしないと、Saveしても反映されない。
        address = row[df_a_col_name_write].cell.coordinate
        ex_data.set_value(str(update_value), address)
        print('[{}] -> {}, col_name_key={}'.format(
            address, update_value, col_name_key))

try:
    ex_data.save_book()
except PermissionError as e:
    msg = '[!]ERROR: ファイルアクセスエラーです。ファイルが開いていたらファイルを閉じてください。'
    print(msg)
    # raise e