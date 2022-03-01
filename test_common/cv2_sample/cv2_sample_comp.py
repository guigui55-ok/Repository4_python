

import import_init
import traceback

debug_mode = True

def excute_sample():
    try:
        import test_com
        import common_utility.cv2_image.cv2_image_comp as cv2_comp
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

        # ###
        # ret_file_name = 'ret-02-is_match_templage_from_some_file.jpg'
        # ret_file_path = test_com.pathjoin(img_dir_path,ret_file_name)
        # flag = cv2_find.is_match_templage_from_some_file(
        #     None,img_base_path,img_dir_path,img_temp_name,threshold,ret_file_path)
        # print('is_match_templage_from_some_file , flag = ' + str(flag))
        flag = cv2_comp.is_same_image_from_path(
            None,img_base_path,img_temp_path)
        print('is_same_image_from_path , flag = ' + str(flag))

        flag = cv2_comp.is_same_image(
            None, cl_base_img.img, cl_temp_img.img
        )
        print('is_same_image , flag = ' + str(flag))

        ret = cv2_comp.get_compareist_value(
            None, cl_base_img.img, cl_temp_img.img
        )
        print('get_compareist_value , flag = ' + str(ret))

        threshold = 0.8
        flag = cv2_comp.is_same_by_calcHist(
            None, cl_base_img.img, cl_temp_img.img, threshold
        )
        print('is_same_by_calcHist , flag = ' + str(flag))

        return
    except:
        traceback.print_exc()


if __name__ == '__main__':
    excute_sample()