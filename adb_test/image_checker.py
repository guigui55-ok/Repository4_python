"""
外部pathからutilを使用する
"""
import sys,os
from pathlib import Path
package_name = 'common_util'
import_path = str(Path('__file__').resolve().parent.parent)+'\\' + package_name
print('import_path:'+import_path)
import_path = os.path.join('..', package_name)
print('import_path:'+import_path)
sys.path.append(import_path)
import cv2_image.cv2_image_util as image_util
import path_util
import numpy as np

def is_same_image(logger,img1_path,img2_path,is_write=True):    
    try:
        path1 = img1_path
        path2 = img2_path
        path2_resize = ''

        # image を読み込む
        cimg1 = image_util.cv2_image(logger,path1)
        print('img.shape='+ str(cimg1.img.shape))
        # (225, 400, 3) height,width,color(3)

        # image を読み込む
        cimg2 = image_util.cv2_image(logger,path2)
        print('img.shape='+ str(cimg2.img.shape))

        # resize
        # 小さいほうに合わせる
        if cimg1.is_bif_self_image(cimg2.img):
            cimg1.resize_by_image(cimg2.img)
        else:
            cimg2.resize_by_image(cimg1.img)

        if is_write:
            # 画像を保存する
            # rename
            path_util.logger = logger
            path1_new = path_util.rename_with_add_str(cimg1.path,'_2')
            path2_new = path_util.rename_with_add_str(cimg2.path,'_2')
            cimg1.save_img(path1_new)
            cimg2.save_img(path2_new)        

        #　画像を比較する
        print('np.array_equal(cimg1.img, cimg2.img)')
        print(np.array_equal(cimg1.img, cimg2.img))
    except Exception as e:
        logger.exp.error(e)