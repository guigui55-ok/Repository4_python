import cv2
import numpy as np
from common_utility.cv2_image.import_logger import log_info,log_error,LoggerUtility

def create_png(path:str,width:int,height:int,color=0)->bool:
    img = np.zeros((height, width, 3))
    img += color
    cv2.imwrite(path,img)
    return True