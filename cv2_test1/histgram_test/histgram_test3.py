import traceback
import cv2
import matplotlib.pyplot as plt
import numpy as np

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

# https://pystyle.info/opencv-histogram/
def hist_test3():
    try:
        img_dir, img_path = get_paths()
        print(img_path)

        # 画像をグレースケール形式で読み込む。
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        # 1次元ヒストグラムを作成する。
        n_bins = 100  # ビンの数
        hist_range = [0, 256]  # 集計範囲

        hist = cv2.calcHist(
            [img], channels=[0], mask=None, histSize=[n_bins], ranges=hist_range
        )
        hist = hist.squeeze(axis=-1)  # (n_bins, 1) -> (n_bins,)
        print(hist)
        #################
        # inline
        # 描画する。
        def plot_hist(bins, hist, color):
            centers = (bins[:-1] + bins[1:]) / 2
            widths = np.diff(bins)
            ax.bar(centers, hist, width=widths, color=color)
        #################

        # 線形に等間隔な数列を生成する
        bins = np.linspace(*hist_range, n_bins + 1)
        print(bins)

        fig, ax = plt.subplots()
        ax.set_xticks([0, 256])
        ax.set_xlim([0, 256])
        ax.set_xlabel("Pixel Value")
        plot_hist(bins, hist, color="k")
        plt.show()
        return
    except:
        traceback.print_exc()

hist_test3()