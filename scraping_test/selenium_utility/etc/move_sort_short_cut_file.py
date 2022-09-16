


from os import mkdir


NEW_LINE = '\n'




def make_file_list_from_dir(dir:str):
    """対象ディレクトリのlnkリストを作成する"""
    import glob,os
    glob_path = os.path.join(dir,'*')
    buf_list = glob.glob(glob_path)
    lnk_list = exact_lnk_path_from_list(buf_list)
    return lnk_list

def exact_lnk_path_from_list(buf_list:'list[str]'):
    import os
    ret = []
    for path in buf_list:
        if os.path.isfile(path):
            if os.path.splitext(path)[1] == '.url':
                ret.append(path)
    return ret

def get_url_from_link(lnk_path:str):
    """lnkからURLを取得する"""
    with open(lnk_path, 'r',encoding='utf-8')as f:
        buf = f.read()
    buf = buf.replace(NEW_LINE,'')
    buf = buf.replace('[InternetShortcut]URL=','')
    return buf

def mkdir_if_not_exists(dir_path:str):
    import os
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    else:
        if os.path.isfile(dir_path):
            os.remove(dir_path)
            os.mkdir(dir_path)
    return dir_path


def main():
    import os
    import pathlib
    import shutil

    dir_path = r'C:\Users\OK\Desktop\0703 you ero'
    move_dir_path_obj = pathlib.Path(dir_path).joinpath('you')
    mkdir_if_not_exists(str(move_dir_path_obj))
    path_list = make_file_list_from_dir(dir_path)
    lnk_list = exact_lnk_path_from_list(path_list)
    for lnk_path in lnk_list:
        url = get_url_from_link(lnk_path)
        if url.startswith('https://www.youtube.com/watch'):
            src = lnk_path
            f_name = os.path.basename(src)
            dist = str(move_dir_path_obj.joinpath(f_name))
            shutil.move(src,dist)

if __name__ == '__main__':
    main()