
if __name__ == '__main__':
    import __init__

import os
from bs4 import BeautifulSoup
from html_editor.html_editor_main import HtmlEditor,HtmlTagName
from html_editor.html_editor_main import HtmlElement as HtmlElementbase
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

    @classmethod
    def cnv_to_html_element_bs(cls,element:'HtmlElementbase'):
        el_bs = HtmlElementBs(
            tag_text=element.tag_text,
            tag_name=element.tag,
            attribute=element.attribute
        )
        return el_bs

    def cnv_html_element_to_tag(self):
        # attrs = self.attribute
        # tag = soup.new_tag(self.tag, attrs=attrs)
        # tag.string = self.tag_text
        tag = self.get_tag_single(self)
        self.child_tags = []
        ch:HtmlElement = None
        for ch in self.child_elements:
            # c_attrs = ch.attribute
            # c_tag = soup.new_tag(ch.tag, attrs=c_attrs)
            # c_tag.string = self.text
            #
            # c_tag = ch.get_tag_single(ch)
            c_tag = ch.cnv_html_element_to_tag()
            self.child_tags.append(c_tag)
            tag.append(c_tag)
        return tag

    def get_tag_single(self,element:'HtmlElement'):
        soup = BeautifulSoup()
        if tag_is_closing_type(element.tag):
            ret = element.cnv_html_element_to_str()
            #BeautifulSoup.new_tagを使用した場合
            #imgなどの閉じるが必要ないタグでも<img></img>となってしまうので
            #HtmlElement.cnv_html_element_to_str を使用してstr:"<img ~ />"とする
            #この場合タグデータが文字列となり扱いにくいので、
            #spanタグ(bs4.element.Tag)の中に入れて扱う
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


################################################################################
################################################################################
################################################################################

