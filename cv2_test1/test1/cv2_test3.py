import cv2
import numpy as np
import cv2_image_io
import os

# def rename_with_add_str(arg_path:str,add_str : str ='_') -> str:
#     try:
#         ret = os.path.dirname(arg_path)
#         ret += '\\' + os.path.basename(arg_path)
#         ret += add_str
#         ext = os.path.splitext(arg_path)
#         return ret + ext[1]
#     except Exception as e:
#         print(e)
#         return arg_path

import logger_init
logger = logger_init.initialize_logger()

path1 = 'image/power_off_screen.png'
path2 = 'image/power_on_screen_changed_size_500_1000.png'
path2_resize = ''

# image を読み込む
cimg1 = cv2_image_io.cv2_image(logger,path1)
print('img.shape='+ str(cimg1.img.shape))
# (225, 400, 3) height,width,color(3)

# image を読み込む
cimg2 = cv2_image_io.cv2_image(logger,path2)
print('img.shape='+ str(cimg2.img.shape))

# resize
# 小さいほうに合わせる
if cimg1.is_bif_self_image(cimg2.img):
    cimg1.resize_by_image(cimg2.img)
else:
    cimg2.resize_by_image(cimg1.img)

# 画像を保存する
# rename
import path_util
path_util.logger = logger
path1_new = path_util.rename_with_add_str(cimg1.path,'_2')
path2_new = path_util.rename_with_add_str(cimg2.path,'_2')
cimg1.save_img(path1_new)
cimg2.save_img(path2_new)

#　画像を比較する
print('np.array_equal(cimg1.img, cimg2.img)')
print(np.array_equal(cimg1.img, cimg2.img))
# True
