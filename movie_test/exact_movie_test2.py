#https://qiita.com/satsukiya/items/9647e20c4e27b3d0362a

import cv2

from movie_util.play_movie import video_capture_frames
from logger_init import initialize_logger

def main():
    """
    video capthre object ver
    """
    try:
        logger = initialize_logger()

        import pathlib,os
        movie_dir = r'C:\ZMyFolder\newDoc\0ProgramingAll\image_sample\parts'
        file_name = 'pad_opening.mp4'
        movie_path = os.path.join(movie_dir,file_name)
        result_path = 'exact_result2.mp4'
        
        print('movie_path')
        print(movie_path)

        # movie を読み込む
        video = video_capture_frames(logger,movie_path)
        # movie 情報を出力、初期値をセットする
        video.info.show_movie_info()
        video.start_capture()
        # movie の幅高さを取得する
        width = video.info.movie_width
        height = video.info.movie_height
        # 抽出したい開始 and 終了時間を指定
        begin_sec = 10
        end_sec = 20
        # 抽出したい開始 and 終了 Frame を取得する
        begin_frame = int(begin_sec * video.info.movie_fps)
        end_frame = int(end_sec * video.info.movie_fps)
        # 抽出したい範囲
        exact_rect = [ 0 , 200 , width, height -200]
        # 抽出する
        flag = video.exact_movie(
            begin_frame,end_frame,exact_rect,result_path)
        
        print('result = ' + str(flag))
        print(result_path)
    except:
        import traceback
        print(traceback.print_exc())

    
if __name__ == '__main__':
    main()