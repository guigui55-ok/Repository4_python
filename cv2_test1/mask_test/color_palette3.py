"""
========================
Visualizing named colors
========================

Simple plot example with the named colors and its visual representation.
"""
from __future__ import division

import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

import import_init
import traceback

def hes_str_to_int(value):
    import common_util.general_util.general_type as general_type
    return general_type.cnv_hex_str_to_int(value)

class ColorCode():
    r:str = 'FF'
    g:str = 'FF'
    b:str = 'FF'
    obj = None
    def __init__(self,value=None) -> None:
        if value == None:return
        self.set_value(value)
    def set_value(self,value):
        if value[0] == '#':
            self.r = value[1:2]
            self.g = value[3:4]
            self.r = value[5:6]
    def get_value(self):
        return '#'+self.r+self.g+self.b
    def cnv_to_rgb(self):
        int_r = hes_str_to_int(self.r)
        int_g = hes_str_to_int(self.g)
        int_b = hes_str_to_int(self.b)
        return int_r,int_g,int_b
    def int_to_hex_str(self,value:int):
        _value:str = hex(value)
        _value = _value.replace('0x','')
        _value = _value.upper()
        # _value = '{:0=2}'.format(_value) #int,str(hex)に対応できない
        if len(_value) == 1:
            _value = '0' + _value
        return _value
    def set_value_from_rgb_oct(self,oct_r,oct_g,oct_b):
        self.r = self.int_to_hex_str(oct_r)
        self.g = self.int_to_hex_str(oct_g)
        self.b = self.int_to_hex_str(oct_b)
    def get_colors(self):        
        colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
        return colors
    def set_color(self):
        val = self.get_value()

class Colors():
    color_code:ColorCode
    def __init__(self,value) -> None:
        self.set_value(value)
    def set_value(self,value):
        if value[0] == '#':
            self.color_code = ColorCode(value)

def cnv_color_code_to_rgb(value:str):
    cc = ColorCode(value)
    return cc.cnv_to_rgb()

def colors_test():
    """カラーコード一覧とそれに対応するrbg値、色名を表示する"""
    try:
        colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
        # print(colors)
        c:str # key name
        for c in colors:
            code = colors[c]
            rgb = cnv_color_code_to_rgb(code)
            print('key={} , value={} , rgb={}'.format(c,code,rgb))
        return
    except:
        traceback.print_exc()

# colors_test()

def show_sample_colors():
    colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

    # Sort colors by hue, saturation, value and name.
    by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                    for name, color in colors.items())
    sorted_names = [name for hsv, name in by_hsv]

    print('len(sorted_names) = {}'.format(len(sorted_names)))
    print('len(colors) = {}'.format(len(colors)))

    n = len(sorted_names)
    # すべての個数
    n = 2
    # col number
    # 一行当たりの表示・列数
    ncols = 2
    # row number {n // ncols + 1 = int(n / ncols + 1)}
    # 表示されるすべての行
    nrows = n // ncols + 1

    # Figure(描画領域全体),Axes(1つ1つのプロットを描く領域)objを取得する
    # Axes
    # nrows×ncols個のサブプロットを生成
    import matplotlib
    from matplotlib import figure
    from matplotlib.figure import Figure
    fig : Figure
    fig, ax = plt.subplots(figsize=(8, 2))

    _figure : Figure
    from matplotlib import axes
    _axes : axes
    _axes = ax
    _figure = fig
    # Get height and width
    # インチ単位を、ピクセル単位に変換するために、ax_w_inch に、解像度 fig.get_dpi() をかけて、ax_w_px に格納しています。
    # dpi は rcParamsから取得されている
    # https://tech-market.org/matplotlib-rcparams/
    dpi = _figure.get_dpi()

    # get_size_inchesで、Axesオブジェクトの全体の大きさ（＝各軸の目盛やラベル（「入力」や「出力」などの文字）も含んだ領域の大きさ）をインチ単位で取得しています。
    inches = fig.get_size_inches()
    # <Python, pptx> Inches(1) のサイズ
    # https://nekoyukimmm.hatenablog.com/entry/2015/09/29/171155
    print(dpi)
    print('inches = {}'.format(inches))

    WINDOW_X, WINDOW_Y = dpi * inches
    # 1行当たりの高さ
    height = WINDOW_X / (nrows + 1)
    height = dpi
    # 1列当たりの幅
    width = WINDOW_Y / ncols

    ############
    # 表示するカラーを選定する
    ############
    targets = [(36,0,0),(70,255,255)]
    targets = [(15,0,0),(36,255,255)]
    import numpy as np
    lower,upper = [np.array([36,25,25]),np.array([70,255,255])] # green
    lower,upper = [np.array([110,150,50]),np.array([120,255,255])] # blue
    targets = [lower,upper]

    new_sorted_names = []
    new_colors = []
    cl_obj = ColorCode()
    tn = 0
    cl_obj.set_value_from_rgb_oct(targets[tn][0],targets[tn][1],targets[tn][2])
    c_code = cl_obj.get_value()
    new_colors.append(c_code)
    tn = 1
    cl_obj.set_value_from_rgb_oct(targets[tn][0],targets[tn][1],targets[tn][2])
    c_code = cl_obj.get_value()
    new_colors.append(c_code)

    for nc in new_colors:
        for i, name in enumerate(sorted_names):
                if colors[name] == nc:
                    new_sorted_names.append(name)
                    break
        else:
            new_sorted_names.append(nc)
    ###########

    for i, new_name in enumerate(new_sorted_names):
        col = i % ncols
        row = i // ncols
        y = WINDOW_Y - (row * width) - width
        y = (row * width) + width

        print('col {}, row {} ,y {}'.format(col,row,y))
        if col == 0:
            xi_line = 0
            xi_text = 0
            xf_line = 0

        xi_line += (width * col) +width * (0.05)
        xf_line += (width * col) +width * (1)
        # xi_text += width * (0.3) + xf_line
        # xi_text += (width * col) + (width * 0.3)
        # xi_text +=  (width * 0.3)
        # xi_text +=  (width * 0.3)
        xi_text += (width * col) + (width * 1.2)

        print('xi {} , xf {} , tx {}'.format(xi_line,xf_line,xi_text))

        font_size = (height * 0.3)
        name = new_name
        # https://python.atelierkobato.com/text/
        # Axes.text
        tx = ax.text(x=xi_text, y=y, s=name, fontsize=font_size,
                horizontalalignment='left',
                verticalalignment='center')

        # _color = colors[name]
        # _color = 'red'
        _color = new_colors[i]
        # colors[name] = '#FFFFFF'
        # Axes.hlines
        print('_color = {}'.format(_color))
        y_lines = y + width * 0.1
        ax.hlines(y_lines, xi_line, xf_line,
                color=_color, linewidth=(height * 0.6))
        # print('colors= {} , name={} , xi={},xf={}'.format(colors[name],name,xi_line,xf_line))

    ax.set_xlim(0, WINDOW_X)
    ax.set_ylim(0, WINDOW_Y)
    ax.set_axis_off()

    fig.subplots_adjust(left=0, right=1,
                        top=1, bottom=0,
                        hspace=0, wspace=0)
    plt.show()

show_sample_colors()