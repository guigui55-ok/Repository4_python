
if __name__ == '__main__':
    import __init__

from bs4 import BeautifulSoup
from html_editor import HtmlEditor,HtmlElement,HtmlTagName
from html_writer import HtmlWriter
from bs4.element import Tag

class HtmlEditorBs(HtmlEditor):
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
    
    def add_element(self, element: Tag):
        # return super().add_element(element)
        self.soup.body.append(element)

    def update_file(self):
        # return super().update_file()
        wbuf = self.soup.prettify()
        with open(self.html_path,'w',encoding='utf-8')as f:
            f.write(wbuf)



def test_main():
    return

if __name__ == '__main__':
    test_main()
    
    