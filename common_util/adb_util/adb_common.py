
from logging import exception
import subprocess

from adb_util.adb_key_const import const_command

# from adb_util import adb_key_const
if __name__ =='__main__':
    print(__name__)
    print(__file__)
    import adb_key_const
else:
    from adb_util import adb_key_const
logger = None


def logout_result_subprocess_run_text(result):
    """subprocess.run の実行結果をログに出力する"""
    try:        
        logger.info('result.stdout = ')
        from subprocess import CompletedProcess
        # returncode から bool に変換する
        if isinstance(result,CompletedProcess):
            # 最後の改行を消す
            if len(result.stdout)>0:
                if result.stdout[-1] == '\n':
                    buf = result.stdout[:-1]
                logger.info(buf)
                logger.info('----------------')
            else:
                pass
            if result.stderr != '':
                logger.info('result.stderr = ')
                logger.info(result.stderr[:-1])
                logger.info('----------------')
            # if result.returncode != 0:
            #     logger.info('result.stderr = ')
            #     logger.info(result.stderr[:-1])
            #     logger.info('----------------')
    except Exception as e:
        logger.exp.error(e)

def get_result_subprocess_run_command(command):
    """subprocess.run でコマンドを実行する(main)"""
    result = None
    try:
        logger.info('get_result_subprocess_run_command')
        # tuple の場合は連結してログを残す
        import general_util.general
        general_util.general.logger = logger
        from general_util.general import cnv_tuple_to_str
        buf = cnv_tuple_to_str(command, ' ')
        logger.info('command = ' + buf)
        # コマンドを実行する
        result = subprocess.run(buf, shell=True, capture_output=True,text=True)
        return result
    except Exception as e:
        logger.exp.error(e)
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
        logger.exp.error(e)
        return result

        
def is_success_adb_result(result,message,is_logout=False)->bool:
    """subprocess.run の実行結果が成功したか判定する"""
    try:
        flag = False
        from subprocess import CompletedProcess
        # returncode から bool に変換する
        if isinstance(result,CompletedProcess):
            if result.returncode != 0: flag = False
            else: flag = True
        else:
            if result != 0: flag = False
            else: flag = True
        # message が無ければコマンドを付加する
        if message == '':
            message = (result.args)
        # 結果をログに出力する
        if is_logout:
            if not flag: logger.info(message + ' : false')
            else: logger.info(message + ' : success')

        return flag
    except Exception as e:
        logger.exp.error(e)
        return False



def screen_capture_for_android(file_name = 'screenshot.png',is_logout_stdout=True)->bool:
    """スクリーンキャプチャをAndroidのSDルートに作成する"""
    try:
        func_name = 'screen_capture_for_android'
        cmd = (
            'adb', 'shell', 'screencap', '-p', 
            '/sdcard/' + file_name)
        result = adb_shell_with_show_result(cmd,is_logout_stdout)
        return is_success_adb_result(result,func_name,is_logout_stdout)            
    except Exception as e:
        logger.exp.error(e)

def screen_record(
    file_name = 'screenrecord.mp4',
    save_dir = '/sdcard/',
    time_limit = 10,
    device_name = '',
    size = '',
    bit_rate = '4000000',
):
    try:
        cmd = 'adb shell ' + str(device_name)
        save_path = save_dir + file_name
        cmd += ' screenrecord'
        cmd += ' --time-limit ' + str(time_limit) 
        cmd += ' ' + save_path
        logout_adb_shell_result(cmd)
        return save_path
    except Exception as e:
        logger.exp.error(e)
        return ''


def save_file_from_android(
    get_path = '',
    save_path = ''
):
    try:
        logger.info('save_file_from_android')            
        command = (
            'adb', 'pull', get_path ,save_path)
        result = adb_shell_with_show_result(command)
        return result
    except Exception as e:
        logger.exp.error(e)
        return None

