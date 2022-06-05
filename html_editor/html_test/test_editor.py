import sys,pathlib

path = str(pathlib.Path(__file__).parent.parent)
sys.path.append(path)

from html_editor import HtmlEditor, HtmlElement
from html_writer import HtmlWriter
from html_const import HtmlTagName

def editer_test_main():
    html_path = str(pathlib.Path(__file__).parent.joinpath('test.html'))
    css_path = str(pathlib.Path(__file__).parent.joinpath('test.html'))
    editor = HtmlEditor()

    editor.create_html(html_path)
    el = HtmlElement('test text',HtmlTagName.DIV)
    editor.add_element(el)
    editor.update_file()

def write_test_main():
    html_path = str(pathlib.Path(__file__).parent.joinpath('test_writer.html'))
    css_path = str(pathlib.Path(__file__).parent.joinpath('test.css'))
    writer = HtmlWriter()

    writer.create_html_content(html_path)
    el = HtmlElement('test text',HtmlTagName.DIV)
    writer.add_to_file(el)
    img_attr = {'src':'test.png','alt':'test_image','class':'image_class'}
    el = HtmlElement('',HtmlTagName.IMG,img_attr)
    writer.add_to_file(el)
    writer.add_outline_body()
    writer.add_css_file_path(css_path)


if __name__ == '__main__':
    # editer_test_main()
    write_test_main()