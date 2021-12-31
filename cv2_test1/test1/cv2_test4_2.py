"""画像検索　matchtemplate2"""
import cv2
import numpy as np

# import sys
# sys.path.append(r'C:\Users\OK\AppData\Roaming\Python\Python37\site-packages')

from matplotlib import pyplot as plt


read_path = 'image/power_on_screen.png'
temp_path = 'image/key_mark2.png'

img_rgb = cv2.imread(read_path)

similarity = cv2.TM_CCOEFF_NORMED #NG
similarity = cv2.COLOR_BAYER_RG2RGBA #NG
similarity = cv2.COLOR_BGR2YCR_CB #NG
similarity = cv2.COLOR_YUV2RGB #NG
similarity = cv2.COLOR_BGR2GRAY
img_gray = cv2.cvtColor(img_rgb, similarity)
template = cv2.imread(temp_path,0)
w, h = template.shape[::-1]

similarity2 = cv2.TM_CCOEFF_NORMED
similarity2 = cv2.TM_SQDIFF_NORMED 
similarity2 = cv2.TM_CCORR 
#similarity2 = cv2.TM_CCORR_NORMED 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('res.png',img_rgb)
print('./res.png')
print('success')