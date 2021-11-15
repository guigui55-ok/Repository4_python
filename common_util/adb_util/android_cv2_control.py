
from logging import exception
from typing import Any
from adb_util import adb_common
import adb_util.android_common as android_common
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

    def reboot_package(self,package_name,class_name,wait_time = 0,devide_id = '',is_logout_stdout=True):
        try:
            ret = adb_common.reboot_package(
                package_name,class_name,wait_time,devide_id,is_logout_stdout)
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return False

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

    def get_screenshot_default_path(self) -> str:
        return const.SAVE_PATH_ROOT_DIR.value + const.SCREEN_CAPTURE_FILE_NAME.value

    def get_screenrecord_defalt_path(self) -> str:
        return const.SAVE_PATH_ROOT_DIR.value + const.SCREEN_RECORD_FILE_NAME.value

    def is_exists_image_in_movie(self,check_image_path,base_movie_path) -> Any:
        """動画の中に画像があるか判定する
        戻り値は tuple(result:bool ,int ,int ,int ,int)
        失敗時は、tuple(false,-1,-1,-1,-1)が返る"""
        ret_rect=(False,-1,-1,-1,-1)
        try:
            from cv2_image.cv2_movie import video_capture_frames
            cap = video_capture_frames(self.logger,base_movie_path)
            ret_bool = cap.initialize_value('check_image')
            if not ret_bool:
                self.logger.exp.error('cv2_image.cv2_movie.video_capture_frames.initialize_value Failed')
                return

            from cv2_image import cv2_image_util
            img_obj = cv2_image_util.cv2_image(self.logger,check_image_path)
            if len(img_obj.img) <= 0 :return
            
            from cv2_image.cv2_find_image_util import is_match_template_from_image
            while(not cap.frame_is_max_or_max_over()):
                img = cap.get_video_capture_image()
                ret_rect = is_match_template_from_image(
                    self.logger,img, img_obj.img)
                # 結果OKなら終了する
                if ret_rect['result']:
                    self.logger.info('is_match_template == True -> return')
                    return ret_rect
                # 次へ進む
                next_frame = cap.frame_int_now + 15
                cap.move_frame(next_frame)
                        
            return ret_rect
        except Exception as e:
            self.logger.exp.error(e)
            # 失敗用データを返す            
            return ret_rect

    def is_exists_image(self,chack_image_path,base_image_path) -> bool:
        try:
            image_path = chack_image_path
            base_path = base_image_path
            import pathlib
            self.logger.info('base_path = ' + str(pathlib.Path(base_path).resolve()))
            result_dir_path = './'
            #temp_path = 'image/button_login_ok.png'
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
            if not match_rect['result']:
                self.logger.exp.error('is_match_template_from_file2 failed. return')
            return match_rect
        except Exception as e:
            self.logger.exp.error(e)
            # 失敗用データを返す
            from cv2_image.cv2_find_image_util import get_result_false_is_match_template_from_file2
            return get_result_false_is_match_template_from_file2()

    def is_exists_image_in_screenrecord(
        self,
        check_image_path,
        time_limit = 3,
        device_id = '',
        screen_record_file_name='',
        screen_record_dir = '') -> bool:
        """Android を screenRcord して、その中に一致する画像があるか判定する
        戻り値は画像が一致した範囲 tuple(int,int,int,int) を返す
        失敗時は(-1,-1,-1,-1)を返す
        """
        ret_rect=(-1,-1,-1,-1)
        try:
            self.logger.info('is_exists_image_in_screenrecord')
            # screensot_path を設定する
            if screen_record_file_name == '':
                # screen_record.mp4
                base_rec_name = const.SCREEN_RECORD_FILE_NAME.value                
                is_save_screen_rec_to_android_sd_root = True
            else:
                base_rec_name = screen_record_file_name               
                is_save_screen_rec_to_android_sd_root = False

            # screensot_path を設定する
            if screen_record_dir == '':
                # ./
                base_rec_dir = const.SAVE_PATH_ROOT_DIR.value
            else:
                base_rec_dir = screen_record_dir

            if is_save_screen_rec_to_android_sd_root:
                # screenrecord を取得する AndroidのSDルートに
                # 成功で save_path、失敗時 ’’が返る
                from adb_util.adb_common import screen_record
                ret = screen_record(
                    const.SCREEN_RECORD_FILE_NAME.value,
                    const.SD_ROOT_DIR.value,
                    time_limit,
                    device_id)            
                if ret == '':
                    self.logger.exp.error('screen_record failed. return')
                    return False
            
            base_rec_path = base_rec_dir + '\\' + base_rec_name
            # screenrecord を PC へ移動
            from adb_util.adb_common import save_file_to_pc_from_android
            ret = save_file_to_pc_from_android(
                base_rec_path,
                const.SD_ROOT_DIR.value,
                const.SCREEN_RECORD_FILE_NAME.value,
            )
            if not ret:
                self.logger.exp.error('save_file_to_pc_from_android failed. return')
                return False

            # is_exists_image_in_movie
            # check_interval_frame
            exists_ret = self.is_exists_image_in_movie(check_image_path,base_rec_path)
            if not exists_ret['result']:
                self.logger.exp.error('is_exists_image_in_screenrecord , match false')
                return ret_rect
            else:
                self.logger.exp.error('is_exists_image_in_screenrecord , match true')
                ret_rect = (
                    int(exists_ret['start_w']),
                    int(exists_ret['start_h']),
                    int(exists_ret['end_w']),
                    int(exists_ret['end_h']))
            return ret_rect
        except Exception as e:
            self.logger.error(e)
            # 失敗用データを返す
            return ret_rect


    def is_exists_image_in_screenshot(self,check_image_path,screenshot_path='') -> bool:
        try:
            self.logger.info('is_exists_image_in_screenshot')
            
            # screensot_path を設定する
            if screenshot_path == '':
                # ./screenshot.png
                base_path = self.get_screenshot_default_path()
                is_save_screenshot_to_android_sd_root = True
            else:
                base_path = screenshot_path
                is_save_screenshot_to_android_sd_root = False

            if is_save_screenshot_to_android_sd_root:
                # screenshot を取得する AndroidのSDルートに
                from adb_util.adb_common import screen_capture_for_android
                ret = screen_capture_for_android()
                if not ret:
                    self.logger.exp.error('screen_capture failed. return')
                    return False

            # screenshot を PC へ移動
            from adb_util.adb_common import save_file_to_pc_from_android
            ret = save_file_to_pc_from_android(
                base_path,
                const.SD_ROOT_DIR.value,
                const.SCREEN_CAPTURE_FILE_NAME.value,
            )
            if not ret:
                self.logger.exp.error('save_file_to_pc_from_android failed. return')
                return False

            ret = self.is_exists_image(check_image_path,base_path)
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            # 失敗用データを返す
            from cv2_image.cv2_find_image_util import get_result_false_is_match_template_from_file2
            return get_result_false_is_match_template_from_file2()

    def tap_image_is_match_image(self,tap_image_path,check_image_path,screenshot_path='',is_tap_point_confirm=False) -> bool:
        try:
            self.logger.info('tap_image_when_exists_image')
            # parts_path が screenshot 内に存在するか判定する
            match_rect = self.is_exists_image(check_image_path,screenshot_path)
            if match_rect['result'] == False:
                self.logger.info('tap_image Failed')
                return False
            # check_image が存在した場合、tap_image_path の真ん中をタップする
            is_taped = self.tap_image(tap_image_path,screenshot_path,is_tap_point_confirm)
            return is_taped
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def tap_center(self,tap_rect)->bool:
        try:
            # 範囲の真ん中をタップする
            from adb_util.adb_common import tap_center
            is_taped = tap_center(tap_rect)
            return is_taped
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def tap_image(self,parts_path,screenshot_path='',is_tap_point_confirm=False) -> bool:
        try:
            self.logger.info('tap_image')
            # parts_path が screenshot 内に存在するか判定する
            match_rect = self.is_exists_image(parts_path,screenshot_path)
            if match_rect['result'] == False:
                self.logger.info('tap_image Failed')
                return False
            # 結果から image が合致した範囲を取得する
            tap_rect = match_rect['start_w'],match_rect['start_h'],\
                match_rect['end_w'],match_rect['end_h']
            print('tap_rect =' + str(tap_rect))
            # 範囲の真ん中をタップする
            from adb_util.adb_common import tap_center
            is_taped = tap_center(tap_rect)
            #
            if is_tap_point_confirm:
                # タップする画面の path を取得する
                check_path = self.get_screenshot_default_path()
                # 前処理で取得した範囲から、タップしたポイントを取得する
                from adb_util.adb_common import get_center_from_rect
                point = get_center_from_rect(tap_rect)
                # 描画して結果を出力する
                from cv2_image.cv2_find_image_util import output_image_draw_point
                result_path = output_image_draw_point(self.logger,check_path,point)
                self.logger.info('output_image_draw_point path = ' + result_path)
            return is_taped
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def start_package(self,package_name,class_name=''):
        try:
            from adb_util.adb_common import start_package
            ret = start_package(package_name,class_name)
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def close_app_all(self):
        pass
    
    def transision_to_home(self):
        pass