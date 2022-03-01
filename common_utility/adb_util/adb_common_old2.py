

from common_utility.global_var import debug_mode
if debug_mode:
    print('    ' + __file__)

try:
    # common_utilityをsys.pathに追加済み
    from common_utility.log_util.logging_util import LoggerUtility
except:
    import traceback
    traceback.print_exc()

import subprocess
# from logging import exception
from typing import Any


if __name__ == '__main__' or __name__ == 'adb_common':
    import adb_key_const
    from adb_key_const import ConstCommand
    from adb_key_const import ConstKeycode
    import sys
    from pathlib import Path
    target_dir = str(Path(__file__).parent) # parent
    target_dir = str(Path(target_dir).parent) # parent_parent == common_util
    sys.path.append(target_dir)
    from log_util.logging_util import LoggerUtility
else:
    # 外部から参照時は、common_util を sys.path へ追加しておくこと
    from common_util.adb_util.adb_key_const import ConstCommand
    from common_util.adb_util.adb_key_const import ConstKeycode
    import common_util.general_util.general as general
    from common_util.log_util.logging_util import logger_info
    from common_util.adb_util import adb_key_const

logger:LoggerUtility = None

def set_logger_in_adb_common(arg_logger:LoggerUtility):
    logger = arg_logger

def log_info(value:str):
    if logger != None:
        log_info(value)
    else:
        print(value)

def logout_result_subprocess_run_text(result):
    """subprocess.run の実行結果をログに出力する"""
    try:        
        log_info('result.stdout = ')
        from subprocess import CompletedProcess
        # returncode から bool に変換する
        if isinstance(result,CompletedProcess):
            # 最後の改行を消す
            if len(result.stdout)>0:
                if result.stdout[-1] == '\n':
                    buf = result.stdout[:-1]
                log_info(buf)
                log_info('----------------')
            else:
                pass
            if result.stderr != '':
                log_info('result.stderr = ')
                log_info(result.stderr[:-1])
                log_info('----------------')
            # if result.returncode != 0:
            #     log_info('result.stderr = ')
            #     log_info(result.stderr[:-1])
            #     log_info('----------------')
    except Exception as e:
        logger.error(e)

def get_result_subprocess_run_command(command):
    """subprocess.run でコマンドを実行する(main)"""
    result = None
    try:
        log_info('get_result_subprocess_run_command')
        # tuple の場合は連結してログを残す
        general.logger = logger
        buf = general.cnv_tuple_to_str(command, ' ')
        log_info('command = ' + buf)
        # コマンドを実行する
        result = subprocess.run(buf, shell=True, capture_output=True,text=True)
        return result
    except Exception as e:
        logger.error(e)
        return result

def adb_shell_with_show_result(command,is_logout_stdout=True):
    """subprocess.run でコマンドを実行する
        is_logout_stdout(bool):標準出力stdout(stderr)をログに出力する
        get_result_adb_shell:recommended
    """
    result = None
    try:
        result = get_result_subprocess_run_command(command)
        if is_logout_stdout:
            logout_result_subprocess_run_text(result)
        return result
    except Exception as e:
        logger.error(e)
        return result

        
def is_success_adb_result(result,message,is_logout=False)->bool:
    """subprocess.run の実行結果が成功したか判定する"""
    try:
        flag = False
        from subprocess import CompletedProcess
        # returncode から bool に変換する
        if isinstance(result,CompletedProcess):
            if result.returncode != 0:
                flag = False
            else:
                flag = True
        else:
            if result != 0: flag = False
            else: flag = True
        # message が無ければコマンドを付加する
        if message == '':
            message = (result.args)
        # 結果をログに出力する
        if is_logout:
            if not flag: ret_msg =  ' : false'
            else: ret_msg =  ' : success'
            log_info(message + ret_msg)

        return flag
    except Exception as e:
        logger.error(e)
        return False



def screen_capture_for_android(
    file_name = 'screenshot.png',
    save_dir = '/sdcard/',
    device_id='',
    is_logout_stdout=True)->str:
    """スクリーンキャプチャをAndroidのSDルートに作成する"""
    try:
        # cmd = ('adb', 'shell', 'screencap', '-p', '/sdcard/' + file_name)
        save_path = save_dir + file_name
        cmd = 'screencap -p ' + save_path
        flag , result = excute_command_adb_shell(cmd,device_id,is_logout_stdout)
        return save_path     
    except Exception as e:
        logger.error(e)
        return ''

