
from logging import exception
from adb_util import adb_common
from adb_util.android_const import const, const_int, const_screen_image_file_names
import adb_util.android_cv2.android_imort_init_cv2
# import common_util
# import common_util.adb_util as adb_util
# from common_util.adb_util.android_const import const as const_main
# from common_util.adb_util.android_const import const_screen_image_file_names as const_images

from adb_util.android_const import const as const_main
from adb_util.android_const import const_screen_image_file_names as const_images
from adb_util.android_const import const_state
import adb_util.adb_common
from adb_util.adb_common import save_file_to_pc_from_android
import adb_util.adb_key as adb_key
from adb_util.adb_key_const import keycoce_const 

class android_control():
    logger = None
    image_dir = None
    adb_util.adb_common.logger = logger

    def __init__(
        self,
        logger,
        image_dir : str
    ) -> None:
        self.logger = logger
        self.image_dir = image_dir
        adb_key.logger = self.logger
        adb_util.adb_common.logger = self.logger

    def initialize(self):
        pass

    def power_on(self)->bool:
        try:
            keycode = keycoce_const.POWER
            result = adb_key.input_keyevent(keycoce_const.POWER)
            return self.__judge_adb_result(
                result,
                'input_keyevent : ' + keycode
            )
        except Exception as e:
            self.logger.exp.error(e)
            return False            

    def reboot(self)->bool:
        try:
            self.logger.info('reboot')
            result = adb_common.adb_reboot()
            return self.__judge_adb_result(
                result,
                'adb_reboot'
            )
        except Exception as e:
            self.logger.exp.error(e)
            return False

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

    def logout_result_adb_shell(self,command):
        try:
            adb_common.logout_adb_shell_result(command)
        except Exception as e:
            self.logger.exp.error(e)

    def get_screenshot(self,save_path):
        try:
            self.logger.info('get_screenshot')
            adb_common.screen_capture_for_android()
            adb_common.save_file_to_pc_from_android(save_path)
        except Exception as e:
            self.logger.exp.error(e)

    def unlock(self,mode):
        """ mode : unlock_control_mode"""
        try:
            self.logger.info('unlock')
            if mode == const_int.CONTROL_SWIPE:
                adb_common.swipe(300,1000,300,200,200)
            else:
                self.logger.exp.error('unlock mode is invalid')
        except Exception as e:
            self.logger.exp.error(e)


    def run_app(self,package_name):
        pass

    def close_app_all(self):
        pass
    
    def transision_to_home(self):
        pass