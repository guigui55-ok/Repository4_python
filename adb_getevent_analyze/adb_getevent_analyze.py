import import_init
import common_util.log_util.logger_init as logger_init
import common_util.log_util.logging_util as logging_util
import common_util.adb_util.adb_common as adb_common

def create_file_name_if_exists(logger,file_name:str,num:int=0,dir:str='.'):
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

def adb_getevent(logger):
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
        # プロンプトで adb shell -> getevent 実行後、デバイスを操作して、デバイス番号をメモしておく
        # その後以下を実行して操作する
        cmd = 'adb shell getevent /dev/input/event2 > ' + file_name
        cmd = 'adb shell getevent /dev/input/event2'
        flag , ret_str = adb_common.excute_command(cmd)
        print(ret_str)
        print('./' + file_name)
        return flag
    except:
        import traceback
        print(traceback.print_exc())
        return False


def main():
    try:
        logger:logging_util = logger_init.initialize_logger()
        adb_common.logger = logger
        adb_getevent(logger)
        return
    except:
        import traceback
        print(traceback.print_exc())
        return

main()

