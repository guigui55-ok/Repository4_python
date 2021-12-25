
#https://qiita.com/satsukiya/items/9647e20c4e27b3d0362a

import cv2

def main():
    """フレーム数指定版"""
    try:
        import pathlib,os
        dir_path = str(pathlib.Path(__file__).parent)
        file_name = 'cut_result.mp4'
        movie_path = os.path.join(dir_path,file_name)
        result_path = 'exact_result1.mp4'

        print('movie_path')
        print(movie_path)

        cap = cv2.VideoCapture(movie_path)

        cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        print( cap_width,cap_height,fps)
        # 切り取る範囲を設定する
        # 上から200、したから200をカットする
        extract_rect = [0,200,cap_width,cap_height-200]
        begin_x,begin_y,end_x,end_y =  extract_rect

        write_movie_width , write_movie_height = [end_x - begin_x,end_y - begin_y ]
        fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
        writer = cv2.VideoWriter(result_path,fourcc, fps, (write_movie_width, write_movie_height))
        frame_max_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # 抽出したい開始and終了フレームを指定
        begin = 100
        end = 200

        # フレーム1枚ずつ処理する
        for i in range(frame_max_count):
            ret, frame = cap.read()
            edit_frame = frame[begin_y:end_y, begin_x:end_x]
            # frame = cv2.resize(frame,(int(width/resize), int(height/resize)))
            if ret:
                writer.write(edit_frame)
            # # 50フレームごとにログを出力する
            if i % 50 == 0:
                print(str(i) + "/" + str(frame_max_count))
            #cv2.imwrite('extract_area' + str(i) + '.jpg', dst)
        # cap.set(cv2.CAP_PROP_POS_FRAMES, begin)
        # for i in range(end-begin):
        #     ret, frame = cap.read()
        #     if ret:
        #         writer.write(frame)

        writer.release()
        cap.release()

        print('result_path')
        print(result_path)
    except:
        import traceback
        print(traceback.print_exc())

    
if __name__ == '__main__':
    main()



