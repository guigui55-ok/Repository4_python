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

def get_template_file_list(logger,dir_path,include_str=''):
    try:
        filenames = [dir_path]
        return filenames
    except Exception as e:
        logger.exp.error(e)
        return []
def get_template_file_names(logger,file_list):
    try:
        import pathlib
        import os
        retlist = []
        if len(file_list)>0:
            for val in file_list:
                retlist.append(os.path.basename(val))
        return retlist
    except Exception as e:
        logger.exp.error(e)
        return []


def is_match_template_from_file2(logger,base_path,temp_path,
        threshold = 0.8,result_file_dir_path:str = '') -> bool:
    try:
        #base_path = 'image/pad07_login.png'
        temp_path = 'image/button_login_ok.png'
        # import pathlib
        # p = pathlib.path('./')
        # print('root dir = '+ str(p.resolve()) )
        import os
        print(os.path.abspath(base_path))
        if not os.path.exists(base_path):
            logger.exp.error('base_path not exists')
            return False

        # Input Image
        img  = cv2.imread(base_path,0)
        if len(img) <= 0:
            logger.exp.error('img is None')
            return False
        
        # Template Image
        TempValname = []
        TempFilenames = get_template_file_list(logger,temp_path)
        
        # for i in range(max_count):            
        #     TempValname.append('Template'+str(i))
        TempValnames = get_template_file_names(logger,TempFilenames)
        max_count = len(TempValnames)
        images = []
        for i in range(max_count):
            # Image read
            images.append(cv2.imread(TempFilenames[i],0))
            #print(len(images[i]))

        
        method = cv2.TM_CCOEFF_NORMED
        is_success = False
        # Template matching
        for i in range(max_count):

            res = cv2.matchTemplate(img, images[i], method)

            loc = np.where(res >= threshold)
            #print('loc[::1] = ' + str(loc[::1]))
            if len(loc[0]) > 0:
                is_success = True
            else:
                continue
            ## is_match True
            h,w = images[i].shape
            #print(h,w)
            is_first = False
            # match_point_sum = {'w':0,'h':0}
            # match_point_sum = dict(result=True,w=0,h=0)
            match_point_sum = {'result':True,'w':0,'h':0}
            for_count = 0
            for pt in zip(*loc[::-1]):
                match_point_sum['w'] += pt[0] + w
                match_point_sum['h'] += pt[1] + h
                for_count += 1
                cv2.rectangle(img,pt,(pt[0]+w,pt[1] + h),(0,0,255),2)
            # match_point_avg = dict(result=True,w=0,h=0)
            match_point_avg = {'result':True,'w':0,'h':0}
            match_point_avg['w'] = int(match_point_sum['w'] / for_count)
            match_point_avg['h'] = int(match_point_sum['h'] / for_count)
            
            # calc point for return
            match_rect = {'result':True,'start_w':0,'start_h':0,'end_w':0,'end_h':0}
            match_rect['start_w'] = match_point_avg['w']
            match_rect['start_h'] = match_point_avg['h']
            match_rect['end_w'] = match_point_avg['w'] + images[i].shape[0]
            match_rect['end_h'] = match_point_avg['h'] + images[i].shape[1]
            img_temp = img

            if False:
                w, h = images[i].shape[::-1]   # Template image size
                print(w,h)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                print(str(i) + ' -> max_val: ' + str('{:.3f}'.format(max_val)), ',  max_loc: ' + str(max_loc))
        
                # Result image
                top_left = max_loc
                btm_right = (top_left[0]+w, top_left[1]+h)
                img_temp = img.copy()
                cv2.rectangle(img_temp, top_left, btm_right, 0, 2)
            ## end if
            
            if is_success:
                file_name = result_file_dir_path + str(i) +'_' + TempValnames[i] + '.png'
                cv2.imwrite(file_name,img_temp)
                logger.info(file_name)
                return match_rect
        ## end for
        return dict(result=False,start_w=0,start_h=0,end_w=0,end_h=0)
    except Exception as e:
        logger.exp.error(e)
        return dict(result=False,start_w=0,start_h=0,end_w=0,end_h=0)


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
        # import traceback
        # traceback.print_exc()
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
