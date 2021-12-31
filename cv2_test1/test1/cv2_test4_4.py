
# def image_to_gray(path:str):
#     # 閾値の設定
#     threshold = 100
#     # 二値化(閾値100を超えた画素を255にする。)
#     ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

import sys
import numpy as np
import logger_init    
import cv2_image_cnv
import cv2_image_io
import cv2_find_image_util

def main():
    logger = logger_init.initialize_logger()
    logger.info('*** ' + __file__)
    logger.info(sys._getframe().f_code.co_name)
    try:
        # set image path 
        read_path = 'image/power_on_screen.png'
        temp_path = 'image/key_mark2.png'
        temp_path = 'image/key_mark3.png'
        # 画像の読み込み
        img_base = cv2_image_io.cv2_image(logger,read_path)
        img_temp =  cv2_image_io.cv2_image(logger,temp_path)
        # 二値化(閾値100を超えた画素を255にする。)
        cv2_image_cnv.logger = logger
        # ret,img_base.img = cv2_image_cnv.image_to_gray(img_base.img)
        # ret,img_temp.img = cv2_image_cnv.image_to_gray(img_temp.img)
        
        # 画像を検索する
        match_template = cv2_find_image_util.match_template(logger)
        match_template.img_base = img_base.img
        match_template.img_temp = img_temp.img
        result_image_path = './ret.png'
        # is_match = match_template.is_match_template_self('./ret.png')
        is_match = cv2_find_image_util.is_match_template_from_file(
            logger,
            read_path,
            temp_path,
            0.8,
            result_image_path
        )
        logger.info('is_match = ' + str(is_match))
        logger.info('result_image_path = '+ result_image_path)
    except Exception as e:
        logger.exp.error(e)
    
if __name__ == '__main__':
    main()