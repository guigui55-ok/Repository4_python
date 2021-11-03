# https://pystyle.info/opencv-template-matching/

import cv2
import numpy as np
from IPython.display import Image, display
from matplotlib import pyplot as plt


def imshow(img):
    """ndarray 配列をインラインで Notebook 上に表示する。
    """
    ret, encoded = cv2.imencode(".jpg", img)
    display(Image(encoded))


path_base = 'image/power_on_screen2.png'
path_temp = 'image/key_mark3.png'
path_temp = 'image/key_mark2.png'

# 入力画像、テンプレート画像を読み込む。
img_base = cv2.imread(path_base)  # 入力画像
img_temp = cv2.imread(path_temp)  # テンプレート画像

# テンプレートマッチングを行う。
result = cv2.matchTemplate(img_base, img_temp, cv2.TM_CCOEFF_NORMED)

print(result.shape)

imshow(img_temp)