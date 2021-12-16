from sre_constants import FAILURE
import traceback
import import_init
import common_util.log_util.logger_init as logger_init
import common_util.log_util.logging_util as logging_util
import common_util.adb_util.adb_common as adb_common

def create_file_name_if_exists(logger,file_name:str,num:int=0,dir:str='.'):
    """
    not recommended
    """
    try:
        path = dir + '/' + file_name
        import os
        if os.path.exists(path):
            ext = os.path.splitext(path)[1]
            name = os.path.splitext(os.path.basename(path))[0]
            num += 1
            path_new = name + '_' + str(num) + ext
            # 再帰的に実行する
            ret = create_file_name_if_exists(logger,path_new,num,dir)
            return ret
        else:
            return file_name
    except Exception as e:
        logger.exp.error(e)
        return file_name

def count_up_file_name(file_name:str,delimita='_'):
    """
    not recommended
    """
    import os
    # 拡張子
    ext = os.path.splitext(file_name)[1]
    # 拡張子なしのファイル名
    basename_without_ext = os.path.splitext(os.path.basename(file_name))[0]
    # get digit
    pos = basename_without_ext.rfind(delimita)
    if pos > 0:
        digit = len(basename_without_ext) - pos + 1
    else:
        # digit = 0
        ret_file_name = basename_without_ext + delimita + str(1) + ext
        return ret_file_name
    # get number
    n_str = basename_without_ext[pos+1:]
    num:int = int(n_str)+1
    ret_num_str = ''
    if len(str(num)) < digit:
        for i in range(digit):
            ret_num_str += '0'
    ret_num_str += str(num)
    # create file name
    ret_file_name = basename_without_ext[:pos+1] + ret_num_str + ext
    return ret_file_name

def get_count_up_number_str(num_str:str):
    """
    count_up_if_last_name_is_number sub method
    """
    # get number
    n_str = num_str # 数字
    digit = len(num_str) # 桁数
    # 1加えておく、999→1000の繰り上がりに対処するため
    num:int = int(n_str)+1
    # 桁数以下ならゼロを加える 00056 : 57=>00057
    ret_num_str = ''
    if len(str(num)) < digit:
        for i in range(digit-len(str(num))):
            ret_num_str += '0'
    ret_num_str += str(num)
    return ret_num_str
    
def is_number(value:str):
    try:
        n = int(value)
        return True
    except:
        return False

def count_up_if_last_name_is_number(file_name,delimita='_'):
    try:
        import os
        if os.path.exists(file_name):
            new_name = count_up_if_last_name_is_number_main(
                file_name,delimita)
            if os.path.exists(new_name):
                    new_name = count_up_if_last_name_is_number(
                        new_name,delimita)
            
            return new_name
        else:
            return file_name
    except:
        traceback.print_exc()
def count_up_if_last_name_is_number_main(file_name,delimita='_'):
    """
    ファイル名が file_name_003.ext の時、file_name_004.ext にする
    ex) file_name_9.ext > file_name_10.ext
    拡張子がない場合はエラー
    * recommended
    """
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
    ret_num = get_count_up_number_str(after_delimita_str)
    ret_file_name = basename_without_ext[:pos+1] + ret_num + ext
    return ret_file_name

def create_next_file_name_when_last_is_number(logger,file_name,delimita='_'):
    """
    not recommended
    ファイル名が file_name_003の時、file_name_004 にする
    """
    try:
        import re
        count = 0
        is_number = [False,False]
        is_last_number = False
        # 逆順に取り出す
        for char in reversed(file_name):
            if re.match('[0-9]',char):
                if count == 0:
                    is_number[1] = True
                else:
                    is_number[0] = is_number[1]
                    is_number[1] = True
            else:
                if count == 0:
                    # is_last_number = False
                    break
                else:
                    is_number[0] = is_number[1]
                    is_number[1] = False
            if ((is_number[0])and(not is_number[1])) and \
                (char == delimita):
                # _123 の場合
                is_last_number = True
            count += 1
        return is_last_number
    except Exception as e:
        logger.exp.error(e)
        return False

def adb_getevent(logger):
    try:
        # ファイル名をセットする
        file_name_base = 'getevent.txt'
        file_name = count_up_if_last_name_is_number(file_name_base)
        print('file_name:')
        print(file_name_base)
        #   
        cmd = 'getevent'
        cmd = 'getevent /dev/input/event0 | ruby record.rb > touch.txt'
        # 'ruby' は、内部コマンドまたは外部コマンド、操作可能なプログラムまたはバッチ ファイルとして認識されていません。
        cmd = 'getevent /dev/input/event0 > touch.txt'
        device_id = '2889adb7'
        # flag , ret_str = adb_common.excute_command_adb_shell(cmd,device_id)
        cmd = 'getevent /dev/input/event0 > touch.txt'
        # https://qiita.com/techno-tanoC/items/b93723618a792c7096ee
        # プロンプト（手動）で adb shell -> getevent 実行後、デバイスを操作して、デバイス番号をメモしておく
        # その後以下を実行して操作する
        cmd = 'adb shell getevent /dev/input/event2 > ' + file_name
        cmd = 'adb shell getevent /dev/input/event2'
        cmd = 'adb shell getevent -tl /dev/input/event2 > ' + file_name
        flag , ret_str = adb_common.excute_command(logger,cmd)
        print(ret_str)
        print('./' + file_name)
        return flag
    except:
        import traceback
        print(traceback.print_exc())
        return False

def adb_getevent_poppen(logger):
    try:
        # ファイル名をセットする
        file_name_base = 'getevent.txt'
        file_name = create_file_name_if_exists(logger,file_name_base)
        #   
        cmd = 'getevent'
        cmd = 'getevent /dev/input/event0 | ruby record.rb > touch.txt'
        # 'ruby' は、内部コマンドまたは外部コマンド、操作可能なプログラムまたはバッチ ファイルとして認識されていません。
        cmd = 'getevent /dev/input/event0 > touch.txt'
        device_id = '2889adb7'
        # flag , ret_str = adb_common.excute_command_adb_shell(cmd,device_id)
        cmd = 'getevent /dev/input/event0 > touch.txt'
        # https://qiita.com/techno-tanoC/items/b93723618a792c7096ee
        # プロンプト（手動）で adb shell -> getevent 実行後、デバイスを操作して、デバイス番号をメモしておく
        # その後以下を実行して操作する
        cmd = 'adb shell getevent /dev/input/event2 > ' + file_name
        cmd = 'adb shell getevent -tl /dev/input/event2 > ' + file_name
        # cmd = 'adb shell getevent /dev/input/event2'
        flag , ret_str = adb_common.excute_command(logger,cmd)
        print(ret_str)
        print('./' + file_name)
        return flag
    except:
        import traceback
        print(traceback.print_exc())
        return False

def sendevent(logger):
    try:
        import os,pathlib
        file_name = 'getevent_3.txt'
        path = os.path.join(str(pathlib.Path(__file__).parent),file_name)
        print('** path = ' + path)
        device_type = '/dev/input/event2'
        flag = adb_common.sendevent_from_file(logger,path,device_type,'',True)
        return flag
    except:
        import traceback
        print(traceback.print_exc())
        return False

def main():
    try:
        logger:logging_util = logger_init.initialize_logger()
        adb_getevent(logger)
        #sendevent(logger)
        return
    except:
        import traceback
        print(traceback.print_exc())
        return

main()

