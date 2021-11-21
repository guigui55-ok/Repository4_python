# https://gammasoft.jp/blog/ocr-by-python/
#元の画像を加工してOCRを実行
#背景による影響を軽減するために、画像を加工します。ここでは、以下のように
# ocr_card_filter.py

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
# PATH が通っていないとエラーとなる?
#Exception has occurred: IndexError
#list index out of range

# 3.原稿画像の読み込み
read_path = r'C:\Users\OK\source\repos\Repository4_python\ocr_test\images\ocr_test.png'
read_path = r'C:\Users\OK\source\repos\Repository4_python\ocr_test\images\screen_sever.png'


img_org = Image.open(read_path)
img_rgb = img_org.convert("RGB")
pixels = img_rgb.load()

# 原稿画像加工（黒っぽい色以外は白=255,255,255にする）
c_max = 169
for j in range(img_rgb.size[1]):
    for i in range(img_rgb.size[0]):
        if (pixels[i, j][0] > c_max or pixels[i, j][1] > c_max or
                pixels[i, j][0] > c_max):
            pixels[i, j] = (255, 255, 255)

# ＯＣＲ実行
builder = pyocr.builders.TextBuilder()
result = tool.image_to_string(img_rgb, lang="jpn", builder=builder)

print('result:')
print(result)