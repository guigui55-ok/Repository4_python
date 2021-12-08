#https://qiita.com/satsukiya/items/9647e20c4e27b3d0362a

import cv2

def main():
    """
    秒指定版
    """
    try:
        movie_path = r'C:\ZMyFolder\newDoc\0ProgramingAll\image_sample\parts'
        file_name = 'pad_opening.mp4'
        movie_path += '\\' + file_name
        result_path = 'cut_result2.mp4'
        
        print('movie_path')
        print(movie_path)

        cap = cv2.VideoCapture(movie_path)

        cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        print('cap_width,cap_height,fps')
        print(cap_width,cap_height,fps)

        fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
        writer = cv2.VideoWriter(result_path,fourcc, fps, (cap_width, cap_height))

        # 抽出したい開始and終了時間を指定
        begin_sec = 10
        end_sec = 20

        # 上記変数から開始and終了フレームを算出し、intにする
        begin_frame = int(begin_sec * fps)
        end_frame = int(end_sec * fps)

        print('begin_frame,end_frame')
        print(begin_frame,end_frame)

        # 開始フレームへセットする
        cap.set(cv2.CAP_PROP_POS_FRAMES, begin_frame)

        # 開始から終了フレームまでファイルへ書き込み
        for i in range(end_frame-begin_frame):
            ret, frame = cap.read()
            if ret:
                writer.write(frame)

        writer.release()
        cap.release()
        print('result_path')
        print(result_path)
    except:
        import traceback
        print(traceback.print_exc())

    
if __name__ == '__main__':
    main()