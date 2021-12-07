import cv2
import numpy as np
import os

from numpy.lib.type_check import imag
def is_same_image_from_path(logger,path_base:str,path_check:str) -> bool:
    """イメージを比較し、完全一致か判定する(np.array_equal)"""
    try:
        logger.info(__file__ + ':is_same_image')
        # check if path exists
        if not (os.path.exists(path_base)):
            logger.exp.error('path_base not exists')
            logger.exp.error('path = '+ path_base)
            return False
        if not (os.path.exists(path_check)):
            logger.exp.error('path_check not exists')
            logger.exp.error('path = '+ path_check)
            return False
        
        # image を読み込む
        im_base = cv2.imread(path_base)
        # image を読み込む
        im_chk = cv2.imread(path_check)
        # 比較する
        flag = np.array_equal(im_base, im_chk)
        # logger.info('is_same_image_from_path = ' + str(flag))
        return flag
    except Exception as e:
        logger.exp.error(e)
        return False


def is_same_image(logger,img_a:str,img_b:str) -> bool:
    """イメージを比較し、完全一致か判定する(np.array_equal)"""
    try:
        # 比較する
        flag = np.array_equal(img_a, img_b)
        return flag
    except Exception as e:
        logger.exp.error(e)
        return False

def get_compareist_value(logger,img_a,img_b)->float:
    try:
        img_a_hist = cv2.calcHist([img_a], [0], None, [256], [0, 256])
        img_b_hist = cv2.calcHist([img_b], [0], None, [256], [0, 256])
        ret = cv2.compareHist(img_a_hist, img_b_hist, 0)
        return ret
    except Exception as e:
        logger.exp.error(e)
        return -1

def is_same_by_calcHist(logger,img_a,img_b,threshold):
    val = get_compareist_value(logger,img_a,img_b)
    if threshold <= val:
        logger.info('is_same_by_calcHist:True , '+str(threshold) + ' <= ' + str(val))
        return True
    else:
        print('is_same_by_calcHist:False , '+str(threshold) + ' <= ' + str(val))
        return False
