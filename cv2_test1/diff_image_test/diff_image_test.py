
import numpy as np
from PIL import Image
import sys

import traceback
import import_init

def get_paths():
    try:
        import pathlib,os
        dir_path = str(pathlib.Path(__file__).parent.parent)
        image_path = os.path.join(dir_path,'image','histgram')
        file_base = 'sample.png'
        base_path = os.path.join(image_path,file_base)
        if not os.path.exists(base_path):
            print('not exists : ' + base_path)
        return dir_path,base_path
    except:
        traceback.print_exc()
        
def main():
    try:        
        logger = import_init.initialize_logger_new()

        return
    except:
        traceback.print_exc()

def test():
    try:
        dir_path = r'C:\Users\OK\source\repos\Repository4_python\movie_test\write_frames_test\write_frames_result_2112_062327'
        import os
        path_a = os.path.join(dir_path,'pad_dunsion_1.png')
        path_b = os.path.join(dir_path,'pad_dunsion_7.png')
        path_b = os.path.join(dir_path,'pad_dunsion_10.png')
        path_b = os.path.join(dir_path,'pad_dunsion_13.png')
        # 画像の読み込み
        image1 = Image.open(path_a)
        image2 = Image.open(path_b)

        # RGB画像に変換
        image1 = image1.convert("RGB")
        image2 = image2.convert("RGB")

        # NumPy配列へ変換
        im1_u8 = np.array(image1)
        im2_u8 = np.array(image2)

        # サイズや色数が違うならエラー
        if im1_u8.shape != im2_u8.shape:
            print("サイズが違います")
            sys.exit()



        # 負の値も扱えるようにnp.int16に変換
        im1_i16 = im1_u8.astype(np.int16)
        im2_i16 = im2_u8.astype(np.int16)

        # 差分配列作成
        diff_i16 = im1_i16 - im2_i16

        '''ここから作成する画像によって異なる処理'''

        # np.uint8型で扱える値に変換
        diff_n_i16 = ((diff_i16 + 256) // 2)

        # NumPy配列をnp.uint8型に変換
        diff_u8 = diff_n_i16.astype(np.uint8)

        # PIL画像に変換
        diff_img = Image.fromarray(diff_u8)

        '''ここまで作成する画像によって異なる処理'''

        # 画像表示
        diff_img.show()
        return
    except:
        traceback.print_exc()

test()