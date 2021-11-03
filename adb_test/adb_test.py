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
import log_init

import subprocess
logger = None
import image_checker
import adb_utility.adb_control

import common as com
import common_util.cv2_image as cv2_image
import common_util.adb_util.adb_common as adb
import common_util.adb_util.adb_key as adb_key
import android_wiko.wiko_const as android_const

def main():
    logger = log_init.initialize_logger_new()
    logger.info('*** ' + __file__)


def init_android():
    try:
        adb.logger =logger
        # path をセット
        screen_off_image_path = 'image/power_off_screen.png'
        get_image_path = 'screenshot.png'

        # 現在の画像を取得    
        img_path = android_const.image_root_dir + '\\' + \
            android_const.const_screen_image_file_names.POWER_OFF
        adb.screen_capture_for_android(img_path)
        # 取得した画像を currentDirectory にコピーする
        adb.save_file_to_pc_from_android('/sdcard/',android_const.const.SCREEN_CAPTURE_FILE_NAME)

        # HOME へ
        # POWER OFF か
        from cv2_image import cv2_image_comp
        is_same = cv2_image_comp.is_same_image(
            logger,screen_off_image_path,get_image_path
        )
        if is_same:
            #power_off
            adb_key.input_keyevent('KEYCODE_POWER')
    except Exception as e:
        logger.exp.error(e)
    # ------------------------------
    # adb_reboot()
    # adb_utility.adb_control.logger = logger
    # 現在の画像を取得    
    # adb_utility.adb_control.screen_capture_for_android(
    #     get_image_path)
    # 取得した画像を currentDirectory にコピーする
    # adb_utility.adb_control.save_file_to_pc_from_android(
    #     '/sdcard/',get_image_path)
    # 画像を比較する
    # is_same = image_checker.cv2_image_comp.is_same_image(
    #     logger,screen_off_image_path,get_image_path
    # )
    # if is_same:
    #     #power_off
    #     adb_utility.adb_control.input_keyevent('KEYCODE_POWER')

# 現在の状態を取得





if __name__ == '__main__':
    main()