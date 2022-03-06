

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
        flag = cl_base_img.set_image(cl_temp_img.img)
        print('set_image , flag = ' + str(flag))
        
        flag = cl_base_img.is_image_none()
        print('is_image_none , flag = ' + str(flag))

        w = cl_base_img.width()
        h = cl_base_img.height()
        print('width height  = {} , {}'.format(w,h))
        ratio = 1.5
        #flag = cl_base_img.resize( w*ratio , h*ratio)
        """    self.img = cv2.resize(self.img,dsize=(width,height))
cv2.error: OpenCV(4.5.4-dev) :-1: error: (-5:Bad argument) in function 'resize'
> Overload resolution failed:
>  - Can't parse 'dsize'. Sequence item with index 0 has a wrong type
        """
        flag = cl_base_img.resize( int(w*ratio) , int(h*ratio*ratio))
        print('resize , flag = ' + str(flag))

        path = cl_base_img.save_img_with_name_auto()
        print('save_img_with_name_auto , ret = ' + str(path))

        cl_buf_img = cv2_util.Cv2Image(path)
        flag = cl_buf_img.is_big_self_image(cl_temp_img.img)
        print('is_big_self_image , flag = ' + str(flag))
        flag = cl_temp_img.is_big_self_image(cl_buf_img.img)
        print('is_big_self_image , flag = ' + str(flag))

        return
    except:
        traceback.print_exc()


if __name__ == '__main__':
    excute_sample()