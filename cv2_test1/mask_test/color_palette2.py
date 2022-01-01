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
    def __init__(self,value) -> None:
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

colors_test()

def show_sample_colors():
    colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

    # Sort colors by hue, saturation, value and name.
    by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                    for name, color in colors.items())
    sorted_names = [name for hsv, name in by_hsv]

    n = len(sorted_names)
    ncols = 4
    nrows = n // ncols + 1

    fig, ax = plt.subplots(figsize=(8, 5))

    # Get height and width
    X, Y = fig.get_dpi() * fig.get_size_inches()
    h = Y / (nrows + 1)
    w = X / ncols

    for i, name in enumerate(sorted_names):
        col = i % ncols
        row = i // ncols
        y = Y - (row * h) - h

        xi_line = w * (col + 0.05)
        xf_line = w * (col + 0.25)
        xi_text = w * (col + 0.3)

        ax.text(xi_text, y, name, fontsize=(h * 0.8),
                horizontalalignment='left',
                verticalalignment='center')

        ax.hlines(y + h * 0.1, xi_line, xf_line,
                color=colors[name], linewidth=(h * 0.6))
        print('colors= {} , name={} , xi={},xf={}'.format(colors[name],name,xi_line,xf_line))

    ax.set_xlim(0, X)
    ax.set_ylim(0, Y)
    ax.set_axis_off()

    fig.subplots_adjust(left=0, right=1,
                        top=1, bottom=0,
                        hspace=0, wspace=0)
    plt.show()