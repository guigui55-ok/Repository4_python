# https://tomomai.com/python-histogram/
import cv2
from matplotlib import pyplot as plt

def get_paths():
    try:
        import pathlib,os
        dir_path = str(pathlib.Path(__file__).parent.parent)
        image_path = os.path.join(dir_path,'image','histgram')
        file_base = 'pad_dunsion.png'
        base_path = os.path.join(image_path,file_base)
        if not os.path.exists(base_path):
            print('not exists : ' + base_path)
        return dir_path,base_path
    except:
        traceback.print_exc()
        
import traceback
def hist_test():
    try:
        img_dir, img_path = get_paths()
        
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