
from __future__ import annotations


# from operator import pos
import os
from typing import Any
# import re
# from typing import Any
import cv2
from PIL import Image
from numpy import true_divide
# from numpy import double, true_divide
# from numpy.char import count
import pyocr
import pyocr.builders

from pad import const

# 1.インストール済みのTesseractのパスを通す
path_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract
    print('path_tesseract add to os.environ[PATH]')
else:
    print('path_tesseract include os.environ[PATH]')

def get_tools_by_initialize_tresseract(logger) -> pyocr.TOOLS:
    try:        
        pyocr.tesseract.TESSERACT_CMD = path_tesseract
        tools:list(pyocr.TOOLS) = pyocr.get_available_tools()
        tool = tools[0]
        return tool
    except Exception as e:
        logger.exp.error(e)
        return None



# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
from enum import IntEnum
class const_ocr(IntEnum):
    DIRECTION_TOP = 1
    DIRECTION_RIGHT = 3
    DIRECTION_LEFT = 4
    DIRECTION_BOTTOM = 8
    DIRECTION_HORIZON = 11
    DIRECTION_VERTICAL = 12
    DEFAULT_THRESHOLD = 1.1



class point:
    x = 0
    y = 0
    def __init__(self,x = 0 ,y = 0) -> None:
        # print('point.__init__:', str(id(self)))
        self.x = int(x)
        self.y = int(y)
    def to_tuple(self):
        return (int(self.x),int(self.y))
    def to_list(self):
        return [int(self.x),int(self.y)]

class pointF:
    x : float = 0.0
    y : float = 0.0
    def __init__(self,x:float = 0.0, y:float = 0.0) -> None:
        self.x = x
        self.y = y

# https://qiita.com/MtDeity/items/fa6cfc4fff8f58140caa
# Pythonでクラスの引数や戻り値の型アノテーションに自己のクラスを指定する
# 型アノテーションに自己のクラスを指定できない
# Python3.7以上の場合: from __future__ import annotationsを使用する

# SyntaxError: from __future__ imports must occur at the beginning of the file
# SyntaxError：from futureのインポートはファイルの先頭で行わなければなりません
# from __future__ import annotations
class OcrBox:
    logger = None
    result = None
    str_value = ''
    width = 0
    height = 0
    begin_point : point
    end_point : point
    # 1文字当たりの大きさ
    char_point : point
    # 次の文字との距離
    to_next_distance = 0
    # 縦読みか横読みか
    direction = const_ocr.DIRECTION_HORIZON
    # 次の距離と1文字当たりの大きさの比率
    # The ratio of the next distance to the size of one character
    raito_next_distans_to_size_of_char = 0.0
        
    def __init__(
        self,
        logger,
        ocr_result:pyocr.builders.Box,
        direction_:direction = const_ocr.DIRECTION_HORIZON,
        next_ocr_box:OcrBox = None) -> None:
        
        self.begin_point = point()
        self.end_point = point()
        # 1文字当たりの大きさ
        self.char_point = point()
        try:
            self.logger = logger
            import copy
            buf = copy.copy(ocr_result)
            flag = self.set_ocr_result(buf,direction_)
            if not flag: 
                self.logger.exp.error('set_ocr_result Failed -> return')
                return
            if next_ocr_box != None:
                flag = self.calc_next_distance(next_ocr_box)
                if not flag: 
                    self.logger.exp.error('calc_next_distance Failed -> return')
                    return
        except Exception as e:
            self.logger.exp.error(e)

    def set_ocr_result(self,ocr_result:pyocr.builders.Box,direction_:direction)->bool:
        try:
            self.result = ocr_result
            self.str_value = str(ocr_result.content)
            self.begin_point.x = ocr_result.position[0][0]
            self.begin_point.y = ocr_result.position[0][1]
            self.end_point.x = ocr_result.position[1][0]
            self.end_point.y = ocr_result.position[1][1]
            self.width = (self.end_point.x - self.begin_point.x)
            self.height = (self.end_point.y - self.begin_point.y)
            # 1文字当たりの幅
            if direction_ == const_ocr.DIRECTION_HORIZON:
                self.char_point.x = self.width / len(self.str_value)
                self.char_point.y = self.height / 1
            
            if direction_ == const_ocr.DIRECTION_VERTICAL:
                self.char_point.x = self.width / 1
                self.char_point.y = self.height / len(self.str_value)

            self.direction = direction_
            # print('box : values')
            # print(
            #     self.str_value , 
            #     [self.begin_point.x , self.begin_point.y] , 
            #     [self.end_point.x , self.end_point.y],
            #     self.width, self.height)
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def logout_ocrbox_info(self):
        try:
            self.logger.info('str_value = '+ self.str_value)
            self.logger.info('char_point = ' + str(self.char_point.to_list()))
            self.logger.info('to_next_distance = ' + str(self.to_next_distance))
            self.logger.info('begin,end = ' + str(self.begin_point.to_list()) + ' , ' +  str(self.end_point.to_list()))
            self.logger.info('raito_next_distans_to_size_of_char = ' + str(self.raito_next_distans_to_size_of_char))
        except Exception as e:
            self.logger.exp.error(e)

    def calc_next_distance(self,next_ocr_box:OcrBox) -> bool:
        try:
            if self.direction == const_ocr.DIRECTION_HORIZON:
                self.to_next_distance = next_ocr_box.begin_point.x - self.end_point.x
                self.raito_next_distans_to_size_of_char = \
                    self.to_next_distance / self.char_point.x
            if self.direction == const_ocr.DIRECTION_VERTICAL:
                self.to_next_distance = next_ocr_box.begin_point.y - self.end_point.y
                self.raito_next_distans_to_size_of_char = \
                    self.to_next_distance / self.char_point.y
            return True
        except Exception as e:
            self.logger.exp.error(e)
        return False
        
