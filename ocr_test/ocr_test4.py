

import time
import cv2

import os
from PIL import Image
import pyocr
import pyocr.builders

# 1.インストール済みのTesseractのパスを通す
path_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract
    #print('os.environ[PATH] = ' + str(os.environ["PATH"]))
    print('path_tesseract add to os.environ[PATH]')
else:
    print('path_tesseract include os.environ[PATH]')

# 2.OCRエンジンの取得
pyocr.tesseract.TESSERACT_CMD = path_tesseract
tools = pyocr.get_available_tools()
tool = tools[0]


time.sleep(2)

# 3.原稿画像の読み込み
dir = r'C:\Users\OK\source\repos\test_media_files\test_jpg'
file_name = 'Screenshot_20230205-134825.jpg'
read_path = os.path.join(dir, file_name)
img_path = read_path
print('img_path={}'.format(img_path))

from pathlib import Path
write_path_obj = os.path.dirname(read_path)
# file name
file_name = str(os.path.splitext(read_path)[0]) + '_ret' + \
     str(os.path.splitext(read_path)[1])
# out_path = str(write_path_obj) + '\\' + file_name
out_path = file_name

img = Image.open(img_path)

lang = 'jpn'
word_boxes = tool.image_to_string(
    img,
    lang=lang,
    builder=pyocr.builders.WordBoxBuilder(tesseract_layout=6)
)

out = cv2.imread(img_path)
content_str = ''
for d in word_boxes:
    content_str += str(d.content)
    print('word_box.content = ' + str(d.content))
    print('word_box.position = ' + str(d.position))
    cv2.rectangle(out, d.position[0], d.position[1], (0, 0, 255), 2) #d.position[0]は認識した文字の左上の座標,[1]は右下
    cv2.imwrite(out_path.format(lang, 'word_boxes'), out)
    x1,y1 = d.position[0]
    x2,y2 = d.position[1]
    print('x1,y1 = ' + str(x1) + ' , ' + str(y1))
    print('x2,y2 = ' + str(x2) + ' , ' + str(y2))
    # if(d.content=='Anaconda3'): #Anacondaのアイコンを認識したらクリックする
    #     x3 = (x1+x2)/2+50
    #     y3 = (y1+y2)/2+100
    #     pg.click(x3,y3)
print('content_str:')
print(content_str)
print('out_path = ' + out_path)