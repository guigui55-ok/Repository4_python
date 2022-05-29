
import os
import glob

def get_file_path_list(path:str,ext:str='/*'):
    """pathのファイルリストを取得する"""
    value = path + ext
    if not os.path.isdir(path):
        return [path]
    file_list = glob.glob(value)
    if False:
        print()
        print('----------')
        for file in file_list:
            print('  ' + file)
    return file_list

def get_file_path_list_all_up_to_bottom_dir(path_list:'list[str]',ext:str='/*'):
    """最下層ディレクトリまですべてのリストを取得する"""
    sub_list = []
    for path in path_list:
        if os.path.isdir(path):
            temp_list = get_file_path_list(path,ext)
            temp_list = get_file_path_list_all_up_to_bottom_dir(temp_list,ext)
            sub_list.extend(temp_list)
    path_list.extend(sub_list)
    return path_list

def get_list_endswith(list:'list[str]',with_str:str):
    """リストの中で後方一致したもののみのリストを取得する"""
    ret_list = [x for x in list if x.endswith(with_str)]
    return ret_list


def test():
    import pathlib
    path = str(pathlib.Path(__file__).parent.parent)
    print(path)
    opt = '/*'
    path_list = get_file_path_list(path,opt)
    print(len(path_list))
    path_list_all = get_file_path_list_all_up_to_bottom_dir(path_list,opt)
    print(len(path_list_all))
    
    py_list = [x for x in path_list_all if x.endswith('.py')]
    print(len(py_list))
    return

if __name__ == '__main__':
    test()