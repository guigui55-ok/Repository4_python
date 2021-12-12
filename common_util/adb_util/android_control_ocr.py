
from ocr_util.ocr_tesseract_util.ocr_tesseract_class import OcrConst


if __name__ == '__main__':
    import adb_common
    from  device_info import DeviceInfo
    from android_const import Constants
    from android_control_adb import AndroidControlAdb
    from common_util.ocr_util.ocr_tesseract_util import ocr_tesseract_class
else:
    # 外部から参照時は、common_util を sys.path へ追加しておくこと
    from common_util.adb_util import adb_common
    from common_util.adb_util.device_info import DeviceInfo
    from common_util.adb_util.android_const import Constants
    from common_util.adb_util.android_control_adb import AndroidControlAdb
    import common_util.ocr_util.ocr_tesseract_util.ocr_tesseract_class as ocr_class
    import common_util.ocr_util.ocr_tesseract_util.ocr_tesseract_method as ocr_method

class AndroidControlOcr():
    logger = None
    constants : Constants
    image_dir = None
    device_info : DeviceInfo
    control_adb : AndroidControlAdb

    ocr_pc_dir : str = './'
    ocr_file_name : str = 'screenshot_for_ocr.png'
    ocr_result_file_name : str = 'ocr_result.png'
    ocr_lang = 'jpn'
    def __init__(
        self,
        logger,
        control_adb :AndroidControlAdb,
        image_dir : str
    ) -> None:
        self.logger = logger
        self.device_info = control_adb.device_info
        self.image_dir = image_dir
        self.control_adb = control_adb
        self.constants = Constants
    def initialize(self):
        self.logger.info(Constants.main.NOT_IMPLEMENTED.value)
    
    def tap_by_ocr(self,keyword,target_index=0):
        rect = []
        try:
            rect = self.get_rect_by_ocr(keyword,target_index)
            if len(rect)<1:
                self.logger.exp.error('len(rect)<1 , return')
                return False
            flag = self.control_adb.tap_center(rect)
            return flag
        except Exception as e:
            self.logger.exp.error(e)
            return True

    def get_rect_by_ocr(self,keyword,target_index=0):
        ret_rect=[]
        try:
            # get screenshot
            img_dir = self.ocr_pc_dir
            screenshot_file_name = self.ocr_file_name
            flag = self.control_adb.get_screenshot(
                img_dir,screenshot_file_name)
            if not flag:
                self.logger.exp.error('save screenshot failed , return')
                return ret_rect
            # set path
            img_path = img_dir + screenshot_file_name
            result_path = img_dir + self.ocr_result_file_name
            lang = self.ocr_lang
            # excute OCR
            rect_list = self.get_rect_list_by_excute_ocr_with_path(
                img_path,keyword,result_path,lang)            
            # process result
            if len(rect_list) < 1:
                self.logger.exp.error('ocr not match , retry lang=jpn+eng')
                rect_list = self.get_rect_list_by_excute_ocr_with_path(
                    self.logger,img_path,keyword,result_path,lang='jpn+eng')
                if len(rect_list) < 1:
                    self.logger.exp.error('ocr not match , return')
                    return ret_rect
            return rect_list[target_index]
        except Exception as e:
            self.logger.exp.error(e)
            return ret_rect
    
    def get_rect_list_by_excute_ocr_with_path(self,img_path,keyword,result_path,lang='jpn'):
        try:
            out_path = result_path
            if lang =='' :lang = 'jpn'
            ocr_direction_is_horizon = True
            # keyword = '自動的にON'
            # keyword = 'バッテリーセーバー'
            
            rect_list = self.excute_ocr_main(
                self.logger,img_path,out_path,keyword,
                lang,ocr_direction_is_horizon)
            
            for i in range(len(rect_list)):
                self.logger.info(rect_list[i])
            return rect_list
        except Exception as e:
            self.logger.exp.error(e)
            return []
    
    def excute_ocr_main(self,img_path,output_path,keyword,lang,ocr_direction_is_horizon):
        try:        
            ocr_obj = ocr_tesseract_class.tesseract(self.logger,img_path,output_path)
            ocr_obj.lang = lang
            flag = ocr_obj.excute(keyword,img_path,output_path,ocr_direction_is_horizon,ocr_obj.lang)
            if not flag:
                self.logger.exp.error('ocr_obj.excute Failed')
            return ocr_obj.rect_list
        except Exception as e:
            self.logger.exp.error(e)
            return []