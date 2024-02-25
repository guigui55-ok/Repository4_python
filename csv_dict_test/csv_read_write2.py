# https://note.nkmk.me/python-csv-reader-writer/

import csv
import pprint

from pathlib import Path
path_c = Path(__file__).parent.joinpath('test_data/power_query_test_data.csv')
path_str_c = str(path_c)

from csv_dict import CsvDict
csv_obj = CsvDict(None)
# csv_obj.encoding = 'shift-jis'
# UnicodeDecodeError: 'shift_jis' codec can't decode byte 0xef in position 0: illegal multibyte sequence
# UnicodeDecodeError: 'cp932' codec can't decode byte 0xef in position 0: illegal multibyte sequence
csv_obj.encoding = 'utf-8-sig'
csv_obj.csv_dict = csv_obj.read_file_as_dict_list(path_str_c)
# list_2d = csv_writer.read_file_as_list_2d()

# https://qiita.com/Ryo-0131/items/7d6b1c772b32c3bbe15e
"""
解決方法
BOMを除去するためには、ファイルを開く際にutf-8-sigのエンコーディングを使用すればOKとのこと。このエンコーディングであれば、BOMを自動的に検出して削除できます。
【Python】CSVを読み込むと文字列の中に\ufeffが入ってしまう場合の原因と解決方法

decoded_file = csvfile.read().decode('utf-8-sig').splitlines() 

"""
key = 'ID'
for val_dict in csv_obj.csv_dict:
    # print(val_dict)
    if val_dict[key] == '41000':
        print(val_dict)
