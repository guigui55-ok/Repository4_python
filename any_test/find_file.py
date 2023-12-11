

from pathlib import Path
from typing import Union
import glob
import re

def find_file(
        root_dir,
        pattern:Union[str, list[str]],
        recurcive=False):
    """ root_dir の中の pettern と合致するパスをすべて取得する """
    root_dir = Path(root_dir)
    if not root_dir.exists():
        raise FileNotFoundError(root_dir)
    if not isinstance(pattern, list):
        patterns = [pattern]
    else:
        patterns = pattern
    paths = []
    for i, pat in enumerate(patterns):
        if i==0:
            if recurcive:
                target = str(root_dir.joinpath('**',pat))
            else:
                target = str(root_dir.joinpath(pat))
            paths = glob.glob(target, recursive=recurcive)
        else:
            paths = get_path_list_match_value(paths, pat)
    return paths

def get_path_list_match_value(path_list:list[str], pattern):
    """ patternに合致するものすべてを取得する """
    ret = []
    for path in path_list:
        value = Path(path).name
        mat = re.search(pattern, value)
        if mat!=None:
            ret.append(path)
    return ret

def get_path_list_include_content(
        path_list:list[str],
        patterns:Union[str, list[str]]):
    """ ファイル内容にpatternsをすべて含むもののパスを取得する """
    if not isinstance(patterns, list):
        patterns = [patterns]
    else:
        patterns = patterns
    ret = []
    for path in path_list:
        with open(str(path), 'r', encoding='utf-8')as f:
            buf = f.read()
        if is_match_all(buf, patterns):
            ret.append(path)
    return ret

def is_match_all(buf:str, pattens):
    for patten in pattens:
        mat = re.search(patten, buf)
        if mat==None:
            return False
    return True


if __name__ == '__main__':
    print()
    print('*****')
    # pyファイルでbeautiflを含むものをすべて取得する
    file_name_patterns = ['*.py']
    text_patterns = ['beautiful']
    root_dir = Path(__file__).parent.parent
    print('dir = {}'.format(root_dir))
    paths = find_file(root_dir, file_name_patterns, True)
    paths = get_path_list_include_content(paths, text_patterns)
    for path in paths:
        print(path)