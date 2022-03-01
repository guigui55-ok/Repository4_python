

import import_init
import traceback

debug_mode = True

def excute_sample():
    try:
        import test_com
        import common_utility.cv2_image.cv2_find_image as cv2_find
        import common_utility.cv2_image.cv2_image_util as cv2_util
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
        cl_base_img = cv2_util.Cv2Image(img_base_path)
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


        # ###
        # ret_file_name = 'ret-03-output_image_draw_point.jpg'
        # ret_file_path = test_com.pathjoin(img_dir_path,ret_file_name)
        # draw_point = (200,200)
        # radius = 20
        # color = (0,255,0)
        # ret = cv2_find.output_image_draw_point(
        #     None,img_base_path,draw_point,radius,color,ret_file_path)
        # print('output_image_draw_point , ret = ' + str(ret))

        # ###
        # read_method = cv2.COLOR_BGR2GRAY
        # cl_base_img_gray = cv2_util.Cv2Image(img_base_path,read_method)
        # threshold = 0.8
        # ret_file_name = 'ret-04-is_match_template_image_file_in_image.jpg'
        # ret_file_path = test_com.pathjoin(img_dir_path,ret_file_name)
        # temp_method = cv2.TM_CCORR_NORMED
        # ret = cv2_find.is_match_template_image_file_in_image(
        #     None, cl_base_img_gray.img ,img_temp_path, read_method, temp_method, threshold,ret_file_path)
        # print('is_match_template_image_file_in_image , ret = ' + str(ret))

        # ###
        # temp_method = cv2.TM_CCORR_NORMED
        # threshold = 0.8
        # ret_file_name = 'ret-05-is_match_template_from_image.jpg'
        # ret_file_path = test_com.pathjoin(img_dir_path,ret_file_name)
        # ret = cv2_find.is_match_template_from_image(
        #     None, cl_base_img_gray.img, cl_temp_img_gray.img, temp_method, threshold, ret_file_path)
        # print('is_match_template_from_image , ret = ' + str(ret))

        # ###
        # threshold = 0.8
        # temp_method = cv2.TM_CCORR_NORMED
        # ret_file_name = 'ret-06-is_match_template_from_file2.jpg'
        # ret_file_path = test_com.pathjoin(img_dir_path,ret_file_name)
        # ret = cv2_find.is_match_template_from_file2(
        #     None, img_base_path, img_dir_path, read_method, threshold, temp_method, ret_file_path)
        # print('is_match_template_from_file2 , ret = ' + str(ret))

        # ###
        # threshold = 0.8
        # temp_method = cv2.TM_CCORR_NORMED
        # ret_file_name = 'ret-07-is_match_template_from_file.jpg'
        # ret_file_path = test_com.pathjoin(img_dir_path,ret_file_name)
        # ret = cv2_find.is_match_template_from_file(
        #     None,img_base_path, img_temp_path, read_method, temp_method ,threshold, ret_file_path)
        # print('is_match_template_from_file , ret = ' + str(ret))


        # ###
        # threshold = 0.8
        # ret_file_name = 'ret-08-is_match_template.jpg'
        # ret_file_path = test_com.pathjoin(img_dir_path,ret_file_name)
        # ret = cv2_find.is_match_template(
        #     None, cl_base_img_gray.img, cl_temp_img_gray.img, threshold, ret_file_path)
        # print('is_match_template , ret = ' + str(ret))

        # ###
        # ret = cv2_find.get_result_match_template_while_resizing(
        #     None, cl_base_img.img, cl_temp_img_gray.img, 0.1, 2, 0.5
        # )
        # print('get_result_match_template_while_resizing , ret = ' + str(ret))

        return
    except:
        traceback.print_exc()


if __name__ == '__main__':
    excute_sample()