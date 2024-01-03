# https://toukei-lab.com/python-image

import matplotlib.pyplot as plt
import glob
import cv2
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
# from tensorflow import keras
# from tensorflow import _KerasLazyLoader as keras
# from tensorflow.keras import layers, models
# from tensorflow.keras.utils import to_categorical
import keras
from keras import layers, models
from keras.utils import to_categorical

"""
https://and-engineer.com/articles/Y52w-BIAACUAW8B5

pip install tensorflow

TensorFlowの動作確認を行う
import tensorflow as tf
print(tf.__version__)

-----
from sklearn.model_selection import train_test_split
ModuleNotFoundError: No module named 'sklearn'
pip install scikit-learn

-----


"""
import numpy
from pathlib import Path

def _debug_print(value, debug_flag:bool=True):
    if debug_flag:
        print(str(value))

import math

_TRAINING_FILE_PATH = r'C:\Users\OK\source\repos\test_media_files\imager_recognition_sub\train.csv'
def get_training_data_file_path(path=None):
    if path ==None:
        path = _TRAINING_FILE_PATH
    if not Path(path).exists():
        msg = 'Training file is nothing (path = {})'.format(path)
        raise FileNotFoundError(msg)
    return path

class Cv2Image():
    def __init__(self, path=None) -> None:
        self.path = path
        self.debug = True
        self.image = None
        self.height = 0
        self.width = 0
        self.channels = 0
    
    def debug_print(self, value='', flag:bool=None):
        if flag ==None:
            flag = self.debug
        _debug_print(flag, value)

    def get_path(self, path=None):
        if path==None:
            path = self.path
        return path

    def read_csv(self, path=None):
        path = self.get_path(path)
        image = cv2.imread(path)
        # image = cv2.imread(path,cv2.IMREAD_COLOR)
        self.image = image
        if not isinstance(image, numpy.ndarray):
            self.debug_print(' [None] path= {}'.format(path))
            return
        # image.shape #(256, 256, 3)
        # print(image.shape)
        self._set_image_data()
    
    def image_is_valid(self):
        if not isinstance(self.image, numpy.ndarray):
            return False
        return True

    def _set_image_data(self):
        height, width, channels = self.image.shape[:3]
        self.height = height
        self.width = width
        self.channels = channels

    
    def get_aspect_ratio_w_h(self):
        # 最大公約数
        num = math.gcd(self.height, self.width)
        w, h = self.width/num, self.height/num
        return w,h
    
    def get_aspect_ratio_str(self):
        w,h = self.get_aspect_ratio_w_h()
        return '{} : {}'.format(w,h)

################################################################################
################################################################################
class ImageDataCreater():
    def __init__(self) -> None:
        self.image_list:list[numpy.ndarray] = []
        self.image_obj_list:list[Cv2Image] = []

    def set_image_from_paths(self, paths, limit=-1):
        if limit == None: limit = -1
        image_list = []
        for i, path in enumerate(paths):
            image_obj = Cv2Image(path)
            image_obj.read_csv()
            if not image_obj.image_is_valid():
                image_obj.debug_print(' [None] path= {}'.format(path))
                continue
            self.image_obj_list.append(image_obj)
            image_list.append(image_obj.image)
            if 0 < limit:
                if limit < i:
                    print('set_image_from_paths : count over limit {}'.format(limit))
                    break
        self.image_list = image_list


from ir_preapare_test1 import get_image_path_list
from ir_preapare_test1 import get_target_dir_path

################################################################################
################################################################################
def main():
    print()
    print('******')
    target_dir_path = get_target_dir_path()
    paths = get_image_path_list(target_dir_path)
    training_path = get_training_data_file_path(None)
    df_label = pd.read_csv(training_path)
    # pandas.errors.EmptyDataError: No columns to parse from file
    # read_csv と read_table は空のファイルでは機能しません
    # https://github.com/pandas-dev/pandas/issues/46048

    image_list = []
    # for i, path in enumerate(paths):
    #     image_obj = Cv2Image(path)
    #     image_obj.read_csv()
    #     if not image_obj.image_is_valid():
    #         image_obj.debug_print(' [None] path= {}'.format(path))
    #         continue
    #     image_list.append(image_obj.image)
    #     if 100 < i:break
    list_creater = ImageDataCreater()
    limit = -1 #No limit
    limit = 100
    image_list = list_creater.set_image_from_paths(paths, limit)
    
    # 続いて得られた画像の画素値を255で割返して正規化していきます。
    file_list = [file.astype(float)/255 for file in image_list] 
    # 画像データとラベルデータの塊を学習データと検証データに分けていきます。
    train_x, valid_x, train_y, valid_y = train_test_split(file_list, df_label, test_size=0.2)
    # train_y, valid_y をダミー変数化
    train_y = to_categorical(train_y["gender_status"])
    valid_y = to_categorical(valid_y["gender_status"])
    # 続いて、リスト型になっている画像データを配列型に直してあげます。
    train_x = np.array(train_x)
    valid_x = np.array(valid_x)


if __name__ == '__main__':
    main()