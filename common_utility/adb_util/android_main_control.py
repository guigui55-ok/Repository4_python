
import traceback
# from common_util.adb_util.adb_common.adb_get_screenshot import main
from common_util.adb_util import android_main_control_swipe_per

try:
    import common_util.adb_util.adb_key  
    from common_util.adb_util.device_info import DeviceInfo
    import common_util.adb_util.adb_common as adb_common
    from common_util.adb_util.android_const import Constants
    from common_util.adb_util.android_control_cv2_image import AndroidControlCv2Image
    from common_util.adb_util.android_control_cv2_movie import AndroidControlCv2Movie
    from common_util.adb_util.android_control_adb import AndroidControlAdb
    from common_util.adb_util.android_main_control_swipe import AndroidControlSwipe
    from common_util.adb_util.android_main_control_swipe_per import AndroidControlSwipePer
    from common_util.adb_util.android_control_ocr import AndroidControlOcr
except:
    traceback.print_exc()

class AndroidControlMain():
    logger = None
    const : Constants= None
    control_cv2_img:AndroidControlCv2Image
    control_cv2_mov:AndroidControlCv2Movie
    control_adb:AndroidControlAdb
    swipe:AndroidControlSwipe
    swipe_p:android_main_control_swipe_per
    control_ocr:AndroidControlOcr
    device_info : DeviceInfo
    control_mode = 1
    def __init__(self,logger,device_info,img_path,device_id='') -> None:
        self.logger = logger
        self.device_info = device_info
        self.device_info.device_id = device_id
        self.const = Constants
        self.control_mode = self.const.main.CONTROL_MODE_IMG_CV2.value
        self.control_adb = AndroidControlAdb(logger,device_info)
        self.control_cv2_img = AndroidControlCv2Image(logger,self.control_adb,img_path)
        self.control_cv2_mov = AndroidControlCv2Movie(logger,self.control_adb,img_path)
        self.swipe = AndroidControlSwipe(logger,self.control_adb)
        self.swipe_p = AndroidControlSwipePer(logger,self.control_adb)
        self.control_ocr = AndroidControlOcr(logger,self.control_adb,img_path)
        self.initialize()
        self.const_screen_image_file_names = self.const.image_file
    
    def initialize(self)->bool:
        try:
            w ,h = self.control_adb.get_screen_size()
            self.device_info.width = w
            self.device_info.height = h
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def power_on(self,mode=Constants.main.CONTROL_MODE_ADB):
        return self.control_adb.power_on()

    def reboot(self,mode=Constants.main.CONTROL_MODE_ADB):
        return self.control_adb.reboot()

    def excute_command(self,command):
        flag ,ret = self.control_adb.excute_command(command)
        return flag, ret

    def input_keycode(self,keycode)->bool:
        try:
            return adb_common.input_keyevent(
                self.logger,
                keycode, self.device_info.device_id, self.device_info.is_output_shell_result)
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def run_app(self):
        pass
    
    def transision_to_home(self,mode=Constants.main.CONTROL_MODE_ADB):
        self.input_keycode(Constants.key.HOME)

    def get_screenrecord (
            self,
            save_dir_pc = '',
            save_file_name='screenrecord.mp4',
            save_dir_android='/sdcard/',
            time_limit=10,
            size='',
            bit_rate=4000000,
            output_format='mp4'
            ):
        try:
            ret = adb_common.screen_record(
                self.logger,
                save_file_name,
                save_dir_android,
                time_limit,
                self.device_info.device_id,
                size,
                bit_rate,
                output_format,
                self.device_info.is_output_shell_result)
            path = ret
            if path == '':
                self.logger.exp.error('get_screenshot failed , return')
                return ''
            flag = adb_common.save_file_to_pc_from_android(
                self.logger,
                save_dir_pc,save_dir_android,save_file_name,
                self.device_info.device_id,
                self.device_info.is_output_shell_result)
            import os
            ret_path = os.path.join(save_dir_pc,save_file_name)
            return ret_path
        except Exception as e:
            self.logger.exp.error(e)
            return ''

    def get_screenshot(self,save_dir_path='',save_android_path='',save_file_name=''):
        """
        スクリーンショットを取りアンドロイド内に保存、
        その後、そのファイルをPCへコピーする
        戻り値：
        [result:bool , saved_pc_path:str]
        失敗時は [False,''] を返す
        """
        try:
            if save_dir_path == '':
                save_dir_path = Constants.main.SAVE_PATH_ROOT_DIR.value
            if save_android_path == '':
                save_android_path = Constants.main.SD_ROOT_DIR.value
            if save_file_name == '':
                save_file_name = Constants.main.SCREEN_CAPTURE_FILE_NAME.value
            path = adb_common.screen_capture_for_android(
                self.logger,
                save_file_name, save_android_path, 
                self.device_info.device_id,
                self.device_info.is_output_shell_result)            
            if path == '':
                self.logger.exp.error('get_screenshot failed , return')
                return False,''
            flag = adb_common.save_file_to_pc_from_android(
                self.logger,
                save_dir_path,save_android_path,save_file_name,
                self.device_info.device_id,
                self.device_info.is_output_shell_result)
            import os 
            saved_pc_path = os.path.join(save_dir_path,save_file_name)
            return flag,saved_pc_path
        except Exception as e:
            self.logger.exp.error(e)
            return False,''
            
    def get_screenshot_default_path(self) -> str:
        return Constants.main.SAVE_PATH_ROOT_DIR.value + Constants.main.SCREEN_CAPTURE_FILE_NAME.value
            
    def unlock(
        self,
        swipe_value=Constants.main.LOCK_OFF_DEFAULT_SWIPE_UP_VALUE.value,
        mode=Constants.main.CONTROL_SWIPE)->bool:
        """ mode : unlock_control_mode"""
        try:
            if mode == self.const.main.CONTROL_SWIPE:
                x1 = swipe_value[0]
                y1 = swipe_value[1]
                x2 = swipe_value[2]
                y2 = swipe_value[3]
                duration = swipe_value[4]
                return self.swipe.swipe(x1,y1,x2,y2,duration)
                # adb_common.swipe(self.logger, x1,y1,x2,y2,duration)                
            else:
                self.logger.exp.error('unlock mode is invalid')
            return False
        except Exception as e:
            self.logger.exp.error(e)
            return False
            
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

    def swipe_normal(self,x1,y1,x2,y2,duration)->bool:
        # CONTROL_MODE_ADB only
        # flag,ret =self.control_adb.swipe(x1,y1,x2,y2,duration)
        flag = self.swipe.swipe(x1,y1,x2,y2,duration)
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
    screen_record_file_name='',
    screen_record_dir = '',
    record_time=3,
    is_tap_point_confirm=True
    )->bool:
        #get_rect_match_image_in_movie
        rect = self.control_cv2_mov.is_exists_image_in_screenrecord(
            check_image_path,
            record_time,
            self.device_info.device_id,
            screen_record_file_name,
            screen_record_dir,
            self.device_info.is_output_shell_result)
        flag = self.tap_center(rect)
        return flag

    def get_connected_adb_devices(self):
        """[device_id,status]が返る"""
        return self.control_adb.get_connected_adb_devices()
    
    def tap_rect_by_ocr(self,keyword,target_index=0)->bool:
        try:
            rect_list = self.control_ocr.get_rect_by_ocr(keyword,target_index)
            if len(rect_list)>1:
                self.logger.exp.error('len(rect_list)>1 , select index 0')
            rect = rect_list[target_index]
            flag = self.control_adb.tap_center(rect)
            return flag
        except Exception as e:
            self.logger.exp.error(e)
            return False