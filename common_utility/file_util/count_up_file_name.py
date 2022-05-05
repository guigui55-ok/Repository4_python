# def count_up_file_name(file_name:str,delimita='_'):
#     import os
#     # 拡張子
#     ext = os.path.splitext(file_name)[1]
#     # 拡張子なしのファイル名
#     basename_without_ext = os.path.splitext(os.path.basename(file_name))[0]
#     # get digit
#     pos = basename_without_ext.rfind(delimita)
#     if pos > 0:
#         digit = len(basename_without_ext) - pos + 1
#     else:
#         # digit = 0
#         ret_file_name = basename_without_ext + delimita + str(1) + ext
#         return ret_file_name
#     # get number
#     n_str = basename_without_ext[pos+1:]
#     num:int = int(n_str)+1
#     if len(str(num)) < digit:
#         ret_num_str = ''
#         for i in range(digit):
#             ret_num_str += '0'
#         ret_num_str += str(num)
#     # create file name
#     ret_file_name = basename_without_ext[:pos+1] + ret_num_str + ext
#     return ret_file_name

import enum
from logging.config import fileConfig


def get_count_up_number_str_keep_digit(num_str:str):
    """
    数字のみの文字列をカウントアップする、桁数を維持したまま
    ex)
    3 => 4
    9 => 10
    0012 => 0013
    0099 => 0100
    0000 -> 0001
    """
    # get number
    n_str = num_str # 数字
    digit = len(num_str) # 桁数
    # 1加えておく、999→1000の繰り上がりに対処するため
    num:int = int(n_str)+1
    # 桁数以下ならゼロを加える 00056 : 57=>00057
    if len(str(num)) < digit:
        ret_num_str = ''
        for i in range(digit-len(str(num))):
            ret_num_str += '0'
        ret_num_str += str(num)
    else:
        ret_num_str:str = str(num)
    return ret_num_str
    
def is_number(value:str):
    try:
        n = int(value)
        return True
    except:
        return False

class FileControlMode(enum.Enum):
    EXISTS_RENAME = 1
    EXISTS_OVERWRITE = 2
    EXISTS_CANCEL = 3
    COPY = 11
    MOVE = 12
    DELETE = 13


import shutil

def debug_print(value):
    print(str(value))

def copy_file(
    src_dir:str,
    src_file_name:str,
    dist_dir:str,
    dist_file_name:str='',
    write_mode:int=FileControlMode.EXISTS_RENAME,
    delimita='_'):
    control_file(
        src_dir,src_file_name,dist_dir,dist_file_name,
        FileControlMode.COPY,write_mode,delimita
    )

def move_file(
    src_path:str,
    dist_path:str,
    write_mode:int=FileControlMode.EXISTS_RENAME,
    delimita='_'):
    import os
    src_dir = os.path.dirname(src_path)
    src_file_name = os.path.basename(src_path)
    if os.path.isdir(dist_path):
        dist_dir = dist_path
        dist_file_name = src_file_name
    else:
        dist_dir = os.path.dirname(dist_path)
        dist_file_name = os.path.basename(dist_path)
    return control_file(
        src_dir,src_file_name,dist_dir,dist_file_name,
        FileControlMode.MOVE,write_mode,delimita
    )

def move_file_(
    src_dir:str,
    src_file_name:str,
    dist_dir:str,
    dist_file_name:str='',
    write_mode:int=FileControlMode.EXISTS_RENAME,
    delimita='_'):
    return control_file(
        src_dir,src_file_name,dist_dir,dist_file_name,
        FileControlMode.MOVE,write_mode,delimita
    )

