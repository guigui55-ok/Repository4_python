
import os
# import cv2
from PIL import Image
from cv2 import CAP_INTELPERC_IR_GENERATOR
from numpy import true_divide
import pyocr
import pyocr.builders

if __name__ == '__main__':
    import ocr_tesseract_method
else:
    from ocr_util.ocr_tesseract_util import ocr_tesseract_method

class tesseract():
    loggger = None
    tool:list = None
    read_path:str = ''
    ret_path:str = ''
    is_output_result_image:bool = True
    ocr_result:pyocr.builders.Box = None
    rect_list_match_keyword_in_ocr_result:list = []
    def __init__(self,logger,read_path='',ret_path='') -> None:
        try:
            self.logger = logger
            # 2.OCRエンジンの取得
            self.tools = ocr_tesseract_method.initialize_tresseract(logger)
            if read_path != '':
                self.set_path(read_path,ret_path)
        except Exception as e:
            logger.exp.error(e)

    def set_path(self,read_path,ret_path = '')->bool:
        """読み込みパスと結果出力パスを設定"""
        try:
            if not os.path.exists(read_path):
                self.logger.exp.error('path not exists. path= ' + read_path)
            self.read_path = read_path
            
            if ret_path == '':
                self.ret_path = str(os.path.splitext(read_path)[0]) + '_ret' + \
                    str(os.path.splitext(read_path)[1])
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def excute(self,lang)->bool:
        try:
            self.ocr_result = ocr_tesseract_method.excute_ocr(
                self.logger,self.tool,self.read_path,self.ret_path,lang,
                self.is_output_result_image)
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def find_str(self,find_value):
        ret_rect = (0,0,0,0)
        try:            
            return ret_rect
        except Exception as e:
            self.logger.exp.error(e)
            return ret_rect
    
    def is_match_keyword_in_ocr_result(self,keyword,ocr_result):
        try:
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def get_rect_list_match_keyword_in_ocr_result(self,keyword,ocr_result=None):
        try:
            if ocr_result == None:
                ocr_result = self.ocr_result
            self.rect_list_match_keyword_in_ocr_result = \
                ocr_tesseract_method.get_rect_list_match_keyword_in_ocr_result(
                    self.logger,keyword,self,ocr_result
                )
        except Exception as e:
            self.logger.exp.error(e)
            return []