# クラスの引数や戻り値の型アノテーションに自己のクラスを指定するため
# assert OcrBox.__annotations__ == {
#     'next_ocr_box': 'OcrBox'
# }
# assert OcrBox.calc_next_distance.__annotations__ == {
#     'next_ocr_box': 'OcrBox'
# }
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
class OcrBoxes():
    logger = None
    box_list : list(OcrBox) = []
    threshold_for_judging_separation = None
    is_separation_box :bool = False
    separation_positions : list(int,int) = [] 
    direction_is_horizon = True
    def __init__(
        self,
        logger,
        ocr_result_list:list(pyocr.builders.Box),
        threshold_for_judging_separation = const_ocr.DEFAULT_THRESHOLD,
        ocr_direction_is_horizon = True,
        ) -> None:
        try:
            self.direction_is_horizon = ocr_direction_is_horizon
            self.threshold_for_judging_separation = threshold_for_judging_separation
            # print('OcrBoxes.__init__:', str(id(self)))
            self.logger = logger
            if ocr_result_list == None:
                logger.exp.error('ocr_result_list == None , return')
                return
            if len(ocr_result_list) < 1:
                logger.exp.error('len(ocr_result_list) < 1 , return')
                return
            new_list:list(OcrBox) = list()
            for result in ocr_result_list:
                if ocr_direction_is_horizon:
                    direc = const_ocr.DIRECTION_HORIZON
                else:
                    direc = const_ocr.DIRECTION_VERTICAL
                box:OcrBox = OcrBox(logger,result,direction_=direc)
                new_list.append(box)
            self.box_list = new_list

            # ここでは高さ、幅は揃えない
            # 行が変わったときに大きくなってしまうため
            # flag = self.allign_points()
            # if not flag:
            #     self.logger.exp.error('allign_points Failed')
        except Exception as e:
            self.logger.exp.error(e)

    def logout_ocrbox_info(self,index:int):
        try:
            box:OcrBox = self.box_list[index]
            box.logout_ocrbox_info()
        except Exception as e:
            self.logger.exp.error(e)

    def logout_ocrbox_info_all(self):
        try:
            for i in range(len(self.box_list)):
                box:OcrBox = self.box_list[i]
                box.logout_ocrbox_info()
        except Exception as e:
            self.logger.exp.error(e)

    # def allign_points(self):
    #     """文字の高さ・幅がそれぞれのboxによって異なるので、max、min値でそろえる"""
    #     try:
    #         # max_point:point = point()
    #         # min_point:point = point()
    #         max_point:point = None
    #         min_point:point = None
    #         if len(self.box_list) < 1:
    #             self.logger.exp.error('allign_points : len(self.box_list) < 1 : return')
    #             return False
            
    #         for i in range(len(self.box_list)):
    #             box:OcrBox = self.box_list[i]
    #             if i == 0:
    #                 max_point = point(box.end_point.x,box.end_point.y)
    #                 min_point = point(box.end_point.x,box.end_point.y)
    #             else:
    #                 if min_point.x > box.begin_point.x: min_point.x = box.begin_point.x
    #                 if min_point.y > box.begin_point.y: min_point.y = box.begin_point.y
    #                 if max_point.x < box.end_point.x: max_point.x = box.end_point.x
    #                 if max_point.y < box.end_point.y: max_point.y = box.end_point.y
    #         for i in range(len(self.box_list)):
    #             box:OcrBox = self.box_list[i]
    #             if self.direction_is_horizon:
    #                 # 横読みの場合は、y 高さをそろえる
    #                 box.begin_point.y = min_point.y
    #                 box.end_point.y = max_point.y
    #             else:
    #                 # 縦よみの場合は、x 幅をそろえる
    #                 box.begin_point.x = min_point.x
    #                 box.end_point.x = max_point.x
    #             # self.box_list[i] = box

    #         return True
    #     except Exception as e:
    #         self.logger.exp.error(e)
    #         return False

    def allign_points_in_separation_position(self):
        """文字の高さ・幅がそれぞれのboxによって異なるので、max、min値でそろえる"""
        try:
            # max_point:point = point()
            # min_point:point = point()
            max_point:point = None
            min_point:point = None
            if len(self.box_list) < 1:
                self.logger.exp.error('allign_points_in_separation_position : len(self.box_list) < 1 : return')
                return False

            if len(self.separation_positions) < 1:
                self.logger.exp.error('allign_points_in_separation_position : len(self.separation_positions) < 1 : return')
                return False
            
            for j in range(len(self.separation_positions)):
                #最大値最小値を取得
                min_index = self.separation_positions[j][0]
                max_index = self.separation_positions[j][1]
                for i in range(min_index,max_index):
                    box:OcrBox = self.box_list[i]
                    if i == 0:
                        max_point = point(box.end_point.x,box.end_point.y)
                        min_point = point(box.end_point.x,box.end_point.y)
                    else:
                        if min_point.x > box.begin_point.x: min_point.x = box.begin_point.x
                        if min_point.y > box.begin_point.y: min_point.y = box.begin_point.y
                        if max_point.x < box.end_point.x: max_point.x = box.end_point.x
                        if max_point.y < box.end_point.y: max_point.y = box.end_point.y
                # 高さ幅をそろえる
                for i in range(len(self.box_list)):
                    box:OcrBox = self.box_list[i]
                    if self.direction_is_horizon:
                        # 横読みの場合は、y 高さをそろえる
                        box.begin_point.y = min_point.y
                        box.end_point.y = max_point.y
                    else:
                        # 縦よみの場合は、x 幅をそろえる
                        box.begin_point.x = min_point.x
                        box.end_point.x = max_point.x
                    # self.box_list[i] = box

            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def calc_next_distance_for_boxes(self):
        try:
            if len(self.box_list) < 1:
                self.logger.exp.error('calc_next_distance_for_boxes len(self.box_list) < 1: retrun')
                return False
            
            flag = False
            now_positions = [0,len(self.box_list)-1]
            self.separation_positions = []
            for i in range(len(self.box_list)-1):
                box : OcrBox = self.box_list[i]
                next_box = self.box_list[i+1]
                box.calc_next_distance(next_box)
                if abs(box.raito_next_distans_to_size_of_char) >= abs(self.threshold_for_judging_separation):
                    flag = True
                    self.logger.info('box is separated. raito = ' + str(box.raito_next_distans_to_size_of_char))
                    now_positions[1] = i
                    self.separation_positions.append(now_positions)
                    now_positions = [i+1,len(self.box_list)-1]
            else:
                self.is_separation_box = flag
                self.separation_positions.append(now_positions)
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False
    
    def get_rect_list(self)->list[list[int,int,int,int]]:
        rect = [0,0,0,0]
        rect_list = []
        try:
            # ないときは作る
            if len(self.separation_positions) < 1:
                self.logger.exp.error('get_rect_list : len(self.separation_positions) < 1 , create positions')
                self.separation_positions = [0,len(self.box_list)-1]
            # separation True/False に関係なく以下で取得する
            for i in range(len(self.separation_positions)):
                begin_pos = self.separation_positions[i][0]
                end_pos = self.separation_positions[i][1]
                # BeginPoint
                box : OcrBox = self.box_list[begin_pos]
                begin_point = box.begin_point
                # EndPoint
                box : OcrBox = self.box_list[end_pos]
                end_point = box.end_point
                rect = [
                    begin_point.x,begin_point.y,
                    end_point.x,end_point.y
                ]
                rect_list.append(rect)
            return rect_list
        except Exception as e:
            self.logger.exp.error(e)
            return rect_list
        

    def decide_separation_box_list(self):
        try:
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False

    def print_mbmber_object_id(self):
        print('box_list id = ' + str(id(self.box_list)))
        if len(self.box_list) < 1:
            return
        for i in range(len(self.box_list)):
            print('OcrBox id ' + str(i) + ' = ' + str(id(self.box_list[i]))) 

    def get_str_value(self)->str:
        fn = 'get_str_value'
        try:
            if len(self.box_list) < 1:
                self.logger.exp.error(fn + ' : len(self.box_list) < 1 , return')
                return ''
            ret = ''
            for i in range(len(self.box_list)):
                box : OcrBox = self.box_list[i]
                ret += box.str_value
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return ''
    
    def get_begin_point(self):
        try:
            if len(self.box_list) < 1:
                self.logger.exp.error('get_begin_point : len(self.box_list) < 1')
                return point(0,0)
            else:
                val :OcrBox = self.box_list[0]
                return val.begin_point
        except Exception as e:
            self.logger.exp.error(e)
            return point(0,0)
    
    def get_begin_point_tuple(self):
        val:point = self.get_begin_point()
        return val.to_tuple()
    
    def get_end_point(self):
        try:
            if len(self.box_list) < 1:
                self.logger.exp.error('get_begin_point : len(self.box_list) < 1')
                return point(0,0)
            else:
                val :OcrBox = self.box_list[-1]
                return val.begin_point
        except Exception as e:
            self.logger.exp.error(e)
            return point(0,0)

    def get_end_point_tuple(self):
        val:point = self.get_begin_point()
        return val.to_tuple()
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////



