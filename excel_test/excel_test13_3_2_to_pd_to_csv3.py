"""
エクセルから読み込んでCsvに出力する

データ集計加工
 元エクセルを作業フォルダにバックアップする
"""


from excel_data import ExcelSheetDataUtil
from pathlib import Path

import datetime
def cnv_date_str(value):
    buf = ExcelSheetDataUtil._cnv_datetime(value)
    if isinstance(buf , datetime.datetime):
        return buf.strftime('%y/%m/%d')
    else:
        return buf

_FILE_NAME = 'excel_with_pass.xlsx'
_SHEET_NAME = 'TestSheet'
_BEGIN_WORD = '日付'
_OFFSET_X, _OFFSET_Y = 0, 0
_OUTPUT_CSV_FILE_NAME = 'excel_with_pass.csv'
_IS_SHIFT_JIS = True
_IS_SHIFT_JIS = False

def main():
    print('*範囲データをCSVにする')
    file_name = _FILE_NAME
    sheet_name = _SHEET_NAME
    # ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=True)

    file_name = _FILE_NAME
    file_path = Path(__file__).parent.joinpath(file_name)
    sheet_name = _SHEET_NAME
    ex_data = ExcelSheetDataUtil(None, None)
    password = 'abc'
    ex_data.set_workbook_with_pass(file_path, password=password, data_only=True)
    ex_data.set_sheet(sheet_name)
    ex_data._update_valid_cell_in_sheet()

    print('*セル取得')
    val = ex_data.get_value('A1')
    print('val = {}'.format(val))


    keyword = _BEGIN_WORD
    ex_data.set_address_by_find(keyword, debug=False,)
    ex_data.move_address(_OFFSET_X, _OFFSET_Y)
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
    print(df.values)

    # https://pythondatascience.plavox.info/pandas/%E3%83%87%E3%83%BC%E3%82%BF%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%82%92%E5%87%BA%E5%8A%9B%E3%81%99%E3%82%8B
    # CSV ファイル (employee.csv) として出力
    if _IS_SHIFT_JIS:
        path = Path(_OUTPUT_CSV_FILE_NAME)
        file_name = path.stem + '_sjis' + path.suffix
    else:
        file_name = _OUTPUT_CSV_FILE_NAME
    w_path = str(Path(__file__).parent.joinpath(file_name))
    df.to_csv(w_path)
    print('###')
    print('write_csv_path = {}'.format(w_path))

    # from csv_dict_test.csv_dict import CsvDict
    # csv_path = Path(__file__).joinpath('data_from_df_by_csv_dict.csv')
    # csv_dict = CsvDict(csv_path)

if __name__ == '__main__':
    main()