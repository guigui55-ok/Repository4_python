
import cv2
import sys

logger = None

def image_to_gray(img,threshold=100):
    """img : cv2.imread で得られたオブジェクト
       threshold : 二値化に用いる閾値"""
    try:
        logger.info(__file__ + '.' + sys._getframe().f_code.co_name)
        # 二値化(閾値100を超えた画素を255にする。)
        ret, img_cnv = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
        return ret,img_cnv
    except Exception as e:
        logger.exp.error(e)
        return None