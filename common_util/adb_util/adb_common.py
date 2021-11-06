
import subprocess

# from adb_util import adb_key_const
if __name__ =='__main__':
    print(__name__)
    print(__file__)
    import adb_key_const
else:
    from adb_util import adb_key_const
logger = None

def screen_capture_for_android(file_name = 'screenshot.png'):
    """スクリーンキャプチャをAndroidのSDルートに作成する"""
    try:
        command = (
            'adb', 'shell', 'screencap', '-p', 
            '/sdcard/' + file_name)
        adb_shell_with_show_result(command)
        #subprocess.call(command)
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
        cmd = 'adb shell' + device_name
        save_path =save_dir + file_name
        cmd += ' screenrecord'
        cmd += ' --time-limit ' + str(time_limit) 
        cmd += ' ' + save_path
        logout_adb_shell_result(cmd)
        return save_path
    except Exception as e:
        logger.exp.error(e)
        return None


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
    file_name = 'screenshot.png'
):
    """android からファイルを取得する
    """
    result = None
    try:
        logger.info('save_file_to_pc_from_android')
        import os
        if not os.path.isfile(save_path):
            if not os.path.isdir(save_path):
                save_path = os.getcwd() + '\\' + file_name
        logger.info('save_path ='+save_path)
        command = (
            'adb', 'pull', android_path + file_name ,save_path)
        result = adb_shell_with_show_result(command)
        return result
    except Exception as e:
        logger.exp.error(e)
        return result

def adb_reboot():
    """再起動させる"""
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

def get_result_adb_shell_by_poppen(commnd):
    result = None
    try:
        logger.error('Not Implemented')
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

def swipe(x1,y1,x2,y2,duration):
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

def is_connect_android():
    try:
        cmd = 'adb devices'
        result = adb_shell_with_show_result(cmd)
        return result
    except Exception as e:
        logger.exp.error(e)
        
def is_success_adb_result(result,message,is_logout=False)->bool:
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

def get_android_version():
    cmd = 'adb shell getprop ro.build.version.release'
    return adb_shell_with_show_result(cmd,'get_android_version')

def get_android_build_version(is_logout_stdout=True):
    cmd = 'adb shell getprop ro.build.display.id'
    return get_result_adb_shell(cmd,'get_android_version',is_logout_stdout)


def get_result_adb_shell(cmd,func_name='',is_logout_stdout=True) -> str:
    """adb shell コマンドを実行して結果を得る"""
    result = adb_shell_with_show_result(cmd,is_logout_stdout)
    if is_success_adb_result(result,func_name,is_logout_stdout):
        if (len(result.stdout) > 0):
            return result.stdout[:-1]
        else:
            return ''
    else:
        if (len(result.stderr) > 0):
            return result.stderr[:-1]
        else:
            return ''

def get_package_version(package_name):
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
    return get_servece_call_iphonesubinfo(1,is_logout)

def get_phone_number(is_logout=True):
    return get_servece_call_iphonesubinfo(13,is_logout)
    # 13,14,17,18
    

def get_servece_call_iphonesubinfo(number,is_logout=True):
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
        return 'error'