def save_file_to_pc_from_android(
    save_path = '',
    android_path = '/sdcard/',
    file_name = 'screenshot.png',
    is_logout_stdout= True
):
    """android からファイルを取得する
    """
    result = None
    try:
        func_name ='save_file_to_pc_from_android'
        logger.info(func_name)
        import os
        if not os.path.isfile(save_path):
            if not os.path.isdir(save_path):
                save_path = os.getcwd() + '\\' + file_name
        logger.info('save_path = '+save_path)
        command = (
            'adb', 'pull', android_path + file_name ,save_path)
        result = adb_shell_with_show_result(command)        
        ret = is_success_adb_result(result,func_name,is_logout_stdout)
        if ret:
            logger.info('get file success. path= ' + save_path)
            return True
        else:
            logger.info('get file failed. path= ' + save_path)
            return False
    except Exception as e:
        logger.exp.error(e)
        return False

def adb_reboot():
    """Android デバイスを再起動させる"""
    result = 0
    try: 
        result = subprocess.call('adb reboot')
        return result
    except Exception as e:
        logger.exp.error(e)
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
        logger.exp.error(e)
        return result



def start_package(package,classname):
    try:
        # exists package
        pass
    except Exception as e:
        logger.exp.error(e)

def input_text(value:str):
    result = None
    try:
        cmd = 'adb shell input text "' + value +'"'
        result = adb_shell_with_show_result(cmd)
        return result
    except Exception as e:
        logger.exp.error(e)
        return result

def make_command_adb_shell(device_name):
    default_cmd = 'adb shell '
    try:
        if device_name == '':
            return default_cmd
        else:
            return 'adb -s '+ device_name + ' shell '
    except Exception as e:
        logger.exp.error(e)
        return default_cmd

def get_center_from_rect(point_rect):
    """int か str 型の(left_top,right_top,left_bottom_right_bottom)tuple から
        中央の値を取得する
    """
    try:
        if(len(point_rect) < 4):
            logger.exp.error('argument length < 4')
        elif(len(point_rect) > 4):
            logger.exp.error('argument length > 4')
        elif(len(point_rect) == 4):
            horizon = int(point_rect[2]) - int(point_rect[0])
            horizon = int(horizon/2)
            horizon = int(point_rect[0]) + horizon
            vertical = int(point_rect[3]) - int(point_rect[1])
            vertical = int(vertical/2)
            vertical = int(point_rect[1]) + vertical
            return (horizon,vertical)
        else:
            logger.exp.error('argument length case else -> unexpected case')
            return (0,0)
        return (0,0)
    except Exception as e:
        logger.exp.error(e)
        return (0,0)

def tap_center(point_rect:tuple,device_name:str='',times=1,is_logout_stdout:bool=True) -> bool:
    point = get_center_from_rect(point_rect)
    return touch_screen(point[0],point[1],device_name,is_logout_stdout)

def tap(x:int,y:int,device_name:str='',is_logout_stdout:bool=True) -> bool:
    return touch_screen(x,y,device_name,is_logout_stdout)

def touch_screen(
    x:int,y:int,
    device_name:str='',
    times = 1,
    interval = 10,
    is_logout_stdout:bool=True
) -> bool:
    try:
        cmd = make_command_adb_shell(device_name)
        cmd += 'input touchscreen tap ' + str(x) + ' ' + str(y)
        result = adb_shell_with_show_result(cmd,is_logout_stdout)
        func_name = 'touch_screen'
        ret = is_success_adb_result(result,func_name,is_logout_stdout)
        if is_logout_stdout:
            if ret:
                logger.info('tap success : ' + str(x) + ',' + str(y))
            else:
                logger.info('tap failed : ' + str(x) + ',' + str(y))
        return ret
    except Exception as e:
        logger.exp.error(e)
        return False


def swipe(x1,y1,x2,y2,duration):
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
        logger.exp.error(e)
        return result