def excute_ocr(
    logger,
    tool:list,
    img_path:str,
    out_path:str,
    lang:str ='jpn',
    direction_is_horizon:bool = True,
    is_output_result_image = True,
    color=(0, 0, 255),
    border_width = 2) -> list(pyocr.builders.Box):
    ret_boxes : list(pyocr.builders.Box) = []
    try:
        img = Image.open(img_path)
        
        if not direction_is_horizon:
            lang = lang.replace('jpn' , 'jpn_vert')
        word_boxes = tool.image_to_string(
            img,
            lang=lang,
            builder=pyocr.builders.WordBoxBuilder(tesseract_layout=6)
)
        out = cv2.imread(img_path)
        content_str = ''

        if len(word_boxes) < 1:
            logger.exp.error('data get word_boxes by ocr is nothing. return False')
            return ret_boxes

        ret_boxes = word_boxes
        for d in word_boxes:
            content_str += str(d.content)
            if is_output_result_image:
                #d.position[0]は認識した文字の左上の座標,[1]は右下
                cv2.rectangle(out, d.position[0], d.position[1], color, border_width)            
                cv2.imwrite(out_path.format(lang, 'word_boxes'), out)
            x1,y1 = d.position[0]
            x2,y2 = d.position[1]
            # print('word_box.content = ' + str(d.content))
            # print('word_box.position = ' + str(d.position))
            # print('x1,y1 = ' + str(x1) + ' , ' + str(y1))
            # print('x2,y2 = ' + str(x2) + ' , ' + str(y2))
        logger.info('content_str = ')
        logger.info(content_str)

        if is_output_result_image:
            logger.info('out_path = ' + out_path)
        return word_boxes
    except Exception as e:
        logger.exp.error(e)
        return ret_boxes

