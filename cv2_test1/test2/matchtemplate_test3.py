import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

import os
rmpath = './res.png'
if os.path.exists(rmpath):
    os.remove(rmpath)

import pathlib
path = './'
pathobj = pathlib.Path(path)
print(pathobj.resolve())

try:
    path_base = 'image/power_on_screen2.png'
    path_temp = 'image/key_mark3.png'
    path_temp = 'image/key_mark2.png'

    print('plt.isinteractive:' + str(plt.isinteractive()))

    img_rgb = cv.imread(path_base)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread(path_temp,0)
    w, h = template.shape[::-1]

    #plt.show(img_rgb,plt.ion)

    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)

    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
    cv.imwrite('./res.png',img_rgb)
    print('./res.png')
except:
    import traceback
    traceback.print_exc()
