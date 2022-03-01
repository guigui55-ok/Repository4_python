"""画像検索　matchtemplate"""
from typing import Any
import cv2
import numpy as np
from matplotlib import pyplot as plt

if not __name__ == '__main__':
    from common_utility.cv2_image.import_logger import log_info,log_error,LoggerUtility
    import common_utility.cv2_image
else:
    # __main__
    from import_logger import log_info,log_error,LoggerUtility

is_log_enable = True

def is_match_templage_from_some_file(
        logger:LoggerUtility,path_base,dir_path_temp,include_file_name ='',
        threshold = 0.8,result_file_path:str = ''
) -> bool:
    ret:bool = False
    from common_util.file_util.file_general import get_file_list
    list = get_file_list(logger,dir_path_temp,include_file_name)
    if len(list) > 0:
        for file in list:
            ret = is_match_template_from_file(
                logger,path_base,file,threshold,result_file_path
            )
            if ret: 
                return True
    else:
        return False

def get_template_file_list(logger:LoggerUtility,dir_path:str,include_str=''):
    try:
        import os
        files = os.listdir(dir_path)
        files_file = [f for f in files if os.path.isfile(os.path.join(dir_path, f))]
        path_list = []
        for file in files_file:
            path_list.append(os.path.join(dir_path,file))
        return path_list
    except Exception as e:
        log_error(e)
        return []

def get_template_file_names(file_list):
    try:
        import pathlib
        import os
        retlist = []
        if len(file_list)>0:
            for val in file_list:
                retlist.append(os.path.basename(val))
        return retlist
    except Exception as e:
        log_error(e)
        return []

def output_image_draw_point(
    logger:LoggerUtility,
    image_path:str,
    draw_point:'tuple(int,int)',
    radius:int=10,
    color:'tuple(int,int,int)'=None,
    output_file_path:str = '')-> str:
    """円を描画"""
    try:
        img = cv2.imread(image_path)
        if color == None:
            color = (0,0,255)
        cv2.circle(img, draw_point, radius, color, 
            thickness=2, lineType=cv2.LINE_8, shift=0)
        if output_file_path == '':
            write_path = './result_output_image_draw_point.png'
        else:
            write_path = output_file_path
        cv2.imwrite(write_path, img)
        return write_path
    except Exception as e:
        log_error(e)
        return ''

def get_image_from_path(logger,image_path,method=0):
    try:        
        # Input Image
        img  = cv2.imread(image_path,method)
        if len(img) <= 0:
            log_error('img is None')
        return img
    except Exception as e:
        log_error(e)
        return None

def get_result_false_is_match_template_from_file2():
    return dict(result=False,start_w=0,start_h=0,end_w=0,end_h=0)

def is_match_template_image_file_in_image(
    logger:LoggerUtility,
    base_image_object:Any,
    temp_image_path:str,
    read_method:int,
    method:int=cv2.TM_CCOEFF_NORMED,
    threshhold:float = 0.8,
    result_file_path:str = '') -> Any:
    """ 画像比較 match_templateを行う\n
    比較の元画像が image、マッチ検索する画像が file の場合\n
    戻り値:
    結果とマッチした座標を含むictを返す
    ex) match_rect = {'result':False,'start_w':0,'start_h':0,'end_w':0,'end_h':0}
    """
    match_rect = {'result':False,'start_w':0,'start_h':0,'end_w':0,'end_h':0}
    try:
        temp_image = get_image_from_path(logger,temp_image_path,read_method)
        ret = is_match_template_from_image(
            logger,base_image_object,temp_image,method,threshhold,result_file_path)
        return ret
    except Exception as e:
        log_error(e)
        return match_rect

def is_match_template_from_image(
    logger:LoggerUtility,
    base_image:Any,
    temp_image:Any,
    method:int=cv2.TM_CCOEFF_NORMED,
    threshold:float = 0.8,
    result_file_path:str = '') -> Any:
    """ 画像比較 match_templateを行う (match_template_main)\n
    比較の元画像が image、マッチ検索する画像が image の場合\n
    戻り値:
    比較結果と一致した範囲 dict {'result':bool,'start_w':int, 'start_h':int, 'end_w':int, 'end_h':int} を返す
    失敗時は dict(False,-1,-1,-1,-1) を返す
    """
    match_rect = {'result':False,'start_w':-1,'start_h':-1,'end_w':-1,'end_h':-1}

    is_success = False
    res = cv2.matchTemplate(base_image, temp_image, method)
    loc = np.where(res >= threshold)
    if len(loc[0]) > 0:
        is_success = True
    else:
        return match_rect
    ## is_match True
    tmp_ary = temp_image.shape
    h,w = (tmp_ary[0],tmp_ary[1])
    is_first = False
    match_point_sum = {'result':True,'w':0,'h':0}
    for_count = 0
    for pt in zip(*loc[::-1]):
        match_point_sum['w'] += pt[0] + w
        match_point_sum['h'] += pt[1] + h
        for_count += 1
        cv2.rectangle(base_image,pt,(pt[0]+w,pt[1] + h),(0,0,255),2)
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
        cv2.imwrite(result_file_path,img_temp)
        log_info('cv2.imwrite  path = ' + result_file_path)
        return match_rect
    return match_rect