# main function for ocr excute
# keywordと完全一致した範囲の、list[ocr_result_list[]]を返す
def get_rect_list_match_keyword_in_ocr_result(
        logger,
        keyword:str,
        ocr_result_list:list(pyocr.builders.Box),
        remove_if_box_is_far_apart = False,
        threshold_for_judging_separation = const_ocr.DEFAULT_THRESHOLD,
        ocr_direction_is_horizon = True
        )->list(OcrBoxes):
    """ocr の結果データから、keyword が含まれている場合、その
    keyword が一致した範囲を1つの要素として、その要素の list 'list(OcrBoxes)' を返す
    keyword と一度も一致しない場合、空の list(OcrBoxes) [] を返す
    ※ remove_if_box_is_far_apart
    文字列が一致したとき、一致した文字列の中に位置が離れたものがある場合除外する
    閾値：Threshold for judging the degree of separation
    読み込んだboxの一文字当たりの幅と、box同士の距離の割合が、上記閾値より上回る場合除外する
    """
    # 戻り値用list
    # ret_rect_list = []
    ret_rect = (0,0,0,0)
    match_box_list:list(OcrBoxes) = list()
    # match_pos_list = []
    fn = 'get_rect_list_match_keyword_in_ocr_result'
    try:
        # keyword がないときは終了する
        if len(keyword) < 1:
            logger.error('len(keyword) < 1 -> return. keyword = ' + keyword)
            return match_box_list
        
        pos_now_result_el = 0
        element_count = 0
        boxes = None
        # ocr_result の最後まで検索する
        while(pos_now_result_el <= len(ocr_result_list)):
            # ここから繰り返し
            ### 初回実行時なら、まず、ocr_result に keyword が存在するかチェックする
            # keyword が存在しなければ NG
            pos_match_keyword = find_keyword_in_ocr_result_str(
                logger,keyword,ocr_result_list,pos_now_result_el)
            if pos_match_keyword < 0:
                # keyword がなければ終了する
                logger.info( fn + ': find end. keyword = '+ keyword)
                logger.info('match_count = ' + str(len(match_box_list)))
                return match_box_list
            else:
                # keyword がある場合
                # keyword 一致する箇所が含む要素の位置を取得する
                # result[pos_now_result_el:] から pos_match_keyword 文字数分カウントした要素番号を取得する
                element_count = get_element_count_match_keyword(
                    logger,ocr_result_list ,pos_now_result_el, pos_match_keyword)
                # element_count = pos_match_keyword
                # 最初に一致した場所(範囲)(ocr_result の range)を取得する
                # pos_now_result_el + element_count 番目からが一致した keyword の場所
                ret_results= get_ocr_result_range_match_keyword(
                    logger,keyword,ocr_result_list,pos_now_result_el,element_count)
                # ここで OcrBoxex に格納する
                # ここでmatch_box_list の0番目が上書きされている
                boxes = OcrBoxes(logger,ret_results,threshold_for_judging_separation,ocr_direction_is_horizon)
                logger.info('match_str = ' + boxes.get_str_value())
                # 取得した値をチェックする
                # flag = box_is_far_apart(logger,boxes.box_list,threshold_for_judging_separation)
                flag = False
                if remove_if_box_is_far_apart and flag:
                    logger.exp.error('not append list')
                else:
                    # 複数一致する場合もあるのでリストに格納する
                    match_box_list.append(boxes)
                    # boxes = None
                    # ret_rect_list.append(ret_rect)

                # 次の検索開始位置
                pos_now_result_el += int(len(boxes.box_list)) + element_count
                logger.info(fn + ': now_pos = ' + str(pos_now_result_el))
                # log
                logger.info( fn + ': match True by find. keyword = '+ keyword)
                logger.info('match_count = ' + str(len(match_box_list)))
            ### end if
        ### end while

        # 一致した文字列の中に離れたものがあれば、
        # 目的のものでない可能性があるので、警告を出力する
        return match_box_list
    except Exception as e:
        logger.exp.error(e)
        return match_box_list

