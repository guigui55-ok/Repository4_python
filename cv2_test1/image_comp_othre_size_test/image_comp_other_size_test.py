
import traceback

from cv2 import startWindowThread, trace
import import_init

def get_paths():
    try:
        import pathlib,os
        dir_path = str(pathlib.Path(__file__).parent.parent)
        image_path = os.path.join(dir_path,'image','image_comp_othre_size')
        file_base = 'comp_target_ok.png'
        file_comp = 'button_ok_base.png'
        file_comp = 'button_ok_2.png'
        base_path = os.path.join(image_path,file_base)
        temp_path = os.path.join(image_path,file_comp)
        if not os.path.exists(base_path):
            print('not exists : ' + base_path)
        if not os.path.exists(temp_path):
            print('not exists : ' + temp_path)
        return base_path,temp_path,image_path
    except:
        traceback.print_exc()

import common_util.cv2_image.cv2_image_comp as cv2_image_comp
import common_util.cv2_image.cv2_find_image as cv2_find_image
def main():
    try: 
        print('-----------------------------')
        logger = import_init.initialize_logger_new()
        base_path , temp_path ,image_dir = get_paths()
        ret = cv2_find_image.is_match_template_from_file2(
            logger,base_path,temp_path,0.8,image_dir)
        print('flag = ' + str(ret['result']))
        return
    except:
        traceback.print_exc()

def get_result(cv2_result,property_name):
    try:
        if property_name == 'max':
            return cv2_result.max.real
        elif property_name == 'min':
            return cv2_result.min.real
        return 0
    except:
        traceback.print_exc()
        return -1
import cv2
import common_util.cv2_image.cv2_image_util as cv2_image_util
def test2():
    try: 
        print('-----------------------------')
        logger = import_init.initialize_logger_new()
        base_path , temp_path ,image_dir = get_paths()
        base_image_obj = cv2_image_util.cv2_image(logger,base_path)
        temp_image_obj = cv2_image_util.cv2_image(logger,temp_path)
        start_width = temp_image_obj.width()
        print('start_width = ' + str(start_width))
        count = 0
        # 1/3まで実施する
        while( float(temp_image_obj.width()) > (start_width/3)):
            ret = cv2_find_image.get_result_by_match_template(
                logger,base_image_obj.img, temp_image_obj.img)
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(ret)
            print('width = {} , count = {} , minVal = {} , maxVal = {} , minLoc = {} , maxLoc = {}'.
                format(temp_image_obj.width(),count, minVal, maxVal, minLoc, maxLoc) )
            # 0.9倍
            temp_image_obj.resize_keep_raito(0.9)
            count += 1

        return
    except:
        traceback.print_exc()


# main()
test2()