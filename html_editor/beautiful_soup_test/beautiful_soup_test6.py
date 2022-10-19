#https://codezine.jp/article/detail/12230


from tkinter.tix import Form
from bs4 import BeautifulSoup, PageElement
from bs4 import element
from bs4.element import Comment
from bs4.element import Tag
import requests

def get_read_path():
    import pathlib
    dir_path = str(pathlib.Path(__file__).parent.parent.joinpath('html_test'))
    file_name='ダウンロード.htm'
    file_name = 'test_writer2.html'
    path = str(pathlib.Path(dir_path).joinpath(file_name))
    ###
    return path

#################################################

from bs4.dammit import EntitySubstitution
def uppercase_and_substitute_html_entities(str):
    return EntitySubstitution.substitute_html(str.upper())

from bs4.formatter import Formatter

#################################################
def test_main6():
    ### 
    #body のdivを置き換える2
    ###
    read_path = get_read_path()
    soup = BeautifulSoup(open(read_path), 'html.parser')
    ###
    tags = soup.select('div')
    print('tags len = {}'.format(len(tags)))

    print('//////')
    body_tag = soup.body
    print('body len = {}'.format(len(body_tag))) #8
    print('type = {}'.format(type(body_tag))) # Tag
    # child:PageElement=None
    # for child in body_tag.children:
    #     if child != '\n':
    #         print(child.text)
    # print('type = {}'.format(type(child)))

    divs = body_tag.find_all('div')
    last_div:Tag = divs[-1]
    print('last_div')
    print(type(last_div))
    print(last_div)
    # last_div.decompose()
    ###
    ### div > p をbodyの最後に追加する
    add_text = 'class abc text p'
    new_tag_p = soup.new_tag('p')
    new_tag_p.string = add_text
    attr = {'class':'class_abc'}
    new_tag_div = soup.new_tag('div', attrs=attr)
    new_tag_div.append(new_tag_p)

    soup.body.append(new_tag_div)
    ###

    print('/////////////')
    formatter = Formatter(indent=4)
    buf = soup.prettify(formatter=formatter)
    write_data(read_path, buf)
    return

#################################################

def write_data(read_path:str,wbuf):
    # print(buf)
    wpath = get_path(read_path)
    with open(wpath, 'w', encoding='utf-8')as f:
        f.write(wbuf)
    print('wpath = {}'.format(wpath))

def get_path(path:str):
    import os
    import datetime
    base_name = os.path.splitext(path)[0]
    dstr = datetime.datetime.now().strftime('_%y%m%d_%H%M%S_')
    file_name = base_name + dstr + os.path.splitext(path)[1]
    dir = os.path.dirname(path)
    return os.path.join(dir, file_name)


if __name__ == '__main__':
    test_main6()
