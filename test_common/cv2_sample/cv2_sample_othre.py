

import import_init
import traceback

debug_mode = True

import common_utility.log_util.logger_init
from common_utility.log_util.logger_init import intialize_logger_util,initialize_logger,initialize_logger_with_args

def excute_sample():
    try:
        import test_com
        import common_utility.cv2_image.cv2_image_util as cv2_util
        from common_utility.cv2_image.cv2_image_util import Cv2Image
        import cv2

        img_dir_path = test_com.get_path(__file__,'cv2_data')
        img_base_name = 'opencv-match-base01.jpg'
        img_base_path = test_com.pathjoin(img_dir_path,img_base_name)
        img_temp_name = 'opencv-match-base01.jpg'
        img_temp_path = test_com.pathjoin(img_dir_path,img_temp_name)
        threshold = 0.8
        ret_file_name = 'result_match_ret01.jpg'
        ret_file_path = test_com.pathjoin(img_dir_path,ret_file_name)
        #########
        read_method = cv2.COLOR_BGR2GRAY
        cl_base_img_gray = cv2_util.Cv2Image(img_base_path,read_method)
        cl_temp_img_gray = cv2_util.Cv2Image(img_temp_path,read_method)
        cl_base_img = cv2_util.Cv2Image(img_base_path)
        cl_temp_img = cv2_util.Cv2Image(img_temp_path)
        #########
        flag = test_com.is_exists_file(img_base_path)
        print('is_exists_file , flag = ' + str(flag))
        flag = test_com.is_exists_file(img_temp_path)
        print('is_exists_file , flag = ' + str(flag))

        import common_utility.cv2_image.cv2_method as cv2_method
        # ###
        ret_file_name = 'ret-301-create_png.jpg'
        ret_file_path = test_com.pathjoin(img_dir_path,ret_file_name)
        width = 300
        height = 400
        color = (100,100,0)
        flag = cv2_method.create_png(
            ret_file_path,width,height,color)
        print('create_png , flag = ' + str(flag))
        print('    path = ' + ret_file_path)

        import common_utility.cv2_image.cv2_image_cnv as cv2_cnv
        
        ret_file_name = 'ret-401-create_png.jpg'
        ret_file_path = test_com.pathjoin(img_dir_path,ret_file_name)
        threshold = 100
        


        return
    except:
        traceback.print_exc()


if __name__ == '__main__':
    excute_sample()