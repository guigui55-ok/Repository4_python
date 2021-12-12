import cv2
import numpy as np

import pathlib
img_dir = str(pathlib.Path(__file__).parent)
file_name = 'create_test.png'
import os
path = os.path.join(img_dir,file_name)

# http://pineplanter.moo.jp/non-it-salaryman/2019/03/24/post-7337/
#ブランク画像
height = 100
width = 200
blank = np.zeros((height, width, 3))
 
cv2.imwrite(path,blank)
print(path)