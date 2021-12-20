# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv
# import android_auto_play_opencv as am
# adbpath = '..\\platform-tools\\'
# def main():
#     aapo = am.AapoManager(adbpath)
#     while True:
#         # 画面キャプチャ
#         aapo.screencap()
import import_init

from types import ClassMethodDescriptorType
import common_util.log_util
from common_util.log_util import logger_init
import subprocess
logger = None
import image_checker
import common_util.adb_util as adb_util
import adb_util.adb_common as adb_common

def main():
    logger = logger_init.initialize_logger()
    logger.info('*** ' + __file__)
    # adb_reboot()
    # adb_util.adb_control.logger = logger

    get_image_path = 'screenshot.png'
    # 現在の画像を取得    
    adb_common.screen_capture_for_android(logger,
        get_image_path)
    # 取得した画像を currentDirectory にコピーする
    adb_common.save_file_to_pc_from_android(logger,
        '/sdcard/',get_image_path)
    logger.info('get screenshot. path='+str(get_image_path))


if __name__ == '__main__':
    main()