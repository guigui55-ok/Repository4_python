

import adb_util
from adb_util import adb_key
from adb_util.adb_key_const import keycoce_const
from adb_util.android_const import const as android_const
from adb_util.android_const import const_int as android_const_int
from adb_util.android_const import const_screen_image_file_names as const_images
from adb_util.android_const import const_state as const_state
from adb_util import adb_common

class android_control():
    logger = None
    const_android : android_const= None
    const_screen_image_file_names : const_images= None
    def __init__(self,logger,const_android,const_screen_image_file_names) -> None:
        self.logger = logger
        self.android_const = const_android
        self.const_screen_image_file_names = const_screen_image_file_names
        adb_util.logger = self.logger
    
    def input_keycode(self,keycode):
        try:
            adb_key.input_keyevent(keycoce_const.POWER)
        except Exception as e:
            self.logger.exp.error(e)

    def run_app(self):
        pass
    
    def transision_to_home(self):
        self.input_keycode(keycoce_const.HOME)

    def get_screenshot(self):
        try:            
            adb_common.screen_capture_for_android()            
            adb_common.save_file_to_pc_from_android()
        except Exception as e:
            self.logger.exp.error(e)
            
    def unlock(self,mode):
        """ mode : unlock_control_mode"""
        try:
            self.logger.info('unlock')
            if mode == android_const_int.CONTROL_SWIPE:
                adb_common.swipe(300,1000,300,200,200)
            else:
                self.logger.exp.error('unlock mode is invalid')
        except Exception as e:
            self.logger.exp.error(e)