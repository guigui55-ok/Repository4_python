# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv
# import android_auto_play_opencv as am
# adbpath = '..\\platform-tools\\'
# def main():
#     aapo = am.AapoManager(adbpath)
#     while True:
#         # 画面キャプチャ
#         aapo.screencap()

from types import ClassMethodDescriptorType
import logger_init
import subprocess
logger = None
import image_checker
import adb_util.adb_control

def main():
    logger = logger_init.initialize_logger()
    logger.info('*** ' + __file__)
    # adb_reboot()
    adb_util.adb_control.logger = logger

    # path をセット
    screen_off_image_path = 'image/power_off_screen.png'
    get_image_path = 'screenshot.png'
    # 現在の画像を取得    
    adb_util.adb_control.screen_capture_for_android(
        get_image_path)
    # 取得した画像を currentDirectory にコピーする
    adb_util.adb_control.save_file_to_pc_from_android(
        '/sdcard/',get_image_path)
    # 画像を比較する
    is_same = image_checker.is_same_image(
        logger,screen_off_image_path,get_image_path
    )
    if is_same:
        #power_off
        adb_util.adb_control.input_keyevent('KEYCODE_POWER')





if __name__ == '__main__':
    main()