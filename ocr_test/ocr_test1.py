# https://gammasoft.jp/blog/ocr-by-python/
import os
from PIL import Image
import pyocr
import pyocr.builders

# 1.インストール済みのTesseractのパスを通す
path_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract
    print('os.environ[PATH] = ' + str(os.environ["PATH"]))
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

# 4.ＯＣＲ実行
builder = pyocr.builders.TextBuilder()
result = tool.image_to_string(img_org, lang="jpn", builder=builder)

print(result)