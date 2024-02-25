# https://note.nkmk.me/python-csv-reader-writer/

import csv
import pprint

from pathlib import Path
path = Path(__file__).parent.joinpath('test_data/data_from_df_sjis.csv')
path_str = str(path)
with open(path_str) as f:
    print(f.read())

# ,ID,Name,Result,ID2,Result2
# 0,A001,01_A001,OK,A001,OK
# 1,A002,01_A002,NG,A002,NG
# ~

with open(path_str) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ['', 'ID', 'Name', 'Result', 'ID2', 'Result2']
# ['0', 'A001', '01_A001', 'OK', 'A001', 'OK']
# ['1', 'A002', '01_A002', 'NG', 'A002', 'NG']
# ~
        
buf_list_2d = [
['', 'ID', 'Name', 'Result', 'ID2', 'Result2'],
['0', 'A001', '01_A001', 'OK', 'A001', 'OK'],
['1', 'A002', '01_A002', 'NG', 'A002', 'NG'],
['2', 'A003', '01_A003', 'OK', 'A003', 'OK'],
['3', 'A004', '01_A004', 'OK', 'A004', 'OK']]
# ['4', 'A005', '01_A005', 'OK', 'A005', 'OK'],
# ['5', 'A006', '02_A006', 'OK', 'A006', 'OK'],
# ['6', 'A007', '02_A007', 'NG', 'A007', 'NG'],
# ['7', 'A008', '05_A008', 'OK', 'A008', 'OK'],
# ['8', 'A009', '05_A009', 'OK', 'A009', 'OK'],
# ['9', 'A010', '05_A010', 'NG', 'A010', 'NG'],
# ['10', 'A011', '05_A011', 'OK', 'A011', 'OK'],
# ['11', 'A012', '04_A012', '#N/A', 'A012', '#N/A'],
# ['12', 'A013', '04_A013', 'OK', 'A013', 'OK'],
# ['13', 'A014', '04_A014', 'NG', 'A014', 'NG'],
# ['14', 'A015', '03_A015', 'OK', 'A015', 'OK'],
# ['15', 'A016', '03_A016', 'NG', 'A016', 'NG']]

from csv_dict import CsvDict
path_b = Path(__file__).parent.joinpath('test_data/csv_write_test.csv')
path_str_b = str(path_b)

# https://qiita.com/ryokurta256/items/defc553f5165c88eac95
# newline設定をしないと、書き込み時1行空いてしまう
with open(path_str_b, 'w', newline="") as f:
    writer = csv.writer(f)
    # for row_data in buf_list_2d:
    #     writer.writerow(row_data)
    writer.writerows(buf_list_2d)

csv_writer = CsvDict(path_str_b)
csv_writer.write_file_by_list_2d(buf_list_2d)

with open(path_str_b) as f:
    print(f.read())