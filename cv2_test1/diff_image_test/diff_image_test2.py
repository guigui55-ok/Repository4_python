
import numpy as np
from PIL import Image
import sys

import traceback
import import_init

def get_paths():
    try:
        import pathlib
        import os
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

def print_data(data,not_print_data = None):
    print('=========================================')
    thresh = 128
    data = (data > thresh) * data
    if not_print_data == None:
        not_print_data = '[{} {} {}]'.format(thresh,thresh,thresh)
        not_print_data = '[{} {} {}]'.format(0,0,0)
    if len(data) > 0:
        for i in range(len(data)):
            buf = data[i] # 720:height
            for j in range(len(buf)):
                buf2 = buf[j] # 360:width
                for k in range(len(buf2)):
                    rgb = buf2[k]
                    # r = rgb[0]  # IndexError: invalid index to scalar variable.
                    # g = rgb[1] 
                    # b = rgb[2]
                if str(buf2) != not_print_data:
                    print('i(h) : j(i) = {} , {} | {}'.format(i,j,buf2))
                # 白255，黒0
    else:
        print(str(data))
    print('=========================================')

def test():
    try:
        dir_path = r'C:\Users\OK\source\repos\Repository4_python\movie_test\write_frames_test\write_frames_result_2112_062327'
        dir_path = r'C:\Users\OK\source\repos\test_media_files\movie_test_media_files\write_frames_result_2112_062327'
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
        ##########
        thresh = 128
        base = diff_u8
        # data = (base > thresh) * base # gray > black
        # data = (base < thresh) * base # ぼやける
        data = (base != thresh) * base # くっきりとなる
        not_print_data = '[{} {} {}]'.format(0,0,0)
        # print_data(data,not_print_data)
        diff_u8 = data
        ##########
        base_img = diff_u8
        im_bool = base_img > 128
        im_new = np.empty((*base_img.shape, 3))
        r, g, b = 255, 128, 32
        buf = im_new[:, :, 0]
        # print('ime_new = {}'.format(buf.tolist()))
        print('ime_new = {}'.format(buf.shape))
        # print(str(buf))
        """
        np.uint8(im_new)にてim_new配列の形状とデータタイプを確認し、
        それが画像として適切な形状（例えば、高さ×幅×色チャネル）とデータタイプ（np.uint8）を持つことを確認する必要があります
        """

        im_new[:, :, 0] = im_bool * r
        im_new[:, :, 1] = im_bool * g
        im_new[:, :, 2] = im_bool * b
        path = './numpy_binarization_color.png'


        Image.fromarray(np.uint8(im_new)).save(path)
        import pathlib
        print(pathlib.Path(path).resolve())
        # ret_img = Image.fromarray(np.uint8(im_new)) #TypeError
            # aise TypeError("Cannot handle this data type: %s, %s" % typekey) from e
            # TypeError: Cannot handle this data type: (1, 1, 3, 3), <f8
        # ret_img = Image.fromarray(im_new) #TypeError
        ##########

        # PIL画像に変換
        # diff_img = Image.fromarray(diff_u8)
        # ret_img = diff_img
        '''ここまで作成する画像によって異なる処理'''

        # 画像表示
        # ret_img.show()
        return
    except:
        traceback.print_exc()

if __name__ == '__main__':
    test()