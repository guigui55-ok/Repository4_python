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
import common_util
import common_util.cv2_image as cv2_image
import common_util.adb_util.adb_common as adb
import common_util.adb_util.adb_key as adb_key
import android_wiko.wiko_const as android_const
import common_util.adb_util.adb_common as adb_common
import common_util.adb_util as adb_util
import common_util.adb_util.android_common as android_common

def main():
    logger = log_init.initialize_logger_new()
    logger.info('*** ' + __file__)
    screenrecord()
    # test(logger)


def test(logger):
    try:
        if logger == None:
            logger = log_init.initialize_logger_new()
        # ------------------------------
        from android_wiko.android_main_wiko import Wiko

        img_dir = './android_wiko/screen_wiko'
        wiko = Wiko(logger,img_dir)

        import common_util.adb_util.adb_common as adb_common
        flag = adb_common.restart_connecting_adb(logger)
        if not flag: print('return');return
        info = wiko.control.get_connected_adb_devices()
        print(str(info))
        wiko.control.unlock()

        # ------------------------------
        # import os
        # img_dir = './image'
        # file_name = 'background.png'
        # path = os.path.join(img_dir,file_name)
        # android = android_common.AndroidCommon(logger,img_dir)
        # size = adb_common.get_screen_size(logger)
        # print(str(size))
        # from common_util.cv2_image.cv2_method import create_png
        # from common_util.cv2_image.cv2_const import const_color
        # flag = create_png(logger,path,size[0],size[1],const_color.WHITE)

    # ------------------------------
    #     # path をセット
    #     screen_off_image_path = 'image/power_off_screen.png'
    #     get_image_path = 'screenshot.png'

    #     # 現在の画像を取得    
    #     img_path = android_const.image_root_dir + '\\' + \
    #         android_const.const_screen_image_file_names.POWER_OFF
    #     adb.screen_capture_for_android(logger,img_path)
    #     # 取得した画像を currentDirectory にコピーする
    #     adb.save_file_to_pc_from_android(
    #         logger,
    #         '/sdcard/',android_const.const.SCREEN_CAPTURE_FILE_NAME)

    #     # HOME へ
    #     # POWER OFF か
    #     from common_util.cv2_image import cv2_image_comp
    #     is_same = cv2_image_comp.is_same_image(
    #         logger,screen_off_image_path,get_image_path
    #     )
    #     if is_same:
    #         #power_off
    #         adb_key.input_keyevent('KEYCODE_POWER')
    # except Exception as e:
    #     logger.exp.error(e)
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
    except:
        import traceback
        traceback.print_exc()


from android_wiko.android_main_wiko import Wiko
def screenrecord():    
    try:
        wiko = initialize()
        wiko.info.device_info.device_id = 'RF8R3202XMW'
        format = 'raw-frames' # NG
        format = '' # OK
        format = 'mp4' # OK
        format = '3gpp' # NG Unknown format '3gpp'
        format = 'frames' # NG
        format = 'h264' # NG Unknown format 'h264-'
        format = '' # OK
        size = '360x720'
        time_limit = 3
        ret = wiko.control.get_screenrecord(
            '',
            'screenrecord.mp4',
            wiko.constants.main.SD_ROOT_DIR.value,
            time_limit,
            size,
            80000000,
            format)
        print('ret='+str(ret))
    except:
        import traceback
        traceback.print_exc()


def screenshot():
    try:
        wiko = initialize()
        wiko.info.device_info.device_id = 'RF8R3202XMW'
        wiko.control.get_screenshot()
    except:
        import traceback
        traceback.print_exc()

def push_files():
    try:
        wiko = initialize()
        import pathlib,os
        path = os.path.join(str(pathlib.Path(__file__).parent),'push_files')
        path_obj = pathlib.Path(path)
        save_path = '/sdcard/Pictures'
        for file in path_obj.glob('*'):
            wiko.control.control_adb.push_file(str(file),save_path)
    except:
        import traceback
        traceback.print_exc()

def initialize():
    try:
        logger = log_init.initialize_logger_new()
        img_dir = './android_wiko/screen_wiko'
        wiko = Wiko(logger,img_dir)
        return wiko
    except:
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    pass
    # screenshot()
    screenrecord()
    # push_files()
    # main()