
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
from cv2_image.cv2_find_image_util import is_match_template_from_file2 

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

    def tap_image(self,parts_path,screenshot_path='') -> bool:
        try:
            self.logger.info('tap_image')
            if screenshot_path == '':
                # ./screenshot.png
                base_path = const.SAVE_PATH_ROOT_DIR.value + const.SCREEN_CAPTURE_FILE_NAME.value
            else:
                base_path = screenshot_path

            from adb_util.adb_common import save_file_to_pc_from_android
            # 現在の状態を screenshot として保存、PC へ移動
            save_file_to_pc_from_android(
                base_path,
                const.SD_ROOT_DIR.value,
                const.SCREEN_CAPTURE_FILE_NAME.value,
            )
            #image_path = self.image_dir + '\\' + const_images.POWER_OFF.value
            image_path = parts_path
            result_dir_path = './'
            # base_path に対して
            # image と合致するか判定する
            from cv2_image.cv2_find_image_util import is_match_template_from_file2
            match_rect = is_match_template_from_file2(
                self.logger,
                base_path,
                image_path,
                0.8,
                result_dir_path
            )
            print('is_match =' + str(match_rect['result']))
            # print(match_rect['start_w'],match_rect['start_h'])
            # print(match_rect['end_w'],match_rect['end_h'])

            tap_rect = match_rect['start_w'],match_rect['start_h'],\
                match_rect['end_w'],match_rect['end_h']
            from adb_util.adb_common import tap_center
            is_taped = tap_center(tap_rect)
            return is_taped
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def run_app(self,package_name):
        pass

    def close_app_all(self):
        pass
    
    def transision_to_home(self):
        pass