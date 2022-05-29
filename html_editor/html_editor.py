
from lib2to3.pgen2.token import NEWLINE
from urllib.error import ContentTooShortError
from pyparsing import htmlComment

import html_const
from html_const import HtmlTagName

NEW_LINE = html_const.NEW_LINE
INDENT = '    '

class HtmlElement():
    def __init__(self,text:str='',tag_name:str=HtmlTagName.DIV,attribute:dict={},indent:int=-1) -> None:
        self.text = text
        self.tag = tag_name
        self.attribute = attribute
        self.child_elements:'list[HtmlElement]' = []
        self.indent_space = 4
        if indent<0:
            self.indent = 0
        else:
            self.indent = indent
    def set_attribute(self,attribute_name:str,value:str):
        self.attribute[attribute_name] = value
    def get_attribute(self,attribute_name:str):
        return self.attribute[attribute_name]
    def add_element(self,element:'HtmlElement'):
        self.child_elements.append(element)
    
class HtmlEditor():
    def __init__(self,html_path:str='') -> None:
        self.html_path = html_path
        self.body:HtmlElement = HtmlElement('',HtmlTagName.BODY,{},1)
        self.indent_space = 4
    
    def init_values(self,css_path:str=''):
        self.css_path = css_path
    
    def create_html(self,html_path:str=''):
        if html_path=='': html_path = self.html_path
        import shutil
        import pathlib
        src_path = str(pathlib.Path(__file__).parent.joinpath(html_const.BASIC_FILE_NAME))
        shutil.copy(src_path,html_path)

    def add_element_by_text(self,text:str='',tag_name:str=HtmlTagName.DIV,attribute:dict={},indent:int=-1):
        self.body.add_element(HtmlElement(text,tag_name,attribute,1))
    def add_element(self,element:HtmlElement):
        element.indent = self.body.indent + 1
        self.body.add_element(element)

    def update_file(self):
        content_text = self.__cnv_html_element_to_str(self.body)
        # content_text = self.__cnv_html_element_list_to_str(self.body.child_elements)
        content_text = content_text[:-1]
        with open(self.html_path,'r',encoding='utf-8')as f:
            all_text = f.read()
        all_text = all_text.replace(html_const.BODY_MAIN_CONTENTS_MARKER,content_text)
        print(all_text)
        with open(self.html_path,'w',encoding='utf-8')as f:
            f.write(all_text)

    def __get_indent_str(self,element:HtmlElement):
        ret = ''
        for _ in range(element.indent):
            for _ in range(self.indent_space):
                ret += ' '
        return ret
    def __cnv_html_element_to_str(self,element:HtmlElement):
        ret = ''
        ret += self.__get_indent_str(element)
        ret += '<'
        ret += element.tag
        ###
        keys = element.attribute.keys()
        attr = ''
        for key in keys:
            attr = key + '=' + element.get_attribute(key) + ' '
        ret += self.__align_str_attr(attr) + '>'
        ###
        ret += element.text
        ###
        buf = ''
        for child in element.child_elements:
            buf += self.__cnv_html_element_to_str(child)
        if buf != '':
            ret += NEW_LINE + buf
        ###
        if element.tag == HtmlTagName.BODY:
            ret += self.__get_indent_str(element) 
        ret += '</' + element.tag + '>' + NEW_LINE
        return ret
    
    def __align_str_attr(self,value):
        if len(value)<1:
            return value
        if value == ' ':
            return ''
        else:
            if value[-1]==' ':
                return value[:-1]
            else:
                return value


    def __cnv_html_element_list_to_str(self,element_list:HtmlElement):
        ret = ''
        for el in element_list:
            ret += self.__cnv_html_element_to_str(el)
        return ret


