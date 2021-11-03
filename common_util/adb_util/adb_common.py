
import subprocess
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

def logout_adb_shell_result(command):
    logger.info('command = ' + command)
    result = get_result_adb_shell(command)
    logout_result_subprocess_run_text(result)


def get_result_adb_shell(command):
    result = None
    try:
        logger.info('get_result_adb_shell')
        import general_util.general
        general_util.general.logger = logger
        from general_util.general import cnv_tuple_to_str
        buf = cnv_tuple_to_str(command, ' ')
        logger.info('command = ' + buf)
        result = subprocess.run(command, shell=True, capture_output=True,text=True)
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

def adb_shell_with_show_result(command):
    result = None
    try:
        result = get_result_adb_shell(command)
        logout_result_subprocess_run_text(result)
        return result
    except Exception as e:
        logger.exp.error(e)
        return result


def logout_result_subprocess_run_text(result):
    try:        
        logger.info('result.stdout = ')
        logger.info(result.stdout)
        logger.info('----------------\nresult.stderr = ')
        logger.info(result.stderr)
    except Exception as e:
        logger.exp.error(e)

def input_text(value:str):
    result = None
    try:
        cmd = 'adb shell input text "' + value +'"'
        result = get_result_adb_shell(cmd)
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
        result = get_result_adb_shell(cmd)
        return result
    except Exception as e:
        logger.exp.error(e)
        return result

def is_connect_android():
    try:
        cmd = 'adb devices'
        print(cmd)
        # result = get_result_adb_shell(cmd)
        result = adb_shell_with_show_result(cmd)
        return result
    except Exception as e:
        logger.exp.error(e)
        
def is_success_adb_result(result,message)->bool:
    try:
        flag = False
        from subprocess import CompletedProcess
        if isinstance(result,CompletedProcess):
            if result.returncode != 0: flag = False
            else: flag = True
        else:
            if result != 0: flag = False
            else: flag = True

        if not flag: logger.info(message + ' false')
        else: logger.info(message + ' success')

        return flag
    except Exception as e:
        logger.exp.error(e)
        return False