def is_match_template_from_file2(
    logger:LoggerUtility,
    base_path:str,
    temp_dir_path:str,
    read_method:int=cv2.COLOR_BGR2GRAY,
    threshold:float = 0.8,
    method:int=cv2.TM_CCOEFF_NORMED,
    result_file_dir_path:str = '') -> Any:
    """base_path(image) に temp_dir_path のイメージのいずれかが存在するか判定する
        戻り値：
        dict:{'result':bool, 'start_w':int, 'start_h':int, 'end_w':int, 'endh':int}
        失敗時は以下の値を返す
        dict{'result':False, 'start_w':0, 'start_h':0, 'end_w':0, 'end_h':0}
    """
    import os
    print(os.path.abspath(base_path))
    if not os.path.exists(base_path):
        log_error('base_path not exists')
        return False
    # Input Image
    img  = cv2.imread(base_path,read_method)
    if len(img) <= 0:
        log_error('img is None')
        return False        
    temp_file_list = get_template_file_list(logger,temp_dir_path)
    # Read Images
    images = []
    for file_path in temp_file_list:
        images.append(cv2.imread(file_path,read_method))
    
    method = cv2.TM_CCOEFF_NORMED
    is_success = False
    # Template matching
    for i in range(len(images)):
        #####
        import os
        filepath = temp_file_list[i]
        basename_without_ext = os.path.splitext(os.path.basename(filepath))[0]
        ext = os.path.splitext(filepath)[1]
        file_name = basename_without_ext + str(i)  + ext
        save_path = os.path.join(result_file_dir_path,file_name)
        #####
        ret = is_match_template_from_image(
            logger,img,images[i],method,threshold,save_path)
        if ret['result']:
            return ret
    ## end for
    return ret


def is_match_template_from_file(
    logger:LoggerUtility,
    path_base:str,
    path_temp:str,
    read_method:int=cv2.COLOR_BGR2GRAY,
    temp_method:int=cv2.TM_CCORR_NORMED,
    threshold:float = 0.8,
    result_file_path:str = ''
) -> bool:
    img_base = cv2.imread(path_base,read_method)
    # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #img_temp = cv2.imread(path_temp,cv2.IMREAD_GRAYSCALE)
    img_temp = cv2.imread(path_temp,read_method)
    # w, h = img_temp.shape[::-1]
    w, h = img_temp.shape[:-1]
    res = cv2.matchTemplate(img_base,img_temp,temp_method)
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_base, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    if result_file_path != '':
        cv2.imwrite(result_file_path,img_base)

    if len(loc[0])<=0:
        log_info('match_template : result = False')
        return False
    log_info('match_template : result = True')
    return True

    


def get_result_by_match_template(
    logger:LoggerUtility,
    img_base:Any,
    img_temp:Any) -> bool:
    """
    """
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
        log_error(e)
        return -1
    
def is_match_template(
    logger:LoggerUtility,
    gray_img_base:Any,
    gray_img_temp:Any,
    threshold:float,
    result_file_path:str = '') -> bool:
    # img_gray = cv2.cvtColor(img_base, cv2.CV_32FC1.COLOR_BGR2GRAY)
    # img_gray = gray_img_base
    # print('img_temp.shape='+str(img_temp.shape))
    
    # img_temp_gray = cv2.cvtColor(img_temp, cv2.CV_32FC1.COLOR_BGR2GRAY)
    # w, h = gray_img_temp.shape[::-1]
    w, h = gray_img_temp.shape[:-1]

    result= cv2.matchTemplate(gray_img_base,gray_img_temp,cv2.TM_CCOEFF_NORMED)
    
    loc = np.where( result >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(gray_img_base, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
    if result_file_path != '':
        cv2.imwrite(result_file_path,gray_img_base)

    if len(loc[0])<=0:
        log_info('match_template : result = False')
        return False
    log_info('match_template : result = True')
    return True


# リサイズしながら画像がテンプレートと一致した結果を取得する
# Get the result that the image matches the template while resizing
def get_result_match_template_while_resizing(
    logger:LoggerUtility,
    img_base:Any,
    img_temp:Any,
    ratio_step:float,
    ratio_max:float,
    ratio_min:float
    ):
    try:
        import common_utility.cv2_image.cv2_image_util as cv2_image_util
        temp_image_obj = cv2_image_util.Cv2Image(img_temp)
        temp_image_obj.resize_keep_raito(ratio_max)
        # このサイズになるまで縮小リサイズし続ける
        end_width = temp_image_obj.width() * ratio_min
        # このサイズから検索開始
        start_width = temp_image_obj.width()
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
        log_error(e)
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
