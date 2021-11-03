import cv2
import numpy as np
import os

def is_same_image(logger,path_base:str,path_check:str) -> bool:
    try:
        logger.info(__file__ + ':is_same_image')
        # check if path exists
        if not (os.path.exists(path_base)):
            logger.error('path_base not exists')
            logger.error('path = '+ path_base)
            return False
        if not (os.path.exists(path_check)):
            logger.error('path_check not exists')
            logger.error('path = '+ path_check)
            return False
        
        # image を読み込む
        im_base = cv2.imread(path_base)
        # image を読み込む
        im_chk = cv2.imread(path_check)
        # 比較する
        logger.info(np.array_equal(im_base, im_chk))
        return True
    except Exception as e:
        logger.ext.error(e)
        return False