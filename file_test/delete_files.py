from pathlib import Path
import re
from typing import Union
import glob
import shutil
import os

NEW_LINE = '\n'
DEBUG = True
def debug_print(value):
    if DEBUG:
        print(str(value))

def is_match_patterns_any(value , patterns:'list[str]'):
    value = str(value)
    for pattern in patterns:
        if re.search(pattern, value)!=None:
            return True
    else:
        return False

def get_value_from_kwargs(key, *args):
    try:
        for arg in args:
            if list(arg.keys())[0] == key:
                return arg[key]
        return None
    except KeyError:
        return None

def delete_file(path, **kwargs):
    i = get_value_from_kwargs('i', kwargs)
    if i==None:
        i==''
    try:
        if Path(path).is_file():
            os.remove(path)
        else:
            if not os.access(path, os.W_OK):
                os.chmod(path, 755)
            shutil.rmtree(path)
            debug_print('  # REMOVE[{}] {}'.format(i, path))
        return True
    except Exception as e:
        debug_print('  # [{}]ERROR:{} (path={})'.format(i, str(e), path))
        return False

def delete_folder(dir_path, patterns:Union[str, 'list[str]'], debug=None):
    global DEBUG
    if debug!=None:
        DEBUG = debug
    if isinstance(patterns , str):
        patterns = [patterns]
    # paths = glob.glob(str(dir_path + '/*'))
    # paths = glob.glob(str(dir_path + '/*'), recursive=True) 
    # paths = glob.glob(str(dir_path + '/**'), recursive=True) #file
    # paths = glob.glob(str(dir_path + '/**/*'), recursive=True) #file
    w_path = Path(__file__).parent.joinpath('memo.txt')
    
    if not w_path.exists():
        buf_flag = glob._ishidden
        glob._ishidden = lambda x: False
        paths = glob.glob(str(dir_path + '/**/'), recursive=True)
        glob._ishidden = buf_flag
        debug_print('len(paths) = {}'.format(len(paths)))
        with open(str(w_path), 'w', encoding='utf-8')as f:
            for i, path in enumerate(paths):
                if Path(path).name.endswith('git'):
                    print('')
                if is_match_patterns_any(path, patterns):
                    delete_file(path, i=i)
                f.write(str(path) + NEW_LINE)
        print('w_path = {}'. format(w_path))
    else:
        with open(str(w_path), 'r', encoding='utf-8')as f:
            paths = f.readlines() 
            for i, path in enumerate(paths):
                path = str(path).strip()
                if Path(path).name.endswith('git'):
                    print('match git')
                if is_match_patterns_any(path, patterns):
                    delete_file(path, i=i)
        


if __name__ == '__main__':
    PATH = r'F:\BACKUP\BKUP_231115\repos'
    # PATTERN = '.*/.git'
    # PATTERN = '\.git'
    # PATTERN = '$\.git'
    # PATTERN = r'$\\.git\\'
    # PATTERN = r'$\.git\\'
    # PATTERN = PATTERN[:-1] #re.error: bad escape (end of pattern) at position 6
    # PATTERN = '/.git/'
    # # F:\BACKUP\BKUP_231115\repos\GitTest\.git\
    # PATTERN = '\\.git\\'
    PATTERN = r'\.git\\\\$'
    PATTERN = r'\.git\\$'
    delete_folder(PATH, PATTERN)