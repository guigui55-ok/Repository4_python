#https://ameblo.jp/soft3133/entry-12211807922.html

# https://pc.atsuhiro-me.net/entry/2013/12/04/232446

import urllib.request
import http.cookiejar
import gzip
import sys,os,os.path
from pathlib import Path

class Main():
    def __init__(self):
        self.cookie_dir:Path = Path(r'C:\Users\OK\source\repos\test_media_files\_test_info')
        self.cookiefile = "cookies.txt"
        self.cj = http.cookiejar.LWPCookieJar()
        if os.path.exists(self.cookiefile):
            self.cj.load(self.cookiefile)
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        urllib.request.install_opener(opener)
    
    def __del__( self ):
        save_path = str(self.cookie_dir.joinpath(self.cookiefile))
        self.cj.save(save_path)
        print("Cookie saved to "+self.cookiefile)
        print('path = {}'.format(save_path))
        
    def getURL(self,url):
        headers = { "User-Agent" :  "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)" }
        req = urllib.request.Request(url, None, headers)
        response = urllib.request.urlopen(req)
        charset = response.headers.get_content_charset()
        if charset==None:
            charset = "utf-8"
        #print(charset)
        dechtml = ""
        if response.info().get("Content-Encoding")=="gzip":
            dechtml = gzip.decompress(response.read())
        else:
            dechtml = response.read()
        html = dechtml.decode(charset,"ignore")
        open("response}.html","w",encoding=charset,errors="ignore").write(html)
        return

url = "http://www.google.com"
url = ''
Main().getURL(url)