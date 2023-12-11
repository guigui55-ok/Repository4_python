#sdmz9n41vur3vq

import sys
flag = False
if flag:
    sys.exit()
    # 実行されないことが確定しているならば、これ以降ソースを記述しない   
else:
    print('到達できないコードであるため、暗く表示される')

def test_func():
    return
    print('到達できないコードであるため、暗く表示される')

def test_func2():
    raise Exception()
    print('到達できないコードであるため、暗く表示される')

def test_func3():
    test_func2()
    print('到達できないコードであるため、暗く表示される')
    
def test_func4():
    if False:
        print('到達できないコードであるため、暗く表示される')

def test_func5():
    for i in range(10):
        print(i)
    else:
        return
    print('到達できないコードであるため、暗く表示される')
    

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Selenium設定
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)