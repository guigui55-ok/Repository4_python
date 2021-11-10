import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def match_template(img_base,img_temp,
        result_file_path:str = '') -> bool:
    try:
        img_gray = cv.cvtColor(img_base, cv.COLOR_BGR2GRAY)
        w, h = img_temp.shape[::-1]

        res = cv.matchTemplate(img_gray,img_temp,cv.TM_CCOEFF_NORMED)

        threshold = 0.9
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv.rectangle(img_base, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        
        if result_file_path != '':
            cv.imwrite(result_file_path,img_base)

        if len(loc[0])<=0:
            return False
        return True
    except:
        import traceback
        traceback.print_exc()
        return False

def main():
    import os
    rmpath = './res.png'
    if os.path.exists(rmpath):
        os.remove(rmpath)

    import pathlib
    path = './'
    pathobj = pathlib.Path(path)
    print(pathobj.resolve())

    try:
        path_base = 'image/power_on_screen2.png'
        path_temp = 'image/key_mark2.png'
        path_temp = 'image/key_mark3.png'
        img_base = cv.imread(path_base)
        img_temp = cv.imread(path_temp,0)
        result_file_path = './res.png'
        result = match_template(img_base,img_temp,result_file_path)
        print('result = ' + str(result))
        print('result_file_path= '+result_file_path)
    except:
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()