"""
エクセルセル
    テーブルマージ（異なるColumn構成）
     DataFrame使用

行、列が異なるものをマージする
表A（基準の表）、表B（列、行ともにAより多い）

----
（未確認）
表A（基準の表）、表B（列が多い、行が少ない）
表A（基準の表）、表B（列が少ない、行が多い）
---
表Bの変更点を優先する
表Bの特定の列（複数）は変更点を優先、それ以外はA

"""

from excel_data import ExcelSheetDataUtil
from pathlib import Path

################################################################################
################################################################################
file_name = 'updated_test_items.xlsx'
sheet_name = '項目書A'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=False)

keyword = '項番'
ex_data.set_address_by_find(keyword, 'A1', 'F10', debug=False,)
print('begin_address = {}'.format(ex_data.address))
buf_right_address = ex_data.get_end_address_to_end_horizon(ex_data.Direction.RIGHT)
print('buf_right_address = {}'.format(buf_right_address))
buf_bottom_address = ex_data.get_end_address_to_end_vertical(ex_data.Direction.DOWN)
print('buf_bottom_address = {}'.format(buf_bottom_address))
ex_data.set_range_address([buf_right_address, buf_bottom_address])
print('range_address = {}'.format(ex_data.range_address))

df_a = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=1)

print('df_a = ')
print(df_a.columns)
print(df_a.shape)

################################################################################
################################################################################

file_name = 'updated_test_items.xlsx'
sheet_name = '項目書B'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=False)

keyword = '項番'
ex_data.set_address_by_find(keyword, 'A1', 'F10', debug=False,)
print('begin_address = {}'.format(ex_data.address))
buf_right_address = ex_data.get_end_address_to_end_horizon(ex_data.Direction.RIGHT)
print('buf_right_address = {}'.format(buf_right_address))
buf_bottom_address = ex_data.get_end_address_to_end_vertical(ex_data.Direction.DOWN)
print('buf_bottom_address = {}'.format(buf_bottom_address))
ex_data.set_range_address([buf_right_address, buf_bottom_address])
print('range_address = {}'.format(ex_data.range_address))

df_b = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=1)

print('df_b = ')
print(df_b.columns)
print(df_b.shape)
################################################################################
################################################################################
print('シートを追加（式を保持するためにファイルを読み直す')
ex_data.reset_book_sheet(data_only=False)
ex_data.add_sheet('項目書C')
print()
ex_data.save_book()
print()
################################################################################
import pandas as pd
print()
print('######')
print('項番 列を文字列型に変換して、A>Bにマージする')
# 'ID'列を文字列型に変換
df_a['項番'] = df_a['項番'].astype(str)
df_b['項番'] = df_b['項番'].astype(str)

# df_aとdf_bを'ID'列を基にして結合
# df = pd.merge(df_a, df_b, on='ID', how='left')
df = pd.merge(df_b, df_a, on='項番', how='left')
print('df = ')
print(df)
################################################################################
################################################################################


