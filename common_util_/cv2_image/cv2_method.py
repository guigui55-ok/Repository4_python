import cv2
import numpy as np

def create_png(logger,path,width,height,color=0)->bool:
    try:
        img = np.zeros((height, width, 3))
        img += color
        cv2.imwrite(path,img)
        return True
    except Exception as e:
        logger.exp.error(e)
        return False