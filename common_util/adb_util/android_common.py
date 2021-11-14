
from adb_util.android_main_control import android_control as control
from adb_util.android_main_state import android_state as state
from adb_util.android_const import const_int as android_const_int
from adb_util.android_const import const as android_const_str
from adb_util.android_const import const_screen_image_file_names as const_images
from adb_util.adb_key_const import keycoce_const
from adb_util.android_const import const_state as android_const_state

import adb_util.android_cv2_control as control_cv2
import adb_util.android_cv2_state as state_cv2
import adb_util.android_main_info as android_main_info
from enum import Enum

class android_constants():
    int_val : android_const_int = android_const_int
    str_val : android_const_str = android_const_str
    images : const_images = const_images
    state : android_const_state = android_const_state
    key : keycoce_const = keycoce_const

class android_common_util():
    # logger object member
    logger = None
    # const object member
    constants : android_constants = None
    const_str : android_const_str= None
    const_images : const_images = None
    const_int : android_const_int = None
    # sub object member 
    control : control_cv2.android_control = None
    state : state_cv2.android_state = None
    info : android_main_info.android_info = None
    mode = None
    # init
    def __init__(
        self,
        logger,
        image_dir,
        mode = android_const_int.OPERATION_CV2_IMAGE
    ) -> None:
        self.logger = logger
        self.constants = android_constants
        self.const_str = android_const_str
        self.const_images = const_images
        self.const_int = android_const_int
        self.mode = mode
        if mode == self.const_int.OPERATION_CV2_IMAGE:
            self.control = control_cv2.android_control(
                logger,
                image_dir
            )
            self.state = state_cv2.android_state(
                logger,
                image_dir
            )
            self.logger.info('mode = '+ self.const_int.OPERATION_CV2_IMAGE.name)
        else:
            self.logger.warning('mode is unknown -> class object is None')
        self.info = android_main_info.android_info(self.logger)

    def transision_to_home_from_any_screen(self):
        try:
            # デバイスが応答状態か判定する
            # 電源 OFF か判定する
            # Screen_off か判定する
            ret = control.power_on()
            if not ret:
                control.reboot()
                import time
                time.sleep(self.const_int.WAIT_AFTER_REBOOT)
                control.power_on()
                # 電源 OFF だと復帰できない
                # error: no devices/emulators found となる
            else:
                control.unlock()
                # unlock する
                # home になる 
            # HOME ボタンを押下する
        except Exception as e:
            self.logger.exp.error(e)

    def __judge_adb_result(self,result,message)->bool:
        try:
            if result != 0:            
                # エラー時の処理
                self.logger.info(message + ' false')
                return False
            # success
            self.logger.info(message + ' success')
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def is_connect_device(self):
        try:
            from adb_common import is_connect_android
            result= is_connect_android()
            flag = self.__judge_adb_result('is_connect_device')
            return flag
        except Exception as e:
            self.logger.exp(e)
            return False

    