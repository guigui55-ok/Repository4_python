"""
エクセルから読み込んでCsvに出力する

データ集計加工
 元エクセルを作業フォルダにバックアップする
   複数ファイル対応、バックアップを追加
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


import shutil

def copy_file_to_dir(src_file, dist_dir):
    if dist_dir=='' or dist_dir==None:
        return
    try:
        shutil.copy(str(src_file), str(dist_dir))
        dist_file_path = Path(dist_dir).joinpath(Path(src_file).name)
        print('# COPIED : {}'.format(dist_file_path))
        return dist_file_path
    except Exception as e:
        import traceback
        print()
        print('##########')
        print('[!] COPY ERROR')
        print('src_file = {}'.format(src_file))
        print('dist_dir = {}'.format(dist_dir))
        print('=====================')
        traceback.print_exc()
        print('##########')
        print()


def create_csv_from_excel_with_copy(
    read_file_path,
    read_sheet_name,
    password,
    work_dir,
    range_begin_word,
    begin_offset_row=0,
    begin_offset_col=0,
    csv_dist_dir=None,
    out_put_csv_file_name=None,
    **kwargs
    ):
    """
    パスワード付きのエクセルファイルを特定の場所からコピーしてきて、
     開いて、特定の連続した表をCSVにする。
    
    Args:
        read_file_path : 読み込むエクセルファイル
        read_sheet_name : シート名
        password : パスワード
        work_dir : 作業フォルダ（読み込みのパスからここにコピーされる）
        range_begin_word : 表の開始文字（この文言とoffsetで設定された位置から右側下側に連続した表を読み込む）
        begin_offset_row : 上記の通り
        begin_offset_col : 上記の通り
        csv_dist_dir : 読み取ったデータをCSVにしてwork_dirに出力するが、csv_dist_dirにもコピーする（Noneの時はコピーしない）
        kwargs:
            csv_sjis {bool} : csvの文字コードをsjisで出力する。


    """
    print('*ファイルをコピーする')
    file_path = copy_file_to_dir(read_file_path, dist_dir=work_dir)
    # i = kwargs['i']
    # i_str = '[{}]'.format(i)
    print('*範囲データをCSVにする')
    sheet_name = read_sheet_name
    if password=='' or password==None:
        ex_data = ExcelSheetDataUtil(file_path, read_sheet_name, data_only=True)
    else:
        ex_data = ExcelSheetDataUtil(None, None)
        password = password
        ex_data.set_workbook_with_pass(file_path, password=password, data_only=True)
        ex_data.set_sheet(sheet_name)
        ex_data._update_valid_cell_in_sheet()

    print('*範囲を取得')
    keyword = range_begin_word
    ex_data.set_address_by_find(keyword, debug=False,)
    ex_data.move_address(begin_offset_row, begin_offset_col)
    print('begin_address = {}'.format(ex_data.address))
    buf_right_address = ex_data.get_end_address_to_end_horizon(ex_data.Direction.RIGHT)
    print('buf_right_address = {}'.format(buf_right_address))
    buf_bottom_address = ex_data.get_end_address_to_end_vertical(ex_data.Direction.DOWN)
    print('buf_bottom_address = {}'.format(buf_bottom_address))
    ex_data.set_range_address([buf_right_address, buf_bottom_address])
    print('range_address = {}'.format(ex_data.range_address))

    print('*dfに変換')
    df = ex_data.get_values_from_range_address_pd(ex_data.range_address, columns=1)
    print('df = ')
    print(df.columns)
    print(df.shape)
    # print(df.values)

    print('*CSVファイルに出力')
    # https://pythondatascience.plavox.info/pandas/%E3%83%87%E3%83%BC%E3%82%BF%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%82%92%E5%87%BA%E5%8A%9B%E3%81%99%E3%82%8B
    # CSV ファイル (employee.csv) として出力
    if out_put_csv_file_name=='' or out_put_csv_file_name==None:
        out_put_csv_file_name = Path(read_file_path).stem + '.csv'
    if get_value_kwargs(kwargs, 'csv_sjis'):
        path = Path(out_put_csv_file_name)
        csv_file_name = path.stem + '_sjis' + path.suffix
        encoding = 'sjis'
    else:
        csv_file_name = out_put_csv_file_name
        encoding = 'utf8'
    w_csv_path = str(Path(work_dir).joinpath(csv_file_name))
    df.to_csv(w_csv_path, encoding=encoding)
    print('###')
    print('write_csv_path = {}'.format(w_csv_path))

    copy_file_to_dir(w_csv_path, csv_dist_dir)

def get_value_kwargs(kwargs, key):
    try:
        return kwargs[key]
    except KeyError:
        return ''

class FileInfo():
    EXCEL_FILE_NAME = 'excel_with_pass.xlsx'
    SHEET_NAME = 'TestSheet'
    PASSWORD = 'abc'
    READ_DIR = Path(__file__).parent
    WORK_DIR = Path(__file__).parent.joinpath('work')
    BEGIN_WORD = '日付'
    OFFSET_ROW, OFFSET_COL = 0, 0
    OUTPUT_CSV_FILE_NAME = 'excel_with_pass.csv'
    CSV_DIST_DIR = Path(__file__).parent.joinpath('result')
    CSV_SJIS = True

class FileinfoB(FileInfo):
    EXCEL_FILE_NAME = 'excel_with_pass2.xlsx'
    SHEET_NAME = 'TestSheet'
    PASSWORD = 'abc'
    READ_DIR = Path(__file__).parent
    WORK_DIR = Path(__file__).parent.joinpath('work')
    BEGIN_WORD = '日付'
    OFFSET_ROW, OFFSET_COL = 0, 0
    OUTPUT_CSV_FILE_NAME = 'excel_with_pass2.csv'
    CSV_DIST_DIR = Path(__file__).parent.joinpath('result')
    # CSV_SJIS = True
    CSV_SJIS = True

if __name__ == '__main__':
    target_info = [FileInfo, FileinfoB]
    info:FileInfo = None
    for i, info in enumerate(target_info):
        print()
        print('=====================')
        print('# i={}, type={}'.format(i, type(info)))
        read_file_path = Path(info.READ_DIR).joinpath(info.EXCEL_FILE_NAME)
        create_csv_from_excel_with_copy(
            read_file_path= read_file_path,
            read_sheet_name=info.SHEET_NAME,
            password=info.PASSWORD,
            work_dir=info.WORK_DIR,
            range_begin_word=info.BEGIN_WORD,
            begin_offset_row=info.OFFSET_ROW,
            begin_offset_col=info.OFFSET_COL,
            csv_dist_dir=info.CSV_DIST_DIR,
            csv_sjis=info.CSV_SJIS)