import sys
import pytesseract
from PIL import Image

from pathlib import Path
image_path = r'C:\Users\OK\Pictures\sample_db_image.png'
if not Path(image_path).exists():
    raise FileNotFoundError(image_path)

def image_to_text(image_path):
    # 画像を読み込む
    img = Image.open(image_path)

    # TesseractでOCRを実行
    text = pytesseract.image_to_string(img, lang='jpn')

    return text

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pass
        image_path = sys.argv[1]  # コマンドライン引数から画像ファイルのパスを取得
    else:
        print("Usage: python app.py <path_to_image>")
    text = image_to_text(image_path)
    print(text)