
from logging import exception
from typing import Any

if __name__ == '__main__':
    import adb_common
    from android_control_cv2_image import AndroidControlCv2Image
    from android_control_adb import AndroidControlAdb
    from android_const import Constants
    from device_info import DeviceInfo
else:
    # 外部から参照時は、common_util を sys.path へ追加しておくこと
    import common_util.adb_util.adb_common as adb_common
    from common_util.adb_util.android_control_cv2_image import AndroidControlCv2Image
    from common_util.adb_util.android_control_adb import AndroidControlAdb
    from common_util.adb_util.android_const import Constants
    from common_util.adb_util.device_info import DeviceInfo

    import common_util.cv2_image as cv2_find_image_util
    from common_util.cv2_image import cv2_find_image_util
    from common_util.cv2_image import cv2_image_util
    from common_util.cv2_image import cv2_movie

if __name__ == '':
    # Intellisence 機能動作させるため
    import common_util.cv2_image as cv2_find_image_util
    from common_util.cv2_image import cv2_find_image_util
    from common_util.cv2_image import cv2_image_util
    from common_util.cv2_image import cv2_movie


class AndroidControlCv2Movie():
    logger = None
    image_dir = None
    control_adb : AndroidControlAdb
    device_info: DeviceInfo

    def __init__(
        self,
        logger,
        control_adb :AndroidControlAdb ,
        image_dir : str
    ) -> None:
        self.logger = logger
        self.control_adb = control_adb
        self.device_info = control_adb.device_info
        self.image_dir = image_dir

    def initialize(self):
        pass


    def get_screenrecord_defalt_path(self) -> str:
        return Constants.main.SAVE_PATH_ROOT_DIR.value + Constants.main.SCREEN_RECORD_FILE_NAME.value

    def is_exists_image_in_movie(self,check_image_path,base_movie_path) -> Any:
        """動画の中に画像があるか判定する
        戻り値は tuple(result:bool ,int ,int ,int ,int)
        失敗時は、tuple(false,-1,-1,-1,-1)が返る"""
        ret_rect=(False,-1,-1,-1,-1)
        try:
            cap = cv2_movie.video_capture_frames(self.logger,base_movie_path)
            ret_bool = cap.initialize_value('check_image')
            if not ret_bool:
                self.logger.exp.error('cv2_image.cv2_movie.video_capture_frames.initialize_value Failed')
                return

            img_obj = cv2_image_util.cv2_image(self.logger,check_image_path)
            if len(img_obj.img) <= 0 :return
            
            while(not cap.frame_is_max_or_max_over()):
                img = cap.get_video_capture_image()
                ret_rect = cv2_find_image_util.is_match_template_from_image(
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

    def is_exists_image_in_screenrecord(
        self,
        check_image_path,
        time_limit = 3,
        device_id = '',
        screen_record_file_name='',
        screen_record_dir = '',
        is_logout_stdout=True) -> Any:
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
                base_rec_name = Constants.main.SCREEN_RECORD_FILE_NAME.value                
                is_save_screen_rec_to_android_sd_root = True
            else:
                base_rec_name = screen_record_file_name               
                is_save_screen_rec_to_android_sd_root = False

            # screensot_path を設定する
            if screen_record_dir == '':
                # ./
                base_rec_dir = Constants.main.SAVE_PATH_ROOT_DIR.value
            else:
                base_rec_dir = screen_record_dir

            if is_save_screen_rec_to_android_sd_root:
                # screenrecord を取得する AndroidのSDルートに
                # 成功で save_path、失敗時 ’’が返る
                ret = adb_common.screen_record(
                    self.logger,
                    Constants.main.SCREEN_RECORD_FILE_NAME.value,
                    Constants.main.SD_ROOT_DIR.value,
                    time_limit,
                    self.device_info.device_id,
                    self.device_info.is_output_shell_result)            
                if ret == '':
                    self.logger.exp.error('screen_record failed. return')
                    return False
            
            base_rec_path = base_rec_dir + '\\' + base_rec_name
            # screenrecord を PC へ移動
            ret = adb_common.save_file_to_pc_from_android(
                self.logger,
                base_rec_path,
                Constants.main.SD_ROOT_DIR.value,
                Constants.main.SCREEN_RECORD_FILE_NAME.value,
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

