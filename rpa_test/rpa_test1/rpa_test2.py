
import import_init
import pyautogui

def main():
    try:
        #PyAutoGUIをインポート
        #毎回pyautoguiと書くのが面倒くさいのでpgで略せるように宣言
        import pyautogui as pg
        #待機をするためのtimeライブラリをインポート
        import time

        #Chromeのショートカットキーで一番左のタブに移動
        #ここに検索ワードリストのスプレッドシートを置く
        pg.hotkey('ctrl', '1')
        #1秒待機
        time.sleep(1)
        #ショートカットでコピーを実行
        pg.hotkey('ctrl', 'c')
        #1秒待機
        time.sleep(1)

        #ショートカットで新しいタブを開く
        pg.hotkey('ctrl', 't')
        #1秒待機
        time.sleep(1)
        #ショートカットで貼付を実行
        pg.hotkey('ctrl', 'v')
        #1秒待機
        time.sleep(1)
        #Enterを押して検索を実行
        pg.press('enter')
        #2秒待機
        time.sleep(2)

        #ショートカットキーで印刷ウィンドウを開く
        pg.hotkey('ctrl', 'p')
        #4秒待機
        time.sleep(4)
        #印刷の実行、予めプリンタをPDFに設定しておいてください
        pg.press('enter')
        #3秒待機、
        time.sleep(3)
        #PDFファイル保存の実行
        pg.press('enter')
        #1秒待機
        time.sleep(1)

        #再びChromeの一番左のタブに移動
        pg.hotkey('ctrl', '1')
        #1秒待機
        time.sleep(1)
        #一つ下のセルに移動、次の検索ワードへ
        pg.press('down')

        #一番上の処理に戻って繰り返すことでリストのワードの検索結果を全てPDF化することができる
        return
    except:
        return

"""
https://note.com/curama/n/nf0c35ca92fcb

"""