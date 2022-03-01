
import enum
class const(enum.IntEnum):
    POSITION_BEFORE = 1
    POSITION_AFTER = 2

def add_str_to_file_name_by_list(
    base_file_name:str,
    add_str_list:list,
    delimita:str='_',
    position:int=const.POSITION_AFTER):
    mn = __file__ + '.add_str_to_file_name_by_list : '
    ret = ''
    if len(add_str_list) < 1 :
        raise Exception(mn + 'len(add_str_list) < 1 , return')
        return base_file_name

    for val in add_str_list:
        ret = add_str_to_file_name(base_file_name,val,delimita,position)
    return ret

def add_str_to_file_name(
    base_file_name:str,
    add_str:str,
    delimita:str='_',
    position:int=const.POSITION_AFTER):
    mn = __file__ + '.add_str_to_file_name : '
    if base_file_name == '': 
        return base_file_name
        #raise Exception(mn + 'base_file_name is blank , return')
    
    import os
    # 拡張子
    ext = os.path.splitext(base_file_name)[1]
    # 拡張子なしのファイル名
    basename_without_ext:str = os.path.splitext(os.path.basename(base_file_name))[0]

    if position == const.POSITION_AFTER:
        ret_file_name = basename_without_ext + delimita + add_str + ext
    elif position == const.POSITION_BEFORE:
        ret_file_name = add_str + delimita + basename_without_ext + ext
    else:
        ret_file_name = basename_without_ext + delimita + add_str + ext
    
    return ret_file_name