"""画像検索　matchtemplate"""
from typing import Any
import cv2
import numpy as np
from matplotlib import pyplot as plt

def is_match_templage_from_some_file(
        logger,path_base,dir_path_temp,include_file_name ='',
        threshold = 0.8,result_file_path:str = ''
) -> bool:
    try:
        ret:bool = False
        from common_util.file_util.file_general import get_file_list
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

def output_image_draw_point(logger,image_path,draw_point,color=None,output_file_path = '')-> str:
    try:
        img = cv2.imread(image_path)
        if color == None:
            color = (0,0,255)
        cv2.circle(img, draw_point, 10, color, 
            thickness=2, lineType=cv2.LINE_8, shift=0)
        if output_file_path == '':
            write_path = './result_output_image_draw_point.png'
        cv2.imwrite(write_path, img)
        return write_path
    except Exception as e:
        logger.exp.error(e)
        return ''

def get_image_from_path(logger,image_path,method=0):
    try:        
        # Input Image
        img  = cv2.imread(image_path,method)
        if len(img) <= 0:
            logger.exp.error('img is None')
        return img
    except Exception as e:
        logger.exp.error(e)
        return None

def get_result_false_is_match_template_from_file2():
    return dict(result=False,start_w=0,start_h=0,end_w=0,end_h=0)

def is_match_template_image_file_in_image(
    logger,base_image_object,temp_image_path,method=None,threshhold = 0.8,result_file_path:str = '') -> Any:
    """ 画像比較 match_templateを行う\n
    比較の元画像が image、マッチ検索する画像が file の場合"""
    match_rect = {'result':False,'start_w':0,'start_h':0,'end_w':0,'end_h':0}
    try:
        temp_image = get_image_from_path(logger,temp_image_path,0)
        if method == None:
            method = cv2.TM_CCOEFF_NORMED
        ret = is_match_template_from_image(
            logger,base_image_object,temp_image,method,threshhold,result_file_path)
        return ret
    except Exception as e:
        logger.exp.error(e)
        return match_rect

def is_match_template_from_image(
    logger,base_image,temp_image,method=None,threshold = 0.8,result_file_path:str = '') -> Any:
    """ 画像比較 match_templateを行う (match_template_main)\n
    比較の元画像が image、マッチ検索する画像が image の場合
    戻り値は、比較結果と一致した範囲 tuple(bool, int, int, int) を返す
    失敗時は tuple(False,-1,-1,-1,-1) を返す
    """
    
    match_rect = {'result':False,'start_w':-1,'start_h':-1,'end_w':-1,'end_h':-1}
    try:
        if method == None:
            method = cv2.TM_CCOEFF_NORMED

        is_success = False
        res = cv2.matchTemplate(base_image, temp_image, method)

        loc = np.where(res >= threshold)
        #print('loc[::1] = ' + str(loc[::1]))
        if len(loc[0]) > 0:
            is_success = True
        else:
            return match_rect
        ## is_match True
        tmp_ary = temp_image.shape
        h,w = (tmp_ary[0],tmp_ary[1])
        #print(h,w)
        is_first = False
        # match_point_sum = {'w':0,'h':0}
        # match_point_sum = dict(result=True,w=0,h=0)
        match_point_sum = {'result':True,'w':0,'h':0}
        for_count = 0
        for pt in zip(*loc[::-1]):
            # print('pt[0] + w , pt[1] + h = ' + str(pt[0] + w) + ' , ' + str(pt[1] + h) )
            match_point_sum['w'] += pt[0] + w
            match_point_sum['h'] += pt[1] + h
            for_count += 1
            cv2.rectangle(base_image,pt,(pt[0]+w,pt[1] + h),(0,0,255),2)
        ### end for - pt in loc
        # match_point_avg = dict(result=True,w=0,h=0)
        match_point_avg = {'result':True,'w':0,'h':0}
        match_point_avg['w'] = int(match_point_sum['w'] / for_count)
        match_point_avg['h'] = int(match_point_sum['h'] / for_count)
        
        # calc point for return
        match_rect = {'result':True,'start_w':0,'start_h':0,'end_w':0,'end_h':0}
        match_rect['end_w'] = match_point_avg['w']
        match_rect['end_h'] = match_point_avg['h']
        match_rect['start_w'] = match_point_avg['w'] - temp_image.shape[1]
        match_rect['start_h'] = match_point_avg['h'] - temp_image.shape[0]
        img_temp = base_image
        
        if is_success:
            if result_file_path=='':
                import os
                result_file_path = os.path.join(result_file_path,'match_template_result.png')
                # result_file_path = './match_template_result.png'
            cv2.imwrite(result_file_path,img_temp)
            logger.info('cv2.imwrite  path = ' + result_file_path)
            return match_rect
        return match_rect
    except Exception as e:
        logger.exp.error(e)
        return match_rect