class HtmlEditorBs(HtmlEditor,HtmlWriter):
    def __init__(self, html_path: str = '') -> None:
        super().__init__(html_path)
        self.init_values_html_writer(html_path)
        
        self.body:Tag = None
        self.soup = None

    def init_values(self,css_path:str=''):
        self.css_path = css_path
        self.js_path = ''

    def create_html(self,html_path:str='',basic_html_file_path:str='', encoding='cp932'):
        super().create_html(html_path, basic_html_file_path)
        self.soup = BeautifulSoup(
            open(self.html_path, encoding=encoding), 'html.parser')

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
        """ write file """
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
        """ save_soup_to_file (write file)"""
        # """
        # bodyタグの前後を追記する
        #  メインコンテンツ部も追記している
        #   <body><div class="main-contents"></div></body> 
        # """
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
    def add_css_file_path(self, css_path: str, absolute_path:str='./'):
        # return super().add_css_file_path(css_path)
        if self._is_exists_css_path(css_path, absolute_path):
            print('[WARNING]css_path is not exists. [path={}[abs={}]]'.format(css_path, absolute_path))
            print('FILE {} , {}:'.format(__file__, 'add_css_file_path'))
        if css_path=='':
            css_path = self.css_path
        css = absolute_path + os.path.basename(css_path)
        header_tag = self.soup.find('head')
        attr = {"rel":"stylesheet"}
        new_tag = self.soup.new_tag(
            'link',href=css, attrs=attr)
        header_tag.append(new_tag)

    def _is_exists_str_in_file(self, path: str, value: str):
        return super()._is_exists_str_in_file(path, value)
    
    def _replace_str_to_file(self, path: str, target_value: str, replace_value: str):
        return super()._replace_str_to_file(path, target_value, replace_value)
    
    def _replace_line_to_file(self, path: str, target_value: str, replace_line: str):
        return super()._replace_line_to_file(path, target_value, replace_line)
    
    def get_default_basic_path(self, basic_html_file_path: str = ''):
        return super().get_default_basic_path(basic_html_file_path)
    
    def create_html_content(self, html_path: str = '', basic_html_path:str=''):
        # return super().create_html_content(html_path)
        if html_path == '': html_path = self.html_path
        self.create_html(html_path, basic_html_path)

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

    def add_css_file_path_list(self, css_path: str, absolute_path: str = './'):
        super().add_css_file_path_list(css_path, absolute_path)
        css = os.path.basename(css_path)
        value = absolute_path + css
        self.add_css_file_path(value)

    def add_css_file_path_from_file(self, css_file_path: str, absolute_path_from_root: str = './'):
        # return super().add_css_file_path_from_file(css_file_path, absolute_path_from_root)
        self.add_css_file_path_list(css_file_path,absolute_path_from_root)

    def write_css_path(self):
        # return super().write_css_path()
        for css_tag in self.css_tags:
            self._create_css_tag(css_tag.path, css_tag.absolute_path)

    def _create_css_tag(self, css_file_path: str, absolute_path_from_root: str = './'):
        # return super()._create_css_tag(css_file_path, absolute_path_from_root)
        # path = self._get_css_absolute_path(css_file_path, absolute_path_from_root)
        # indent = self._get_indent(self.indent_space)
        # tag = indent + html_const.CSS_TAG_SAMPLE.replace(
        #     html_const.REPLACE_VALUE,path) + NEW_LINE
        # self._insert_str_to_file(self.html_path, '</head>',tag)
        self.add_css_file_path(css_file_path, absolute_path_from_root)

    def add_tag_to_body(self,add_element):
        self.add_tag_to(add_element, 'body')


    def clear_tag(
        self,
        tag_name=None,
        attrs={},
        recursive=True,
        text=None,
        limit=None,
        index:int=-1,
        **kwargs
        ):
        """
        既存のタグを削除する
         （soup.find で検索して見つかったタグリストのindexで指定したタグをclearする）
        Args:
            tag_name: 対象のタグ名 （soup.findで使用する）
            attrs : 対象のタグ属性 （soup.findで使用する）
            recursive : （soup.findで使用する）
            text : （soup.findで使用する）
            limit : 使用していません
            index : soup.find で複数見つかったときに指定する(default=-1)
        """
        """
        Memo:
            https://beautiful-soup-4.readthedocs.io/en/latest/
            clear
            extract
            decompose
            replace_with
        """
        tags = self.soup.find(
            tag_name,attrs,recursive,text=text,kwargs=kwargs)
        if len(tags)==1:
            tags.clear()
        else:
            pass
            tags = self._get_tag_list_after_find(tags)
            # add = add_element.get_tag()
            # # 240105 リストの値が「\n」の時は以下のエラーとなる
            # # tag_list[index].append(add_element.get_tag())
            # # AttributeError  NavigableString' object has no attribute 'contents'
            # tags[index].append(add)
            for tag in tags:
                tag.clear()

    def add_tag_to(
        self,
        add_element:HtmlElementBs,
        tag_name=None,
        attrs={},
        recursive=True,
        text=None,
        limit=None,
        index:int=-1,
        **kwargs
        ):
        """
        既存のタグにタグを新たに追加する
         （soup.find で検索して見つかったタグリストのindexで指定したものにadd_elementが追加される）
        Args:
            add_element: 新たに追加するタグ
            tag_name: 追加される対象のタグ名 （soup.findで使用する）
            attrs : 追加される対象のタグ属性 （soup.findで使用する）
            recursive : （soup.findで使用する）
            text : （soup.findで使用する）
            limit : 使用していません
            index : soup.find で複数見つかったときに指定する(default=-1)

        """
        tags = self.soup.find(
            tag_name,attrs,recursive,text=text,kwargs=kwargs)
        if len(tags)==1:
            tags.append(add_element.get_tag())
        else:
            tags = self._get_tag_list_after_find(tags)
            add = add_element.get_tag()
            # 240105 リストの値が「\n」の時は以下のエラーとなる
            # tag_list[index].append(add_element.get_tag())
            # AttributeError  NavigableString' object has no attribute 'contents'
            tags[index].append(add)
    
    def _get_tag_list_after_find(self, tags)->'list[Tag]':
        """
        soup.find で取得した戻り値からタグのリストを取得する
         要素が改行のみのデータがあるのでそれは除外している
        """
        # tag_list = [t for t in tags]
        # tag_list = list(tags)
        ret = []
        tag:Tag = None
        for tag in tags:
            if '\n' == tag:
                continue
            ret.append(tag)
        return ret
        
        """
        以下のように改行のみの時があるのでそれは除外する
0:
'\n'
1:
<tr>
<th>番号</th>
<th>コメント</th>
<th>スマホ画面</th>
</tr>
2:
'\n'
3:
<tr>
<td>1</td>
<td>コメント内容A</td>
<td><img alt="スマホ画面A" src="placeholder.jpg" style="width:100px;height:100px;"/></td>
</tr>
4:
'\n'
5:
<tr>
<td>2</td>
<td>コメント内容B</td>
<td><img alt="スマホ画面B" src="placeholder.jpg" style="width:100px;height:100px;"/></td>
</tr>
6:
'\n'
        """

    # def add_tag_by_id(self,add_element:HtmlElementBs, id:str):
    #     tag = self.soup.find_all(id=id)
    #     tag.append(add_element.get_tag())

    # def add_tag_by_class(self,add_element:HtmlElementBs, class_name:str, index:int=-1):
    #     tags = self.soup.find_all(class_=class_name)
    #     tags[index].append(add_element.get_tag())

    def add_tag_to_last_div(self, add_element:HtmlElementBs):
        self.add_tag_to(add_element,'div')

    def _get_first_dict(attrs:dict):
        for k in attrs.keys():
            return k,attrs[k]


    def add_js_file_path(self, js_path: str, absolute_path:str='./'):
        # return super().add_css_file_path(css_path)
        if self._is_exists_css_path(js_path, absolute_path):
            print('[WARNING]js_path is not exists. [path={}[abs={}]]'.format(
                js_path, absolute_path))
            print('FILE {} , {}:'.format(__file__, 'add_css_file_path'))
        if js_path=='':
            js_path = self.js_path
        js = absolute_path + os.path.basename(js_path)
        header_tag = self.soup.find('head')
        # <script src="consoleLogDir.js"></script>
        attr = {"src":"stylesheet"}
        new_tag = self.soup.new_tag(
            'script',href=js, attrs=attr)
        header_tag.append(new_tag)