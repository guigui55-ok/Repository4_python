
import cv2

def main():
    try:
        rect_list = []
        rect = [[100,200],[200,300]]
        rect_list.append(rect)
        rect = [[500,600],[600,700]]
        rect_list.append(rect)

        img_path = r'C:\Users\OK\source\repos\Repository4_python\ocr_test\images\screen_sever.png'

        import os
        # dirpath = os.path.dirname(img_path)
        dirpath = './'
        import pathlib
        dirpath = str(pathlib.Path(dirpath).resolve())

        filename = os.path.basename(img_path)
        ext = os.path.splitext(img_path)[1]
        out_path = dirpath + '\\' + filename + '_1' + ext

        color=(0, 0, 255)
        border_width = 2
        img = cv2.imread(img_path)
        for i in range(len(rect_list)):
            img = cv2.rectangle(
                img, rect_list[i][0] ,rect_list[i][1], 
                color, border_width)
            print(i)
            print(str(rect_list[i]))
        cv2.imwrite(out_path, img)
        print(out_path)
    except:
        import traceback
        print(traceback.print_exc())

main()