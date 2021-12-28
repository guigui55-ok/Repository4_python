
from common_util.general_util.rectangle import Point,RectAngle
from common_util.general_util.general_const import Direction,Order


class GridCell():
    """
    
    * index は 0 から len(ary) -1 を想定
    """
    row:int
    col:int
    row_step:int
    col_step:int
    begin_point:Point
    end_point:Point
    rect:RectAngle
    def __init__(self,begin_point:Point,row=0,col=0,row_step=0,col_step=0) -> None:
        self.begin_point = begin_point
        self.row = row
        self.col = col
        if row >= 0 and \
            col >= 0 and \
            row_step > 0 and \
            col_step > 0:
            # すべて値があるときには実行する
            self.set_value(row_step,col_step)

    def set_value(self,row_step,col_step):
        self.row_step = row_step
        self.col_step = col_step
        temp_rect = [
            int(self.row) * self.row_step,
            int(self.col) * self.col_step,
            int(self.row+1) * self.row_step,
            int(self.col+1) * self.col_step
        ]
        temp_rect[0] += self.begin_point.x
        temp_rect[1] += self.begin_point.y
        temp_rect[2] += self.begin_point.x
        temp_rect[3] += self.begin_point.y
        self.rect = RectAngle(temp_rect)
    def get_rectangle(self):
        return self.rect

class GridTable():
    # begin_point : Point
    # end_point : Point
    # now_row : int = 0
    # now_col : int = 0
    rect : RectAngle
    max_index : int = 0

    row_max : int = 0
    col_max : int = 0
    direction : int = Direction.HORIZON
    order : int = Order.SCENDING
    row_step : int = 0
    col_step : int = 0
    coordinate_list : list
    current_index : int = 0
    def __init__(self,rect,row_max,col_max) -> None:
        self.begin_point = Point(rect[0],rect[1])
        self.end = Point(rect[2],rect[3])
        self.rect = RectAngle(rect)
        self.row_max = row_max
        self.col_max = col_max
        self.max_index = row_max * col_max
        if rect != None:
            if row_max > 0 and col_max > 0:
                self.init_value()

    def init_value(self):
        self.row_step = int(self.rect.height / self.row_max)
        self.col_step = int(self.rect.width / self.col_max)

        coordinate_list = []
        if self.direction == Direction.HORIZON:
            if self.order == Order.SCENDING:
                for col in range(self.col_max):
                    for row in range(self.row_max):
                        coordinate_list.append([row,col])
            else:
                #self.order == Direction.DESCENDING
                for col in reversed(range(self.col_max)):
                    for row in reversed(range(self.row_max)):
                        coordinate_list.append(row,col)
        else:
            # direction == Direction.VERTICAL
            if self.order == Order.SCENDING:
                for row in range(self.row_max):
                    for col in range(self.col_max):
                        coordinate_list.append(row,col)
            else:
                #self.order == Direction.DESCENDING
                for row in reversed(range(self.row_max)):
                    for col in reversed(range(self.col_max)):
                        coordinate_list.append(row,col)
        self.max_index = self.row_max * self.col_max
        self.current_index = 0
        self.coordinate_list = coordinate_list
    
    def move_next(self):
        if not self.is_over_max_index():
            self.current_index += 1
        else:
            self.current_index = self.max_index

    def is_over_max_index(self):
        if self.max_index <= self.current_index:
            return True
        else:
            return False
    
    def get_current_coordinate_str(self,delimita='_')->str:
        row ,col = self.get_current_coordinage()
        return str(row) + delimita + str(col)

    def get_current_coordinage(self):
        row = self.coordinate_list[self.current_index][0]
        col = self.coordinate_list[self.current_index][1]
        return row,col


    def get_current_rectangle(self):
        if len(self.coordinate_list) <= self.current_index:
            print(str(__class__) + '.get_current_rectangle : len(self.coordinate_list) <= self.current_index')
            print('row ,col = self.coordinate_list[self.max_index]')
            row = self.coordinate_list[self.max_index][0]
            col = self.coordinate_list[self.max_index][1]
        else:
            row = self.coordinate_list[self.current_index][0]
            col = self.coordinate_list[self.current_index][1]
        grid_data = GridCell(self.rect.begin, row, col, self.row_step, self.col_step)
        ret = grid_data.get_rectangle()
        return ret

    