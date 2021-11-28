


if __name__ == '__main__':
    from android_const import Constants
    from device_info import DeviceInfo
    from android_main_control import AndroidControlMain
    from android_main_state import AndroidState
    from android_main_info import AndroidInfo

    import android_cv2_control as control_cv2
    import android_cv2_state as state_cv2
else:
    # 外部から参照時は、common_util,adb_util を sys.path へ追加しておく
    from adb_util.android_const import Constants
    from adb_util.device_info import DeviceInfo
    from adb_util.android_main_control import AndroidControlMain
    from adb_util.android_main_state import AndroidState
    from adb_util.android_main_info import AndroidInfo

    import adb_util.android_cv2_control as control_cv2
    import adb_util.android_cv2_state as state_cv2
from enum import Enum
from os import device_encoding

from adb_util import adb_common

# class android_constants():
#     int_val : android_const_int = android_const_int
#     str_val : android_const_str = android_const_str
#     images : const_images = const_images
#     state : android_const_state = android_const_state
#     key : keycoce_const = keycoce_const




class AndroidCommon():
    # logger object member
    logger = None
    # const object member
    constants : Constants = Constants
    # sub object member 
    control : AndroidControlMain = None
    state : AndroidState = None
    info : AndroidInfo = None
    device_info : DeviceInfo
    mode = None
    # init
    def __init__(
        self,
        logger,
        image_dir,
        mode = Constants.main.OPERATION_CV2_IMAGE
    ) -> None:
        try:
            self.logger = logger
            self.constants = Constants
            self.mode = mode
            self.device_info = DeviceInfo()
            self.control = AndroidControlMain(logger,self.device_info,image_dir)
            self.state = AndroidState(logger,self.control.control_adb,image_dir)
            self.info = AndroidInfo(logger,self.control.control_adb,image_dir)
            self.logger.info('mode = '+ self.constants.main.OPERATION_CV2_IMAGE.name)
        except Exception as e:
            self.logger.exp.error(e)

    def transition_to_home(self):
        self.control.control_adb.input_keyevent(Constants.key.HOME)

    def transition_to_home_from_any_screen(self):
        try:
            # デバイスが応答状態か判定する
            # 電源 OFF か判定する
            # Screen_off か判定する
            ret = self.control.power_on()
            if not ret:
                self.control.reboot()
                import time
                time.sleep(self.constants.main.WAIT_AFTER_REBOOT.value)
                self.control.power_on()
                # 電源 OFF だと復帰できない
                # error: no devices/emulators found となる
            else:
                self.control.unlock()
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

    