import cv2
class Cv2Result():
    min:float
    max:float
    minLoc:list
    maxLoc:list
    def __init__(self,result=None) -> None:
        if len(result) > 0:
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
            self.min = minVal
            self.max = maxVal
            self.minLoc = minLoc
            self.maxLoc = maxLoc

    def print_result(self):
        print('cv2.minMaxLoc : minVal = {} , maxVal = {} , minLoc = {} , maxLoc = {}'.
        format(self.min, self.max ,self.minLoc, self.maxLoc))

