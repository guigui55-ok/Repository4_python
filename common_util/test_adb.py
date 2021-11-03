import adb_util
from adb_util.android_common import android_common_util
from log_util import logger_init
from adb_util.android_const import const_int as android_const_int
from adb_util.android_const import const_screen_image_file_names
from adb_util.android_common import android_constants



def main():
    import os 
    image_path = os.getcwd()
    from pathlib import Path
    image_path = str(Path('__file__').resolve().parent) + \
        'adb_test/android_wiko/screen_wiko'
    logger = logger_init.initialize_logger()
    android = android_common_util(
        logger,
        image_path,
        android_const_int.OPERATION_CV2_IMAGE
    )
    try:
        ret = android.state.is_connected_device()
        if not ret: return

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

            # cmd = 'adb shell pm list packages'        
            # android.control.logout_result_adb_shell(cmd)
            else:
                android.control.get_screenshot('./image/')
                from adb_util.adb_common import swipe
                swipe(300,1000,300,200,200)
    except Exception as e:
        logger.exp.error(e)

if __name__ == '__main__':
    main()