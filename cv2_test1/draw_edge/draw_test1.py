
# https://note.nkmk.me/python-opencv-draw-function/

import cv2
import numpy as np

print(cv2.__version__)
# 3.3.0

# グレーの背景を作成
img = np.full((210, 425, 3), 128, dtype=np.uint8)

# 描画座標、計算用関数
def get_end_point(begin_point , width, height):
    return (begin_point[0] + width,  begin_point[1] + height)
_WIDTH, _HEIGHT = 75, 50

_BLUE = (255, 0, 0)
_LIGHT_GREEN = (0, 255, 0)
_RED = (0, 0, 255)
_LIGHT_BLUE = (255, 255, 0)
_GRAY = (255, 255, 255)
_WHITE = (0, 0, 0)

class ColorRGB():
    BLUE = (255, 0, 0)
    LIGHT_GREEN = (0, 255, 0)
    RED = (0, 0, 255)
    LIGHT_BLUE = (255, 255, 0)
    GRAY = (255, 255, 255)
    WHITE = (0, 0, 0)

class Cv2Const():
    """
    https://www.codevace.com/vscode-py-rectangle/
        線の種類	説明
        * cv2.FILLED	塗りつぶし
        * cv2.LINE_4	4 連結
        * cv2.LINE_8	8 連結（デフォルト）
        * cv2.LINE_AA	アンチエイリアス処理された線
    """
    FILLED = cv2.FILLED # 塗りつぶし
    LINE_4 = cv2.LINE_4 # int(4)
    LINE_8 = cv2.LINE_8 # int(8)
    LINE_AA = cv2.LINE_AA # int(16)
    THIN = 1
    MID = 4
    BOLD = 8
    THICKNESS_BOLD = 8



###左上
#外枠のみ
begin_point = (50, 10)
end_point = get_end_point(begin_point, _WIDTH, _HEIGHT)
cv2.rectangle(img, begin_point, end_point, _BLUE)

###左中段
#塗りつぶし thickness=-1
begin_point = (50, 80)
end_point = get_end_point(begin_point, _WIDTH, _HEIGHT)
cv2.rectangle(img, begin_point, end_point, _RED, thickness=Cv2Const.FILLED)

###左下
# 外枠と内枠塗りつぶし（別の色）
begin_point = (50, 150)
end_point = get_end_point(begin_point, _WIDTH, _HEIGHT)
cv2.rectangle(img, begin_point, end_point, _LIGHT_BLUE, thickness=Cv2Const.FILLED)

begin_point = (50, 150)
end_point = get_end_point(begin_point, _WIDTH, _HEIGHT)
cv2.rectangle(img, begin_point, end_point, _LIGHT_GREEN)


###真ん中上
begin_point = (175, 10)
end_point = get_end_point(begin_point, _WIDTH, _HEIGHT)
# 外枠線太め
cv2.rectangle(
    img, begin_point, end_point, _GRAY,
    thickness=Cv2Const.BOLD, lineType=Cv2Const.LINE_4)
# 線を引く
cv2.line(
    img, begin_point, end_point, _WHITE,
    thickness=Cv2Const.THIN, lineType=Cv2Const.LINE_4)
###真ん中中段
begin_point = (175, 80)
end_point = get_end_point(begin_point, _WIDTH, _HEIGHT)
cv2.rectangle(
    img, begin_point, end_point, _LIGHT_GREEN,
    thickness=Cv2Const.MID, lineType=Cv2Const.LINE_8)
cv2.line(
    img, begin_point, end_point, _WHITE,
    thickness=Cv2Const.MID, lineType=Cv2Const.LINE_8)
###真ん中下
begin_point = (175, 150)
end_point = get_end_point(begin_point, _WIDTH, _HEIGHT)
cv2.rectangle(
    img, begin_point, end_point, _GRAY,
    thickness=Cv2Const.MID, lineType=Cv2Const.LINE_AA)
cv2.line(
    img, begin_point, end_point, _WHITE,
    thickness=Cv2Const.THIN, lineType=Cv2Const.LINE_AA)

"""引数のshiftを設定すると、pt1とpt2の座標に対して(2^shift)で割った値の座標で描画されます。
以下に示す図は一番上がshift=2、真ん中がshift=1、一番下がshift指定なし（shift=0）の描画の結果です。
"""
###m右側上段
begin_point = (600, 20)
w, h = 150, 100
end_point = get_end_point(begin_point, w, h)
cv2.rectangle(
    img, begin_point, end_point, _WHITE,
    lineType=Cv2Const.LINE_AA, shift=1)
###m右側中段
begin_point = (601, 160)
end_point = get_end_point(begin_point, w, h)
cv2.rectangle(
    img, begin_point, end_point, _RED,
    lineType=Cv2Const.LINE_AA, shift=1)
###m右側下段
begin_point = (602, 300)
end_point = get_end_point(begin_point, w, h)
cv2.rectangle(
    img, begin_point, end_point, _WHITE,
    lineType=Cv2Const.LINE_AA, shift=1)

from pathlib import Path
file_name = 'opencv_draw_argument.png'
path = str(Path(__file__).parent.joinpath(file_name))
cv2.imwrite(path, img)

print('cv2描画テスト')
print('path = ')
print(path)
