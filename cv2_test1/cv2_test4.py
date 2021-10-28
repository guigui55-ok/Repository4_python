# https://thr3a.hatenablog.com/entry/20150727/1437973061

# xx Mac
# https://qiita.com/anzanshi/items/5ce80d3e5daa5b247d34 
# 
import sys
import cv2
import numpy

read_path = 'image/power_on_screen.png'
temp_path = 'image/key_mark2.png'

image = cv2.imread(read_path)
template = cv2.imread(temp_path)

th, tw = template.shape[:2]

result = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)
threshold = 0.99
loc = numpy.where(result >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + tw, pt[1] + th), 0, 2)
cv2.imwrite("reuslt.png", image)