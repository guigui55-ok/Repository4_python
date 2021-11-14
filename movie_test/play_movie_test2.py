import cv2

import argparse

def main(args_value=''):
    try:
        window_size = get_window_size_pc()
        movie_path = r'C:\ZMyFolder\newDoc\0ProgramingAll\image_sample\parts'
        file_name = 'pad_opening.mp4'
        movie_path += '\\' + file_name
        if args_value != '':
            movie_path = args_value
        print('movie_path = ' + movie_path)
        play_movie(movie_path,window_size)
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


def play_movie(movie_path,window_size):
    try:
        is_pause = False
        cap :cv2.VideoCapture= cv2.VideoCapture(movie_path)
        # cap.set(cv2.CAP_PROP_POS_FRAMES, 20)
        if (cap.isOpened()== False):  
            print("ビデオファイルを開くとエラーが発生しました") 
            return
        print_movie_info(cap)
        window_title = 'Video'
        
        cv2.namedWindow(window_title,cv2.WINDOW_NORMAL)
        # cv2.setWindowProperty(window_title,cv2.WND_PROP_ASPECT_RATIO,cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(window_title,cv2.WND_PROP_ASPECT_RATIO,cv2.WINDOW_AUTOSIZE)

        ret, frame = cap.read()
        cv2.imshow(window_title, frame)
        # デスクトップサイズより大きい場合、サイズ変更、比率は保持する
        new_size = resize_to_fit_when_lager_than_new_size(
            (frame.shape[1],frame.shape[0]),window_size)
        print(str(new_size))
        cv2.resizeWindow(window_title,new_size[0],new_size[1])

        # 総フレーム数の取得
        frame_max = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
        frame_now = 0
        while(cap.isOpened()):
            
            # cv2.setWindowProperty(window_title,cv2.WND_PROP_ASPECT_RATIO,cv2.WINDOW_AUTOSIZE)
            
            # cv2.imshow(window_title, frame)
            # prop_val = cv2.getWindowProperty(window_title, cv2.WND_PROP_ASPECT_RATIO)
            # print(prop_val)
            # if prop_val < 0:
            #     break
            if frame_now < frame_max:
                if not is_pause:
                    ret, frame = cap.read()
            
            
            if ret == True:
                # 可視化されていないとエラーとなる
                # print(str(frame.shape[1]) + ',' + str(frame.shpae[0]))
                try:
                    prop = cv2.getWindowProperty(window_title,cv2.WND_PROP_VISIBLE)
                    if not prop:
                        print('cv2.window visible False -> break')
                        break

                    #prop = cv2.getWindowProperty(window_title,cv2.WND_PROP_ASPECT_RATIO) #Error
                    prop = cv2.getWindowProperty(window_title,cv2.WND_PROP_AUTOSIZE)
                except:
                    print('prop=' + str(prop))
                    
                    # 閉じるを押したとき以下例外によりここに来る
                    import traceback
                    print(traceback.print_exc())
                    # cv2.error: OpenCV(4.5.4-dev) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window_w32.cpp:857:
                    # error: (-27:Null pointer) NULL window: 'Video' in function 'cvGetRatioWindow_W32'
                    break

                # print(str(prop))
                cv2.imshow(window_title, frame)
                #print(str(frame.shape[0]) , str(frame.shape[1]))#1440 720

                    
                # key'q'で終了する
                # ord method : 文字をUnicode値に変換する
                key_pushed = cv2.waitKey(20) & 0xFF
                if key_pushed == ord('q'): 
                    break
                elif key_pushed == ord('p') or key_pushed == ord(' '): 
                    is_pause = not is_pause
                    if is_pause:print('pause')
                    else: 
                        print('play')
                        if frame_now >= frame_max:
                            # 始点から再生、終点で停止中から再生なら
                            print('frame_now >= frame_max -> play')
                            frame = 0
                            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                            ret, frame = cap.read()
                            cv2.imshow(window_title, frame)
                # elif key_pushed == ord(' '): 
                #     is_pause = not is_pause
                #     if is_pause:print('pause')
                #     else:                         
                #         print('play')
                #         if frame_now >= frame_max:
                #             # 始点から再生、終点で停止中から再生なら
                #             print('frame_now >= frame_max -> play')
                #             frame = 0
                #             cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                #             ret, frame = cap.read()
                #             cv2.imshow(window_title, frame)
                elif key_pushed == ord('c'):
                    write_path='./movie_capture.png'
                    cv2.imwrite(write_path,frame)
                    print(write_path)
                elif key_pushed == ord('1'):
                    is_pause = True
                    # 現在の再生位置（フレーム位置）の取得
                    frame_now = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
                    # 総フレーム数の取得
                    #frame_all = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                    frame_all = frame_max
                    frame_now -= 2
                    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_now)
                    print('frame_now = ' + str(frame_now) + ' / ' + str(frame_all))
                    frame = frame_now
                    ret, frame = cap.read()
                    cv2.imshow(window_title, frame)
                elif key_pushed == ord('3'):
                    # 現在の再生位置（フレーム位置）の取得
                    frame_now = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
                    # 総フレーム数の取得
                    frame_all = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
                    frame_all = frame_max
                    # frame_now -= 2
                    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_now)
                    print('frame_now = ' + str(frame_now) + ' / ' + str(frame_all))
                    if frame_now < frame_max:
                        ret, frame = cap.read()
                        cv2.imshow(window_title, frame)
                    else:
                        print('frame_now >= frame_max')
                else:
                    if key_pushed != 255:
                        print('push key')
                        key_pushed = 255
                frame_now = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

                # 終わりまで来たら、
                if int(frame_now) >= int(frame_max):
                    if not is_pause:
                        # 終点で止める、再生中なら
                        is_pause = True
                        print('frame >= frame_max -> pause')
                    else:
                        pass
            else:
                #ret==False
                break
            ## end if (ret, frame = cap.read(),ret=False)
        ## end loop 

        cap.release()

        cv2.destroyAllWindows()
    except:
        import traceback
        print(traceback.print_exc())

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