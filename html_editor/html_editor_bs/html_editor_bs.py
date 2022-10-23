
if __name__ == '__main__':
    import __init__

from bs4 import BeautifulSoup
from html_editor.html_editor import HtmlEditor,HtmlTagName
from html_editor.html_editor import HtmlElement as HtmlElementbase
from html_editor.html_writer import HtmlWriter
from bs4.element import Tag
from bs4.formatter import Formatter
import html_editor.html_const as html_const
from html_editor.html_const import tag_is_closing_type

class HtmlElementBs(HtmlElementbase,Tag):
    def __init__(
        self,
        tag_text: str = '',
        tag_name: str = HtmlTagName.DIV,
        attribute: dict = {},
        indent: int = -1) -> None:
        """
        """
        self.tag = tag_name
        self.tag_text = ''
        super().__init__(tag_text, tag_name, attribute, indent)
        self.child_tags:'list[Tag]' = []

    def cnv_html_element_to_tag(self):
        # soup = BeautifulSoup()
        # attrs = self.attribute
        # tag = soup.new_tag(self.tag, attrs=attrs)
        # tag.string = self.tag_text
        tag = self.get_tag_single(self)
        self.child_tags = []
        for ch in self.child_elements:
            # c_attrs = ch.attribute
            # c_tag = soup.new_tag(ch.tag, attrs=c_attrs)
            # c_tag.string = self.text
            c_tag = ch.get_tag_single(ch)
            self.child_tags.append(c_tag)
            tag.append(c_tag)
        return tag

    def get_tag_single(self,element:'HtmlElement'):
        soup = BeautifulSoup()
        if tag_is_closing_type(element.tag):
            ret = element.cnv_html_element_to_str()
            #BeautifulSoup.new_tagを使用した場合
            #imgなどの単体でのタグでも<img></img>となってしまうので
            #HtmlElement.cnv_html_element_to_str を使用して<img ~>とする
            #この場合タグデータが文字列となり扱いにくいので、
            #spanタグの bs4.element.Tag の中に入れて扱う
            tag = soup.new_tag('span')
            if not isinstance(tag.string, type(None)):
                tag.string += ret
            else:
                tag.string = ret
        else:
            attrs = self.attribute
            tag = soup.new_tag(self.tag, attrs=attrs)
            tag.string = self.tag_text
        return tag



    def add_element(self, element: 'HtmlElement'):
        super().add_element(element)
        self.child_tags.append(element.get_tag())
    
    def get_tag(self):
        return self.cnv_html_element_to_tag()
        
class HtmlElement(HtmlElementBs):
    pass


class HtmlEditorBs(HtmlEditor,HtmlWriter):
    def __init__(self, html_path: str = '') -> None:
        super().__init__(html_path)
        self.body:Tag = None
        self.soup = None

    def init_values(self,css_path:str=''):
        self.css_path = css_path

    def create_html(self,html_path:str='',basic_html_file_path:str=''):
        super().create_html(html_path, basic_html_file_path)
        self.soup = BeautifulSoup(open(self.html_path), 'html.parser')

    def add_element_by_text(
        self, text: str = '',
        tag_name: str = HtmlTagName.DIV,
        attribute: dict = ...,
        indent: int = -1):
        # return super().add_element_by_text(text, tag_name, attribute, indent)
        tag = self.soup.new_tag(
            tag_name, attrs=attribute)
        tag.string = text
        self.soup.body.append(tag)
    
    def add_element(self, element: HtmlElement):
        # return super().add_element(element)
        self.soup.body.append(element.get_tag())

    def update_file(self):
        # return super().update_file()
        wbuf = self.soup.prettify()
        with open(self.html_path,'w',encoding='utf-8')as f:
            f.write(wbuf)

    def __cnv_html_element_to_str(self, element: HtmlElement):
        # return super().__cnv_html_element_to_str(element)
        return element.get_text()

    #####
    # Writer
    #####
    # def init_values(self, css_path: str = ''):
    #     return super().init_values(css_path)

    def add_outline_body_with_div(self, html_basic_path: str = ''):
        # return super().add_outline_body_with_div(html_basic_path)
        return 
    def remover_html_source_outer_main_contents(self):
        # return super().remover_html_source_outer_main_contents()
        return
    # def add_outline_body(self, html_basic_path: str = ''):
        # return super().add_outline_body(html_basic_path)
    def add_outline_body(self,html_basic_path:str=''):
        """
        bodyタグの前後を追記する
         メインコンテンツ部も追記している
          <body><div class="main-contents"></div></body> 
        """
        # html_basic_path = self.get_default_basic_path(html_basic_path)
        # with open(html_basic_path, 'r',encoding='utf-8')as f:
        #     html_buf = f.read()
        # with open(self.html_path,'r',encoding='utf-8')as f:
        #     contents_buf = f.read()
        # before_str = BODY_BEFORE_STR
        # after_str = '{}{}{}'.format(
        #     BODY_AFTER_LEFT_STR, NEW_LINE+contents_buf , BODY_AFTER_RIGHT_STR)
        # w_data = html_buf.replace(before_str,after_str)
        w_data = self.soup.prettify(formatter=Formatter(indent=self.indent_space))
        with open(self.html_path,'w',encoding='utf-8')as f:
            f.write(w_data)
        return
    def add_css_file_path(self, css_path: str):
        # return super().add_css_file_path(css_path)
        if css_path=='':
            css_path = self.css_path
        header_tag = self.soup.find('head')
        attr = {"rel":"stylesheet"}
        new_tag = self.soup.new_tag(
            'link',href=css_path, attrs=attr)
        header_tag.append(new_tag)

    def _is_exists_str_in_file(self, path: str, value: str):
        return super()._is_exists_str_in_file(path, value)
    
    def _replace_str_to_file(self, path: str, target_value: str, replace_value: str):
        return super()._replace_str_to_file(path, target_value, replace_value)
    
    def _replace_line_to_file(self, path: str, target_value: str, replace_line: str):
        return super()._replace_line_to_file(path, target_value, replace_line)
    
    def get_default_basic_path(self, basic_html_file_path: str = ''):
        return super().get_default_basic_path(basic_html_file_path)
    
    def create_html_content(self, html_path: str = ''):
        return super().create_html_content(html_path)

    def add_to_file(self, element: 'HtmlElement'):
        """ html ファイルの body タグの最後に追記する"""
        self.soup.body.append(element.get_tag())
        # return super().add_to_file(element)
    
    def add_to_file_by_text(
        self, 
        text: str = '', 
        tag_name: str = HtmlTagName.DIV, 
        attribute: dict = ..., 
        is_begin_only: bool = False, 
        indent: int = -1):
        tag = self.soup.new_tag(
            name=tag_name, attrs=attribute)
        self.add_to_file(tag)
        # return super().add_to_file_by_text(text, tag_name, attribute, is_begin_only, indent)

    def __add_element_by_text(
        self, 
        text: str = '', 
        tag_name: str = HtmlTagName.DIV, 
        attribute: dict = ..., 
        is_begin_only: bool = False, 
        indent: int = -1):
        return super().__add_element_by_text(text, tag_name, attribute, is_begin_only, indent)

    def __add_element(self, element: HtmlElement):
        # return super().__add_element(element)
        self.soup.body.append(element.get_tag())