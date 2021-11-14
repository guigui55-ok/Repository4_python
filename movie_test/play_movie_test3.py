import cv2

import argparse

def main(args_value=''):
    try:
        logger = logger_init.initialize_logger()
        window_size = get_window_size_pc()
        movie_path = r'C:\ZMyFolder\newDoc\0ProgramingAll\image_sample\parts'
        file_name = 'pad_opening.mp4'
        movie_path += '\\' + file_name
        if args_value != '':
            movie_path = args_value
        print('movie_path = ' + movie_path)

        play_movie_method(logger,movie_path,window_size)
    except:
        import traceback
        print(traceback.print_exc())

def get_window_size_pc():
    try:
        from screeninfo import get_monitors
        mon_info = get_monitors()
        """
Moniter の配列が返る、Monitor1-2それぞれ取得されている
Monitor(x=0, y=0, width=1920, height=1080, width_mm=597, height_mm=336, name='\\\\.\\DISPLAY1', is_primary=True)
Monitor(x=1920, y=0, width=1360, height=768, width_mm=820, height_mm=460, name='\\\\.\\DISPLAY2', is_primary=False)
        """
        print(str(mon_info))
        # for m in get_monitors():
        #     print(str(m))
            # Monitor(x=0, y=0, width=1920, height=1080, width_mm=597, height_mm=336, name='\\\\.\\DISPLAY1', is_primary=True)
        
        print('width = ' + str(mon_info[0].width))
        print('height = ' + str(mon_info[0].height))
        return mon_info[0].width,mon_info[0].height
    except:
        import traceback
        print(traceback.print_exc())
        return (0,0)

import movie_util.play_movie as play_movie
from movie_util.play_movie import movie_info,video_capture_frames,movie_player

import logger_init

def play_movie_method(logger,movie_path,window_size):
    try:
        info:movie_info = movie_info(logger,movie_path)
        player:movie_player = movie_player(logger,'',window_size,'video',info)

        ret = info.show_movie_info()
        if not ret:
            logger.exp.error('info_show_movie_info False return')
            return
        logger.info('info_show_movie_info done.')
        
        ret = player.play_initialize()
        if not ret:
            logger.exp.error('player_play_initialize False return')
            return
        logger.info('player_play_initialize done.')

        ret = player.play(is_do_play_initialize=False)
        if not ret:
            logger.exp.error('player_play False return')
            return
        logger.info('player_play done.')

        logger.info('all done. success.')
        return 
    except Exception as e:
        logger.exp.error(e)
        return

# https://note.nkmk.me/python-opencv-videocapture-file-camera/
def print_movie_info(cap):
    try:
        print('movie_width=')
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # 640.0
        print('movie_height')
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # 360.0
        print('movie_fps=')
        print(cap.get(cv2.CAP_PROP_FPS))
        # 29.97002997002997
        print('movie_all_frame_count=')
        print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # 360.0
        print('movie_time(sec)=')
        print(cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS))
        # 12.012
    except:
        import traceback
        print(traceback.print_exc())

# new size より大きいときフィットするようリサイズする
# Resize to fit when larger than new size
def resize_to_fit_when_lager_than_new_size(frame_size,new_size):
    try:
        new_width = new_size[0]
        new_height = new_size[1]
        frame_width = frame_size[0]
        frame_height = frame_size[1]
        # new_size がゼロの場合は何もしない
        if (new_width <= 0) or (new_height <= 0):
            return frame_size
        # new_size より小さい場合は何もしない
        if (frame_width >= new_width) and (frame_height >= new_height):
            return frame_size
        # 縦横それぞれの比率を求める
        width_raito = frame_width / new_width
        height_raito = frame_height / new_height
        # 比率が大きいほうに合わせる
        if width_raito > height_raito:
            new_raito = width_raito
        else:
            # width_raito <= height_raito
            new_raito = height_raito
        
        ret_width = int(frame_width / new_raito)
        ret_height = int(frame_height / new_raito)
        return ret_width,ret_height
    except:
        import traceback
        print(traceback.print_exc())
        return frame_size

def sample1():
    #https://github-wiki-see.page/m/atinfinity/lab/wiki/%5Bopencv-python%5D%E7%94%BB%E5%83%8F%E3%82%A2%E3%82%B9%E3%83%9A%E3%82%AF%E3%83%88%E6%AF%94%E3%82%92%E7%B6%AD%E6%8C%81%E3%81%97%E3%81%9F%E3%82%A6%E3%82%A3%E3%83%B3%E3%83%89%E3%82%A6%E8%A1%A8%E7%A4%BA
    import cv2
    import sys

    img = cv2.imread("lena.jpg", cv2.IMREAD_UNCHANGED)

    if img is None:
        print("Failed to load image file.")
        sys.exit(1)

    cv2.namedWindow("image", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main() 
else:
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1')
    args = parser.parse_args()
    args_value = ''
    if args.arg1 != None:
        if args.arg1 != '':
            args_value = args.arg1
    main(args_value)