

import re

import requests
from bs4 import BeautifulSoup

def get_text_url(url):
    url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
    url = 'https://sports.yahoo.co.jp/keiba/race/denma/2306030111/'
    html_text = requests.get(url).text
    return html_text

def get_text_html_local(path_str):
    with open(path_str, 'r', encoding='utf-8')as f:
        buf = f.read()
    return buf

def main():
    path_str = r'C:\Users\OK\source\repos\test_media_files\scraping\test1.html'
    html_text = get_text_html_local(path_str)
    # html_text = get_text_url('')
    
    # soup = BeautifulSoup(html_text, 'html5lib')
    # 例外が発生しました: FeatureNotFound
# Couldn't find a tree builder with the features you requested: html5lib. Do you need to install a parser library?

    soup = BeautifulSoup(html_text, 'html.parser')

    if __name__ == '__main__':
        tracks = soup.find_all('a')

        count = 0
        for track in tracks:
            print(track)
            count += 1
            # if 15 < count:
            #     break
        print(len(tracks))


if __name__ == '__main__':
    print()
    print('******')
    main()