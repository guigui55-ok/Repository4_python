"""
エクセルセル読み取りテスト
　パスワード付きエクセル
"""


from excel_data import ExcelSheetDataUtil
from pathlib import Path

file_name = 'excel_with_pass.xlsx'
file_path = Path(__file__).parent.joinpath(file_name)
sheet_name = 'Sheet1'
ex_data = ExcelSheetDataUtil(None, None)
password = 'abc'
ex_data.set_workbook_with_pass(file_path, password=password, data_only=True)
ex_data.set_sheet(sheet_name)
ex_data._update_valid_cell_in_sheet()

print('*セル取得')
val = ex_data.get_value('A1')
print('val = {}'.format(val))