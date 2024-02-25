"""
エクセルから読み込んで
 DataFrameにして、さらに条件からデータを抽出する

データ集計加工
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

_FILE_NAME = 'updated_test_items.xlsx'
_SHEET_NAME = '項目書'
_BEGIN_WORD = '項番'
_OFFSET_X, _OFFSET_Y = 0, 0
_OUTPUT_CSV_FILE_NAME = 'updated_test_items_test.csv'
_IS_SHIFT_JIS = True

def main():
    print('*範囲データをCSVにする')
    file_name = _FILE_NAME
    # file_name = 'myworkbook.xlsm'
    ### 書き込み処理するときは念のためバックアップ
    import shutil
    back_path = Path(__file__).parent.joinpath('back')
    back_path.mkdir(exist_ok=True)
    shutil.copy(file_name, back_path)
    ###
    sheet_name = _SHEET_NAME
    ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=True)

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

    # # CSV ファイル (employee.csv) として出力
    # if _IS_SHIFT_JIS:
    #     path = Path(_OUTPUT_CSV_FILE_NAME)
    #     file_name = path.stem + '_sjis' + path.suffix
    #     w_path = str(Path(__file__).parent.joinpath(file_name))
    #     df.to_csv(w_path, encoding="shift_jis") 
    # else:
    #     file_name = _OUTPUT_CSV_FILE_NAME
    #     w_path = str(Path(__file__).parent.joinpath(file_name))
    #     df.to_csv(w_path)
    # print('###')
    # print('write_csv_path = {}'.format(w_path))


if __name__ == '__main__':
    main()