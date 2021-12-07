

if __name__ == '__main__':
    import adb_common
    from  device_info import DeviceInfo
    from android_const import Constants
    from android_control_adb import AndroidControlAdb
else:
    # 外部から参照時は、common_util を sys.path へ追加しておくこと
    import common_util.adb_util.adb_common
    from  common_util.adb_util.device_info import DeviceInfo
    from common_util.adb_util.android_const import Constants
    from common_util.adb_util.android_control_adb import AndroidControlAdb
    

class AndroidState():
    logger = None
    image_dir = None
    const:Constants = None
    device_info : DeviceInfo
    __is_device_connected = False

    def __init__(
        self,
        logger,
        device_info,
        image_dir : str
    ) -> None:
        self.logger = logger
        self.const = Constants
        self.device_info = device_info
        self.image_dir = image_dir

    def initialize(self):
        pass
    
    def get_now_state_from_screen(self):
        try:
            img_path = self.image_dir + '\\' + \
                Constants.image_file.POWER_OFF.value
            # スクリーンショットを Android の SD_ROOT に作成する
            adb_common.save_file_to_pc_from_android(
                Constants.main.SD_ROOT_DIR.value,
                Constants.main.SCREEN_CAPTURE_FILE_NAME.value
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
                base_path = Constants.main.SAVE_PATH_ROOT_DIR.value + Constants.main.SCREEN_CAPTURE_FILE_NAME.value
            else:
                base_path = screenshot_path

            # 現在の状態を screenshot として保存、PC へ移動
            adb_common.save_file_to_pc_from_android(
                base_path,
                Constants.main.SD_ROOT_DIR.value,
                Constants.main.SCREEN_CAPTURE_FILE_NAME.value,
            )
            image_path = self.image_dir + '\\' + Constants.image_file.POWER_OFF.value
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
            # 現在の状態を screenshot として保存、PC (スクリプトルート) へ移動
            # ./screenshot.png
            adb_common.save_file_to_pc_from_android(
                Constants.main.SD_ROOT_DIR.value,
                Constants.main.SAVE_PATH_ROOT_DIR.value,
                Constants.main.SCREEN_CAPTURE_FILE_NAME.value
            )
            base_path = Constants.main.SAVE_PATH_ROOT_DIR.value + Constants.main.SCREEN_CAPTURE_FILE_NAME.value
            #image_path = self.image_dir + '\\' + const_images.HOME_MAIN
            # base_path に対して
            # image_dir から HOME_INCLUDE を含むファイルリストの
            # image 含まれるか判定する
            from cv2_image.cv2_find_image_util import is_match_templage_from_some_file
            result = is_match_templage_from_some_file(
                self.logger,
                base_path,
                self.image_dir,
                Constants.image_file.LOCK_INCLUDED.value,
                float(Constants.main.DEFAULT_THRESHOLD.value),
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
            return Constants.state.UNKNOWN.value

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
            return result
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def state_is(self) -> str:
        pass