def screen_record(
    file_name = 'screenrecord.mp4',
    save_dir = '/sdcard/',
    time_limit = 10,
    device_id = '',
    size = '',
    bit_rate = '4000000',
    is_logout_stdout=True)->str:
    try:
        if device_id != '' : device_id + ' '
        cmd = 'adb shell ' + device_id
        save_path = save_dir + file_name
        cmd += ' screenrecord'
        cmd += ' --time-limit ' + str(time_limit) 
        cmd += ' ' + save_path
        flag , ret = excute_command(cmd,is_logout_stdout)
        return save_path
    except Exception as e:
        logger.error(e)
        return ''


def save_file_from_android(
    get_path = '',
    save_path = '',
    device_id = '',    
    is_logout_stdout=True)->bool:
    try:
        log_info('save_file_from_android')
        cmd = 'pull ' + get_path + ' ' + save_path
        flag , ret = excute_command_adb(cmd,is_logout_stdout)
        return flag
    except Exception as e:
        logger.error(e)
        return False

def save_file_to_pc_from_android(
    save_path = '',
    android_path = '/sdcard/',
    file_name = 'screenshot.png',
    device_id = '',
    is_logout_stdout= True
)->bool:
    """android からファイルを取得する
    """
    try:
        func_name ='save_file_to_pc_from_android'
        import os
        if not os.path.isfile(save_path):
            if not os.path.isdir(save_path):
                save_path = os.getcwd() + '\\' + file_name
        log_info('save_path = '+save_path)
        cmd = 'pull ' + android_path + file_name + ' ' + save_path
        flag ,result = excute_command_adb(cmd,device_id, is_logout_stdout)
        return flag
    except Exception as e:
        logger.error(e)
        return False

def adb_reboot():
    """Android デバイスを再起動させる"""
    result = 0
    try: 
        result = subprocess.call('adb reboot')
        return result
    except Exception as e:
        logger.error(e)
        return result

def logout_adb_shell_result(command)->str:
    """get_result_adb_shell を is_logout=True にしたもの"""
    is_logout = True
    func_name = 'logout_adb_shell_result'
    result = get_result_adb_shell(command,func_name,is_logout)
    return result



def get_result_adb_shell_by_poppen(commnd):
    result = None
    try:
        logger.error('Not Implemented')
        return result
    except Exception as e:
        logger.error(e)
        return result



def start_package(package,classname):
    try:
        # exists package
        pass
    except Exception as e:
        logger.error(e)

def input_text(value:str):
    result = None
    try:
        cmd = 'adb shell input text "' + value +'"'
        result = adb_shell_with_show_result(cmd)
        return result
    except Exception as e:
        logger.error(e)
        return result

def make_command_adb(device_name):
    default_cmd = 'adb '
    try:
        if device_name == '':
            return default_cmd
        else:
            return 'adb -s '+ device_name + ' '
    except Exception as e:
        logger.error(e)
        return default_cmd

def make_command_adb_shell(device_id):
    default_cmd = 'adb shell '
    try:
        if device_id == '':
            return default_cmd
        else:
            return 'adb -s '+ device_id + ' shell '
    except Exception as e:
        logger.error(e)
        return default_cmd

def get_center_from_rect(point_rect):
    """int か str 型の(left_top,right_top,left_bottom_right_bottom)tuple から
        中央の値を取得する
    """
    try:
        if(len(point_rect) < 4):
            logger.error('argument length < 4')
        elif(len(point_rect) > 4):
            logger.error('argument length > 4')
        elif(len(point_rect) == 4):
            horizon = int(point_rect[2]) - int(point_rect[0])
            horizon = int(horizon/2)
            horizon = int(point_rect[0]) + horizon
            vertical = int(point_rect[3]) - int(point_rect[1])
            vertical = int(vertical/2)
            vertical = int(point_rect[1]) + vertical
            return (horizon,vertical)
        else:
            logger.error('argument length case else -> unexpected case')
            return (0,0)
        return (0,0)
    except Exception as e:
        logger.error(e)
        return (0,0)

def tap_center(point_rect:tuple,device_id:str='',times=1,interval=3,is_logout_stdout:bool=True) -> bool:
    point = get_center_from_rect(point_rect)
    return touch_screen(point[0],point[1],device_id,is_logout_stdout)

def tap(x:int,y:int,device_id:str='',is_logout_stdout:bool=True) -> bool:
    return touch_screen(x,y,device_id,is_logout_stdout)

