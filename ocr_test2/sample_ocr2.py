import import_init

from common_util.log_util import logger_init
from common_util.ocr_util.ocr_tesseract_util  import ocr_tesseract_class
from common_util.ocr_util.ocr_tesseract_util  import ocr_tesseract_method
from common_util.adb_util.adb_common import logger as adb_logger

def initialize():
    try :
        logger = logger_init.initialize_logger()
        return logger
    except Exception as e:
        print(e)

def main():
    logger = initialize()
    try:
        adb_logger = logger
        img_dir = './'
        screenshot_file_name = 'sceenshot_comp.png'
        flag = save_screenshot(logger,img_dir,screenshot_file_name)
        if not flag:
            logger.exp.error('save screenshot failed , return')
            return
        img_path = img_dir + screenshot_file_name
        result_path = img_dir + 'ocr_result.png'
        keyword = 'ニュース'
        rect = excute_ocr_with_path(logger,img_path,keyword,result_path)
        if len(rect) < 1:
            logger.exp.error('ocr not match , retry lang=jpn+eng')
            rect = excute_ocr_with_path(
                logger,img_path,keyword,result_path,lang='jpn+eng')
            if len(rect) < 1:
                logger.exp.error('ocr not match , return')
                return

        import common_util.adb_util.adb_common as adb_common
        flag = adb_common.tap_center(rect)
        if flag:
            logger.info('tap success')
        else:
            logger.exp.error('tap failed')
        
    except Exception as e:
        logger.exp.error(e)

def save_screenshot(logger,img_dir,screenshot_file_name):
    try:
        from common_util.adb_util.android_common import AndroidCommon
        android = AndroidCommon(logger,img_dir)
        from common_util.adb_util.android_const import Constants
        save_android_path = Constants.main.SD_ROOT_DIR.value
        android.control.get_screenshot(img_dir,save_android_path,screenshot_file_name)
        return True
    except Exception as e:
        logger.exp.error(e)
        return False

def excute_ocr_with_path(logger,img_path,keyword,result_path,lang='jpn'):
    try:
    #     dir_path = r'C:\Users\OK\source\repos\Repository4_python\ocr_test\images'
    #     dir_path = img_path
    #     file_name = 'screen_sever.png'
    #     img_path = dir_path + '\\' + file_name
    #     out_path = dir_path + '\\' + 'ocr_ret_' + file_name
        out_path = result_path
        if lang =='' :lang = 'jpn'
        ocr_direction_is_horizon = True
        # keyword = '自動的にON'
        # keyword = 'バッテリーセーバー'
        
        rect_list = excute_ocr_main(
            logger,img_path,out_path,keyword,
            lang,ocr_direction_is_horizon)
        
        for i in range(len(rect_list)):
            print('rect_list ' + str(i) + ' = ' + str(id(rect_list[i])))
            print(rect_list[i])
        return rect_list[0]
    except Exception as e:
        logger.exp.error(e)
        return []

def excute_ocr_main(logger,img_path,output_path,keyword,lang,ocr_direction_is_horizon):
    try:        
        ocr_obj = ocr_tesseract_class.tesseract(logger,img_path,output_path)
        ocr_obj.lang = lang
        flag = ocr_obj.excute(keyword,img_path,output_path,ocr_direction_is_horizon,ocr_obj.lang)
        if not flag:
            logger.exp.error('ocr_obj.excute Failed')
        return ocr_obj.rect_list
    except Exception as e:
        logger.exp.error(e)
        return []

def sub():
    try:
        logger = initialize()
        dir_path = r'C:\Users\OK\source\repos\Repository4_python\ocr_test\images'
        file_name = 'screen_sever.png'
        img_path = dir_path + '\\' + file_name
        out_path = dir_path + '\\' + 'ret_' + file_name
        lang = 'jpn+eng'
        ocr_direction_is_horizon = True
        # tools : pyocr.TOOLS
        tools = ocr_tesseract_method.get_tools_by_initialize_tresseract(logger)
        ocr_results = ocr_tesseract_method.excute_ocr(
            logger,tools,img_path,out_path,lang,ocr_direction_is_horizon)

        keyword = '自動的にON'
        keyword = 'バッテリーセーバー'
        # list(OcrBoxes)
        ocr_boxes = ocr_tesseract_method.get_rect_list_match_keyword_in_ocr_result(
            logger,keyword,ocr_results,False,1.0)
        rect_list = ocr_tesseract_method.get_rect_from_ocr_result_boxes_list(
            logger,ocr_boxes)
        flag = ocr_tesseract_method.write_result_image_for_ocr(
            logger,img_path,rect_list)
        
        print('rect_list : ')
        for i in range(len(rect_list)):
            print('rect_list ' + str(i) + ' = ' + str(id(rect_list[i])))
            print(rect_list[i])
    except Exception as e:
        logger.exp.error(e)    

main()