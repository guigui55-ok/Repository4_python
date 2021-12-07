
logger = None

def cnv_tuple_to_str(value,delimita=',') -> str:
    try:
        if isinstance(value, tuple):
            ret = ''
            for buf in value:
                ret += str(buf) + delimita
            if len(ret) > len(delimita):
                ret = ret[:len(ret)-len(delimita)]
            return ret
        else:
            # logger.info('cnv_tuple_to_str : value type is not tuple')
            print('cnv_tuple_to_str : value type is not tuple')
            return value
    except Exception as e:
        logger.exp.error(e)
        return ''

def cnv_int(value) -> int:
    try:
        if not isinstance(value, str):
            return 0
        else:
            if value.isnumeric():
                return int(value)
            else:
                return 0
    except Exception as e:
        logger.exp.error(e)
        return 0

import sys
from types import FunctionType, MethodType
def get_method_name_now_process() -> str:
    try:        
        ret = sys._getframe().f_code.co_name
        return ret
    except Exception as e:
        logger.exp.error(e)
        return ''

def print_now_method(function_):
    #print(get_method_name_now_process())
    try:
        if str(type(function_)) == "<class 'function'>":
            print(function_.__name__)
        #elif type(function_) is function: #error name 'function' is not defined
        #elif isinstance(function_, function): #error NameError: name 'function' is not defined
            #print(function(function_).__name__)
        else:
            print(function_.__name__)
            print(str(type(function_)))
            # print(str(type(function_)))
    except:
        # import traceback
        # print(traceback.print_exc())
        print(str(type(function_)))

def get_datetime():
    import datetime
    datetime.datetime.now().strftime('%y%m_%H%M%S')

def get_path_info(path):
    try:
        # https://note.nkmk.me/python-os-basename-dirname-split-splitext/
        import os
        # 拡張子ありのファイル名
        basename = os.path.basename(path)
        # 拡張子なしのファイル名
        basename_without_ext = os.path.splitext(os.path.basename(path))[0]
        # フォルダ名（ディレクトリ名）
        dirname = os.path.dirname(path)
        # ファイル名, フォルダ名
        dirname = os.path.split(path)[0]
        filename = os.path.split(path)[0]
        # ※注意
        # 末尾に区切り文字がある場合。
        # './dir/subdir/' => ('./dir/subdir', '')
        # 拡張子を取得
        root_ext_pair = os.path.splitext(path)
        # ファイル名とフォルダ名を結合してパス文字列を作成
        path = os.path.join('dir', 'subdir', 'filename.ext')
        # 同じフォルダの別のファイルのパス文字列を作成
        other_filepath = os.path.join(os.path.dirname(path), 'other_file.ext')

        # 親ディレクトリを取得する
        from pathlib import Path
        parent_dir = str(Path(path).parent)
        parent_dir = os.path.abspath(os.path.join(path, os.pardir))
        parent_dir = os.path.abspath(os.path.join(path, '..')) # Windows 

        return 
    except:
        import traceback
        print(traceback.print_exc())