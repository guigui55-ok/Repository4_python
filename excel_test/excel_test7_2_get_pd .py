"""
エクセルから読み込んで合計

"""


from excel_data import ExcelSheetDataUtil


from pathlib import Path

print('*セルを読み取って合計')
file_name = 'py_ref_test.xlsx'
### 書き込むとファイルが不可逆になりそうなのでバックアップ
import shutil
back_path = Path(__file__).parent.joinpath('back')
shutil.copy(file_name, back_path)
###
sheet_name = 'TestData'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=False)

title = '■TableC'
title = '■TableA'
ex_data.set_address_by_find(title, debug=False)
if not ex_data.address_is_valid(ex_data.address):
    raise Exception('Not found value(address={})'.format(ex_data.address))
ex_data.move_address(2,0)
print('begin_address = {}'.format(ex_data.address))

range_address = ex_data.get_range_address()
print('range_address = {}'.format(ex_data.range_address))
df = ex_data.get_values_from_range_address_pd(range_address, columns=1)

print('df = ')
print(df.columns)
print(df.values)

import pandas as pd
df_b = df.groupby(by='Enable')['Amount'].sum()
print('合計用の別のDataFrameを作成')
df_c = pd.DataFrame(list(df_b.index), columns=['Enable'])
df_c['Amount'] = df_b.values
print(df_c)


"""
# https://note.nkmk.me/python-pandas-time-series-resample-asfreq/
D: 毎日
B: 毎営業日（月曜 - 金曜）
W: 毎週（日曜始まり）
M: 月末ごと
SM: 15日と月末ごと
Q: 四半期末ごと
AまたはY: 年末ごと
"""
print('合計用の別のDataFrameを作成（日付ごとに計算）')
df_sum = df.set_index('Date').resample('M')['Amount'].sum()
df_d = pd.DataFrame(list(df_sum.index), columns=['DateB'])
df_d['SUM'] = df_sum.values
print(df_d)