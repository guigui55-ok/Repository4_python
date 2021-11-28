
from logging import exception
from typing import Any

if __name__ == '__main__':
    import adb_common   
    from adb_common import logger as adb_common_logger
    from adb_key import logger as adb_key_logger
    from android_const import Constants
    from device_info import DeviceInfo
else:
    # 外部から参照時は、common_util,adb_util を sys.path へ追加しておく
    import adb_util.adb_common as adb_common
    from adb_util.adb_common import logger as adb_common_logger
    from adb_util.adb_key import logger as adb_key_logger
    from adb_util.android_const import Constants
    from adb_util.device_info import DeviceInfo

class AndroidControlAdb():
    logger = None
    device_info: DeviceInfo

    def __init__(
        self,
        logger,
        device_info
    ) -> None:
        self.logger = logger
        adb_key_logger = self.logger
        adb_common_logger = self.logger
        if device_info != None:
            self.device_info = device_info
        else:
            self.device_info = DeviceInfo()

    def initialize(self):
        pass

    def cnv_complete_process(self,result,func_name='',is_logout_stdout=True,ret_type=Constants.main.TYPE_BOOL):
        if ret_type == Constants.main.TYPE_BOOL: mode = 1
        elif ret_type == Constants.main.TYPE_STRING: mode = 2
        return adb_common.cnv_complete_process(result,func_name,is_logout_stdout,mode)

    def excute_command(self,command,func_name='',is_logout_stdout = True)->Any:
        """コマンドを実行して結果を取得する
        戻り値：成功時は(bool,str)が返る
        失敗時は(False,'')が返る"""
        try:
            # コマンドを実行する
            # ログに出力する
            # 結果をbool,strで取得する
            flag, ret_str = adb_common.excute_adb_command(
                command,self.device_info.device_id,is_logout_stdout)
            return flag,ret_str
        except Exception as e:
            self.logger.exp.error(e)            
            return False,''
    
    def power_on(self)->bool:
        try:
            self.logger.info('power_on')
            keycode = Constants.key.POWER
            command = 'input_keyevent : ' + keycode
            flag, ret_str = adb_common.excute_adb_command(
                command,
                self.device_info.device_id, 
                self.device_info.is_output_shell_result)
            return flag
        except Exception as e:
            self.logger.exp.error(e)
            return False            

    def reboot(self)->bool:
        try:
            self.logger.info('reboot')
            command = 'reboot'
            flag, ret_str = adb_common.excute_command_adb(
                command,
                self.device_info.device_id,
                self.device_info.is_output_shell_result)
            return flag
        except Exception as e:
            self.logger.exp.error(e)
            return False

    # def judge_adb_result(self,result,message)->bool:
    #     try:

    def get_screenshot(self,
        save_file_name=Constants.main.SCREEN_CAPTURE_FILE_NAME.value,
        device_save_dir=Constants.main.SD_ROOT_DIR.value,
        pc_save_path=Constants.main.SAVE_PATH_ROOT_DIR.value):
        try:
            self.logger.info('get_screenshot')
            adb_common.screen_capture_for_android(
                save_file_name,device_save_dir,
                self.device_info.device_id,
                self.device_info.is_output_shell_result)
            flag = adb_common.save_file_to_pc_from_android(
                pc_save_path,device_save_dir,save_file_name,
                self.device_info.device_id,
                self.device_info.is_output_shell_result)
            if flag: return pc_save_path + '\\' + save_file_name
            else: return ''
        except Exception as e:
            self.logger.exp.error(e)
            return '' 

    def reboot_package(self,package_name,class_name,wait_time = 0):
        try:
            self.logger.info('reboot_package')
            ret = adb_common.reboot_package(
                package_name,class_name,wait_time,
                self.device_info.device_id, 
                self.device_info.is_output_shell_result)
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def unlock(self,mode):
        """ mode : unlock_control_mode"""
        try:
            self.logger.info('unlock')
            if mode == Constants.main.CONTROL_SWIPE:
                adb_common.swipe(300,1000,300,200,200)
            else:
                self.logger.exp.error('unlock mode is invalid')
        except Exception as e:
            self.logger.exp.error(e)

    def get_screenshot_default_path(self) -> str:
        return Constants.main.SAVE_PATH_ROOT_DIR.value + Constants.main.SCREEN_CAPTURE_FILE_NAME.value


    # def is_exists_image_in_movie(self,check_image_path,base_movie_path) -> Any:
    #     """動画の中に画像があるか判定する
    #     戻り値は tuple(result:bool ,int ,int ,int ,int)
    #     失敗時は、tuple(false,-1,-1,-1,-1)が返る"""
    #     ret_rect=(False,-1,-1,-1,-1)
    #     try:

    # def is_exists_image(self,chack_image_path,base_image_path) -> bool:
    #     try:

    # def is_exists_image_in_screenrecord(
    #     self,
    #     check_image_path,
    #     time_limit = 3,
    #     device_id = '',
    #     screen_record_file_name='',
    #     screen_record_dir = '') -> bool:
    #     """Android を screenRcord して、その中に一致する画像があるか判定する
    #     戻り値は画像が一致した範囲 tuple(int,int,int,int) を返す
    #     失敗時は(-1,-1,-1,-1)を返す
    #     """
    #     ret_rect=(-1,-1,-1,-1)
    #     try:

    # def is_exists_image_in_screenshot(self,check_image_path,screenshot_path='') -> bool:
    #     try:

    # def tap_image_is_match_image(self,tap_image_path,check_image_path,screenshot_path='',is_tap_point_confirm=False) -> bool:
    #     try:

    def tap_center(self,tap_rect,times=1,interval_sec=1)->bool:
        try:
            self.logger.info('tap_center')
            # 範囲の真ん中をタップする
            is_taped = adb_common.tap_center(
                tap_rect, 
                self.device_info.device_id, 
                times,interval_sec,
                self.device_info.is_output_shell_result)
            return is_taped
        except Exception as e:
            self.logger.exp.error(e)
            return False


    def start_package(self,package_name,class_name='')->bool:
        try:
            self.logger.info('start_package')
            ret = adb_common.start_package(
                package_name,
                class_name,
                self.device_info.device_id,
                self.device_info.is_output_shell_result)
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return False
    
    def swipe(self,x1,y1,x2,y2,duration)->bool:
        try:
            self.logger.info('swipe')
            ret = adb_common.swipe(
                x1,y1,x2,y2,duration,
                self.device_info.device_id,
                self.device_info.is_output_shell_result)
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def get_screenshot(
        self,
        save_path_pc='./',
        save_dir_device='/sdcard/',
        save_file_name='screenshot.png')->bool:
        try:
            self.logger.info('get_screenshot')
            android_save_path = adb_common.screen_capture_for_android(
                save_file_name,
                save_dir_device,
                self.device_info.device_id,
                self.device_info.is_output_shell_result
            )
            flag , ret = adb_common.save_file_to_pc_from_android(
                save_path_pc, save_dir_device, save_file_name,
                self.device_info.device_id,
                self.device_info.is_output_shell_result)
            return flag
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def input_keyevent(self,keycode):
        try:
            self.logger.info('input_keyevent')
            ret = adb_common.input_keyevent(
                keycode,
                self.device_info.device_id,
                self.device_info.is_output_shell_result)
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return False


    def close_app_all(self):
        pass
    
    def transision_to_home(self):
        pass