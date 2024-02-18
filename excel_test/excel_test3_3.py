"""
Excelの行列から特定の文字列を検索し、そこから入力連続したセルを縦・横に取得して、矩形アドレスを取得する
"""
# https://ramunememo.hatenablog.com/entry/2021/09/23/182202
import openpyxl
from openpyxl.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.utils import get_column_letter
from openpyxl.utils import column_index_from_string
import re
from typing import Union

import excel_test3_2_3 as ex_mod
from excel_test3_2_3 import CellUtil, Direction



def main():
    # filename = 'FileIO.xlsm'
    filename = 'myworkbook.xlsx'
    wb = openpyxl.load_workbook(filename)
    sheet = wb['TestData']

    cellu = CellUtil(sheet)
    begin_address  = cellu.set_address_by_find('■TableA','A1', 'F38')
    cellu.address = 'U10'
    print(cellu.get_value())
    print('begin_address = {}'.format(begin_address))
    begin_cell_b = cellu.move_address(2,0)
    begin_address_b = begin_cell_b.coordinate
    print('begin_address_b = {}'.format(begin_address_b))
    table_address = cellu.get_table_address()
    print('table_address = {}'.format(table_address))
    table_cells = cellu.get_range_cells()
    table_address = cellu.get_range_address_in_cell_list(table_cells)
    print('table_cell = {}'.format(table_address))
    ###
    print('=========')
    address = 'A1:B5'
    row, col = ex_mod.get_row_and_col_from_a1_address(address)
    print((address, row, col))

if __name__ == '__main__':
    main()