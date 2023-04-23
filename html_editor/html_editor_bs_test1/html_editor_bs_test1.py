import pathlib
import sys

path_str = str(pathlib.Path(__file__).parent.parent)
print(path_str)
sys.path.append(path_str)
path_str = str(pathlib.Path(__file__).parent.parent.parent)
print(path_str)
sys.path.append(path_str)

import html_editor_main
import html_editor_bs
from html_editor_bs.html_editor_bs_main import HtmlEditor, HtmlElementBs, Tag, HtmlTagName


def main():
    file_name = 'table_sample.html'
    path = pathlib.Path(__file__).parent.joinpath(file_name)
    print(path)
    editor = HtmlEditor(path)
    attr = {'class':'add_p'}
    el = HtmlElementBs('tag_text', HtmlTagName.P, attr)
    editor.add_element(el)
    editor.update_file()
    return


if __name__ == '__main__':
    print()
    print('')
    main()