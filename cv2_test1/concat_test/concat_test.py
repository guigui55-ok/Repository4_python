import cv2
import traceback

# https://note.nkmk.me/python-opencv-hconcat-vconcat-np-tile/
def concat_test():
    try:
        import pathlib,os
        img_dir = str(pathlib.Path(__file__).parent.parent)
        img_dir = os.path.join(img_dir,'image/concat')
        image_file_name1 = 'image1.png'
        image_file_name2 = 'image2.png'
        img_path1 = os.path.join(img_dir,image_file_name1)
        img_path2 = os.path.join(img_dir,image_file_name2)

        im1 = cv2.imread(img_path1)
        im2 = cv2.imread(img_path2) 
        # 幅が等しい画像を縦に連結
        save_name = 'voncat.png'
        save_path = os.path.join(img_dir,save_name)
        im_v = cv2.vconcat([im1, im2])
        cv2.imwrite(save_path,im_v)
        print(save_path)

        # 高さが等しい画像を横に連結
        save_name = 'honcat.png'
        save_path = os.path.join(img_dir,save_name)
        im_v = cv2.hconcat([im1, im2])
        cv2.imwrite(save_path,im_v)
        print(save_path)
        return
    except:
        traceback.print_exc()

concat_test()


# 同一画像を繰り返し縦に連結