from input.input import input,input_init
input_init()
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

#条件が一致したときに加算する数値
ADD_NUM_WHEN_MATCHED = 1

import numpy as np
class InputValuesNumpy():
    """inputで取得したデータを加工するためのクラス"""
    def __init__(self,row:int=0,col:int=0) -> None:
        self.values = np.zeros((row, col))
    def append_value_by_split(self,value:str,delimita:str=' ',axis=0):
        """valueをsplitしてself.valuesへ追加する"""
        add_list = [value.split(delimita)]
        if len(self.values)<1:
            self.values = np.array(add_list)
        else:
            self.values = np.append(self.values, add_list, axis=axis)
    def confirm_amount_row_and_col(self,row:int ,col:int):
        """行と列の数が引数とあっているか確認する"""
        shape = self.values.shape
        if shape == (row,col):
            return True
        else:
            return False
    def swap_values_row_and_column(self):
        """行と列の値を入れ替える"""
        self.values = self.values.T
    def cnv_values_to_int(self):
        """self.valuesの値を数値にする"""
        # self.values = [int(buf) for buf in self.values]
        self.values = np.array(self.values,dtype=int)

def main():
    """メイン処理部"""
    map_manager = MapManager()
    # 1行目のマップサイズと閾値を取得する
    map_manager.set_value_from_args(input())
    maps = Maps(map_manager.map_size)

    # 標準入力からそのまま使用できないので、numpyリストに格納し、行列を入れ替え、数値に変換する
    main_value = InputValuesNumpy()
    for _ in range(map_manager.map_size):
        main_value.append_value_by_split(input())
    valuse_is_valid = main_value.confirm_amount_row_and_col(map_manager.map_size,map_manager.map_size)
    if not valuse_is_valid:
        raise Exception('取得したデータの行と列が想定と異なります。')
    main_value.swap_values_row_and_column()
    main_value.cnv_values_to_int()
    
    # 1行目以降の降水量リストよりマップを作成する
    for value in main_value.values:
        # 降水量リストを読み込み数値化する
        maps.add_map_data(value)
    # マップの大きさとあっているか確認する
    if not maps.data_is_valid():
        raise Exception('取得した降水量データの数がマップの大きさと異なります。')
    # ルートが閾値以上か判定して、ルート番号を取得する
    cl_judge = JudgePass()
    for i in range(len(maps.map_list)):
        precipitation_amount_int_list = maps.map_list[i]
        is_pass = cl_judge.judge_one_line(map_manager.threshold,precipitation_amount_int_list)
        if is_pass:
            cl_judge.add_result(i+ADD_NUM_WHEN_MATCHED)
    #自宅待機か判定する
    cl_judge.judge_wait()
    #最後に改行を付与する
    result = cl_judge.result + '\n'
    #結果を出力する
    print(result)
    return

class ReadValues():
    def __init__(self) -> None:
        self.read_list:'list[list[str]]' = []
        self.row_max = 0
        self.col_max = 0
    def read_line(self,input_value:str,delimita:str=' '):
        """値を読み込む"""
        temp_list = input_value.split(delimita)
        self.read_list.append(temp_list)
    
    def cnv_to_2d_array(self,read_list:'list[list[str]]',dim_number:int):
        ret_list = [[0 for i in range(number)] for j in range(number)]

    
    def length_is_valid(self,number):
        """配列の個数がすべてあっているか判定する"""
        for temp_list in self.read_list:
            if len(temp_list) != number:
                return False
        return True
    def swap_array_row_and_column(self,number):
        """2次元配列の行と列を入れ替える"""
        ret_list = [[0 for i in range(number)] for j in range(number)]
        for i in number:
            col_list = self.read_list[i]
            for j in number:
                row = col_list[j]
                ret_list[j][i] = row


    

class JudgePass():
    """道が通れるか判定する"""
    def __init__(self):
        self.result = ''
    def judge_one_line(self,threshold:int,precipitation_amount:'list[int]'):
        value:int = 0
        for value in precipitation_amount:
            if value >= threshold:
                return False
        return True
    def add_result(self,value:int):
        """通過可能なルート番号を結果に追記する"""
        if self.result != '':
            self.result += ' ' + str(value)
        else:
            self.result = str(value)
    
    def judge_wait(self):
        """自宅待機か判定する"""
        if self.result == '':
            self.result = 'wait'

class MapManager():
    """地図のサイズと閾値の降水量を保持するクラス"""
    def __init__(self):
        # マップのサイズ
        self.map_size = 0
        # 降水量 (Precipitation amount)
        self.threshold = 0
    
    def set_value_from_args(self,input_line_first:str):
        """引数より、メンバ変数をセットす"""
        values = input_line_first.split(' ')
        self.map_size = int(values[0])
        self.threshold = int(values[1])
        
class Maps():
    """マップを作成して降水量を数値として管理する"""
    def __init__(self,map_size:int):
        self.map_size = map_size
        self.map_list = []
        
    def add_map_data(self,precipitation_amount:'list[int]'):
        """降水量リスト1行よりマップを追加する"""
        self.map_list.append(precipitation_amount)
    
    def data_is_valid(self):
        """得られた降水量データすべてが,1 行目にそれぞれ地図のサイズとあっているか確認する"""
        if len(self.map_list) != self.map_size:
            return False
        for buf_map in self.map_list:
            if len(buf_map) != self.map_size:
                return False
        return True

#メイン処理を実行する
main()

