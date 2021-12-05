
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

