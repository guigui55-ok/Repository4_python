
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
            # print('cnv_tuple_to_str : value type is not tuple')
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
    """ datetime.now().strftime('%y%m%d_%H%M%S') γθΏγ
    """
    import datetime
    return datetime.datetime.now().strftime('%y%m%d_%H%M%S')


def get_path_info(path):
    try:
        # https://note.nkmk.me/python-os-basename-dirname-split-splitext/
        import os
        # ζ‘εΌ΅ε­γγγ?γγ‘γ€γ«ε
        basename = os.path.basename(path)
        # ζ‘εΌ΅ε­γͺγγ?γγ‘γ€γ«ε
        basename_without_ext = os.path.splitext(os.path.basename(path))[0]
        # γγ©γ«γεοΌγγ£γ¬γ―γγͺεοΌ
        dirname = os.path.dirname(path)
        # γγ‘γ€γ«ε, γγ©γ«γε
        dirname = os.path.split(path)[0]
        filename = os.path.split(path)[0]
        # β»ζ³¨ζ
        # ζ«ε°Ύγ«εΊεγζε­γγγε ΄εγ
        # './dir/subdir/' => ('./dir/subdir', '')
        # ζ‘εΌ΅ε­γεεΎ
        root_ext_pair = os.path.splitext(path)
        # γγ‘γ€γ«εγ¨γγ©γ«γεγη΅εγγ¦γγΉζε­εγδ½ζ
        path = os.path.join('dir', 'subdir', 'filename.ext')
        # εγγγ©γ«γγ?ε₯γ?γγ‘γ€γ«γ?γγΉζε­εγδ½ζ
        other_filepath = os.path.join(os.path.dirname(path), 'other_file.ext')

        # θ¦ͺγγ£γ¬γ―γγͺγεεΎγγ
        from pathlib import Path
        parent_dir = str(Path(path).parent)
        parent_dir = os.path.abspath(os.path.join(path, os.pardir))
        parent_dir = os.path.abspath(os.path.join(path, '..')) # Windows 

        return 
    except:
        import traceback
        print(traceback.print_exc())

