
from __future__ import annotations


# from operator import pos
import os
# import re
# from typing import Any
import cv2
from PIL import Image
# from numpy import double, true_divide
# from numpy.char import count
import pyocr
import pyocr.builders

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
class direction(IntEnum):
    TOP = 1
    RIGHT = 3
    LEFT = 4
    BOTTOM = 8
    HORIZON = 11
    VERTICAL = 12

class point():
    x = 0
    y = 0
    def __init__(self,x = 0 ,y = 0) -> None:
        self.x = 0
        self.y = 0

class pointF():
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
    begin_point : point = point()
    end_point : point = point()
    # 1文字当たりの大きさ
    char_point : point = point()
    # 次の文字との距離
    to_next_distance = 0
    # 縦読みか横読みか
    direction = direction.HORIZON
    # 次の距離と1文字当たりの大きさの比率
    # The ratio of the next distance to the size of one character
    raito_next_distans_to_size_of_char = 0.0
        
    def __init__(
        self,
        logger,
        ocr_result:pyocr.builders.Box,
        direction_:direction = direction.HORIZON,
        next_ocr_box:OcrBox = None) -> None:
        
        try:
            self.logger = logger
            flag = self.set_ocr_result(ocr_result,direction_)
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
            self.str_value = ocr_result.content
            self.begin_point.x = ocr_result.position[0][0]
            self.begin_point.y = ocr_result.position[0][1]
            self.end_point.x = ocr_result.position[1][0]
            self.end_point.y = ocr_result.position[1][1]
            self.width = self.end_point.x - self.begin_point.x
            self.height = self.end_point.y - self.begin_point.y

            # 1文字当たりの幅
            if direction_ | direction.HORIZON:
                self.char_point.x = self.width / len(self.str_value)
                self.char_point.y = self.height / 1
            
            if direction_ | direction.VERTICAL:
                self.char_point.x = self.width / 1
                self.char_point.y = self.height / len(self.str_value)
            return True
        except Exception as e:
            self.logger.exp.error(e)
            return False


    def calc_next_distance(self,next_ocr_box:OcrBox) -> bool:
        try:
            if self.direction.HORIZON:
                self.to_next_distance = next_ocr_box.begin_point.x - self.end_point.x
                self.raito_next_distans_to_size_of_char = \
                    self.to_next_distance / self.char_point.x
            if self.direction.VERTICAL:
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
class OcrBoxes:
    logger = None
    box_list : list(OcrBox) = []

    def __init__(
        self,
        logger,
        ocr_result_list:list(pyocr.builders.Box)
        ) -> None:
        try:
            self.logger = logger
            if ocr_result_list == None:
                logger.exp.error('ocr_result_list == None , return')
                return
            if len(ocr_result_list) < 1:
                logger.exp.error('len(ocr_result_list) < 1 , return')
                return
            for result in ocr_result_list:
                box:OcrBox = OcrBox(logger,result)
                self.box_list.append(box)

        except Exception as e:
            self.logger.exp.error(e)
    
    def get_begin_point(self):
        ret_p = point()
        try:
            p : point()
            return p
        except Exception as e:
            self.logger.exp.error(e)
            return ret_p

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
    is_output_result_image = True,
    color=(0, 0, 255),
    border_width = 2) -> list(pyocr.builders.Box):
    ret_boxes : list(pyocr.builders.Box) = []
    try:
        img = Image.open(img_path)
        
        lang = 'jpn'
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
        threshold_for_judging_separation = 0.6
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
    match_box_list:list(OcrBoxes) = []
    # match_pos_list = []
    fn = 'get_rect_list_match_keyword_in_ocr_result'
    try:
        # keyword がないときは終了する
        if len(keyword) < 1:
            logger.error('len(keyword) < 1 -> return. keyword = ' + keyword)
            return match_box_list
        
        pos_now_result_el = 0
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
                element_count = get_element_count_match_keyword(
                    logger,ocr_result_list,pos_match_keyword)
                # 最初に一致した場所(範囲)(ocr_result の range)を取得する
                ret_results= get_ocr_result_range_match_keyword(
                    logger,keyword,ocr_result_list,element_count)
                # ここで OcrBoxex に格納する
                boxes = OcrBoxes(logger,ret_results)
                # 取得した値をチェックする
                flag = box_is_far_apart(logger,boxes.box_list,threshold_for_judging_separation)
                if remove_if_box_is_far_apart and flag:
                    logger.exp.error('not append list')
                else:
                    # 複数一致する場合もあるのでリストに格納する
                    match_box_list.append(boxes)
                    # ret_rect_list.append(ret_rect)

                # 次の検索開始位置
                element_count += int(len(ret_rect))
                pos_now_result_el = element_count
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
        pos_match_keyword:int) -> int:
    try:
        element_count = 0
        char_leave_count = pos_match_keyword 
        # 一致した場所まで要素を進めて、keyword[0] と一致した場所が含む要素の位置を返す
        for el in ocr_result:
            char_leave_count -= len(str(el.content))
            if char_leave_count <= 0:
                break
            element_count += 1
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
        ocr_result_edit = ocr_result[begin_element_pos:len(ocr_result)]
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
    ocr_ret_pos_match_begin:int) -> list(pyocr.builders.Box):

    ret_result_ocr_boxes:list(pyocr.builders.Box) = []
    try:
        # keyword と一致したところからの ocr_result を取得する
        ocr_result_range_match = ocr_result[ocr_ret_pos_match_begin:len(ocr_result)]
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
    separation_border_value:float=0.6)->bool:
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
def get_rect_from_ocr_result_boxes_list(logger,ocr_boxes_list:list(OcrBoxes)):
    fn = 'get_rect_from_ocr_result_boxes_list'
    ret_rect_list = []
    try:
        if len(ocr_boxes_list) < 1:
            logger.exp.error(fn + ' : len(ocr_boxes_list) < 1 , return')
            return ret_rect_list
        max = int(len(ocr_boxes_list))
        for i in range(max):
            boxes = ocr_boxes_list[i]
            ret_rect = get_rect_from_ocr_result_boxes(logger,boxes)
            ret_rect_list.append(ret_rect)
        return ret_rect_list
    except Exception as e:
        logger.exp.error(e)
        return ret_rect_list

