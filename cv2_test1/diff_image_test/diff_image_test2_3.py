"""



必要なライブラリ
pip install opencv-python-headless
pip install scikit-image

pip install protobuf<4

ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
grpcio-status 1.60.0 requires protobuf>=4.21.6, but you have protobuf 3.20.3 which is incompatible.

pip install scikit-image --force-reinstall

"""

import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np

def calculate_similarity(image_path1, image_path2):
    # 画像をグレースケールで読み込む
    img1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    # サイズが異なる場合、リサイズ
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # SSIMを計算
    s = ssim(img1, img2)
    return s

# 画像パス（これは例です、実際のパスに置き換えてください）
from pathlib import Path
# dir_path = Path(__file__).parent
dir_path = Path(r'C:\Users\OK\source\repos\test_media_files\movie_test_media_files\write_frames_result_2112_062327')
image_path1 = str(dir_path.joinpath('pad_dunsion_1.png'))
# path_b = dir_path.joinpath('pad_dunsion_7.png')
# path_b = dir_path.joinpath('pad_dunsion_10.png')
image_path2 = str(dir_path.joinpath('pad_dunsion_13.png'))

# 類似度を計算
print('image_path1 = {}'.format(image_path1))
print('image_path2 = {}'.format(image_path2))
similarity = calculate_similarity(image_path1, image_path2)
print(f"画像の類似度（SSIM）: {similarity:.4f}")


"""
画像比較SSIMについて

SSIM（Structural Similarity Index Measure）の計算プロセス：
明るさの比較：二つの画像のピクセル平均を比較して、画像の明るさを評価します。
コントラストの比較：標準偏差を用いて画像のコントラストを評価します。これにより、画像のピクセル値のばらつき具合を測ります。
構造の比較：画像のピクセル値の相関関係を分析して、画像のテクスチャやパターンの類似性を評価します。
実装の概要：
画像はまずグレースケールで読み込まれます。これにより、色情報を無視して明るさ情報のみに焦点を当てます。
二つの画像が異なるサイズの場合、片方の画像をもう一方のサイズにリサイズします。これは、ピクセル単位での比較を行うために必要です。
上記のSSIMの計算を行い、得られた値が画像間の類似度として出力されます。SSIMの値は-1から1までの範囲で、1は完全に同一の画像を意味し、-1は全く異なる画像を意味します。
この方法は、特に画像の質の変化やノイズの影響を評価するのに有効で、画像処理や品質評価の分野で広く用いられています。

比較結果について
SSIMは画像の輝度、コントラスト、構造の3つの比較を組み合わせた指標で、-1（全く異なる）から1（完全に同じ）の範囲の値を返します。






"""