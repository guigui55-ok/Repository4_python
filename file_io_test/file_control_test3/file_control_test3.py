
from msilib.schema import MoveFile
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
from common_utility.file_util.count_up_file_name import move_file,copy_file,FileControlMode
# copy_file(src_dir,src_file_name,dist_dir,'')
move_file_(src_dir,src_file_name,dist_dir,'')