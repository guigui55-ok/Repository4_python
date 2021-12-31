"""
外部pathから common_util ,logger_util を使用する
"""

import os ,pathlib , sys
path = str(pathlib.Path(__file__).resolve().parent)
path = str(pathlib.Path(path).resolve().parent)
# path = str(Path(path).resolve().parent)
sys.path.append(path)
print('sys.path.append')
print(path)

import common_util

import common_util.log_util.logger_init as logger_init
import common_util.log_util.logging_util as logging_util
from common_util.file_util.file_class import MyFile
def initialize_logger_new() -> logging_util.logger_util:
    return logger_init.initialize_logger()

def get_current_dir()->str:
    import pathlib
    dir_path = str(pathlib.Path(__file__).parent)
    return dir_path

def get_path_from_current_dir(child_path:str)->str:
    import os
    dir_path = get_current_dir()
    path = os.path.join(dir_path,child_path)
    return path