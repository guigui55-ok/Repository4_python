
"""
# https://note.nkmk.me/python-opencv-draw-function/
# 矢印を描画: cv2.arrowedLine()
# 円を描画: cv2.circle()
楕円を描画: cv2.ellipse()
円弧を描画: cv2.ellipse()
マーカーを描画: cv2.drawMarker()
折れ線、多角形を描画: cv2.polylines(), cv2.fillPoly(), fillConvexPoly()
文字列（テキスト）を描画: cv2.putText()

https://qiita.com/mo256man/items/82da5138eeacc420499d
https://qiita.com/mo256man/items/f07bffcf1cfedf0e42e0

"""


import cv2
import numpy as np
from draw_test1 import Cv2Const, ColorRGB

# グレーの背景を作成
img = np.full((210, 425, 3), 128, dtype=np.uint8)

begin_point = (190, 35)
cv2.circle(
    img, begin_point, 15,
    ColorRGB.GRAY, thickness=Cv2Const.FILLED)
begin_point = (240, 35)
cv2.circle(
    img, begin_point, 20,
    ColorRGB.WHITE, thickness=Cv2Const.MID, lineType=Cv2Const.LINE_AA)

cv2.drawMarker(img, (300, 20), (255, 0, 0))
cv2.drawMarker(img, (337, 20), (0, 255, 0), markerType=cv2.MARKER_TILTED_CROSS, markerSize=15)
cv2.drawMarker(img, (375, 20), (0, 0, 255), markerType=cv2.MARKER_STAR, markerSize=10)

cv2.drawMarker(img, (300, 50), (0, 255, 255), markerType=cv2.MARKER_DIAMOND)
cv2.drawMarker(img, (337, 50), (255, 0, 255), markerType=cv2.MARKER_SQUARE, markerSize=15)
cv2.drawMarker(img, (375, 50), (255, 255, 0), markerType=cv2.MARKER_TRIANGLE_UP, markerSize=10)



from pathlib import Path
file_name = 'opencv_draw_argument2.png'
path = str(Path(__file__).parent.joinpath(file_name))
cv2.imwrite(path, img)

print('cv2描画テスト2')
print('path = ')
print(path)
