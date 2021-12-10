# https://symfoware.blog.fc2.com/blog-entry-2163.html
import traceback
import cv2 as cv
def main():
    try:
        import pathlib
        import os
        img_dir = str(pathlib.Path(__file__).parent.parent)
        img_dir = os.path.join(img_dir,'image/pickup_test')
        image_file_name = 'pickup_sample.png'
        img_path = os.path.join(img_dir,image_file_name)
        print(img_path)

        # ファイルを読み込み
        src = cv.imread(img_path, cv.IMREAD_COLOR)
        # グレースケール化
        img_gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
        # しきい値指定によるフィルタリング
        retval, dst = cv.threshold(img_gray, 127, 255, cv.THRESH_TOZERO_INV )
        cv.imwrite('debug_1.png', dst)
        # 白黒の反転
        dst = cv.bitwise_not(dst)
        cv.imwrite('debug_2.png', dst)
        # 再度フィルタリング
        retval, dst = cv.threshold(dst, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        # 結果を保存
        cv.imwrite('result.png', dst)
    except Exception as e:
        # print(str(e))
        traceback.print_exc()
    
if __name__ == '__main__':
    main()