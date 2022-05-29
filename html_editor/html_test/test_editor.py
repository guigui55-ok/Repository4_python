import sys,pathlib
path = str(pathlib.Path(__file__).parent.parent)
sys.path.append(path)

from html_editor import HtmlEditor, HtmlElement
from html_const import HtmlTagName

def main():
    html_path = str(pathlib.Path(__file__).parent.joinpath('test.html'))
    editor = HtmlEditor(html_path)

    editor.create_html()
    el = HtmlElement('test text',HtmlTagName.DIV)
    editor.add_element(el)
    editor.update_file()

if __name__ == '__main__':
    main()