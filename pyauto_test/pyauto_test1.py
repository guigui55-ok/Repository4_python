"""

https://qiita.com/konitech913/items/301bb63c8a69c3fcb1bd
pip install pyautogui

"""
import pyautogui

def main():
    img_dir_path = r'C:\Users\OK\source\repos\test_media_files\pyauto'
    import os

    # (, )の位置にマウスカーソルを移動
    pyautogui.moveTo(50,50)
    
    # クリック
    pyautogui.click()
    pyautogui.doubleClick()
    pyautogui.easeInSine()

    return

if __name__ == '__main__':
    main()