# get_rect_from_ocr_result_boxes_list 内で使われる
# keyword に一致した結果 (ocr_boxes) の rect(x,y,x,y) を取得する
# OcrBoxes (list(OcrBox))
def get_rect_from_ocr_result_boxes(logger,ocr_boxes:OcrBoxes):
    fn = 'get_rect_from_ocr_result_boxes'
    ret_rect =[0,0,0,0]
    try:
        if len(ocr_boxes.box_list) < 1:
            logger.exp.error(fn + ' : len(ocr_boxes) < 1 , return')
            return 

        ocr_box_list:list(OcrBox) = ocr_boxes.box_list
        if len(ocr_box_list) < 1:
            logger.exp.error('len(ocr_box_list) < 1 -> return')
            return ret_rect

        # 最初の要素の begin_point
        tmp_box : OcrBox = ocr_box_list[0]
        begin_point : point = tmp_box.begin_point
        # 最後の要素の end_point
        tmp_box = ocr_box_list[len(ocr_box_list)-1]
        end_point : point = tmp_box.end_point

        ret_rect = [
            begin_point.x,begin_point.y,
            end_point.x,end_point.y
        ]
        return ret_rect
    except Exception as e:
        logger.exp.error(e)
        return ret_rect

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
        for i in range(len(rect_list)):
            add_str = '_ocr_ret' + str(i)
            if out_path == '':
                out_path = create_write_path(logger,img_path,add_str)
            else:
                out_path = add_number_to_path(logger,img_path,i)
            flag = write_image_and_paint_rectangle(
                logger,img_path,rect_list[i],out_path,color,border_width)
            if flag:
                logger.info('result_path ' + str(i) + ' : ' + out_path)
                print(out_path)
            else:
                logger.exp.error('write_image failed , '+ str(i) +' path = ' + out_path)
                logger.exp.error('write_result_image_for_ocr failed , return')
                return flag
        return flag
    except Exception as e:
        logger.exp.error(e)

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