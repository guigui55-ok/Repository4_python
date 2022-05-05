
import import_init

import shutil

import pathlib,os
src_path = r'C:\Users\OK\source\repos\Repository4_python\file_io_test\file_control_test2\files\testfile.txt'
src_dir = os.path.dirname(src_path)
src_file_name = os.path.basename(src_path)
dist_dir = str(pathlib.Path(__file__).parent)
dist_dir = os.path.join(dist_dir,'files')

print()
print('---------')
print('src_path =')
print(os.path.join(src_dir,src_file_name))
print('dist_dir =')
print(dist_dir)

# from common_utility.file_util.file_name_util import add_str_to_file_name
from common_utility.file_util.count_up_file_name import create_dist_file_path
new_file_path = create_dist_file_path(dist_dir,src_file_name)
if not os.path.exists(src_path):
    print('file not exists')
    print('path = ' + src_path)
    exit()

try:
    if new_file_path != src_path:
        # shutil.move(src_path, new_file_path)#rename
        shutil.copy(src_path, new_file_path)#copy
    else:
        print('file name is same')
        print('path = ' + src_path)
except:
    import traceback
    traceback.print_exc()


# shutil.move(path,move_dir)
#既に存在するとエラー
#例外が発生しました: Error Destination path 

# shutil.copy(path,move_dir)
#既に存在するとエラー
#例外が発生しました: SameFileError
