import cv2
import numpy as np

print(cv2.__version__)
# 3.3.0

def main():
    try:
        paint1_test2()
    except:
        import traceback
        print(traceback.print_exc())

def paint1_test2():
    try:
        # img = np.full((210, 425, 3), 128, dtype=np.uint8)
        read_path = r'C:\Users\OK\source\repos\Repository4_python\common_util\screenshot.png'
        # image を読み込む
        im_base = cv2.imread(read_path)
        img = im_base
        print(im_base.shape)
        pt = 472,1008
        pt = 406,847
        pt = 439 , 928
        pt = 406 ,847
        print('pt = ' + str(pt))
        cv2.circle(img, pt, 10, (0,0,255), 
            thickness=2, lineType=cv2.LINE_8, shift=0)
        
        path = './image/cv2_paint1_test2.png'
        cv2.imwrite(path, img)
        print(path)
    except:
        import traceback
        print(traceback.print_exc())

def paint1_test1():
    try:
        img = np.full((210, 425, 3), 128, dtype=np.uint8)

        cv2.rectangle(img, (50, 10), (125, 60), (255, 0, 0))
        cv2.rectangle(img, (50, 80), (125, 130), (0, 255, 0), thickness=-1)
        cv2.rectangle(img, (50, 150), (125, 200), (0, 0, 255), thickness=-1)
        cv2.rectangle(img, (50, 150), (125, 200), (255, 255, 0))

        cv2.rectangle(img, (175, 10), (250, 60), (255, 255, 255), thickness=8, lineType=cv2.LINE_4)
        cv2.line(img, (175, 10), (250, 60), (0, 0, 0), thickness=1, lineType=cv2.LINE_4)
        cv2.rectangle(img, (175, 80), (250, 130), (255, 255, 255), thickness=8, lineType=cv2.LINE_8)
        cv2.line(img, (175, 80), (250, 130), (0, 0, 0), thickness=1, lineType=cv2.LINE_8)
        cv2.rectangle(img, (175, 150), (250, 200), (255, 255, 255), thickness=8, lineType=cv2.LINE_AA)
        cv2.line(img, (175, 150), (250, 200), (0, 0, 0), thickness=1, lineType=cv2.LINE_AA)

        cv2.rectangle(img, (600, 20), (750, 120), (0, 0, 0), lineType=cv2.LINE_AA, shift=1)
        cv2.rectangle(img, (601, 160), (751, 260), (0, 0, 0), lineType=cv2.LINE_AA, shift=1)
        cv2.rectangle(img, (602, 300), (752, 400), (0, 0, 0), lineType=cv2.LINE_AA, shift=1)

        path = './image/cv2_paint1_test.png'
        cv2.imwrite(path, img)
        print(path)
    except:
        import traceback
        print(traceback.print_exc())


main()