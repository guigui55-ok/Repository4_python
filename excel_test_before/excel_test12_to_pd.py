"""
エクセルから読み込んでDataFrameに変換

セルの日付シリアル値を文字列(y/m/d)に変換
日付のデータをカウント
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
sheet_name = 'my_sheet2'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=False)

keyword = '行番号'
ex_data.set_address_by_find(keyword, 'A1', 'F10', debug=False,)
print('begin_address = {}'.format(ex_data.address))
buf_right_address = ex_data.get_end_address_to_end_horizon(ex_data.Direction.RIGHT)
print('buf_right_address = {}'.format(buf_right_address))
buf_bottom_address = ex_data.get_end_address_to_end_vertical(ex_data.Direction.DOWN)
print('buf_bottom_address = {}'.format(buf_bottom_address))
ex_data.set_range_address([buf_right_address, buf_bottom_address])
print('range_address = {}'.format(ex_data.range_address))

df = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=1)

print('df = ')
print(df.columns)

import datetime
def cnv_date_str(value):
    buf = ExcelSheetDataUtil._cnv_datetime(value)
    if isinstance(buf , datetime.datetime):
        return buf.strftime('%y/%m/%d')
    else:
        return buf

df['カテゴリA'] = df['カテゴリA'].map(cnv_date_str)
df['カテゴリB'] = df['カテゴリB'].map(cnv_date_str)
print(df.values)

target_date = datetime.datetime(year=2024, month=1, day=19).strftime('%y/%m/%d')
# target_date = '24/1/19' # KeyError
df_cat_a = df['カテゴリA'].value_counts()
print('df_cat_a = ')
print(df_cat_a)
count = df_cat_a[target_date]
print('カテゴリA [{}] = {}'.format(target_date ,count))

