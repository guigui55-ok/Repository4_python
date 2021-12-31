# https://tomomai.com/python-histogram/
import traceback
import cv2
from matplotlib import pyplot as plt
import import_init
from common_util.cv2_image.cv2_result import Cv2Result

def get_paths():
    try:
        import pathlib,os
        dir_path = str(pathlib.Path(__file__).parent.parent)
        # dir_path = r'C:\Users\OK\source\repos\Repository4_python\cv2_test1\cut_sample\images'
        image_path = os.path.join(dir_path,'cut_sample','images')
        file_base = 'buttle2_64_0_0.png'
        base_path = os.path.join(image_path,file_base)
        if not os.path.exists(base_path):
            print('not exists : ' + base_path)
        return dir_path,base_path
    except:
        traceback.print_exc()

def print_hist(histgram):
    h = histgram
    print('histgram')
    print('max={} , min={} , shape = [ {} , {} ]'.format(
        h.max,h.min,h.shape[0],h.shape[1]))

def hist_test():
    try:
        img_dir, img_path = get_paths()
        print(img_path)

        import holoviews as hv
        hv.extension('matplotlib')

        img = cv2.imread(img_path)
        # RGB で取得、HSV ではなく
        img_1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        colors = ("r", "g", "b")
        for i, channel in enumerate(colors):
            histgram = cv2.calcHist([img_1], [i], None, [256], [0, 256])
            ret = Cv2Result(histgram)
            ret.print_result()
            

            histgram = histgram.squeeze(axis=-1)
            curve = hv.Curve(histgram)
            curve
            print(curve)
            # print_hist(histgram)
            plt.plot(histgram, color = channel)
            plt.xlim([0, 256])
            print()
        plt.show()
    except:
        traceback.print_exc()

hist_test()