# get_rect_list_match_keyword_in_ocr_result 内で使用する
# keyword 一致する箇所が含む要素の位置を取得する
def get_element_count_match_keyword(
        logger,
        ocr_result:list(pyocr.builders.Box),
        now_ocr_pos_begin:int,
        pos_match_keyword:int) -> int:
    try:
        ocr_result_part = ocr_result[now_ocr_pos_begin:]
        element_count = 0
        char_leave_count = pos_match_keyword
        str_count = 0
        # 一致した場所まで要素を進めて、keyword[0] と一致した場所が含む要素の位置を返す
        for el in ocr_result_part:
            char_leave_count -= len(str(el.content))
            str_count += len(str(el.content))
            element_count += 1
            if char_leave_count <= 0:
                break
        return element_count
    except Exception as e:
        logger.exp.error(e)
        return -1

# get_rect_list_match_keyword_in_ocr_result 内で使用する
# ocr_result に keyword が存在するかチェックする
# keyword が存在しなければ NG
def find_keyword_in_ocr_result_str(
        logger,
        keyword:str,
        ocr_result:list(pyocr.builders.Box),
        begin_element_pos:int):
    """ocr_result をつなげて文字列にして、その中に keyword と一致するか検索する
    戻り値は、一致した位置
    """
    try:
        # begin_element_pos 以降の ocr_result を抜き出す
        ocr_result_edit = ocr_result[begin_element_pos:]
        ### ocr_result に keyword が存在するかチェックする
        # keyword が存在しなければ NG
        ocr_result_str = ''
        # ocr_result_edit をすべてつなげて文字列にする
        for el in ocr_result_edit: ocr_result_str += str(el.content)
        # keyword 存在チェック
        keyword_match_pos = ocr_result_str.find(keyword)
        return keyword_match_pos
    except Exception as e:
        logger.exp.error(e)
        return -1

