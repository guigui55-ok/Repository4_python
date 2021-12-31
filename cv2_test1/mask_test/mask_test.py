import traceback
import import_init

import cv2 as cv
import numpy as np

from common_util.file_util.file_class import MyFile
def ger_file_obj():
    # MyFile Object
    mf = MyFile(__file__)
    # mf.move_child_dir('image','image_mask')
    mf.move_to_parent_until_match('cv2_test1') # 遡って設定
    mf.move_dir_from_self('cut_sample','images_1') # 上記から辿って設定
    file_name = 'buttle2_64_0_0.png'
    mf.set_file_name(file_name) # ファイル名を設定
    return mf
    
def mask_test():
    try:
        mf :MyFile= ger_file_obj()
        #画像データの読み込み
        img = cv.imread(mf.path)
        mf.print_path()

        #BGR色空間からHSV色空間への変換
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        #色検出しきい値の設定
        lower = np.array([90,64,0])
        upper = np.array([150,255,255])
        
        #色検出しきい値範囲内の色を抽出するマスクを作成
        frame_mask = cv.inRange(hsv, lower, upper)

        #論理演算で色検出
        dst = cv.bitwise_and(img, img, mask=frame_mask)

        cv.imshow("img", dst)

        if cv.waitKey(0) & 0xFF == ord('q'):
            cv.destroyAllWindows()
    except:
        traceback.print_exc()

mask_test()