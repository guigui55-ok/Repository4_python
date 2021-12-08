#https://qiita.com/satsukiya/items/9647e20c4e27b3d0362a

import cv2

def main():
    """フレーム数指定版"""
    try:
        movie_path = r'C:\ZMyFolder\newDoc\0ProgramingAll\image_sample\parts'
        file_name = 'pad_opening.mp4'
        movie_path += '\\' + file_name
        result_path = 'cut_result1.mp4'

        print('movie_path')
        print(movie_path)

        cap = cv2.VideoCapture(movie_path)

        cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        print( cap_width,cap_height,fps)

        fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
        writer = cv2.VideoWriter(result_path,fourcc, fps, (cap_width, cap_height))

        # 抽出したい開始and終了フレームを指定
        begin = 100
        end = 200

        cap.set(cv2.CAP_PROP_POS_FRAMES, begin)
        for i in range(end-begin):
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