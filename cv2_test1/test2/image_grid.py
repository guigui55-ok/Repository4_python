def create_point_list(max,base):
    ret = []
    try:
        base_p = int(max/base)
        now_p = 0
        for i in range(base):
            now_p = int(base_p * i)
            if i == base:
                now_p = max
            ret.append(now_p)
        return ret
    except:
        import traceback
        print(traceback.print_exc())
        return ret
# 格子状にカットした一部を取得
# Get a part cut in a grid pattern
def get_img_part_cut_in_grid_pattern(img,cut_x,cut_y,get_x,get_y):
    try:
        th , tw = img.shape[:-1]
        point_list_x = create_point_list(tw,cut_x)
        point_list_y = create_point_list(th,cut_y)

        begin_point_x = get_x
        end_point_x = get_x + 1
        begin_point_y = get_y
        end_point_y = get_y + 1

        begin_point_x = point_list_x[get_x]
        end_point_X = point_list_x[get_x + 1]
        begin_point_y = point_list_y[get_y]
        end_point_y = point_list_y[get_y + 1]
    except:
        import traceback
        print(traceback.print_exc())
        return None

def SampleLoggerExp():
    logger = None
    exp = None
    def __init__(self,logger) -> None:
        self.logger = logger
    def info(self,value):
        print(value)
    def error(self,value):
        print(value)

class SampleLogger():
    logger = None
    exp:SampleLoggerExp = None
    def __init__(self,logger) -> None:
        self.logger = logger
    def info(self,value):
        print(value)

class GridPoint():
    x = 0
    y = 0
    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y

class GridRect():
    begin : GridPoint = None
    end : GridPoint = None
    def __init__(self,begin:GridPoint,end:GridPoint) -> None:
        self.begin = GridPoint(begin.x,begin.y)
        self.end = GridPoint(end.x,end.y)

class ImageGrid():
    logger = None
    img = None
    rect_list:list()  = []
    now_index = 0
    def __init__(self,img) -> None:
        self.img = img
    
    def set_img_part_cut_in_grid_pattern(self,cut_x,cut_y):
        try:    
            th , tw = self.img.shape[:-1]
            point_list_x = create_point_list(tw,cut_x)
            point_list_y = create_point_list(th,cut_y)

            count = 0
            for j in range(len(point_list_y)-1):
                for i in range(len(point_list_x)-1):
                    t_begin_p = GridPoint(point_list_x[i],point_list_y[j])
                    t_end_p = GridPoint(point_list_x[i+1],point_list_y[j]+1)
                    self.rect_list.append(GridRect(t_begin_p,t_end_p))
                    count += 1
        except Exception as e:
            self.logger.exp.error(e)
    
    def get_current_grid(self,index = -1):
        rect:GridRect = None
        try:
            if index == -1:
                index = self.index
            else:
                self.now_index = index
            rect = self.rect_list[index]
            self.now_index += 1
            return rect
        except Exception as e:
            self.logger.exp.error(e)
            return rect

    def grid_to_rect(self,value:GridRect):
        try:
            ret = [[value.begin.x, value.begin.y] , [value.end.x , value.end.y]]
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return [[0,0],[0,0,]]
        
    
    def get_current_rect(self,index = -1):
        try:
            rect = self.get_current_grid(index)
            ret = self.grid_to_rect(rect)
            return ret
        except Exception as e:
            self.logger.exp.error(e)
            return [[0,0],[0,0,]]

    def get_crrent_img_grid(self,index = -1):
        try:
            grid = self.get_current_grid(index)
            # img_base = img_base[int(th/2):int(th),0:tw]
            ret_img = self.img[grid.begin.y : grid.end.y , grid.begin.x : grid.end.x]
            return ret_img
        except Exception as e:
            self.logger.exp.error(e)
            return None
        
    def is_end(self)->bool:
        if self.now_index >= len(self.rect_list):
            return True
        else:
            return False