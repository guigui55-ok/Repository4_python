import enum
import cv2
import traceback

from numpy import result_type

class Cv2Type(enum.IntEnum):
    RESULT = 2
    IMAGE = 1

import numpy
class Cv2Image():
    image =None
    width = 0
    height = 0
    ignore_data = None
    def __init__(self,image) -> None:
        self.image = image
    @property
    def max(self):return self.image.max
    @property
    def min(self):return self.image.min
    @property
    def width(self):return self.image.shape[1]
    @property
    def height(self):return self.image.shape[0]
    @property
    def dtype_str(self):return str(self.dtype)
    
    def print_data(self):
        if self.ignore_data == None:
            self.ignore_data = numpy.array([0,0,0])
            print(self.ignore_data)
        for i , h_data in enumerate(self.image):
            for j , w_data in enumerate(h_data):
                if str(self.ignore_data) != str(w_data):
                    print('i={} ,j={} ,data={}'.format(i,j,w_data))
                    if i==len(h_data)-1:
                        if j==len(w_data)-1:
                            # print('last data')
                            pass
    def count_data(self):
        if self.ignore_data == None:
            self.ignore_data = numpy.array([0,0,0])
        count = 0
        for i , h_data in enumerate(self.image):
            for j , w_data in enumerate(h_data):
                if str(self.ignore_data) != str(w_data):
                    # print('i={} ,j={} ,data={}'.format(i,j,w_data))
                    count += 1
        return count


class Cv2Result():
    result=None
    image:Cv2Image=None
    min:float
    max:float
    minLoc:list
    maxLoc:list
    data_type:int
    def __init__(self,result=None) -> None:
        self.set_value(result)
    
    def set_value(self,result)->bool:
        self.result = result
        try:
            if self.is_exists_minMaxLoc(result):
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
                self.min = minVal
                self.max = maxVal
                self.minLoc = minLoc
                self.maxLoc = maxLoc
                self.data_type = Cv2Type.RESULT
            else:
                self.data_type = Cv2Type.IMAGE
                self.set_value_image(result)

        except:
            traceback.print_exc()
            print(str(__class__) + ' : set_value Failed')
    
    def is_exists_minMaxLoc(self,value):
        try:
            cv2.minMaxLoc(value)
            return True
        except:
            return False
    
    def set_value_image(self,value):
        self.image = Cv2Image(value)

    def print_result_all(self):
        try:
            ignore_data = [0,0,0]
            ret = self.result
            if len(ret) > 0:
                for i ,i_buf in enumerate(ret):
                    for j,j_buf in enumerate(i_buf):
                        if str(ignore_data) != str(j_buf):
                            print('i={} ,j={} ,data={}'.format(i,j,j_buf))
        except:
            traceback.print_exc()
            print(str(__class__) + ' : print_result_all Failed')

    def print_result(self):
        if self.data_type == Cv2Type.RESULT:
            print('cv2.minMaxLoc : minVal = {} , maxVal = {} , minLoc = {} , maxLoc = {}'.
            format(self.min, self.max ,self.minLoc, self.maxLoc))
        elif self.data_type == Cv2Type.IMAGE:
            self.image.print_data()
        else:
            print('Cv2Result DataType is Invalid. print_result Failed')

    def count_data(self):
        if self.data_type == Cv2Type.RESULT:
            # print('cv2.minMaxLoc : minVal = {} , maxVal = {} , minLoc = {} , maxLoc = {}'.
            # format(self.min, self.max ,self.minLoc, self.maxLoc))
            return 1
        elif self.data_type == Cv2Type.IMAGE:
            return self.image.count_data()
        else:
            print('Cv2Result DataType is Invalid. print_result Failed')
            return -1