# get_rect_list_match_keyword_in_ocr_result 内で使用する
# 最初に一致した場所(範囲)(ocr_result の range)を取得する
# keyword と一致した範囲の ocr_result を取得する(前方からの比較)
# すでに一致していることがわかっている
def get_ocr_result_range_match_keyword(
    logger,
    keyword:str,
    ocr_result:list(pyocr.builders.Box),
    edit_begin_result_element_index:int,
    ocr_ret_pos_match_begin:int) -> list(pyocr.builders.Box):

    ret_result_ocr_boxes:list(pyocr.builders.Box) = list()
    try:
        # keyword と一致したところからの ocr_result を取得する
        cut_pos = edit_begin_result_element_index + ocr_ret_pos_match_begin
        ocr_result_range_match = ocr_result[cut_pos:]
        # 取得する文字数
        get_leave_length = len(keyword)
        for el in ocr_result_range_match:
            # 一致していることがわかっているので、単純に list に追加していく
            ret_result_ocr_boxes.append(el)
            # 取得した文字数分分引いていく
            get_leave_length -= len(el.content)
            # ゼロ以下で終了
            if get_leave_length <= 0:
                break
        ## end for
        return ret_result_ocr_boxes
    except Exception as e:
        logger.exp.error(e)
        return ret_result_ocr_boxes

    
# def is_match_keyword_in_ocr_result(logger,keyword,ocr_result_char):
#     try:
#         ret_char = ocr_result_char
#         # keyword の1文字目が合致したら、keyword2文字目以降も比較していく
#         if ret_char == keyword[0]:
#             # keyword が一致した数
#             match_count = 1
#             # 2文字目から比較
#             for key_char in keyword[1:len(keyword)]:
#                 # char が合致したとき
#                 if ret_char == key_char:
#                     match_count += 1
#                 else:
#                     # 一度でも合致しないと抜ける
#                     break 
#             # すべて合致したとき
#             if len(keyword) == match_count:
#                 pass
#         return True
#     except Exception as e:
#         logger.exp.error(e)
#         return False

