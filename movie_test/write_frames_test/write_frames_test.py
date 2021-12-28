
import numpy as np
from PIL import Image
import sys

import traceback
import import_init

def get_paths():
    try:
        import pathlib,os
        dir_path = str(pathlib.Path(__file__).parent)
        # image_path = os.path.join(dir_path,'image','histgram')
        movie_path = dir_path
        file_base = 'buttle2.mp4'
        base_path = os.path.join(movie_path,file_base)
        if not os.path.exists(base_path):
            print('not exists : ' + base_path)
        return movie_path,base_path
    except:
        traceback.print_exc()

def get_datetime():
    import datetime
    val = datetime.datetime.now().strftime('%y%m_%H%M%S')
    return val

def get_result_path():
    import pathlib,os
    dir_path = str(pathlib.Path(__file__).parent)
    child_dir_name = 'write_frames_result_' + get_datetime()
    result_path = os.path.join(dir_path,child_dir_name)
    if not os.path.exists(result_path):
        os.mkdir(result_path)
    return result_path

def addstr_to_file_name(logger,base_file_name,addstr):
    import common_util.file_util.file_name_util as file_name_util
    return file_name_util.add_str_to_file_name(logger,base_file_name,addstr)

import common_util.cv2_image.cv2_movie as cv2_movie
import common_util.cv2_image.cv2_image_util as cv2_image_util
def main():
    try:        
        logger = import_init.initialize_logger_new()
        movie_dir , file_path = get_paths()
        img_obj = cv2_image_util.Cv2Image(logger) # 書き込むためのもの
        result_dif_path = get_result_path()
        import os
        if not os.path.exists(result_dif_path):
            logger.exp.error('dir not exists , result_path = '+result_dif_path)
        # 拡張子なしのファイル名
        import os
        basename_without_ext:str = os.path.splitext(os.path.basename(file_path))[0]
        base_file_name = basename_without_ext + '.png'

        cap = cv2_movie.VideoCaptureFrames(logger,file_path)
        cap.info.show_movie_info()
        cap.initialize_value('movie')
        sec_step = 0.1
        frame_step = int(sec_step * cap.info.movie_fps)
        print('frame_step = ' + str(frame_step))
        while (not cap.frame_is_max_or_max_over()):
            # 基本のファイル名に追加する文字列を取得する
            addstr = str(cap.frame_int_now)
            # 書き込みファイル名を設定する
            output_file_name = addstr_to_file_name(logger,base_file_name,addstr)
            # 書き込みのパスを設定する
            out_put_path = os.path.join(result_dif_path,output_file_name)
            # フレームイメージの書き込み
            img_obj.save_img_other(out_put_path,cap.get_video_capture_image())
            # フレームを次へ移動する
            cap.move_frame(frame_step)
        return
    except:
        traceback.print_exc()

main()