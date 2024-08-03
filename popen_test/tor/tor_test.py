
"""
PythonでTorを使ってIPを変える for Windows
https://qiita.com/kawagoe6884/items/2c4a2476db65e9bedb89

pip install PySocks
Torブラウザのダウンロード

"""

# coding:utf-8
import subprocess
import getpass
import time
import socks
import socket
import urllib.request

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# ------ Torの起動 ------
def Tor_start():
    # 下1行のコメントアウト切り替えで出力プロセスを表示
    # subprocess.call(r'taskkill /F /T /IM firefox.exe')
    # 下1行のコメントアウト切り替えで出力プロセスを非表示
    subprocess.call(r'taskkill /F /T /IM firefox.exe', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    Tor = f'"C:\\Users\\{getpass.getuser()}\\Desktop\\Tor Browser\\Browser\\firefox.exe" --headless'
    subprocess.Popen(Tor)
    time.sleep(8)