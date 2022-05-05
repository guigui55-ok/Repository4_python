from typing import Any
import cv2
import numpy as np
import os


from common_utility.cv2_image.import_logger import log_info,log_error,LoggerUtility

def is_same_image_from_path(
    logger:LoggerUtility,
    path_base:str,
    path_check:str) -> bool:
    """イメージを比較し、完全一致か判定する(np.array_equal)"""
    if not (os.path.exists(path_base)):
        log_error('path_base not exists')
        log_error('path = '+ path_base)
        return False
    if not (os.path.exists(path_check)):
        log_error('path_check not exists')
        log_error('path = '+ path_check)
        return False
    
    # image を読み込む
    im_base = cv2.imread(path_base)
    # image を読み込む
    im_chk = cv2.imread(path_check)
    # 比較する
    flag = np.array_equal(im_base, im_chk)
    return flag


def is_same_image(logger,img_a:Any,img_b:Any) -> bool:
    """イメージを比較し、完全一致か判定する(np.array_equal)"""
    # 比較する
    flag = np.array_equal(img_a, img_b)
    return flag

def get_compareist_value(logger,img_a,img_b)->float:
    img_a_hist = cv2.calcHist([img_a], [0], None, [256], [0, 256])
    img_b_hist = cv2.calcHist([img_b], [0], None, [256], [0, 256])
    ret = cv2.compareHist(img_a_hist, img_b_hist, 0)
    return ret

def is_same_by_calcHist(logger:LoggerUtility, img_a:Any, img_b:Any, threshold:float):
    """画像を比較してしきい値以上か判定する"""
    val = get_compareist_value(logger,img_a,img_b)
    if threshold <= val:
        log_info('is_same_by_calcHist:True , '+str(threshold) + ' <= ' + str(val))
        return True
    else:
        log_info('is_same_by_calcHist:False , '+str(threshold) + ' <= ' + str(val))
        return False

def is_same_by_calcHist_(img_a:Any, img_b:Any, threshold:float):
    """画像を比較してしきい値以上か判定する"""
    val = get_compareist_value(None,img_a,img_b)
    if threshold <= val:
        return True
    else:
        return False