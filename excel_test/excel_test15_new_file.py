"""
エクセルセル ファイル新規作成
"""


from excel_data import ExcelSheetDataUtil
from pathlib import Path

file_name = 'test_write.xlsx'
file_path = Path(__file__).parent.joinpath(file_name)
if Path(file_path).exists():
    import os
    os.remove(file_path)
    print('# REMOVED : {}'.format(file_path))
else:
    print('# NOTHING : {}'.format(file_path))
sheet_name = 'test_write'
ex_data = ExcelSheetDataUtil(None, None)
ex_data.create_new_file(file_path, sheet_name, set_self=True)
print('# CREATED : {}'.format(ex_data.file_path))

print('* change sheet name')
ex_data.sheet.title = 'test_write_rename'
ex_data.save_book()
print('# SAVED : {}'.format(ex_data.file_path))