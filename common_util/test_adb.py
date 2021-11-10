import adb_util
from adb_util import adb_key_const
from adb_util.android_common import android_common_util
from log_util import logger_init
from adb_util.android_const import const_int as android_const_int
from adb_util.android_const import const_screen_image_file_names
from adb_util.android_common import android_constants

def initialize():
    try :
        import os 
        image_path = os.getcwd()
        from pathlib import Path
        image_path = str(Path('__file__').resolve().parent) + \
            'adb_test/android_wiko/screen_wiko'
        logger = logger_init.initialize_logger()
        android = android_common_util(
            logger,
            image_path,
            android_const_int.OPERATION_CV2_IMAGE)
        return logger,android
    except Exception as e:
        logger.exp.error(e)


def main():
    logger , android = initialize()
    try:
        ret = android.state.is_connected_device()
        if not ret: return

        read_path = './screenshot.png'
        temp_path = r'C:\ZMyFolder\newDoc\0ProgramingAll\image_sample\button_login_ok.png'
        temp_path = './image/button_login_ok.png'
        # flag = android.control.tap_image(temp_path,read_path)
        flag = android.control.tap_image(temp_path,'')
        if flag : print('tap success')
        else : print('tap failed')
        return
        ret = android.state.is_off_screen()
        if ret:
            ret = android.control.power_on()
            if not ret:
                android.control.reboot()
                import time
                time.sleep(android_const_int.WAIT_AFTER_REBOOT)
                android.control.power_on()
                # 電源 OFF だと復帰できない
                # error: no devices/emulators found となる
            else:
                android.control.get_screenshot('./image/')
                from adb_util.adb_common import swipe
                swipe(300,1000,300,200,200)
    except Exception as e:
        logger.exp.error(e)

def get_screenshot():
    try:
        logger , android = initialize()
        android.control.get_screenshot('./image/')
        save_path = ''
        import adb_util.adb_common as adb_common
        adb_common.save_file_to_pc_from_android(save_path)
    except Exception as e:
        logger.exp.error(e)

def get_screenrecord():
    try:
        logger , android = initialize()
        import adb_util.adb_common as adb_common
        adb_common.logger = logger
        path = '/sdcard/screenrecord.mp4'
        path = adb_common.screen_record()
        if path:
            adb_common.save_file_from_android(path)
    except Exception as e:
        logger.exp.error(e)

def run_adb_command():
    try:
        logger , android = initialize()
        from adb_util.adb_key_const import const_command
        cmd = const_command.GET_API_LEVEL
        import adb_util.adb_common as adb_common
        adb_common.logger = logger
        # adb_common.logout_adb_shell_result(cmd)  
        # ret = adb_common.get_phone_number()
        ret = adb_common.get_servece_call_iphonesubinfo(21)
        print(ret)
    except Exception as e:
        logger.exp.error(e)

def run_adb_commands():
    try:
        # initialize
        logger , android = initialize()
        import adb_util.adb_common as adb_common
        from adb_util.adb_key_const import const_command
        adb_common.logger = logger
        # getApiLevel
        cmd = const_command.GET_API_LEVEL
        adb_common.logout_adb_shell_result(cmd)
        # make commands iphonesubinfo
        base_cmd = 'adb shell service call iphonesubinfo'
        cmds = []
        for i in range(50):
            cmds.append(base_cmd + ' ' + str(i))
        
        for buf_cmd in cmds:
            adb_common.logout_adb_shell_result(buf_cmd)
    except Exception as e:
        logger.exp.error(e)

if __name__ == '__main__':
    # get_screenshot()
    # get_screenrecord()
    #run_adb_command()
    # run_adb_commands()
    main()
                
