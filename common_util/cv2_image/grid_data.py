
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
            int(self.col) * self.col_step,
            int(self.row) * self.row_step,
            int(self.col+1) * self.col_step,
            int(self.row+1) * self.row_step
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
    image_list : list = []
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
        # self.row_step = int(self.rect.height / self.row_max)
        # self.col_step = int(self.rect.width / self.col_max)
        self.row_step = int(self.rect.height / self.row_max)
        self.col_step = int(self.rect.width / self.col_max)

        coordinate_list = []
        if self.direction == Direction.HORIZON:
            if self.order == Order.SCENDING:
                for row in range(self.row_max):
                    for col in range(self.col_max):
                        coordinate_list.append([row,col])
            else:
                #self.order == Direction.DESCENDING
                for row in reversed(range(self.row_max)):
                    for col in reversed(range(self.col_max)):
                        coordinate_list.append(row,col)
        else:
            # direction == Direction.VERTICAL
            if self.order == Order.SCENDING:
                for col in range(self.col_max):
                    for row in range(self.row_max):
                        coordinate_list.append(row,col)
            else:
                #self.order == Direction.DESCENDING
                for col in reversed(range(self.col_max)):
                    for row in reversed(range(self.row_max)):
                        coordinate_list.append(row,col)
        self.max_index = self.row_max * self.col_max
        self.current_index = 0
        self.coordinate_list = coordinate_list
        print(self.coordinate_list)
    
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


import common_util.cv2_image.cv2_image_util as image_util
import common_util.general_util.general as general
from common_util.file_util.file_class import MyFile
def cut_image_as_grid_to_file_1(
    logger,
    base_image_path:str,
    rect:list,
    row_max:int,
    col_max:int,
    log_image_dir_path:str=''):
    """
    イメージファイルの指定範囲を、縦横均等に切り分け、ファイルへ出力する
    """
    
    table_obj = GridTable(rect, row_max= row_max, col_max= col_max)
    import os
    # set file path object
    mf = MyFile(base_image_path)
    basename_without_ext =  mf.get_basename_without_ext()
    ext = mf.get_ext()
    # ret_dir    
    child_dir_name = '' + general.get_datetime() + '_' + basename_without_ext
    if log_image_dir_path != '':
        log_image_dir_path = mf.dir_path
    log_image_dir_path = os.path.join(log_image_dir_path,child_dir_name)
    # read image
    img_obj = image_util.Cv2Image(logger,base_image_path) # 書き込むためのもの
    if log_image_dir_path != '':
        # 基本イメージをファイルへ保存する        
        buf_img = img_obj.triming(rect)
        buf_ret_path = os.path.join(log_image_dir_path,'zz_cut_grid_base_image.png')
        img_obj.save_img_other(buf_ret_path,buf_img)
    while(not table_obj.is_over_max_index()):
        # 現在の範囲を取得
        buf_rectangle = table_obj.get_current_rectangle()
        buf_rectangle.print_value()
        # 取得した範囲を切り取る
        buf_img = img_obj.triming(buf_rectangle.get_value_as_list())
        if log_image_dir_path != '':
            # イメージを保存する
            # ファイル名、パスを設定する
            buf_addstr = '_' + table_obj.get_current_coordinate_str()
            buf_ret_name = basename_without_ext + buf_addstr + ext
            buf_ret_path = os.path.join(log_image_dir_path,buf_ret_name)
            img_obj.save_img_other(buf_ret_path,buf_img)
        table_obj.image_list.append(buf_img)
        # 次の範囲へ
        # table.move_next()
        table_obj.current_index += 1
    return log_image_dir_path


def cut_image_as_grid_to_file(
    logger,
    base_image_path:str,
    rect:list,
    row_max:int,
    col_max:int,
    log_image_dir_path:str=''):
    """
    イメージファイルの指定範囲を、縦横均等に切り分け、ファイルへ出力する
    """  
    image_list,addstr_list = get_image_list_by_cut_as_grid(
        logger,base_image_path,rect,row_max,col_max,log_image_dir_path)

    import os
    # set file path object
    mf = MyFile(base_image_path)
    basename_without_ext =  mf.get_basename_without_ext()
    ext = mf.get_ext()
    # ret_dir    
    child_dir_name = '' + general.get_datetime() + '_' + basename_without_ext
    if log_image_dir_path != '':
        log_image_dir_path = mf.dir_path
    log_image_dir_path = os.path.join(log_image_dir_path,child_dir_name)
    # mkdir
    if not os.path.exists(log_image_dir_path):
        os.mkdir(log_image_dir_path)
    # read image
    img_obj = image_util.Cv2Image(logger,base_image_path) # 書き込むためのもの

    for i in range(len(image_list)):
        img = image_list[i]
        addstr = addstr_list[i]
        if log_image_dir_path != '':
            # イメージを保存する
            # ファイル名、パスを設定する
            buf_ret_name = basename_without_ext + addstr + ext
            buf_ret_path = os.path.join(log_image_dir_path,buf_ret_name)
            img_obj.save_img_other(buf_ret_path,img)


def get_image_list_by_cut_as_grid(
    logger,
    base_image_path:str,
    rect:list,
    row_max:int,
    col_max:int,
    log_image_dir_path:str=''):
    """
    イメージファイルの指定範囲を、縦横均等に切り分け、イメージリストを取得する
    """
    
    table_obj = GridTable(rect, row_max= row_max, col_max= col_max)
    import os
    # set file path object
    mf = MyFile(base_image_path)
    basename_without_ext =  mf.get_basename_without_ext()
    ext = mf.get_ext()
    # ret_dir    
    ret_file_name = '' + general.get_datetime() + '_' + basename_without_ext + ext
    if log_image_dir_path != '':
        log_image_dir_path = mf.dir_path
        log_image_dir_path = os.path.join(log_image_dir_path,ret_file_name)
    # read image
    img_obj = image_util.Cv2Image(logger,base_image_path) # 書き込むためのもの
    if log_image_dir_path != '':
        # 基本イメージをファイルへ保存する        
        buf_img = img_obj.triming(rect)
        buf_ret_path = ret_file_name
        img_obj.save_img_other(buf_ret_path,buf_img)
    
    images = []
    coordinates_str = []
    while(not table_obj.is_over_max_index()):
        # 現在の範囲を取得
        buf_rectangle = table_obj.get_current_rectangle()
        buf_rectangle.print_value()
        # 取得した範囲を切り取る
        buf_img = img_obj.triming(buf_rectangle.get_value_as_list())
        # 付与する文字列(座標)
        buf_addstr = '_' + table_obj.get_current_coordinate_str()
        coordinates_str.append(buf_addstr)
        # イメージを変数へ格納する
        images.append(buf_img)
        table_obj.image_list.append(buf_img)
        # 次の範囲へ
        # table.move_next()
        table_obj.current_index += 1
    return images,coordinates_str