def is_connect_android(is_logout_stdout:bool=True) -> bool:
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
        cmd = 'adb devices'
        # result = adb_shell_with_show_result(cmd)
        
        result = adb_shell_with_show_result(cmd,is_logout_stdout)
        ret = is_success_adb_result(result,func_name,is_logout_stdout)
        # if is_logout_stdout:
        #     if ret:
        #         logger.info(func_name + ' success')
        #     else:
        #         logger.info(func_name + ' failed')
        return ret
    except Exception as e:
        logger.exp.error(e)
        return False

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
        logger.exp.error(e)
        return 'get_package_version Error'

def get_device_product_model(is_stdout_to_logout=True,replace_befor = '\n',replace_after =' / '):
    """デバイスのプロダクトモデルを取得する"""
    try:
        #cmd = 'adb shell getprop ro.product.model'
        cmd = adb_key_const.const_command.GET_DEVICE_INFO
        result = adb_shell_with_show_result(cmd)
        #print(result)
        if is_success_adb_result(result,'get_package_version'):
            ret = result.stdout[:-1]
            ret = ret.replace(replace_befor,replace_after)
            return ret
        else:
            return result.stderr[:-1].replace(replace_befor,' / ')
    except Exception as e:
        logger.exp.error(e)
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
        cmd = adb_key_const.const_command.GET_API_LEVEL
        func_name = 'get_servece_call_iphonesubinfo'
        level = get_result_adb_shell(cmd,func_name,is_logout)
        if level.isnumeric():
            if int(level) >= 0:
                cmd = 'adb shell service call iphonesubinfo ' + str(number)
        else:
            logger.exp.error('get_servece_call_iphonesubinfo Failed:get api level Failed')
            logger.exp.error('number = '+ str(number))
            logger.exp.error('command result = '+level)
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
        logger.exp.error(e)
        return ''

        
def start_package(
    package_name : str,
    class_name : str,
    device_name:str='',
    is_logout_stdout:bool=True
) -> bool:
    try:
        func_name = 'start_package'
        cmd = make_command_adb_shell(device_name)
        cmd += const_command.START_PACKAGE
        if class_name != '':
            cmd += '-n ' + package_name + '/' + class_name
        else:
            cmd += package_name
        result = adb_shell_with_show_result(cmd,is_logout_stdout)
        ret = is_success_adb_result(result,func_name,is_logout_stdout)
        return ret
    except Exception as e:
        logger.exp.error(e)
        return False

def get_info_package_list(
    package_name_filter : str = '',
    option : str = '' ,
    device_id : str = '',
    is_logout_stdout : bool = True
)-> str:
    try:
        func_name = 'get_info_package_list'
        cmd = make_command_adb_shell(device_id)
        cmd += const_command.GET_INFO_PACAGE_LIST + package_name_filter
        if option != '':
            cmd += ' ' + option
        result = adb_shell_with_show_result(cmd,is_logout_stdout)
        ret = is_success_adb_result(result,func_name,is_logout_stdout)
        if is_logout_stdout:
            if ret:
                logger.info('command success : ' + package_name_filter)
            else:
                logger.info('command failed : ' + package_name_filter)
        if ret:
            ret_val = result.stdout
        else:
            ret_val = ''
        return ret_val
    except Exception as e:
        logger.exp.error(e)
        return ''
        
def excute_adb_command(
    adb_command : str = '',
    device_id : str = '',
    is_logout_stdout : bool = True
)-> str:
    try:
        func_name = 'excute_adb_command'
        cmd_start = 'adb shell'
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
                logger.info('command success')
            else:
                logger.info('command failed')
        if ret:
            ret_val = result.stdout
        else:
            ret_val = ''
        return ret_val
    except Exception as e:
        logger.exp.error(e)
        return ''
    
def stop_package(
        package_name,
        device_id : str = '',
        is_logout_stdout : bool = True) -> bool:
    try:
        cmd = const_command.STOP_PACKAGE.value + ' ' + package_name
        return excute_adb_command(cmd,device_id,is_logout_stdout)
    except Exception as e:
        logger.exp.error(e)
        return ''

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
        logger.exp.error(e)
        return ''