def control_file(
    src_dir:str,
    src_file_name:str,
    dist_dir:str,
    dist_file_name:str='',
    control_mode:int=FileControlMode,
    write_mode:int=FileControlMode.EXISTS_RENAME,
    delimita='_'):
    """ファイルをコピー・移動時、コピー先に同名があるときに、ファイル名に番を打を付与、カウントアップする
     shutil で実行時既に存在するときエラーとなる時に使用する。
    """
    import os
    if dist_file_name == '': dist_file_name = src_file_name

    dist_path = os.path.join(dist_dir,dist_file_name)
    src_path = os.path.join(src_dir,src_file_name)
    # if dist_path == src_path:
    #     msg = 'dist_path == src_path , path = ' + src_path
    #     debug_print(msg)
    #     return True
    if not os.path.exists(src_path):
        return src_path

    if os.path.exists(dist_path):
        if write_mode == FileControlMode.EXISTS_CANCEL:
            msg = 'dist_path is exists >> cancel , path = ' + dist_path
            debug_print(msg)
            return dist_path
    
        elif write_mode == FileControlMode.EXISTS_OVERWRITE:
            pass
            #delete
            os.remove(dist_path)
        elif write_mode == FileControlMode.EXISTS_RENAME:
            pass
            #no action
        else:
            pass
            raise Exception('wrive_mode is invalid')

    new_file_path = create_dist_file_path(dist_dir,src_file_name)
    if control_mode == FileControlMode.COPY:
        shutil.copy(src_path,new_file_path)
        return new_file_path
    elif control_mode == FileControlMode.MOVE:
        #rename or move
        shutil.move(src_path, new_file_path)
        return new_file_path
    else:
        raise Exception('control_mode is Invalid')


def create_dist_file_path(dist_dir:str,dist_file_name:str,delimita='_'):
    """ファイルをコピー・移動時、コピー先に同名があるときに、ファイル名に番を打を付与、カウントアップする
     shutil で実行時既に存在するときエラーとなる時に使用する。
    """
    import os
    path = os.path.join(dist_dir,dist_file_name)
    ret_file_name:str = count_up_if_last_name_is_number(path,delimita)
    ret_path:str = os.path.join(dist_dir,ret_file_name)
    return ret_path

def count_up_if_last_name_is_number(file_path:str,delimita='_'):
    """
    ファイル名の末尾が 「_数値」 かつ、すでに存在する場合、末尾の数値部をカウントアップする
    ファイル名が file_name_003.ext の時、file_name_004.ext にする
    ex) file_name_9.ext > file_name_10.ext
    拡張子がない場合はおそらくエラー
    同名がある場合はさらにカウントアップする
    * recommended
    戻り値：
    成功時はファイル名を返す
    　　ファイル名が存在しない場合はそのまま file_name を返す
    失敗時は空文字''を返す
    """
    try:
        new_name:str=''
        import os
        if os.path.exists(file_path):
            new_name = count_up_if_last_name_is_number_main(
                file_path,delimita)
            dir_name = os.path.dirname(file_path)
            new_path = os.path.join(dir_name,new_name)
            if os.path.exists(new_path):
                # リネーム後さらに存在する場合、再帰的に実行する
                new_name = count_up_if_last_name_is_number(
                    new_path,delimita)
            ret_path = os.path.join(dir_name,new_name)
            return ret_path
        else:
            return file_path
    except:
        import traceback
        traceback.print_exc()
        return ''

def count_up_if_last_name_is_number_main(file_name,delimita='_'):
    """
    ファイル名が file_name_003.ext の時、file_name_004.ext にする
    ex) file_name_9.ext > file_name_10.ext
    file_name.ext > file_name_1.ext
    拡張子がない場合はエラー
    """
    ret_file_name:str = ''
    import os
    # 拡張子
    ext = os.path.splitext(file_name)[1]
    # 拡張子なしのファイル名
    basename_without_ext:str = os.path.splitext(os.path.basename(file_name))[0]
    # find
    pos = basename_without_ext.rfind(delimita)
    if pos < 0:
        # 最後が _1 形式ではないときは、数字を付加して終了
        ret_file_name = basename_without_ext + delimita + '1' + ext
        return ret_file_name
    # pos >= 0
    after_delimita_str = basename_without_ext[pos+1:]
    if not is_number(after_delimita_str):
        # 最後が _1 形式ではないときは、数字を付加して終了
        ret_file_name = basename_without_ext + delimita + '1' + ext
        return ret_file_name
    ret_num = get_count_up_number_str_keep_digit(after_delimita_str)
    ret_file_name = basename_without_ext[:pos+1] + ret_num + ext
    return ret_file_name

