# https://tomomai.com/python-histogram/
import cv2
from matplotlib import pyplot as plt

import traceback
def hist_test():
    try:
        import pathlib,os
        file_name = 'abc.png'
        dir_path = str(pathlib.Path(__file__).parent)
        img_path = os.path.join(dir_path,'image',file_name)
        
        img = cv2.imread(img_path)
        img_1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        colors = ("r", "g", "b")
        for i, channel in enumerate(colors):
            histgram = cv2.calcHist([img_1], [i], None, [256], [0, 256])
            plt.plot(histgram, color = channel)
            plt.xlim([0, 256])
        plt.show()
    except:
        traceback.print_exc()

hist_test()