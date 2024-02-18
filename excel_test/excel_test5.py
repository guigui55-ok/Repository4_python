"""
エクセルセル読み取りテスト
"""


from excel_data import ExcelSheetDataUtil


# file_name = 'FileIO.xlsm'
file_name = 'myworkbook.xlsx'
# sheet_name = 'Sheet1'
sheet_name = 'Sheet'
ex_data = ExcelSheetDataUtil(file_name, sheet_name)

print('*結合セル取得')
val = ex_data.get_value('B4')
print('val = {}'.format(val))
val = ex_data.get_value('N4')
print('val = {}'.format(val))
val = ex_data.get_value('N5')
print('val = {}'.format(val))
val = ex_data.get_value('O4')
print('val = {}'.format(val))
val = ex_data.get_value('O5')
print('val = {}'.format(val))
val = ex_data.get_value('N6')
print('val = {}'.format(val))

print('*式取得 値（計算値）')
val = ex_data.get_value('N11')
print('val = {}'.format(val))

print('*式取得 式')
ex_data.reset_book_sheet(data_only=False)
val = ex_data.get_value('N11')
print('val = {}'.format(val))
#
ex_data.reset_book_sheet(data_only=True)