def is_match_template_from_file2(logger,base_path,temp_path,
        threshold = 0.8,result_file_dir_path:str = '') -> Any:
    """base_path に temp_path が存在するか判定する
        戻り値：
        tuple:[result:bool, start_w:int, start_h:int, end_w:int, endh:int ]
        失敗時は以下の値を返す
        dict(result=False,start_w=0,start_h=0,end_w=0,end_h=0)
    """
    try:
        #base_path = 'image/pad07_login.png'
        #temp_path = 'image/button_login_ok.png'
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
            import os
            file_name = TempValnames[i] + str(i)  + '.png'
            save_path = os.path.join(result_file_dir_path,file_name)
            ret = is_match_template_from_image(
                logger,img,images[i],method,threshold,save_path)
            if ret['result']:
                return ret
        ## end for
        return ret
    except Exception as e:
        logger.exp.error(e)
        return get_result_false_is_match_template_from_file2()


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

    


def get_result_by_match_template(logger,img_base,img_temp) -> bool:
    try:
        ################
        img_gray = cv2.cvtColor(img_base, cv2.COLOR_BGR2GRAY)
        img_gray = img_base
        # print('img_temp.shape='+str(img_temp.shape))
        
        img_temp_gray = cv2.cvtColor(img_temp, cv2.COLOR_BGR2GRAY)
        # w, h = img_temp_gray.shape[::-1]
        ################
        img_gray = img_base
        img_temp_gray = img_temp

        result= cv2.matchTemplate(img_gray,img_temp_gray,cv2.TM_CCOEFF_NORMED)
        
        return result
    except Exception as e:
        logger.exp.error(e)
        return -1      
    
def is_match_template(logger,img_base,img_temp,threshold,
        result_file_path:str = '') -> bool:
    try:
        img_gray = cv2.cvtColor(img_base, cv2.CV_32FC1.COLOR_BGR2GRAY)
        img_gray = img_base
        # print('img_temp.shape='+str(img_temp.shape))
        
        img_temp_gray = cv2.cvtColor(img_temp, cv2.CV_32FC1.COLOR_BGR2GRAY)
        w, h = img_temp.shape[::-1]

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


# リサイズしながら画像がテンプレートと一致した結果を取得する
# Get the result that the image matches the template while resizing
def get_result_match_template_while_resizing(
    logger,
    img_base,img_temp,ratio_step,ratio_max,ratio_min
    ):
    try:
        import common_util.cv2_image.cv2_image_util as cv2_image_util
        temp_image_obj = cv2_image_util.cv2_image(logger,img_temp)
        temp_image_obj.resize_keep_raito(ratio_max)
        # このサイズになるまで縮小リサイズし続ける
        end_width = temp_image_obj.width() * ratio_min
        # このサイズから検索開始
        start_width = temp_image_obj.width()
        # デバッグ用出力
        # print('start_width = ' + str(start_width))
        # print('end_width = ' + str(end_width))
        count = 0
        # 比較開始
        ret_list = []
        while( float(temp_image_obj.width()) > float(end_width)):
            ret = get_result_by_match_template(
                logger,img_base, temp_image_obj.img)
            ret_list.append(ret)
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(ret)
            # デバッグ用
            # print('width = {} , count = {} , minVal = {} , maxVal = {} , minLoc = {} , maxLoc = {}'.
            #     format(temp_image_obj.width(),count, minVal, maxVal, minLoc, maxLoc) )
            # リサイズする
            temp_image_obj.resize_keep_raito(ratio_step)
            count += 1
        
        max_index:int = 0
        now_val:float = 0
        for i in range(len(ret_list)):
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(ret_list[i])
            if now_val < maxVal:
                now_val = maxVal
                max_index = i
        max_ret = ret_list[max_index]
        return max_ret
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.exp.error(e)
        return -1,-1,(0,0),(0,0)



from common_util.cv2_image.cv2_result import Cv2Result
class MatchTemplateResult(Cv2Result):
    pass

class MatchTemplate():
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
