
class Point():
    x : int
    y : int
    def __init__(self,x=0,y:int=0) -> None:
        if len(x) > 1:
            self.x = x[0]
            self.y = x[1]
            return
        self.x = x
        self.y = y

class RectAngle():
    begin : Point
    end : Point
    def __init__(self,begin=None,end:Point=None) -> None:
        if len(begin)>3:
            self.begin = Point(begin[0],begin[1])
            self.end = Point(begin[2],begin[3])
            return
        if begin == None:
            begin = Point()
        else:
            self.begin = begin
        if end == None:
            end = Point()
        else:
            self.end = end
    def set_value_by_list(self,value:list):
        self.begin.x = value[0]
        self.begin.y = value[1]
        self.end.x = value[2]
        self.end.y = value[3]
    def get_value_as_list(self):
        ret = [self.begin.x, self.begin.y, self.end.x, self.end.y]
        return ret
    def width(self):
        w = self.end.x = self.begin.x
        return w
    def height(self):
        h = self.end.y = self.begin.y
        return h
        