"""

pip3 install requests
pip3 install beautifulsoup4
from bs4 import BeautifulSoup

https://fich-labo.com/scraping/
https://www.twilio.com/blog/web-scraping-and-parsing-html-in-python-with-beautiful-soup-jp

"""
import requests
import shutil
from bs4 import BeautifulSoup,ResultSet

def main():
    url = 'https://fich-labo.com/scraping/'
    url_res = requests.get(url)

    soup = BeautifulSoup(url_res.content, "html.parser")
    # print(soup)

    link:ResultSet=None
    for link in soup.find_all('a'):
        print(link.get('href'))


def download(download_url,file_name):
    # Download the track
    r = requests.get(download_url, allow_redirects=True)
    with open(file_name, 'wb') as f:
        f.write(r.content)
main()