def touch_screen(
    x:int,y:int,
    device_id:str='',
    times = 1,
    interval = 10,
    is_logout_stdout:bool=True
) -> bool:
    try:
        if times > 1: logger.error('touch_screen multiple time : Unimplemented')
        cmd = make_command_adb_shell(device_id)
        cmd += 'input touchscreen tap ' + str(x) + ' ' + str(y)
        result = adb_shell_with_show_result(cmd,is_logout_stdout)
        func_name = 'touch_screen'
        ret = is_success_adb_result(result,func_name,is_logout_stdout)
        if is_logout_stdout:
            if ret:
                log_info('tap success : ' + str(x) + ',' + str(y))
            else:
                log_info('tap failed : ' + str(x) + ',' + str(y))
        return ret
    except Exception as e:
        logger.error(e)
        return False

def swipe(x1,y1,x2,y2,duration,device_id='',is_logout_stdout=True)->bool:
    """スワイプする"""
    try:
        cmd = 'input swipe ' \
            + str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2) + ' ' + str(duration)
        flag ,result = excute_command_adb_shell(cmd,device_id,is_logout_stdout)
        return flag
    except Exception as e:
        logger.error(e)
        return False

def swipe_(x1,y1,x2,y2,duration):
    """スワイプする"""
    result = None
    try:
        # coordinate = (x1,y1,x2,y2,duration)
        # cmd = 'adb shell input swipe'
        # cmd = (cmd,x1,y1,x2,y2,duration)
        cmd = 'adb shell input swipe ' \
            + str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2) + ' ' + str(duration)
        print(cmd)
        result = adb_shell_with_show_result(cmd)
        return result
    except Exception as e:
        logger.error(e)
        return result

def is_connect_android(device_id = '' ,is_logout_stdout:bool=True) -> bool:
    try:
        dev_list = get_connect_adb_devices(is_logout_stdout)
        if len(dev_list) < 0:
            logger.error('get_connect_adb_devices : len(dev_list) < 0 , False')
            return False
        # デバイス指定なしでつながっている場合は
        if device_id == '':
            return True
        else:
            # dev_list = ['device_id','status']
            # statsus = device / offline
            for i in range(len(dev_list)):
                if device_id == dev_list[i][0]:
                    return True
        return False
    except Exception as e:
        logger.error(e)
        return False

def get_connect_adb_devices(is_logout_stdout:bool=True) -> list([str,str]):
    """
    Android が USB 接続しているか
    """
    # 出力
    # List of devices attached
    # 2889adb7        offline
    # List of devices attached
    # 2889adb7        device
    try:
        func_name = 'is_connect_android'
        cmd = 'devices'
        # result = adb_shell_with_show_result(cmd)        
        flag ,ret = excute_command_adb(cmd,'',is_logout_stdout)
        buf:str = str(ret)
        results = buf.split('\n')
        ret_id_list:list(str) = []
        # i=1 から実行する
        for i in range(len(results))[1:]:
            buf = results[i]
            if len(buf)>0:
                # device_id\tdevice
                info = buf.split('\t')
                if info[1] == 'device':
                    ret_id = info[0]
                    ret_status = info[1]
                    ret_id_list.append([ret_id,ret_status])                    
            
        return ret_id_list
    except Exception as e:
        logger.error(e)
        return []

def get_android_version():
    """Androidのバージョンを取得する"""
    cmd = 'adb shell getprop ro.build.version.release'
    return adb_shell_with_show_result(cmd,'get_android_version')

def get_android_build_version(is_logout_stdout=True):
    """Androidソフトウェア情報のビルドバージョンを取得する"""
    cmd = 'adb shell getprop ro.build.display.id'
    return get_result_adb_shell(cmd,'get_android_version',is_logout_stdout)

def get_result_adb_shell(cmd,func_name='',is_logout_stdout=True) -> str:
    """adb shell コマンドを実行して結果を得る"""
    result = adb_shell_with_show_result(cmd,is_logout_stdout)
    return cnv_completed_process_to_str(result,func_name,is_logout_stdout)

def cnv_complete_process(self,result,func_name='',is_logout_stdout=True,ret_type=1):
    try:
        # 結果をboolで取得する
        ret_bool = is_success_adb_result(result,func_name,is_logout_stdout,ret_type=1)
        # ログに出力する
        if is_logout_stdout:
            if ret_bool:
                self.log_info('command success')
            else:
                self.log_info('command failed')
        # 引数によって戻り値の型を変更する
        # 1:bool,2:str
        if ret_type == 1:
            return ret_bool
        elif ret_type == 2:
            ret_str = cnv_completed_process_to_str(result,func_name,is_logout_stdout)
            return ret_str
        else:
            self.logger.error('cnv_complete_process : ret_type is invalid. return None')
            return None
    except Exception as e:
        self.logger.error(e)
        # 引数によって戻り値の型を変更する
        if ret_type == 1:
            return False
        elif ret_type == 2:
            return ''
        else:
            self.logger.error('cnv_complete_process : ret_type is invalid. return None')
            return None

