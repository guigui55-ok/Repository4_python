
from pathlib import Path
from typing import Union
import glob
from delete_files import debug_print
from delete_files import is_match_patterns_any
from delete_files import NEW_LINE

def debug_print(value, debug, flush=True):
    if debug:
        print(str(value), flush=flush)

def search_folder(
        dir_path,
        patterns:Union[str, 'list[str]'],
        name_only:bool=True,
        dir_only:bool=False,
        debug=None):
    global DEBUG
    if debug!=None:
        DEBUG = debug
    if isinstance(patterns , str):
        patterns = [patterns]    
    buf_flag = glob._ishidden
    glob._ishidden = lambda x: False
    if dir_only:
        dir_paths = glob.glob(str(dir_path + '/**/'), recursive=True)
        glob._ishidden = buf_flag
        debug_print('len(dir_paths) = {}'.format(len(dir_paths)), debug)
        match_list = get_match_list_path(patterns, dir_paths, name_only, debug)
    else:
        # file_paths = glob.glob(str(dir_path + '/*'), recursive=True)#25
        file_paths = glob.glob(str(dir_path + '/**/*'), recursive=True)
        glob._ishidden = buf_flag
        debug_print('len(file_paths) = {}'.format(len(file_paths)), debug)
        match_list = get_match_list_path(patterns, file_paths, name_only, debug)

def get_match_list_path(patterns, check_list:'list[str]', name_only:bool=True, debug:bool=True):
    if name_only:
        check_list_b = [Path(x).name for x in check_list]
    ret_list = []
    for i, check_value in enumerate(check_list_b):
        if is_match_patterns_any(check_value, patterns):
            ret_list.append(check_list[i])
            debug_print('  #MATCH i={}, value = {}'.format(i, check_list[i]), debug)
    if len(ret_list)<1:
            debug_print('  #MATCH list is Nothing', debug)
    return ret_list


if __name__ == '__main__':
    PATH = r'F:\BACKUP\BKUP_231115\repos'
    PATTERN = '.*/.git'
    PATTERN = '\.git'
    PATTERN = '.git'
    search_folder(PATH, PATTERN, debug=True)