from cv2 import isContourConvex
from numpy import False_
from adb_util.android_cv2 import android_imort_init_cv2
from adb_util import adb_common
from adb_util import android_common

from enum import Enum

class const(Enum):
    PACKAGE_NAME = 'jp.gungho.pad'
    START_ACTIVITY = '.AppDelegate'

class const_images(Enum):
    BUTTON_OK_SMALL = 'button_ok_small.png'
    BUTTON_OK_LOGIN = 'button_login_ok.png'
    CHANGE_DATE = 'pad01_change_date_dialog.png'
    ERROR_GOOGLE_PLAY = 'pad01_2_error1_google_play_parts.png'
    MENU_ICON_DUNGEON = 'pad20_menu_icon_dungeon.png'
    START_BUTTON_OPENING = 'pad_opening_start_logo.png'

class pad_player():
    # Member
    logger = None
    image_dir : str = ''
    android : android_common.AndroidCommon = None
    def __init__(
        self,
        logger_,
        image_dir_:str,
        android_:android_common.AndroidCommon
    ) -> None:
        self.image_dir = image_dir_
        self.logger = logger_
        self.android = android_

    def start_package(self) -> bool:
        try:
            return self.android.control.start_package(
                const.PACKAGE_NAME.value, const.START_ACTIVITY.value)
            
            # #pacakge_name = 'package:jp.gungho.pad'#NG
            # pacakge_name = 'jp.gungho.pad'
            # # class_name = '.AppDelegate,android.intent.action.MAIN'#NG
            # class_name = '.AppDelegate'
            # # class_name = '.android.intent.action.MAIN'#NG
        except Exception as e:
            self.logger.exp.error(e)
            return False
    def reboot_package(self) -> bool:
        try:
            ret = self.android.control.reboot_package(
                const.PACKAGE_NAME.value,
                const.START_ACTIVITY.value,
                0)
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return False


    def tap_image_center(self, tap_img_path, base_func_name='',is_confirm_tap_point=True) -> bool:
        try:
            func_name = base_func_name
            # base_path = self.android.control.get_screenshot_default_path()
            # read_path の中に temp_path があったら、その場所をタップする
            # flag = self.android.control.get_screenshot(
            #     self.android.constants.main.SAVE_PATH_ROOT_DIR.value,
            #     self.android.constants.main.SD_ROOT_DIR.value,
            #     self.android.constants.main.SCREEN_CAPTURE_FILE_NAME.value)
            self.android.device_info.is_output_shell_result = is_confirm_tap_point
            flag = self.android.control.tap_image(tap_img_path)
            if flag : print('tap success : '+ func_name)
            else : print('tap failed : ' + func_name)
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def tap_image_is_match_image(self,tap_image_path,check_image_path,base_func_name,is_tap_point_confirm=False) -> bool:
        try:
            func_name = base_func_name
            # read_path の中に temp_path があったら、その場所をタップする
            flag = self.android.control.tap_image_is_match_image(tap_image_path,check_image_path,'',is_tap_point_confirm)
            if flag : print('tap success : '+ func_name)
            else : print('tap failed : ' + func_name)
        except Exception as e:
            self.logger.exp.error(e)
            return False
            
    def tap_ok_when_change_update(self) -> bool:
        func_name = 'tap_ok_when_change_update'
        temp_path = self.image_dir + '\\' + const_images.CHANGE_DATE.value
        return self.tap_image_center(temp_path,func_name)
        
    def tap_ok_when_error_google_play(self,is_confirm_tap_point=False) -> bool:
        func_name = 'tap_ok_when_error_google_play'
        check_path = self.image_dir + '\\' + const_images.ERROR_GOOGLE_PLAY.value
        tap_path = self.get_image_path(const_images.BUTTON_OK_SMALL.value)
        return self.tap_image_is_match_image(
            tap_path,check_path,func_name,is_confirm_tap_point)
    
    def tap_ok_login(self,is_confirm_tap_point=False) -> bool:
        func_name = 'tap_ok_login'
        tap_path = self.get_image_path(const_images.BUTTON_OK_SMALL.value)
        return self.tap_image_center(tap_path,func_name,is_confirm_tap_point)

    def tap_ok(self,base_func_name ,is_confirm_tap_point=False) -> bool:
        func_name = base_func_name
        tap_path = self.get_image_path(const_images.BUTTON_OK_SMALL.value)
        return self.tap_image_center(tap_path,func_name,is_confirm_tap_point)

    def tap_ok_mail_box(self,is_confirm_tap_point=False) -> bool:
        func_name = 'tap_ok_mail_box'
        return self.tap_ok(func_name,is_confirm_tap_point)

    def get_image_path(self,file_name):
        return self.image_dir + '\\' + file_name

    def tap_menu_dungeon(self,is_confirm_tap_point=False) -> bool:
        func_name = 'tap_menu_dungeon'
        tap_path = self.get_image_path(const_images.MENU_ICON_DUNGEON.value)
        return self.tap_image_center(tap_path,func_name,is_confirm_tap_point)

    def tap_start(self) -> bool:
        func_name = 'tap_start'
        image_path = self.get_image_path(const_images.START_BUTTON_OPENING.value)
        flag = self.android.control.tap_image_match_image_in_movie(
            image_path,
            self.android.control.const.main.SCREEN_RECORD_FILE_NAME.value,
            self.android.control.const.main.SD_ROOT_DIR.value,
            3,True)
        return flag