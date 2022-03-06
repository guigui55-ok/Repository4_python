
import import_init
import pyautogui

def main():
    try:
        #Enterキーを押す
        pyautogui.press('enter')
        #Spaceキーを押す
        pyautogui.press('space')

        #矢印の右（→）を押す
        pyautogui.press('right')
        #コピーする
        pyautogui.hotkey('ctrl', 'c')
        #貼付する
        pyautogui.hotkey('ctrl', 'v')
        #ウィンドウを切り替える
        pyautogui.hotkey('alt', 'tab')
        return
    except:
        return

"""
https://note.com/curama/n/nf0c35ca92fcb

"""