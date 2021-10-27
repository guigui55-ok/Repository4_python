import cv2
import numpy as np


# image を読み込む
im_base = cv2.imread('image/power_off_screen.png')
print(im_base.shape)
# (225, 400, 3) height,width,color(3)

print(im_base.dtype)
# uint8

# image を書き込む
#cv2.imwrite('image/power_on_screen2.png', im) 

# image を読み込む
im_chk = cv2.imread('image/target_screenshot.png')

print(np.array_equal(im_base, im_chk))
# True