from genericpath import isdir
from shutil import copy
import shutil


def sub():
    import os
    import pathlib
    path = str(pathlib.Path(__file__).parent.joinpath('test_dir'))
    path = str(pathlib.Path(__file__).parent.joinpath('test_dir2'))
    path = './test_dir'
    print(path)
    flag = os.path.exists(path)
    print(flag)

def main():
    import pathlib
    src_path = str(pathlib.Path(__file__).parent.joinpath('test_dir'))
    # PermissionError: [Errno 13] Permission denied: 'c:\\Users\\OK\\source\\repos\\Repository4_python\\zzz\\test_dir'
    # src_path = str(pathlib.Path(__file__).parent.joinpath('test_dir'))
    # src_path = src_path.replace('\\','/')
    src_path = './test_dir'
    # src_path = './test2.py'
    # src_path = str(pathlib.Path(__file__).parent.joinpath('test1.py'))
    dist_path = str(pathlib.Path(__file__).parent.joinpath('test_dir2'))
    dist_path = './test_dir2'
    print(src_path)
    # copy(src_path, dist_path)
    shutil.copytree(src_path, dist_path)
    return


if __name__ == '__main__':
    sub()
    main()

import os
from shutil import copy, copytree

src_path = 'コピー元パス'
dist_path = 'コピー先パス'
if os.path.isfile(src_path):
    copy(src_path, dist_path)
else:
    copytree(src_path, dist_path)