# box 同士が離れているか判定する
# 読み取ったocrが改行されて離れているが、一つの単語としたい場合もあるので注意
def box_is_far_apart(
    logger,
    ocr_box_list:list(OcrBox),
    separation_border_value:float=const_ocr.DEFAULT_THRESHOLD)->bool:
    try:
        avg_separation_val = 0
        cl_box_list:list(OcrBox) = []
        # 平均の距離を算出する
        boxes_length = int(len(ocr_box_list))
        # 
        min_raito = 0
        max_raito = 0
        val = 0
        for i in range(boxes_length-1):
            box:OcrBox = ocr_box_list[i]
            val = box.raito_next_distans_to_size_of_char
            if i == 0:
                min_raito = val
                max_raito = val
            else:
                if min_raito < val: min_raito = val
                if max_raito > val: max_raito = val
        # 最小値と最大値が ボーダー値より大きければFalse
        # 読み取ったocrが改行されて離れているが、一つの単語としたい場合もあるので注意
        if ((max_raito - min_raito) > separation_border_value):
            flag = True
        else:
            flag = False
        if flag:
            logger.info('box_is_far_apart True')
        else:
            logger.info('box_is_far_apart False')
        return flag
    except Exception as e:
        logger.exp.error(e)
        return True

# get_rect_list_match_keyword_in_ocr_result の後に実行する
# 上記関数で取得された結果(ocr_box)から、座標範囲を得る
# keyword に一致した結果 (ocr_boxes) の rect(x,y,x,y) を取得する
# list(OcrBoxes)
def get_rect_from_ocr_result_boxes_list(logger,ocr_boxes_list:list(OcrBoxes),is_remove_separation = True):
    fn = 'get_rect_from_ocr_result_boxes_list'
    ret_rect_list:list[int,int,int,int] = list()
    try:
        if len(ocr_boxes_list) < 1:
            logger.exp.error(fn + ' : len(ocr_boxes_list) < 1 , return')
            return ret_rect_list
        get_rect_list :list[int,int,int,int] = list()
        max = len(ocr_boxes_list)
        for i in range(max):
            buf_boxes:OcrBoxes = ocr_boxes_list[i]
            # 分離しきい値を計算
            flag = buf_boxes.calc_next_distance_for_boxes()
            if not flag:
                logger.exp.error('calc_next_distance_for_boxes Failed. i = ' + str(i))
            # 分離閾値を計算した後、高さ、幅をそろえる
            flag = buf_boxes.allign_points_in_separation_position()
            if not flag:
                logger.exp.error('allign_points_in_separation_position Failed. i = ' + str(i))
            # 分離を含まない True かつ Boxes が分離している場合は、次へ
            if is_remove_separation and buf_boxes.is_separation_box:
                logger.info('is_remove_separation = ' + str(is_remove_separation))
                buf_boxes.logout_ocrbox_info_all()
                continue
            # buf_boxes.print_mbmber_object_id()
            get_rect_list = buf_boxes.get_rect_list()
            # 取得した Rect_List を Ret_rect_list へ格納する
            for get_rect in get_rect_list:
                ret_rect_list.append(get_rect)
            #ret_rect_list.extend()
        return ret_rect_list
    except Exception as e:
        logger.exp.error(e)
        return ret_rect_list

# get_rect_from_ocr_result_boxes_list 内で使われる
# keyword に一致した結果 (ocr_boxes) の rect(x,y,x,y) を取得する
# OcrBoxes (list(OcrBox))
def get_rect_from_ocr_result_boxes(logger,ocr_boxes:OcrBoxes):
    fn = 'get_rect_from_ocr_result_boxes'
    ret_rect_ =[0,0,0,0]
    try:
        if len(ocr_boxes.box_list) < 1:
            logger.exp.error(fn + ' : len(ocr_boxes) < 1 , return')
            return 

        ocr_box_list:list(OcrBox) = ocr_boxes.box_list
        if len(ocr_box_list) < 1:
            logger.exp.error('len(ocr_box_list) < 1 -> return')
            return ret_rect_

        # 最初の要素の begin_point
        begin_point = ocr_boxes.get_begin_point()
        # 最後の要素の end_point
        end_point = ocr_boxes.get_end_point()

        ret_rect_ = [
            begin_point.x,begin_point.y,
            end_point.x,end_point.y
        ]
        return ret_rect_
    except Exception as e:
        logger.exp.error(e)
        return ret_rect_

