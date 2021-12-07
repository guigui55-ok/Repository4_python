

# from common_util.adb_util import device_info
# from common_util.adb_util.adb_common import is_success_adb_result, screen_capture_for_android


if __name__ == '__main__' or __name__ == 'android_main_control':
    import adb_key  
    from  device_info import DeviceInfo
    import adb_common
    from android_const import Constants
    from android_control_cv2_image import AndroidControlCv2Image
    from android_control_cv2_movie import AndroidControlCv2Movie
    from android_control_adb import AndroidControlAdb
    from adb_common import logger as adb_comon_logger
else:
    # 外部から参照時は、common_util を sys.path へ追加しておくこと
    import common_util.adb_util.adb_key  
    from common_util.adb_util.device_info import DeviceInfo
    import common_util.adb_util.adb_common as adb_common
    from common_util.adb_util.android_const import Constants
    from common_util.adb_util.android_control_cv2_image import AndroidControlCv2Image
    from common_util.adb_util.android_control_cv2_movie import AndroidControlCv2Movie
    from common_util.adb_util.android_control_adb import AndroidControlAdb
    from common_util.adb_util.adb_common import logger as adb_comon_logger

class AndroidControlMain():
    logger = None
    const : Constants= None
    control_cv2_img:AndroidControlCv2Image
    control_cv2_mov:AndroidControlCv2Movie
    control_adb:AndroidControlAdb
    device_info : DeviceInfo
    ocr_control = None
    control_mode = 1
    def __init__(self,logger,device_info,img_path) -> None:
        self.logger = logger
        self.device_info = device_info
        self.const = Constants
        self.control_mode = self.const.main.CONTROL_MODE_IMG_CV2.value
        self.control_adb = AndroidControlAdb(logger,device_info)
        self.control_cv2_img = AndroidControlCv2Image(logger,self.control_adb,img_path)
        self.control_cv2_mov = AndroidControlCv2Movie(logger,self.control_adb,img_path)
        adb_comon_logger = self.logger

        self.const_screen_image_file_names = self.const.image_file
    
    def power_on(self,mode=Constants.main.CONTROL_MODE_ADB):
        return self.control_adb.power_on()

    def reboot(self,mode=Constants.main.CONTROL_MODE_ADB):
        return self.control_adb.reboot()

    def excute_command(self,command):
        flag ,ret = self.control_adb.excute_command(command)
        return flag, ret

    def input_keycode(self,keycode)->bool:
        try:
            return adb_common.input_keyevent(keycode, self.device_info.device_id, self.device_info.is_output_shell_result)
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def run_app(self):
        pass
    
    def transision_to_home(self,mode=Constants.main.CONTROL_MODE_ADB):
        self.input_keycode(Constants.key.HOME)

    def get_screenshot(self,save_dir_path='',save_android_path='',save_file_name=''):
        try:
            if save_dir_path == '':
                save_dir_path = Constants.main.SAVE_PATH_ROOT_DIR.value
            if save_android_path == '':
                save_android_path = Constants.main.SD_ROOT_DIR.value
            if save_file_name == '':
                save_file_name = Constants.main.SCREEN_CAPTURE_FILE_NAME.value
            adb_common.screen_capture_for_android(
                save_file_name, save_android_path, 
                self.device_info.device_id,
                self.device_info.is_output_shell_result)            
            adb_common.save_file_to_pc_from_android(
                save_dir_path,save_android_path,save_file_name,
                self.device_info.device_id,
                self.device_info.is_output_shell_result)
        except Exception as e:
            self.logger.exp.error(e)
            
    def get_screenshot_default_path(self) -> str:
        return Constants.main.SAVE_PATH_ROOT_DIR.value + Constants.main.SCREEN_CAPTURE_FILE_NAME.value
            
    def unlock(self,mode=Constants.main.CONTROL_SWIPE):
        """ mode : unlock_control_mode"""
        try:
            if mode == self.const.main.CONTROL_SWIPE:
                adb_common.swipe(300,1000,300,200,200)
            else:
                self.logger.exp.error('unlock mode is invalid')
        except Exception as e:
            self.logger.exp.error(e)
            
    def reboot_package(self,package_name,class_name,wait_time,
    mode=Constants.main.CONTROL_MODE_ADB)->bool:
        flag =self.control_adb.reboot_package(package_name, class_name, wait_time)
        return flag

    def tap_center(self,tap_rect,time=1,interval_sec=1)->bool:
        # CONTROL_MODE_ADB only
        flag,ret =self.control_adb.tap_center(tap_rect, time, interval_sec,)
        return flag
    
    def start_package(self,package_name,class_name,mode=Constants.main.CONTROL_MODE_ADB)->bool:
        flag,ret =self.control_adb.start_package(package_name,class_name)
        return flag

    def swipe(self,x1,y1,x2,y2,duration)->bool:
        # CONTROL_MODE_ADB only
        flag,ret =self.control_adb.swipe(x1,y1,x2,y2,duration)
        return flag

    def tap_image(self,tap_image_path,screenshot_path=''):
        if screenshot_path == '':
            screenshot_path = self.get_screenshot_default_path()
        self.control_adb.get_screenshot()
        flag = self.control_cv2_img.tap_image(
            tap_image_path,
            screenshot_path,
            self.device_info.is_output_shell_result)
        return flag

    def tap_image_is_match_image(self,
    tap_image_path,
    check_image_path,
    screenshot_path,
    is_tap_point_confirm
    )->bool:
        flag = self.control_cv2_img.tap_image_is_match_image(
            tap_image_path,check_image_path,screenshot_path,is_tap_point_confirm)

    def tap_image_match_image_in_movie(
    self,
    check_image_path,
    screen_record_file_name,
    screen_record_dir,
    record_time=3,
    is_tap_point_confirm=True
    )->bool:
        #get_rect_match_image_in_movie
        rect = self.control_cv2_mov.is_exists_image_in_screenrecord(
            check_image_path,
            record_time,
            self.device_info.device_id,
            '',
            '',
            self.device_info.is_output_shell_result)
        flag = self.tap_center(rect)
        return flag
        