import cv2
import numpy as np
from matplotlib import pyplot as plt

import pathlib,os
img_dir = str(pathlib.Path(__file__).parent.parent)
img_dir = os.path.join(img_dir,'image/pickup_test')
image_file_name = 'pickup_sample.png'
image_file_name = 'screenshot_home_white'
ext = '.png'
img_path = os.path.join(img_dir,image_file_name+ext)
print(img_path)

img = cv2.imread(img_path,0)
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()