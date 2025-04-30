

from PIL import Image
from pathlib import Path

def run_convert_append_image_main():
    """
    ファイルAとファイルBの画像を連結させて1つのファイルにする。
    ファイルA=左、ファイルB=右
    入力ディレクトリはAB同じ
    """
    src_dir_path = Path(r"C:\Users\OK\Desktop\250304交通費image2_2")
    dist_dir_path = src_dir_path

    # src_file_name_a = "経路図_362037_大窪利之_241203_1.jpg"
    # src_file_name_b = "経路図_362037_大窪利之_241203_2.jpg"
    # dist_file_name = "経路図_362037_大窪利之_241203.jpg"
    # src_file_name_a = "経路図_362037_大窪利之_241216_1.jpg"
    # src_file_name_b = "経路図_362037_大窪利之_241216_2.jpg"
    # dist_file_name = "経路図_362037_大窪利之_241216.jpg"
    # src_file_name_a = "経路図_362037_大窪利之_241220_1.jpg"
    # src_file_name_b = "経路図_362037_大窪利之_241220_2.jpg"
    # dist_file_name = "経路図_362037_大窪利之_241220.jpg"
    # src_file_name_a = "経路図_362037_大窪利之_241225_1.jpg"
    # src_file_name_b = "経路図_362037_大窪利之_241225_2.jpg"
    # dist_file_name = "経路図_362037_大窪利之_241225.jpg"
    # src_file_name_a = "経路図_362037_大窪利之_250130_1.jpg"
    # src_file_name_b = "経路図_362037_大窪利之_250130_2.jpg"
    # dist_file_name = "経路図_362037_大窪利之_250130.jpg"
    # src_file_name_a = "経路図_362037_大窪利之_250207_1.jpg"
    # src_file_name_b = "経路図_362037_大窪利之_250207_2.jpg"
    # dist_file_name = "経路図_362037_大窪利之_250207.jpg"
    # src_file_name_a = "経路図_362037_大窪利之_250210_1.jpg"
    # src_file_name_b = "経路図_362037_大窪利之_250210_2.jpg"
    # dist_file_name = "経路図_362037_大窪利之_250210.jpg"
    # src_file_name_a = "経路図_362037_大窪利之_250214_1.jpg"
    # src_file_name_b = "経路図_362037_大窪利之_250214_2.jpg"
    # dist_file_name = "経路図_362037_大窪利之_250214.jpg"
    # src_file_name_a = "経路図_362037_大窪利之_250228_1.jpg"
    # src_file_name_b = "経路図_362037_大窪利之_250228_2.jpg"
    # dist_file_name = "経路図_362037_大窪利之_250228.jpg"
    src_file_name_a = "経路図_250228_1.jpg"
    src_file_name_b = "経路図_250228_2.jpg"
    dist_file_name = "経路図_250228.jpg"

    src_path_a = src_dir_path / src_file_name_a
    src_path_b = src_dir_path / src_file_name_b
    dist_path = dist_dir_path / dist_file_name
    print("dist_file_name = " + dist_file_name)
    convert_append_image(
        src_path_a, src_path_b, dist_path)
    print("done convert_append")

def convert_append_image(img_path_a:str, img_path_b:str, save_path:str):
    img1 = Image.open(img_path_a)
    img2 = Image.open(img_path_b)

    # 横に結合
    new_img = Image.new("RGB", (img1.width + img2.width, max(img1.height, img2.height)))
    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (img1.width, 0))

    new_img.save(save_path)

if __name__ == "__main__":
    run_convert_append_image_main()