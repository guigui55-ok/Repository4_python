
import traceback

from cv2 import RETR_FLOODFILL, startWindowThread, trace
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
def test3():
    try: 
        print('-----------------------------')
        logger = import_init.initialize_logger_new()
        base_path , temp_path ,image_dir = get_paths()
        base_image_obj = cv2_image_util.cv2_image(logger,base_path)
        temp_image_obj = cv2_image_util.cv2_image(logger,temp_path)
        ret = cv2_find_image.get_result_match_template_while_resizing(
            logger,
            base_image_obj.img,
            temp_image_obj.img,
            0.9,
            2,0.2
        )
        ret_obj = cv2_find_image.MatchTemplateResult(ret)
        print('ret_obj')
        ret_obj.print_result()
        return
    except:
        traceback.print_exc()


# main()
test3()