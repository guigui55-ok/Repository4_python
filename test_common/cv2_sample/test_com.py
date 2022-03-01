import os,pathlib

from numpy import true_divide

def get_path(file_path:str,sub_path:str=''):
    path_obj = pathlib.Path(file_path).parent
    if sub_path != '':
        ret = str(path_obj.joinpath(sub_path))
    else:
        ret = str(path_obj)
    return ret

def pathjoin(main_path:str,sub_path:str):
    return os.path.join(main_path,sub_path)

def print_alert(value:str):
    bar = '##################################################'
    print()
    print(bar)
    print(value)
    print(bar)
    print()

def is_exists_file(path:str)->bool:
    if os.path.exists(path):
        return True
    else:
        print_alert('path not exists , path = ' + path)
        return False

from common_utility.log_util.logging_util import LoggerUtility
from common_utility.log_util.logger_init import initialize_logger
def initialize_logger_():
    initialize_logger()