"""
シートの任意の位置からデータ入力
 StrCellではない普通のstrを値に持つDataFrameをエクセルに書き込み、ファイルを保存

"""
from pathlib import Path
from excel_data import ExcelSheetDataUtil

print('*シートの任意の位置からデータ入力 DataFrame')
file_name = 'test_write.xlsx'
sheet_name = 'test_write'
file_path = Path(__file__).parent.joinpath(file_name)
ex_data = ExcelSheetDataUtil(file_path, sheet_name, data_only=True)

ex_data.book.remove(ex_data.sheet)

print('sheet_names = ')
print(ex_data.book.get_sheet_names())

ex_data.book.create_chartsheet()
print('sheet_names = ')
print(ex_data.book.get_sheet_names())

import pandas as pd
DF_DATA_A = [
 ['001', 'ItemA', 1, '●', 50, '2022-08-06 00:00:00'],
 ['002', 'ItemB', 2, '', 20, '2021-12-07 00:00:00'],
 ['005', 'ItemE', 5, '', 220, '2022-12-07 00:00:00'],
 ['003', 'ItemC', 3, '', 80, '2023-02-25 00:00:00']]

df_a = pd.DataFrame(DF_DATA_A, columns=DF_DATA_A)
print('df_a =')
print(df_a)
# print(df_a.dtypes)


ex_data.set_cell('C3')
begin_address = ex_data.address
begin_cell = ex_data._get_cell(begin_address)
print('begin_address = {}'.format(begin_address))
# end_cell = ex_data._get_cell(range_end_address)
# begin_cell_buf = ex_data.find_entire_row_in_range(0, keyrowd='Result', debug=None)
# print('begin_cell_buf = {}'.format(begin_cell_buf))
# print('******')
# begin_cell_buf = ex_data.find_entire_col_in_range(0, keyrowd='A005')
# print(begin_cell_buf)
# ex_data.reset_book_sheet(data_only=False)
# cells_2d = ex_data.get_entire_col_in_range_by_cell(begin_cell_buf)
from openpyxl.cell import Cell
# print(type(df_a.loc[0]))
# <class 'pandas.core.series.Series'>
cell:Cell=None
# df = df_a['Result']

print('格納先のCellをリスト[cells_2d]にすべて取得ない処理パターン')
print('開始セルアドレスをセットして、dfの配列を順番に書き込んでいく')
# cells_2d:list[numpy.ndarray]
# for num , ds in enumerate(cells_2d):
w_df = df_a
columns = w_df.columns
for i , column_name in enumerate(columns):
    # print('### {}'.format(i))
    # for (data, cell) in zip(df, row_cells):
    # for j, ds in enumerate(w_df.loc[i]): #KeyError: 4
    # for j, ds in enumerate(w_df.iloc[column_name]): #pandas.core.indexing.IndexingError: Too many indexers
    for j, ds in enumerate(w_df[column_name]):
        val = ds
        # ex_data.set_value_offset(val, i, j)
        cell:Cell = ex_data.get_offset_cell(j, i)
        ex_data.set_value(val, cell.coordinate)
        print('{}, ij[{}, {}] = {}'.format(cell,i,j, val))
        cell.value = val
print()


try:
    ex_data.save_book()
except PermissionError as e:
    msg = '[!]ERROR: ファイルアクセスエラーです。ファイルが開いていたらファイルを閉じてください。'
    print(msg)
    # raise e
