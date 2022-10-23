

if __name__ == '__main__' or __name__ == 'html_editor':
    import html_const
    from html_const import HtmlTagName
    from html_const import tag_is_closing_type
else:
    import html_editor.html_const as html_const
    from html_editor.html_const import HtmlTagName
    from html_editor.html_const import tag_is_closing_type

NEW_LINE = html_const.NEW_LINE
INDENT = '    '

class HtmlElement():
    def __init__(
        self,
        tag_text:str='',
        tag_name:str=HtmlTagName.DIV,
        attribute:dict={},
        indent:int=-1) -> None:
        """
        
        """
        self.tag_text = tag_text
        self.tag = tag_name
        self.attribute = attribute
        self.child_elements:'list[HtmlElement]' = []
        self.indent_space = 4
        if indent<0:
            self.indent = 0
        else:
            self.indent = indent
    @classmethod
    def create_html_element_img(
        cls,src_image_path:str,alt:str='',add_attribute:dict={},indent:int=-1):
        attr_dict = {
                'src':src_image_path,
                'alt':alt
        }
        attr_dict.update(add_attribute)
        el = HtmlElement('', HtmlTagName.IMG,attr_dict)
        return el

    def add_class_name(self, class_name:str):
        if len(self.attribute)<1:
            self.attribute = {'class':class_name}
        else:
            for k in self.attribute.keys():
                if k=='class':
                    buf = self.attribute['class'] 
                    buf  += ' ' + class_name
                    self.attribute['class'] = buf
                    break

    def set_attribute(self,attribute_name:str,value:str):
        self.attribute[attribute_name] = value
    def get_attribute(self,attribute_name:str):
        return self.attribute[attribute_name]
    def add_element(self,element:'HtmlElement'):
        self.child_elements.append(element)
    def __get_indent_str(self,element:'HtmlElement'):
        ret = ''
        for _ in range(element.indent):
            for _ in range(self.indent_space):
                ret += ' '
        return ret
    def cnv_html_element_to_str(self,element:'HtmlElement'=None):
        """
        HtmlElementをタグ文字列に変換する (htmlへ書き込むため)
         HtmlElement [tag_name=HtmlTagName.P, text='test', {'class':'p_tag'}]
          -> <p class="p_tag">test</p>
        """
        if element==None: 
            element=self
        ret = ''
        ret += self.__get_indent_str(element)
        ret += '<'
        ret += element.tag
        ### add Attribute Front Tag
        keys = element.attribute.keys()
        attr = ''
        for key in keys:
            attr += key + '="' + element.get_attribute(key) + '" '
        ret += self.__align_str_attr(attr) + '>'
        ###
        ### add Tag Text
        if not tag_is_closing_type(element.tag):
            ret += element.text
        ### add Child Element Tag
        buf = ''
        for child in element.child_elements:
            buf += self.cnv_html_element_to_str(child)
        if buf != '':
            ret += NEW_LINE + buf
        ###
        ### add End Tag
        if element.tag == HtmlTagName.BODY:
            ret += self.__get_indent_str(element) 
        if not tag_is_closing_type(element.tag):
            ret += '</' + element.tag + '>' + NEW_LINE
        else:
            ret += NEW_LINE
        ###
        return ret
    
    def __align_str_attr(self,value:str):
        """
        """
        if len(value)<1:
            return value
        if value == ' ':
            return ''
        else:
            if value[0]!=' ':
                value = ' '+value
            if value[-1]==' ':
                return value[:-1]
            else:
                return value

    
class HtmlEditor():
    def __init__(self,html_path:str='') -> None:
        self.html_path = html_path
        self.body:HtmlElement = HtmlElement('',HtmlTagName.BODY,{},1)
        self.indent_space = 4
    
    def init_values(self,css_path:str=''):
        self.css_path = css_path
    
    def get_default_basic_path(self,basic_html_file_path:str=''):
        import pathlib
        if basic_html_file_path=='':
            basic_html_file_path = str(pathlib.Path(__file__).parent.joinpath(html_const.BASIC_FILE_NAME))
        return basic_html_file_path
    
    def create_html(self,html_path:str='',basic_html_file_path:str=''):
        if html_path=='': html_path = self.html_path
        else: self.html_path = html_path
        import shutil
        src_path = self.get_default_basic_path(basic_html_file_path)
        shutil.copy(src_path,html_path)

    def add_element_by_text(
        self,text:str='',
        tag_name:str=HtmlTagName.DIV,
        attribute:dict={},
        indent:int=-1):
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
        return element.__get_indent_str(element)
        ret = ''
        for _ in range(element.indent):
            for _ in range(self.indent_space):
                ret += ' '
        return ret
    def __cnv_html_element_to_str(self,element:HtmlElement):
        return element.cnv_html_element_to_str(element)
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
        return HtmlElement().__align_str_attr(value)
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


