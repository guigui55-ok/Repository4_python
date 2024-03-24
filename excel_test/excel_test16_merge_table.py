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
################################################################################
################################################################################
import pandas as pd
# 'ID'列を文字列型に変換
df_a['項番'] = df_a['項番'].astype(str)
df_b['項番'] = df_b['項番'].astype(str)

# df_aとdf_bを'ID'列を基にして結合
df = pd.merge(df_a, df_b, on='ID', how='left')

# import datetime
# def cnv_date_str(value):
#     buf = ExcelSheetDataUtil._cnv_datetime(value)
#     if isinstance(buf , datetime.datetime):
#         return buf.strftime('%y/%m/%d')
#     else:
#         return buf

# df['カテゴリA'] = df['カテゴリA'].map(cnv_date_str)
# df['カテゴリB'] = df['カテゴリB'].map(cnv_date_str)
# print(df.values)

# target_date = datetime.datetime(year=2024, month=1, day=19).strftime('%y/%m/%d')
# # target_date = '24/1/19' # KeyError
# df_cat_a = df['カテゴリA'].value_counts()
# print('df_cat_a = ')
# print(df_cat_a)
# count = df_cat_a[target_date]
# print('カテゴリA [{}] = {}'.format(target_date ,count))

