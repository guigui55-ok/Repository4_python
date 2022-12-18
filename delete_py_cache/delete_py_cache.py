import enum
import os

class ConstDebug(enum.Enum):
    TRACE = 1
    DEBUG = 2
    INFO = 3

debug_mode:int = ConstDebug.TRACE.value

def get_file_path_list(path:str,ext:str='/*'):
    import glob
    value = path + ext
    file_list = glob.glob(value)
    if False:
        print()
        print('----------')
        for file in file_list:
            print('  ' + file)
    return file_list

def get_file_paths_list_all_up_to_bottom_dir(path_list:'list[str]',ext:str):
    """最下層ディレクトリまですべてのリストを取得する"""
    sub_list = []
    for path in path_list:
        if os.path.isdir(path):
            temp_list = get_file_path_list(path,ext)
            temp_list = get_file_paths_list_all_up_to_bottom_dir(temp_list,ext)
            sub_list.extend(temp_list)
    path_list.extend(sub_list)
    return path_list

def change_setrecursionlimit():
    import sys
    import threading

    #変更前の再帰関数の実行回数の上限を表示
    print(sys.getrecursionlimit())

    sys.setrecursionlimit(67108864) #64MB
    threading.stack_size(1024*1024)  #2の20乗のstackを確保=メモリの確保

    #変更後の再帰関数の実行回数の上限を表示
    print(sys.getrecursionlimit())

def delete_py_chache_core(path_list:'list[str]'):
    import os
    import shutil
    count = 0
    rm_count = 0
    dir_name = '__pycache__'
    for path in path_list:
        count += 1
        if not os.path.isdir(path):
            continue
        buf = path[-len(dir_name):]
        if buf == dir_name:
            shutil.rmtree(path)
            rm_count += 1

    print('proc count = {}'.format(count))
    print('rm_count = {}'.format(rm_count))


def main():
    print()
    print('*****')
    #####
    base_dir = r'C:\Users\OK\source\repos\Repository4_python'
    ext = '/*'
    path_list = get_file_path_list(base_dir,ext)
    # print(len(path_list))
    path_list = get_file_paths_list_all_up_to_bottom_dir(path_list,ext)
    print('file_list_count = {}'.format( len(path_list) ))
    delete_py_chache_core(path_list)
    #####
    print(f'base_dir = {base_dir}')

    return

if __name__ == '__main__':
    main()
