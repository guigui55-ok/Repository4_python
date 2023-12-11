# from pynput import mouse
# from pyautogui import *
# from threading import *

# def click_ren1():
#     for i in range(10):
#         mouseDown(x=None,y=None)
#         mouseUp(x=None,y=None)

# def click_ren2():
#     for i in range(10):
#         click(x=None,y=None)

# def key_ren():
#     for i in range(10):
#         press("z")

# def on_move(x, y):
#     pass

# def on_click(x, y, button, pressed):
#     click_ren1()

#     if not pressed:
#          return False

# def on_scroll(x, y, dx, dy):
#     pass

# Collect events until released
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()
 
# mouse_listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)

# mouse_listener.start()
# import time
# for _ in range(10):
    # time.sleep(0.2)

import pyautogui
import time
i = 0
# for i in range(10):
# print('*' + str(i))
# # pyautogui.click()
# pyautogui.click(20, 100, button="right", duration=0.5)
# time.sleep(0.2)
# pyautogui.mouseUp()
# time.sleep(0.2)
# pyautogui.click(25, 105, button="left", duration=0.5)
# pyautogui.mouseUp()
# # time.sleep(0.2)
# pyautogui.move()
# # time.sleep(0.2)

# for i in range(5):
#     print('*' + str(i))
#     pyautogui.moveTo(100,100, duration=0.5)
#     pyautogui.click(
#         x=100,
#         y=100,
#         clicks=1,
#         interval=0.01,
#         button=pyautogui.LEFT,
#         duration=0.2,
#         logScreenshot=True,
#         _pause=False
#     )
#     pyautogui.moveTo(300,300, duration=0.5)
    


#https://teratail.com/questions/o1rwu9gegec8hm

import ctypes

ULONG_PTR = ctypes.POINTER(ctypes.c_ulong)

# マウスイベントの情報
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ULONG_PTR)]


class INPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("mi", MOUSEINPUT)]

LPINPUT = ctypes.POINTER(INPUT)

SendInput = ctypes.windll.user32.SendInput
SendInput.argtypes = (ctypes.c_uint, LPINPUT, ctypes.c_int)
SendInput.restype = ctypes.c_uint

x, y = 200, 300
x = x * 65536 // 1920
y = y * 65536 // 1080
_mi = MOUSEINPUT(x, y, 0, (0x0001 | 0x8000), 0, None)
SendInput(1, INPUT(0, _mi), ctypes.sizeof(INPUT))