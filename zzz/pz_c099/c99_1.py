from input.input import Input,input_init
input_init()
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

#条件が一致したときに加算する数値
ADD_NUM = 2

def main()->str:
    map_manager = MapManager()
    # 1行目のマップサイズと閾値を取得する
    map_manager.set_value_from_args(Input())
    # 1行目以降の降水量リストよりマップを作成する
    maps = Maps(map_manager.map_size)

    # 降水量リストを読み込み数値化する
    for _ in range(map_manager.map_size):
        maps.add_map_data(Input())
    # マップの大きさとあっているか確認する
    if not maps.data_is_valid():
        raise Exception('precipitation_amount data is invalid')
    # ルートが閾値以上か判定して、ルート番号を取得する
    cl_judge = JudgePass()
    for i in range(len(maps.map_list)):
        precipitation_amount_int_list = maps.map_list[i]
        is_pass = cl_judge.judge_one_line(map_manager.threshold,precipitation_amount_int_list)
        if is_pass:
            cl_judge.add_result(i+ADD_NUM)
    #自宅待機か判定する
    cl_judge.judge_wait()
    #最後に改行を付与する
    result = cl_judge.result + '\n'
    #結果を出力する
    print(result)
    return
    

class InputLine():
    """与えられたデータを処理するクラス"""
    def __init__(self,input_line:str):
        self.input_line = input_line
    def split_value(self,delimita:str=' '):
        """区切り文字によって値を分ける"""
        self.input_line_list = self.input_line.split(delimita)

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
        
    def init_precipitation_amount(self,precipitation_amount_list:'list[str]'):
        """降水量複数行よりマップリストを作成する"""
        for precipitation_amount in precipitation_amount_list:
            self.add_map_data(precipitation_amount)

    def add_map_data(self,precipitation_amount):
        """降水量リスト1行よりマップを追加する"""
        values = precipitation_amount.split(' ')
        buf_list:'list[int]' = []
        for value in values:
            buf_list.append(int(value))
        self.map_list.append(buf_list)
    
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


