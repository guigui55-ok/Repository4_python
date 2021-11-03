
# from adb_util  import androidcv android_cv2.android_imort_init_cv2

from adb_util.android_const import const_int
from adb_util.android_const import const
from adb_util.android_const \
    import const_screen_image_file_names as const_images
from adb_util.android_const import const_state

from adb_util import adb_common

    

class android_state():
    logger = None
    image_dir = None
    const = None
    __is_device_connected = False
    adb_common.logger = logger

    def __init__(
        self,
        logger,
        image_dir : str
    ) -> None:
        self.logger = logger
        self.const = const
        self.image_dir = image_dir

    def initialize(self):
        pass
    
    def get_now_state_from_screen(self):
        try:
            img_path = self.image_dir + '\\' + \
                self.image.POWER_OFF
            # スクリーンショットを Android の SD_ROOT に作成する
            from adb_common import save_file_to_pc_from_android
            save_file_to_pc_from_android(
                const.SD_ROOT_DIR,
                const.SCREEN_CAPTURE_FILE_NAME
            )
        except Exception as e:
            self.logger.exp.error(e)

    def is_power_off(self):
        pass

    def is_off_screen(self,screenshot_path='') -> bool:
        try:
            self.logger.info('is_off_screen')
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
            image_path = self.image_dir + '\\' + const_images.POWER_OFF.value
            # base_path に対して
            # image と合致するか判定する
            from cv2_image.cv2_image_comp import is_same_image
            is_same = is_same_image(
                self.logger,
                base_path,
                image_path
            )
            return is_same
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def is_lock(self,screenshot_path,screen_mode) -> bool:
        try:
            from adb_util.adb_common import save_file_to_pc_from_android
            # 現在の状態を screenshot として保存、PC (スクリプトルート) へ移動
            # ./screenshot.png
            save_file_to_pc_from_android(
                const.SD_ROOT_DIR,
                const.SAVE_PATH_ROOT_DIR,
                const.SCREEN_CAPTURE_FILE_NAME
            )
            base_path = const.SAVE_PATH_ROOT_DIR + const.SCREEN_CAPTURE_FILE_NAME
            #image_path = self.image_dir + '\\' + const_images.HOME_MAIN
            # base_path に対して
            # image_dir から HOME_INCLUDE を含むファイルリストの
            # image 含まれるか判定する
            from cv2_image.cv2_find_image_util import is_match_templage_from_some_file
            result = is_match_templage_from_some_file(
                self.logger,
                base_path,
                self.image_dir,
                const_images.LOCK_INCLUDE,
                float(const.DEFAULT_THRESHOLD),
                screenshot_path
            )
            return result
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def get_screen_mode(self,screenshot_path)-> int:
        try:
            pass
        except Exception as e:
            self.logger.exp.error(e)
            return const_state.UNKNOWN

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
            flag = self.is_success_adb_result(result)
            return flag
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def state_is(self) -> str:
        pass
