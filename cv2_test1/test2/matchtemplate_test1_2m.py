# https://pystyle.info/opencv-template-matching/

import cv2
import numpy as np
from matplotlib import pyplot as plt



def main():
    path_base = 'image/power_on_screen2.png'
    path_temp = 'image/key_mark2.png'
    path_temp = 'image/template_comp_sample.png'
    path_temp = 'image/key_mark3.png'
    # 入力画像、テンプレート画像を読み込む。
    img_base = cv2.imread(path_base)  # 入力画像
    img_temp = cv2.imread(path_temp)  # テンプレート画像
    ret = match_template(img_base,img_temp)
    print('ret=' + str(ret))
    print('len(ret)=' + str(len(ret)))

def match_template(img_base,img_temp):
    try:
        # テンプレートマッチングを行う。
        result = cv2.matchTemplate(
            img_base, img_temp, cv2.TM_CCOEFF_NORMED
        )
        return result
    except:
        import traceback
        traceback.print_exc()
        return None

if __name__ == '__main__':
    main()


