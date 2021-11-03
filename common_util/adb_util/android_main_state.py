from adb_util.adb_common import is_success_adb_result
from adb_util.android_const import const as const_str
from adb_util.android_const import const_screen_image_file_names as const_images
from adb_util.android_const import const_int
from adb_util import adb_common

class android_state():
    logger = None
    const_android : const_str = None
    const_android_int : const_int = None
    const_screen_image_file_names : const_images = None
    image_dir = None

    def __init__(
        self,
        logger,
        image_dir : str
    ) -> None:
        self.logger = logger
        self.image_dir = image_dir
        self.android_const = const_str
        self.const_android_int = const_int
        self.const_screen_image_file_names = const_images

    def initialize(self):
        self.logger.info(const_str.NOT_IMPLEMENTED.value)
    
    def get_now_state_from_screen(self):
        try:
            img_path = self.image_dir + '\\' + \
                self.const_screen_image_file_names.POWER_OFF
            self.logger.info(const_str.NOT_IMPLEMENTED.value)
        except Exception as e:
            self.logger.exp.error(e)

    def is_off(self):
        try:
            img_path = self.image_dir + '\\' + \
                self.const_screen_image_file_names.POWER_OFF
            

            from cv2_image.cv2_image_comp import is_same_image
            is_same_image()
            
        except Exception as e:
            self.logger.exp.error(e)
        
    def is_success_adb_result(self,result,message):
        try :
            result = adb_common.is_success_adb_result(result,message)
            return result
        except Exception as e:
            self.logger.exp.error(e)
            return None

    def is_connected_device(self):
        try:
            result = adb_common.is_connect_android()
            flag = is_success_adb_result(result)
            return flag
        except Exception as e:
            self.logger.exp.errro(e)
            return False

    def is_home(self):
        pass

    def state_is(self) -> str:
        pass
