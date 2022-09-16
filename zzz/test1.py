#https://teratail.com/questions/tu2mgrwc5jgosg

from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk,width=400 , height=400)
canvas.pack()
    
# def random_rectangle(max_width, max_height):
#     x2 = random.randrange(1, max_width)
#     y2 = random.randrange(1, max_height)
#     x1 = random.randrange(1, max_width-x2)
#     y1 = random.randrange(1, max_height-y2)
#     canvas.create_rectangle(x1,y1,x2,y2)
#     print('x1={}, y1={}, x2={}, y2={}'.format(x1, y1, x2, y2)) #確認用

class RectAngle():
    """
    四角形のデータを扱うクラス（値の保持、判定、描画）
    """
    def __init__(self,left,top,right,bottom) -> None:
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
    def is_same_value(self,rect_angle:'RectAngle'):
        """引数の四角形データと保持しているものが合致しているか判定する。"""
        if self.left == rect_angle.left \
            and self.top == rect_angle.top \
            and self.right == rect_angle.right \
            and self.bottom == rect_angle.bottom:
            return True
        return False
    def draw_to_canvas(self):
        """保持している四角形のデータをキャンバスに描画する"""
        canvas.create_rectangle(
            self.left, self.top, self.right, self.bottom)
    @classmethod
    def create_random_rectangle(cls,max_width,max_height):
        """引数よりランダムな四角形のデータを作成する"""
        x2 = random.randrange(1, max_width-1)
        y2 = random.randrange(1, max_height-1)
        x1 = random.randrange(1, max_width-x2)
        y1 = random.randrange(1, max_height-y2)
        print('x1={}, y1={}, x2={}, y2={}'.format(x1, y1, x2, y2)) #確認用
        return RectAngle(x1,y1,x2,y2)

def random_rectangle_loop(width, height, max_count):
    rect_angle_list = []
    for i in range(max_count):
        print('count={}, '.format(i), end='')
        #作成済みの四角形のデータと比較して、異なるものができるまでランダムな値を取得する
        rect_angle_new = RectAngle.create_random_rectangle(width, height)
        while is_same_value(rect_angle_list,rect_angle_new):
            rect_angle_new = RectAngle.create_random_rectangle(width, height)
        #取得した四角形のデータを描画する
        rect_angle_new.draw_to_canvas()
        #描画済みの四角形のデータを保持しておく
        rect_angle_list.append(rect_angle_new)

def is_same_value(rect_angle_list:'list[RectAngle]', rect_angle_new:RectAngle):
    for rect_angle in rect_angle_list:
        if rect_angle.is_same_value(rect_angle_new):
            return True
    return False

def random_rectangle(max_width, max_height):
    x2 = random.randrange(1, max_width)
    y2 = random.randrange(1, max_height)
    x1 = random.randrange(1, max_width-x2)
    y1 = random.randrange(1, max_height-y2)
    canvas.create_rectangle(x1,y1,x2,y2)

# def random_rectangle(width,height):
#     x1 = random_rectangle(width,height)
#     y1 = random_rectangle(width,height)
#     x2 = x1 + random_rectangle(width,height)
#     y2 = y1 + random_rectangle(width,height)
#     canvas.create_rectangle(x1,y1,x2,y2)

# random_rectangle(400,400)

random_rectangle_loop(400,400,100)

tk.mainloop()