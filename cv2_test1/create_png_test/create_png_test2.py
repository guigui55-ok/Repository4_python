import cv2
import numpy as np

from enum import IntEnum
from enum import Enum

class const_mono(IntEnum):
    BLACK = 0
    WHITE = 255
    GRAY = 127

# http://pineplanter.moo.jp/non-it-salaryman/2019/03/24/post-7337/
# OpenCVでの色指定は逆のBGRらしくリバースが必要
class const_color(Enum):
    BLUE = [0,0,255]
    WHITE = [255,255,255]
    BLACK = [0,0,0]
    GRAY = [128,128,128]

def create_png(path,width,height,color=0):
    try:
        img = np.zeros((height, width, 3))
        img += color
        cv2.imwrite(path,img)
    except:
        import traceback
        traceback.print_exc()

def main():
    try:
    
        import pathlib
        img_dir = str(pathlib.Path(__file__).parent)
        file_name = 'create_test2.png'
        import os
        path = os.path.join(img_dir,file_name)
        color = const_color.BLACK.value[::-1]
        width = 720
        height = 1440
        create_png(path,width,height,color)
        print(path)
    except:
        import traceback
        traceback.print_exc()

main()