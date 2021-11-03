# https://pystyle.info/opencv-template-matching/
# 類似度が最も高い場所を探す

import cv2
from IPython.display import Image, display,display_png
import os

def imshow(img,path):
    """ndarray 配列をインラインで Notebook 上に表示する。
    """
    name , ext = os.path.splitext(path)
    print('imshow path.splittext=' + ext[1])
    #ret, encoded = cv2.imencode(os.path.splitext(path), img)
    ret, encoded = cv2.imencode(ext, img)
    #ret, encoded = cv2.imencode(img)
    # display(img)
    if ext == '.png':
        display_png(img)
    else:
        display(Image(encoded))


path_base = 'image/power_on_screen2.png'
path_temp = 'image/key_mark3.png'
path_temp = 'image/key_mark2.png'
# display(path_base)

# 入力画像、テンプレート画像を読み込む。
img_base = cv2.imread(path_base)  # 入力画像
img_temp = cv2.imread(path_temp)  # テンプレート画像

# テンプレートマッチングを行う。
result = cv2.matchTemplate(img_base, img_temp, cv2.TM_CCOEFF_NORMED)

print(result.shape,'./_.png')
#imshow(result,'_.png')
imshow(result,path_base)


# 最も類似度が高い位置を取得する。
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
print(f"max value: {maxVal}, position: {maxLoc}")
# max value: 0.9999998211860657, position: (392, 124)

# 描画する。
tl = maxLoc[0], maxLoc[1]
br = maxLoc[0] + img_temp.shape[1], maxLoc[1] + img_temp.shape[0]

dst = img_base.copy()
cv2.rectangle(dst, tl, br, color=(0, 255, 0), thickness=2)
imshow(dst,path_base)