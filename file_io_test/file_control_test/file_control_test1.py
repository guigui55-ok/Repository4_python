

import shutil

path = r'C:\Users\OK\source\repos\Repository4_python\file_io_test\file_control_test\files\testfile.txt'
import pathlib,os
move_dir = str(pathlib.Path(__file__).parent)
move_dir = os.path.join(move_dir,'files')

print()
print('---------')
print('file_path=')
print(path)
print('move_dir=')
print(move_dir)

# shutil.move(path,move_dir)
#既に存在するとエラー
#例外が発生しました: Error Destination path 

# shutil.copy(path,move_dir)
#既に存在するとエラー
#例外が発生しました: SameFileError
