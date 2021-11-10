# -*- coding: utf-8 -*-
import cv2
import numpy as np

def matchtemplate_test6():
    base_path = 'image/power_on_screen.png'
    temp_path = 'image/key_mark3.png'
    temp_path = 'image/key_mark2.png'
    temp_path = 'image/key_mark4.png'
    write_path = 'image/matchtemplate_test5_result.png'
    print(base_path)
    print(temp_path)
    # 入力画像とテンプレート画像をで取得
    img = cv2.imread(base_path)
    temp = cv2.imread(temp_path)

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    temp = cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)

    # テンプレート画像の高さ・幅
    h, w = temp.shape

    # テンプレートマッチング（OpenCVで実装）
    match = cv2.matchTemplate(gray, temp, cv2.TM_CCOEFF_NORMED)
    min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)
    pt = max_pt

    # テンプレートマッチングの結果を出力
    cv2.rectangle(img, (pt[0], pt[1]), (pt[0] + w, pt[1] + h), (0, 0, 200), 3)
    cv2.imwrite(write_path, img)
    print('result= '+ write_path)

if __name__ == '__main__':
    matchtemplate_test6()