def cnv_completed_process_to_str(
    result:subprocess.CompletedProcess,
    func_name:str,
    is_logout_stdout:bool)->str:
    """CommandPrompt(Terminal)で得られた結果を文字列へ変換する"""
    try:
        if is_success_adb_result(result,func_name,is_logout_stdout):
            if (len(result.stdout) > 0):
                # 最後の1文字は改行コードなので除外する
                return result.stdout[:-1]
            else:
                return ''
        else:
            if (len(result.stderr) > 0):
                # 最後の1文字は改行コードなので除外する
                return result.stderr[:-1]
            else:
                return ''
    except Exception as e:
        logger.error(e)
        return ''

def get_package_version(package_name):
    """デバイス内のパッケージのバージョンを取得する"""
    try:
        cmd = 'adb shell dumpsys package ' + package_name
        result = adb_shell_with_show_result(cmd)
        if is_success_adb_result(result,'get_package_version'):
            buf_ret:str = str(result.stdout)
            check_str = 'versionName='
            pos_start = buf_ret.find(check_str)
            if pos_start < 0:
                return 'get_package_version Failed(pos_start<0)'
            pos_end = buf_ret.find('\n',pos_start)
            if pos_end < 0:
                return 'get_package_version Failed(pos_end<0)'
            ret_ver = buf_ret[pos_start + len(check_str):pos_end]
            return ret_ver
        else:
            logger.error('get_package_version Failed')
            buf_ret = result.stderr
            buf_ret = buf_ret.replace('\n',' / ')
            buf_ret = 'get_package_version Failed / ' + buf_ret
            return buf_ret
    except Exception as e:
        logger.error(e)
        return 'get_package_version Error'

def get_device_product_model(is_stdout_to_logout=True,replace_befor = '\n',replace_after =' / '):
    """デバイスのプロダクトモデルを取得する"""
    try:
        #cmd = 'adb shell getprop ro.product.model'
        cmd = ConstCommand.GET_DEVICE_INFO
        result = adb_shell_with_show_result(cmd)
        #print(result)
        if is_success_adb_result(result,'get_package_version'):
            ret = result.stdout[:-1]
            ret = ret.replace(replace_befor,replace_after)
            return ret
        else:
            return result.stderr[:-1].replace(replace_befor,' / ')
    except Exception as e:
        logger.error(e)
        return 'get_device_product_model Error'

def get_emei(is_logout=True):
    """adb Shell dumpsys iphonesubinfo 13 の実行結果を取得する
        デバイスの SIM Phone Number を取得する
    """
    return get_servece_call_iphonesubinfo(1,is_logout)

def get_phone_number(is_logout=True):
    """adb Shell dumpsys iphonesubinfo 13 の実行結果を取得する
        デバイスの IMEI を取得する
    """
    return get_servece_call_iphonesubinfo(13,is_logout)
    # 13,14,17,18


def get_servece_call_iphonesubinfo(number,is_logout=True):
    """adb Shell dumpsys iphonesubinfo [Number] の実行結果を取得する"""
    try:
        cmd = ConstCommand.GET_API_LEVEL
        func_name = 'get_servece_call_iphonesubinfo'
        level = get_result_adb_shell(cmd,func_name,is_logout)
        if level.isnumeric():
            if int(level) >= 0:
                cmd = 'adb shell service call iphonesubinfo ' + str(number)
        else:
            logger.error('get_servece_call_iphonesubinfo Failed:get api level Failed')
            logger.error('number = '+ str(number))
            logger.error('command result = '+level)
            return ''
        cmd_ret:str = get_result_adb_shell(cmd,func_name,is_logout)
        lines = cmd_ret.split('\n')
        ret = ''
        if len(lines) > 0:
            for line in lines:
                left = line.find('\'')
                if left < 0: continue
                right = line.rfind('\'')
                val = line[left+1:right]
                val = val.replace('.','')
                ret += val
        return ret
    except Exception as e:
        logger.error(e)
        return ''

        
def start_package(
    package_name : str,
    class_name : str,
    device_id:str='',
    is_logout_stdout:bool=True
) -> bool:
    try:
        func_name = 'start_package'
        cmd = ConstCommand.START_PACKAGE
        if class_name != '':
            cmd += '-n ' + package_name + '/' + class_name
        else:
            cmd += package_name
        flag,result = excute_command_adb_shell(cmd,device_id,is_logout_stdout)
        return flag
    except Exception as e:
        logger.error(e)
        return False

