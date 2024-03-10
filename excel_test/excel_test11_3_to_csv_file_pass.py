"""
エクセルから読み込んで、日付を読み込み、対象の月のデータのみをCSVにする
 パス付エクセル用

"""

from excel_data import ExcelSheetDataUtil
import excel_data
from pathlib import Path



###
_FILE_NAME = 'excel_with_pass.xlsx'
_READ_DIR = r''
_SAVE_DIR = r'C:\Users\OK\source\repos\test_media_files\excel_test_data\test3'
_START_DATE = '02-01'

###
file_name = _FILE_NAME 
if _READ_DIR!='':
    read_dir_path = Path(_READ_DIR)
else:
    read_dir_path = Path(__file__).parent
if _SAVE_DIR!='':
    save_dir_path = Path(_READ_DIR)
else:
    save_dir_path = Path(__file__).parent
###
print('*ファイル読み込み')
file_path = read_dir_path.joinpath(file_name)
sheet_name = 'TestSheet'
ex_data = ExcelSheetDataUtil(None, None)
password = 'abc'
unlock_file_name = Path(_FILE_NAME).stem + '_unlock' + Path(_FILE_NAME).suffix
unlock_file_path = save_dir_path.joinpath(unlock_file_name)
ex_data.set_workbook_with_pass(
    file_path, password=password, data_only=True, out_put_file_path=unlock_file_path, debug=True)
ex_data.set_sheet(sheet_name)
ex_data._update_valid_cell_in_sheet()

# 月末を算出
start_date = _START_DATE
import datetime
start_datetime = datetime.datetime(
    year=datetime.datetime.now().year,
    month=int(start_date.split('-')[0]),
    day=int(start_date.split('-')[1]))
import calendar
end_date = calendar.monthrange(
    start_datetime.year, start_datetime.month)[1].__str__()
end_date = start_date.split('-')[0] + '-' + end_date
print('start_date = {}'.format(start_date))
print('end_date = {}'.format(end_date))

###################

print('テーブルの最初のセルを検索')
keyword = '日付'
ex_data.set_address_by_find(keyword, 'A1', 'F10', debug=False,)
buf_begin_address = ex_data.address
print('buf_begin_address = {}'.format(buf_begin_address))

print('テーブルの右端のセルを検索')
buf_right_address = ex_data.get_end_address_to_end_horizon(ex_data.Direction.RIGHT)
print('buf_right_address = {}'.format(buf_right_address))

print('開始日付（読み込み開始行）を検索')
find_date = start_date
find_begin = ex_data.get_column_letter() + '1'
buf_list = ex_data.find_value(ex_data.sheet, find_date, find_begin, None, debug=False,)
if len(buf_list)<1:
    msg = '値が見つからない（fid_date={}）'.format(find_date)
    raise Exception(msg)
begin_row_address = buf_list[0]
print('begin_row_address = {}'.format(begin_row_address))


print('終了日付（読み込み終了行）を検索')
find_date = end_date
find_begin = ex_data.get_column_letter() + '1'
buf_list = ex_data.find_value(ex_data.sheet, find_date, find_begin, None, debug=False,)
if len(buf_list)<1:
    msg = '値が見つからない（fid_date={}）'.format(find_date)
    # raise Exception(msg)
    print('終了日がなければ最終行を取得する')
    end_row_address = ex_data.get_end_address_to_end_vertical(ex_data.Direction.DOWN)
else:
    print('終了日を発見')
    end_row_address = buf_list[0]
    end_row_address = excel_data.get_offset_address(end_row_address, -1, 0)
print('end_row_address = {}'.format(end_row_address))

print('右端と左下のアドレスから、右下を取得する。')
ex_data.set_address_a1(begin_row_address)
range_end_address = excel_data.get_max_address([buf_right_address, end_row_address])
print('range_end_address = {}'.format(range_end_address))

print('取得する範囲をセットする。')
ex_data.set_range_address([begin_row_address, range_end_address])
print('range_address = {}'.format(ex_data.range_address))
range_address_a = ex_data.range_address

print('データを読み込みDataFrameに変換')
df_a = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=1)
print('df_a = ')
print(df_a.columns)
print(df_a.values)

print('DataFrameをCSVファイルに出力')
csv_file_name = 'csv_file.csv'
csv_path = save_dir_path.joinpath(csv_file_name)
# df_a.to_csv("data_from_df.csv")
df_a.to_csv(csv_path, encoding="shift_jis")

print('csv_save_path = {}'.format(csv_path))
