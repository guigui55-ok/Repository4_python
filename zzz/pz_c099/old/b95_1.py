from input.input import debug_print_file, input,input_init
input_init(2)
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
#input_line = input()
#print("XXXXXX")

DEBUG = False
def debug_print(value):
    """デバッグ出力用"""
    if DEBUG:
        print(str(value))

class SingingPersion():
    """うたった人のデータクラス"""
    def __init__(self):
        self.init_data()
        
    def init_data(self):
        #うたった順番
        self.order = 0
        #音程
        self.sing_pitches = []
        #得点
        self.score = 0
        
    def set_pitch_list(self,values:'list[str]'):
        """音程を追加する"""
        self.sing_pitches = list_to_int(values)

class ScoreCalclator():
    """得点を計算するクラス"""
    def __init__(self,music_length:int):
        #課題曲の長さ
        self.music_length = music_length
        #正しい音程
        self.correct_pitches = []
    
    def calc_score_main(self,sing_pitches:'list[int]'):
        total_substract = 0
        for i in range(self.music_length):
            correct_pitch = self.correct_pitches[i]
            sing_pitch = sing_pitches[i]
            now_substract = self.calc_score_single(correct_pitch,sing_pitch)
            debug_print(now_substract)
            total_substract += now_substract
        return self.fix_score(100 - total_substract)

    def fix_score(self,score):
        if score < 0:
            return 0
        else:
            return score
    
    def calc_score_single(self,correct_pitch:int,sing_pitch:int):
        diff = abs(correct_pitch - sing_pitch)
        if diff <= 5:
            score_substract = 0
        elif diff <= 10:
            score_substract = 1
        elif diff <= 20:
            score_substract = 2
        elif diff <= 30:
            score_substract = 3
        else:
            score_substract = 5
        return score_substract
            
def list_to_int(list_val):
    """文字列のリストを数値のリストに変換する"""
    ret = []
    for val in list_val:
        ret.append(int(val))
    return ret

def get_singer_amount_and_music_length():
    """うたった人の人数と、課題曲の長さを取得する"""
    ary = input().split(' ')
    return int(ary[0]) , int(ary[1])

def get_data(number:int):
    """値を回数分取得して、リストで取得する"""
    ret = []
    for _ in range(number):
        ret.append(input())
    return ret

def main():
    """メイン処理部"""
    #うたった人数、曲の長さを取得する
    singer_amount , music_length = get_singer_amount_and_music_length()
    debug_print([singer_amount , music_length])
    #課題曲の正しい音程を取得する
    cl_score_calclator = ScoreCalclator(music_length)
    cl_score_calclator.correct_pitches = list_to_int(get_data(music_length))
    debug_print(cl_score_calclator.correct_pitches)
    #うたった人の得点を処理する
    result_list:'list[int]' = []
    cl_singer = SingingPersion()
    for i in range(singer_amount):
        #うたった人のデータを初期化
        cl_singer.init_data()
        #うたった順番
        cl_singer.order = i+1
        #うたった音程リストを取得
        cl_singer.set_pitch_list(get_data(music_length))
        debug_print(cl_singer.sing_pitches)
        #歌を採点
        cl_singer.score = cl_score_calclator.calc_score_main(cl_singer.sing_pitches)
        #結果を一旦リストへ
        result_list.append(cl_singer.score)
    
    #結果を出力
    print(max(result_list))
    
main()
    
    