def get_info_package_list(
    package_name_filter : str = '',
    option : str = '' ,
    device_id : str = '',
    is_logout_stdout : bool = True
)-> str:
    try:
        func_name = 'get_info_package_list'
        cmd = ConstCommand.GET_INFO_PACAGE_LIST + package_name_filter
        if option != '':
            cmd += ' ' + option
        flag,ret = excute_command_adb_shell(cmd,device_id,is_logout_stdout)
        # result = adb_shell_with_show_result(cmd,is_logout_stdout)
        # ret = is_success_adb_result(result,func_name,is_logout_stdout)
        # if is_logout_stdout:
        #     if ret:
        #         log_info('command success : ' + package_name_filter)
        #     else:
        #         log_info('command failed : ' + package_name_filter)
        # if ret:
        #     ret_val = result.stdout
        # else:
        #     ret_val = ''
        return ret
    except Exception as e:
        logger.error(e)
        return ''

def excute_command(
    command : str = '',
    is_logout_stdout : bool = True
)-> Any:
    """コマンドを実行し、結果を取得する
    戻り値は(bool,str)が返る"""
    try:
        func_name = 'excute_command'
        cmd = command
        result = adb_shell_with_show_result(cmd,is_logout_stdout)
        ret_bool = is_success_adb_result(result,func_name,is_logout_stdout)
        if is_logout_stdout:
            if ret_bool:
                log_info('command success')
            else:
                log_info('command failed')
        if ret_bool:
            ret_val = result.stdout
        else:
            ret_val = ''
        return ret_bool,ret_val
    except Exception as e:
        logger.error(e)
        return False,''

def excute_command_adb_shell(
    command : str = '',
    device_id : str = '',
    is_logout_stdout : bool = True)->Any:
    """adb shell コマンドを実行し、結果を取得する
    戻り値は(bool,str)が返る"""
    try:
        cmd = make_command_adb_shell(device_id)
        cmd += command
        return excute_command(cmd,is_logout_stdout)
    except Exception as e:
        logger.error(e)

def excute_command_adb(
    command : str = '',
    device_id : str = '',
    is_logout_stdout : bool = True)->Any:
    """adb コマンドを実行し、結果を取得する
    戻り値は(bool,str)が返る"""
    try:
        cmd = make_command_adb(device_id)
        cmd += command
        return excute_command(cmd,is_logout_stdout)
    except Exception as e:
        logger.error(e)
    

def excute_adb_command(
    adb_command : str = '',
    device_id : str = '',
    is_logout_stdout : bool = True,
    is_not_adb_shell = False
)-> Any:
    """adbコマンドを実行し、結果を取得する
    戻り値は(bool,str)が返る"""
    try:
        func_name = 'excute_adb_command'
        if not is_not_adb_shell:
            cmd_start = 'adb shell'
        else:
            cmd_start = ''
        pos = adb_command.find(cmd_start)
        if pos == 1:
            cmd_shell_after = adb_command[len(cmd_start):]
        else:
            cmd_shell_after = adb_command
        cmd = make_command_adb_shell(device_id)
        cmd += cmd_shell_after
        result = adb_shell_with_show_result(cmd,is_logout_stdout)
        ret = is_success_adb_result(result,func_name,is_logout_stdout)
        if is_logout_stdout:
            if ret:
                log_info('command success')
            else:
                log_info('command failed')
        if ret:
            ret_val = result.stdout
        else:
            ret_val = ''
        return ret,ret_val
    except Exception as e:
        logger.error(e)
        return ''
    
def stop_package(
        package_name,
        device_id : str = '',
        is_logout_stdout : bool = True) -> bool:
    try:
        cmd = ConstCommand.STOP_PACKAGE + ' ' + package_name
        flag ,ret = excute_adb_command(cmd,device_id,is_logout_stdout)
        return flag
    except Exception as e:
        logger.error(e)
        return False

def reboot_package(
        package_name,
        class_name,
        wait_time=0,
        device_id : str = '',
        is_logout_stdout : bool = True) -> bool:
    try:
        result = stop_package(package_name,device_id,is_logout_stdout)
        import time
        time.sleep(wait_time)
        result = start_package(package_name,class_name,device_id,is_logout_stdout)
        return result
    except Exception as e:
        logger.error(e)
        return False

def input_keyevent(keycode,device_id='',is_logout_stdout : bool = True) -> bool:
    try:
        cmd = 'input keyevent ' + keycode
        flag ,ret = excute_adb_command(cmd,device_id,is_logout_stdout)
        return flag
    except Exception as e:
        logger.error(e)
        return False

