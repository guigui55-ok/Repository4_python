import pynput
from pynput import keyboard
import traceback

def main():
    try:
        # pynput.keyboard.Listener
        return
    except:
        traceback.print_exc()

main()

# マウス・キーボード監視
import pynput

# キーを押したときの処理
def press(key):
    try:
        # 英字キーを入力したときはこっちに行くみたい
        print(key.char)
    except AttributeError:
        # Enterやタブなど特殊なキーはこっち
        print(key)

# キーを離したときの処理
def release(key):
    print(key)
    if key == pynput.keyboard.Key.esc:
        return False

# クリックしたときの処理
def click(x, y, button, pressed):
    print(x, y)
    # 押したときだけ処理するならpressedを追加
    if pressed:
        print('pressed')
    else:
        print('release')

# キーボードリスナー起動 押したときと離したときのイベントを取得
keylistener = pynput.keyboard.Listener(on_press=press,on_release=release)
keylistener.start()

# マウスリスナー起動 クリックしたときのイベントを取得
with pynput.mouse.Listener(on_click=click) as mouselistener:
    mouselistener.join()