# https://toukei-lab.com/python-image


import matplotlib.pyplot as plt
import cv2
import numpy

import glob
import re
from pathlib import Path

_TARGET_DIR_PATH = r'C:\Users\OK\source\repos\test_media_files\imager_recognition_sub\traning_image_3po_all'

def get_target_dir_path(target_dir = None):
    if target_dir==None:
        target_dir = _TARGET_DIR_PATH
    print('target_dir_path = {}'.format(target_dir))
    if not Path(target_dir).exists():
        msg = 'Target dir path is nothing (path = {})'.format(target_dir)
        raise FileNotFoundError(msg)
    return target_dir


def get_image_path_list(target_dir, include_pattern_list=['*.jpg']):
    all_paths = []
    for pattern in include_pattern_list:
        paths = glob.glob(target_dir + '/' + pattern)
        if 0<len(list(paths)):
            all_paths.extend(paths)
    sorted(paths)
    print(len(all_paths))
    return all_paths

def read_csv(path):
    image = cv2.imread(path)
    if not isinstance(image, numpy.ndarray):
        print(' [None] path= {}'.format(path))
        return
    image.shape #(256, 256, 3)
    print(image.shape)

def main():
    print()
    print('****')
    dir_path = get_target_dir_path()
    paths = get_image_path_list(dir_path)
    for i,path in enumerate(paths):
        print(f'{i}:', end='')
        read_csv(path)

if __name__ == '__main__':
    main()