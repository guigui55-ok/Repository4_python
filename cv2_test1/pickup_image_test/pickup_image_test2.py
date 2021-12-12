# https://symfoware.blog.fc2.com/blog-entry-2163.html
import traceback
import cv2 as cv

def apply_threshold(num,img,thresh,maxval,type):
    try:
        retval, ret = cv.threshold(img, thresh, maxval, type)
        path = 'pickup_sample_debug_' + str(num) + '.png'
        cv.imwrite(path, ret)
        return ret
    except:
        import traceback
        traceback.print_exc()
        return None

def main():
    try:
        import pathlib,os
        img_dir = str(pathlib.Path(__file__).parent.parent)
        img_dir = os.path.join(img_dir,'image/pickup_test')
        image_file_name = 'pickup_sample.png'
        image_file_name = 'screenshot_home_white'
        ext = '.png'
        img_path = os.path.join(img_dir,image_file_name+ext)
        print(img_path)
        n = 0

        # ファイルを読み込み
        src = cv.imread(img_path, cv.IMREAD_COLOR)
        # グレースケール化
        # img_gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
        # # しきい値指定によるフィルタリング
        # n+=1
        # dst = apply_threshold(n,img_gray,127,255,cv.THRESH_TOZERO_INV)
        # # 白黒の反転
        # dst = cv.bitwise_not(dst)
        # # 再度フィルタリング
        # dst = apply_threshold(n,dst,0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)




        # 結果を保存
        result_path = image_file_name + 'result' + ext
        cv.imwrite(result_path, dst)
        print(result_path)
    except Exception as e:
        # print(str(e))
        traceback.print_exc()
    
if __name__ == '__main__':
    main()