# https://pystyle.info/opencv-template-matching/
# 類似度が最も高い場所を探す

import cv2
import numpy
from IPython.display import Image, display,display_png
import os


import os
rmpath = './res.png'
if os.path.exists(rmpath):
    os.remove(rmpath)

import pathlib
path = './'
pathobj = pathlib.Path(path)
print(pathobj.resolve())

def match_temp_main(img_base,img_temp)->bool:
    try:
        # テンプレートマッチングを行う。
        result = cv2.matchTemplate(img_base, img_temp, cv2.TM_CCOEFF_NORMED)

        print('result.shape='+ str(result.shape))
        print('len(result)='+ str(len(result)))
        # w, h = img_temp.shape[::-1]
        threshold = 0.8
        loc = numpy.where( result >= threshold)
        print('loc = ' + str(loc))
        print('len(loc) = ' + str(len(loc)))
        print('len(loc[0]) = ' + str(len(loc[0])))
        print('len(loc[1]) = ' + str(len(loc[1])))
        w, h = img_temp.shape[:-1]
        if len(loc[0]) < 1:
            print('matchTemplate : False')
            return False,img_base,img_temp
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_base, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        return True,img_base,img_temp
    except:
        import traceback
        print(traceback.print_exc())
        return False,img_base,img_temp

def resize_img(img,raito):
    try:
        th , tw = img.shape[:-1]
        img = cv2.resize(img,(int(tw*raito),int(th*raito)))
        return img
    except:
        import traceback
        print(traceback.print_exc())
        return None

import image_grid

def match_temp(img_base,img_temp,retry)->bool:
    try:
        if True:
            img_base = resize_img(img_base,1)
            img_grid = image_grid.ImageGrid(img_base)
            img_grid.set_img_part_cut_in_grid_pattern(2,2)
            # # 切り取り
            # # img_base = img_base[int(tw/2):int(tw),int(th/2):int(th)]
            # img_base = img_base[int(th/2):int(th),0:tw]
            
        th , tw = img_base.shape[:-1]
        print('img_base.shape = ' + str(tw) + ',' + str(th))
        for i in range(retry):
            raito = 1.5
            if i==0 : raito = 1
            img_temp = resize_img(img_temp,raito)
            th , tw = img_temp.shape[:-1]
            print('img_temp.shape = ' + str(tw) + ',' + str(th))
            flag,img_base,img_temp = match_temp_main(img_base,img_temp)
            if flag:
                print('match_temp_main = True , break')
                break

        return flag,img_base,img_temp
    except:
        import traceback
        print(traceback.print_exc())
        return False,img_base,img_temp


def main():
    path_base = 'image/power_on_screen2.png'
    path_temp = 'image/template_comp_sample.png'
    path_temp = 'image/key_mark3.png'
    path_temp = 'image/key_mark2.png'

    # path_base = 'image/pad_kyu_yami_hikari_kon_kyu_dam.png'
    # path_temp = 'image/pad_icon_kon.png'
    # path_base = 'image/pad_icon_kon.png'
    # display(path_base)
    print('path_base = ' + path_base)
    print('path_temp = ' + path_temp)
    # 入力画像、テンプレート画像を読み込む。
    img_base = cv2.imread(path_base)  # 入力画像
    img_temp = cv2.imread(path_temp)  # テンプレート画像
    
    flag ,img_base, img_temp = match_temp(img_base,img_temp,10)

    cv2.imwrite('./res.png',img_base)
    cv2.imwrite('./res_temp.png',img_temp)
    print('./res.png')
    print('./res_temp.png')

main()
# # 最も類似度が高い位置を取得する。
# minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
# print(f"max value: {maxVal}, position: {maxLoc}")
# # max value: 0.9999998211860657, position: (392, 124)

# # 描画する。
# tl = maxLoc[0], maxLoc[1]
# br = maxLoc[0] + img_temp.shape[1], maxLoc[1] + img_temp.shape[0]

# dst = img_base.copy()
# cv2.rectangle(dst, tl, br, color=(0, 255, 0), thickness=2)