# OcrBox.ocr_result == pyocr.builder.box
# get_rect_list_match_keyword_in_ocr_result の後に実行する
# 上記関数で取得された結果(ocr_box)から、座標範囲を得る
# class OcrBox 内のプロパティで対応可能
# def get_rect_from_ocr_result_box(logger,ocr_box_list:list(OcrBox)):
#     pass


# class OcrBox 内のプロパティで対応可能
# def get_point_from_ocr_result(logger,ocr_result:pyocr.builders.box,direction_:direction):
#     ret_point = [-1,-1]
#     try:
#         x1,y1 = ocr_result.position[0]
#         x2,y2 = ocr_result.position[1]
#         # vertical point
#         if direction.TOP | direction_:
#             ret_point[1] = y1
#         elif direction.BOTTOM | direction_:
#             ret_point[1] = y2
#         # Horizon point    
#         if direction.LEFT | direction_:
#             ret_point[0] = x1
#         elif direction.Right | direction_:
#             ret_point[0] = x2

#         return ret_point
#     except Exception as e:
#         logger.exp.error(e)
#         return ret_point

def patint_rectangle(
    logger,
    img,
    rect:list[int,int,int,int],
    color=(0, 0, 255),
    border_width = 2):
    try:
        begin_pos = [rect[0],rect[1]]
        end_pos = [rect[2],rect[3]]
        img = cv2.rectangle(img, begin_pos ,end_pos, color, border_width)   
        return img
    except Exception as e:
        logger.exp.error(e)
        return img

def write_image_and_paint_rectangle(
    logger,
    img_path:str,
    rect:list[int,int,int,int],
    out_path:str,
    color=(0, 0, 255),
    border_width = 2) -> bool:
    try:
        begin_pos = [rect[0],rect[1]]
        end_pos = [rect[2],rect[3]]
        # img = Image.open(img_path)
        out = cv2.imread(img_path)
        cv2.rectangle(out, begin_pos ,end_pos, color, border_width)            
        cv2.imwrite(out_path, out)
        return True
    except Exception as e:
        logger.exp.error(e)

def write_result_image_for_ocr(
    logger,
    img_path:str,
    rect_list:list[list[int,int,int,int]],
    out_path:str='',
    color=(0, 0, 255),
    border_width = 2) -> bool:
    try:
        add_str = '_ocr_ret'
        if out_path == '':
            out_path = create_write_path(logger,img_path,add_str)
        else:
            out_path = add_number_to_path(logger,img_path,0)
        
        img = cv2.imread(img_path)
        for i in range(len(rect_list)):
            img = patint_rectangle(logger,img,rect_list[i])
            # flag = write_image_and_paint_rectangle(
            #     logger,img_path,rect_list[i],out_path,color,border_width)
            #   The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
            # if img == None:
            #     #logger.exp.error('write_image failed , '+ str(i) +' path = ' + out_path)
            #     logger.exp.error('patint_rectangle failed , return False')
            #     return False         
        cv2.imwrite(out_path, img)
        print(out_path)
        return True
    except Exception as e:
        logger.exp.error(e)
        return False

def add_number_to_path(logger,base_path,num)->str:
    ret = ''
    try:
        import os
        dir = os.path.dirname(base_path)
        basename_without_ext = os.path.splitext(os.path.basename(base_path))[0]
        from pathlib import Path
        root_ext_pair = os.path.splitext(base_path)
        add_str = str(num)
        ret = dir + '\\' + basename_without_ext + add_str + str(root_ext_pair[1])
        return ret
    except Exception as e:
        logger.exp.error(e)
        return ''


def create_write_path(logger,base_path,add_str)->str:
    ret = ''
    try:
        import os
        dir = os.path.dirname(base_path)
        basename_without_ext = os.path.splitext(os.path.basename(base_path))[0]
        from pathlib import Path
        root_ext_pair = os.path.splitext(base_path)
        ret = dir + '\\' + basename_without_ext + add_str + str(root_ext_pair[1])
        return ret
    except Exception as e:
        logger.exp.error(e)
        return ''