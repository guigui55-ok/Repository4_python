
from log_util import logger_init
from ocr_util.ocr_tesseract_util  import ocr_tesseract_class
from ocr_util.ocr_tesseract_util  import ocr_tesseract_method

def initialize():
    try :
        logger = logger_init.initialize_logger()
        return logger
    except Exception as e:
        print(e)

def main():
    try:
        logger = initialize()
        dir_path = r'C:\Users\OK\source\repos\Repository4_python\ocr_test\images'
        file_name = 'screen_sever.png'
        img_path = dir_path + '\\' + file_name
        out_path = dir_path + '\\' + 'ret_' + file_name
        lang = 'jpn'
        ocr_direction_is_horizon = True
        # tools : pyocr.TOOLS
        tools = ocr_tesseract_method.get_tools_by_initialize_tresseract(logger)
        ocr_results = ocr_tesseract_method.excute_ocr(logger,tools,img_path,out_path,lang,ocr_direction_is_horizon)

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