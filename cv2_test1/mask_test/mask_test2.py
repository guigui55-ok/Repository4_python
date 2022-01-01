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
    
from common_util.cv2_image.cv2_result import Cv2Result
def mask_test():
    try:
        mf :MyFile= ger_file_obj()
        #画像データの読み込み
        img = cv.imread(mf.path)
        mf.print_path()

        #BGR色空間からHSV色空間への変換
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        #色検出しきい値の設定
        # lower = np.array([90,64,0])
        # upper = np.array([150,255,255])
        
        # #元画像と同じ
        # lower = np.array([0,0,0])
        # upper = np.array([255,255,255])
    
        # lower = np.array([255,255,255])
        # upper = np.array([255,255,255])# 真っ黒
        # lower = np.array([0,0,0])
        # upper = np.array([0,0,0])# 真っ黒

        lower,upper = [np.array([36,25,25]),np.array([70,255,255])]
        lower,upper = [np.array([110,150,50]),np.array([120,255,255])] # blue
        lower,upper = [np.array([90,64,0]),np.array([120,255,255])]
        lower,upper = [np.array([127,127,127]),np.array([255,255,255])]
        print('lower {}, upeer {}'.format(lower,upper))
        #色検出しきい値範囲内の色を抽出するマスクを作成
        frame_mask = cv.inRange(hsv, lower, upper)

        #論理演算で色検出
        dst = cv.bitwise_and(img, img, mask=frame_mask)

        print(dst.shape[0])
        print(dst.shape[1])
        print(dst.shape[2])
        print(dst.size)
        print(len(dst))
        ret = Cv2Result(dst)
        ret.print_result()

        print('excute imshow')
        cv.imshow("img", dst)

        if cv.waitKey(0) & 0xFF == ord('q'):
            cv.destroyAllWindows()
    except:
        traceback.print_exc()

mask_test()