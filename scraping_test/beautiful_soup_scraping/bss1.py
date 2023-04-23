
# https://www.twilio.com/ja/blog/web-scraping-and-parsing-html-in-python-with-beautiful-soup-jp
# https://ai-inter1.com/beautifulsoup_1/


import re

import requests
from bs4 import BeautifulSoup


def main():
    vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
    html_text = requests.get(vgm_url).text
    soup = BeautifulSoup(html_text, 'html.parser')


    if __name__ == '__main__':
        attrs = {
            'href': re.compile(r'\.mid$')
        }

        tracks = soup.find_all('a', attrs=attrs, string=re.compile(r'^((?!\().)*$'))

        count = 0
        for track in tracks:
            print(track)
            count += 1
        print(len(tracks))


if __name__ == '__main__':
    main()