"""画像検索　matchtemplate"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

def is_match_templage_from_some_file(
        logger,path_base,dir_path_temp,include_file_name ='',
        threshold = 0.8,result_file_path:str = ''
) -> bool:
    try:
        ret:bool = False
        from file_util.file_general import get_file_list
        list = get_file_list(logger,dir_path_temp,include_file_name)
        if list.count > 0:
            for file in list:
                ret = is_match_template_from_file(
                    logger,path_base,file,threshold,result_file_path
                )
                if ret: 
                    return True
        else:
            return False
    except Exception as e:
        logger.exp.error(e)
        return False

def is_match_template_from_file(logger,path_base,path_temp,
        threshold = 0.8,result_file_path:str = ''
) -> bool:
    try:

        img_rgb = cv2.imread(path_base)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        #img_temp = cv2.imread(path_temp,cv2.IMREAD_GRAYSCALE)
        img_temp = cv2.imread(path_temp,0)
        w, h = img_temp.shape[::-1]

        similarity2 = cv2.TM_CCORR_NORMED 
        res = cv2.matchTemplate(img_gray,img_temp,cv2.TM_CCOEFF_NORMED)
        # threshold = 0.8
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_gray, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

        if result_file_path != '':
            cv2.imwrite(result_file_path,img_rgb)

        if len(loc[0])<=0:
            logger.info('match_template : result = False')
            return False
        logger.info('match_template : result = True')
        return True
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.exp.error(e)
        return False

def is_match_template(logger,img_base,img_temp,threshold,
        result_file_path:str = '') -> bool:
    try:
        img_gray = cv2.cvtColor(img_base, cv2.CV_32FC1.COLOR_BGR2GRAY)
        img_gray = img_base
        # print('img_temp.shape='+str(img_temp.shape))
        
        img_temp_gray = cv2.cvtColor(img_temp, cv2.CV_32FC1.COLOR_BGR2GRAY)
        w, h = img_temp_gray.shape[::-1]

        result= cv2.matchTemplate(img_gray,img_temp_gray,cv2.TM_CCOEFF_NORMED)
        
        loc = np.where( result >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_base, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        
        if result_file_path != '':
            cv2.imwrite(result_file_path,img_base)

        if len(loc[0])<=0:
            logger.info('match_template : result = False')
            return False
        logger.info('match_template : result = True')
        return True
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.exp.error(e)
        return False

class match_template():
    logger = None
    img_base = ''
    img_temp = ''
    img_rgb = None
    threshold = 0.8
    img_result = None
    def __init__(self,logger) -> None:
        self.logger = logger

    def is_match_template_self(self,result_file_path:str = '') -> bool:
        return self.is_match_template(
            self.img_base,
            self.img_temp,
            result_file_path
        )

    def is_match_template(self,img_base,img_temp,
            result_file_path:str = '') -> bool:
        return is_match_template(
            self.logger,
            img_base,
            img_temp,
            0.8,
            result_file_path
        )
