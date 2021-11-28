
import os
# import cv2
from PIL import Image
from cv2 import CAP_INTELPERC_IR_GENERATOR
from numpy import true_divide
import pyocr
import pyocr.builders
import cv2

if __name__ == '__main__':
    import ocr_tesseract_method
else:
    from ocr_util.ocr_tesseract_util import ocr_tesseract_method

class OcrConst():
    DIRECTION_HORIZON = 11
    DIRECTION_VERTICAL = 12

class tesseract():
    loggger = None
    tool:list = None
    read_path:str = ''
    ret_path:str = ''
    lang:str = ''
    is_output_result_image:bool = True
    ocr_result:pyocr.builders.Box = None
    rect_list_match_keyword_in_ocr_result:list = []
    const = OcrConst()
    direction = OcrConst.DIRECTION_HORIZON
    direction_is_horizon = True
    threshold_for_judging_separation = 0.0
    rect_list = []
    def __init__(self,logger,read_path='',ret_path='') -> None:
        try:
            self.logger = logger
            # 2.OCRエンジンの取得
            self.tools = ocr_tesseract_method.get_tools_by_initialize_tresseract(logger)
            if read_path != '':
                self.set_path(read_path,ret_path)
            self.threshold_for_judging_separation = ocr_tesseract_method.const_ocr.DEFAULT_THRESHOLD
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
            else:
                self.ret_path = ret_path
        except Exception as e:
            self.logger.exp.error(e)
            return False
    
    def excute_main_ertical(self)->bool:
        try:
            lang='eng+jpn_vert', #ここを日本語縦書き認識用に変更しています。
            self.direction = self.const.DIRECTION_VERTICAL
            self.ocr_result = ocr_tesseract_method.excute_ocr(
                self.logger,self.tool,self.read_path,self.ret_path,lang,
                self.is_output_result_image)
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def excute(self,keyword,img_path='',out_img_path='',ocr_direction_is_horizon=True,lang='') -> bool:
        try:
            if img_path ==  '' : img_path = self.read_path
            if out_img_path == '' : out_img_path = self.ret_path
            out_path = out_img_path
            self.direction_is_horizon = ocr_direction_is_horizon
            if self.direction_is_horizon: self.direction = OcrConst.DIRECTION_HORIZON
            else: self.direction = OcrConst.DIRECTION_VERTICAL
            if lang == '' : self.lang ='jpn+eng'
            # tools : pyocr.TOOLS
            # OCR を実行する
            tools = ocr_tesseract_method.get_tools_by_initialize_tresseract(self.logger)
            ocr_results = ocr_tesseract_method.excute_ocr(
                self.logger,
                tools,
                img_path,
                out_path,
                self.lang,
                ocr_direction_is_horizon)
            # OCR により得られた ocrbox を切り取る
            ocr_boxes = ocr_tesseract_method.get_rect_list_match_keyword_in_ocr_result(
                self.logger,keyword,ocr_results,False,1.0)
            # キーワードと一致したOcrBoxが改行などで分離しているか判定して
            # 離れ具合が閾値以上の物は省く
            # 閾値以下の範囲を取得する
            rect_list = ocr_tesseract_method.get_rect_from_ocr_result_boxes_list(
                self.logger,ocr_boxes)
            # 得られた結果を画像へ出力する
            flag = ocr_tesseract_method.write_result_image_for_ocr(
                self.logger,img_path,rect_list)
            
            self.rect_list = rect_list
            return flag
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def excute_main(self,lang='eng+jpn')->bool:
        try:
            self.direction = self.const.DIRECTION_HORIZON
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