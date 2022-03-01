
if __name__ == '__main__':
    import adb_common
    from  device_info import DeviceInfo
    from android_const import Constants
    from android_control_adb import AndroidControlAdb
else:
    # 外部から参照時は、common_util を sys.path へ追加しておくこと
    from common_util.adb_util import adb_common
    from common_util.adb_util.device_info import DeviceInfo
    from common_util.adb_util.android_const import Constants
    from common_util.adb_util.android_control_adb import AndroidControlAdb

class AndroidState():
    logger = None
    constants : Constants
    image_dir = None
    device_info : DeviceInfo
    control_adb : AndroidControlAdb

    def __init__(
        self,
        logger,
        control_adb :AndroidControlAdb,
        image_dir : str
    ) -> None:
        self.logger = logger
        self.device_info = control_adb.device_info
        self.image_dir = image_dir
        self.control_adb = control_adb
        self.constants = Constants
    def initialize(self):
        self.logger.info(Constants.main.NOT_IMPLEMENTED.value)
    
    def get_now_state_from_screen(self):
        """非推奨"""
        try:
            img_path = self.image_dir + '\\' + \
                Constants.image_file.POWER_OFF.value
            self.logger.info(Constants.main.NOT_IMPLEMENTED.value)
        except Exception as e:
            self.logger.exp.error(e)

    def is_off(self):
        """非推奨"""
        try:
            chk_path = self.image_dir + '\\' + \
                Constants.image_file.POWER_OFF.value
            img_path = self.control_adb.get_screenshot()
            from cv2_image.cv2_image_comp import is_same_image
            flag = is_same_image(self.logger,img_path,chk_path)
            return flag
        except Exception as e:
            self.logger.exp.error(e)
            return False
        
    def is_connected_device(self,device_id=''):
        try:
            ret = adb_common.is_connect_android(
                self.logger,
                device_id,self.device_info.is_output_shell_result)
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def is_home(self):
        """非推奨"""
        pass

    def state_is(self) -> str:
        """非推奨"""
        pass
