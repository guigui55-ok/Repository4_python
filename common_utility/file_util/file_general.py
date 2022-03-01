
import os

def get_file_list(dir_path:str,include_file_name:str = ''):
    ret_list = list(range(0))
    if os.path.isdir(dir_path):
        condition = ''
        if include_file_name != '':
            condition = '\\*' + condition + '*'
        import glob
        files = glob.glob(dir_path + condition)
        for file in files:
            ret_list.append(file)
    else:
        raise Exception('path is not directory. path=' + dir_path)
    return ret_list

def create_dir_if_nothing(dir : str)->str:
    if os.path.exists(dir) and os.path.isdir(dir):
        return dir
    else:
        os.mkdir(dir)
        raise Exception('create_dir_if_nothing : mkdir , dir = ' + dir)
    return dir

def read_line_file(file_path):
    lines = []
    with open(file_path) as f:
        lines = f.readlines()
    return lines

def cnv_resolve_path(path:str):
    import pathlib
    ret = pathlib.Path(path).resolve
    return ret