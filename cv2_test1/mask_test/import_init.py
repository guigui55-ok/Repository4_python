"""
外部pathから common_util ,logger_util を使用する
"""

import os 
image_path = os.getcwd()
from pathlib import Path
path = str(Path(__file__).resolve().parent)
print('__file__.parent = ' + path)
path = str(Path(path).resolve().parent)
path = str(Path(path).resolve().parent)
import sys
sys.path.append(path)
print('sys.path.append')
print(path)

import common_util

import common_util.log_util.logger_init as logger_init
import common_util.log_util.logging_util as logging_util
def initialize_logger_new() -> logging_util.logger_util:
    return logger_init.initialize_logger()

def get_current_dir()->str:
    """__file__(import_init.py) があるディレクトリ"""
    import pathlib
    dir_path = str(pathlib.Path(__file__).parent)
    return dir_path

def get_path_from_current_dir(child_path:str)->str:
    """__file__(import_init.py) があるディレクトリ に child_path をjoinしたものを返す"""
    import os
    dir_path = get_current_dir()
    path = os.path.join(dir_path,child_path)
    return path

def path_join(*args):
    """import os、os.path.join を1行で書くためのメソッド"""
    import os 
    val = args
    if len(val) < 1 : return ''
    path = ''
    for i in range(len(val)):
        buf = val[i]
        if i==0:
            path = buf
        else:
            path = os.path.join(path,buf)
    return path