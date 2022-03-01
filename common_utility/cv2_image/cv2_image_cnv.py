
import cv2
import sys

from common_utility.cv2_image.import_logger import log_info,log_error,LoggerUtility

def image_to_gray(img,threshold=100):
    """取得してイメージを2値化する
    img : cv2.imread で得られたオブジェクト
       threshold : 二値化に用いる閾値"""
    log_info(__file__ + '.' + sys._getframe().f_code.co_name)
    # 二値化(閾値100を超えた画素を255にする。)
    ret, img_cnv = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return ret,img_cnv