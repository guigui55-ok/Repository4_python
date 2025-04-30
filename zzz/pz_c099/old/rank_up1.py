# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def main():
    """メイン処理部"""
    #input1行目のデータから、盤面の列数、行数、与えられる座標の数をセットする
    row , col , coordinate_amount = get_data_from_nput()
    #盤面をセットする
    string_table_list = []
    for _ in range(row):
        string_table_list.append(input())
    #与えられる座標を取得し、座標から文字列を取得、結果出力用変数に格納する
    result_list = []
    for _ in range(coordinate_amount):
        # 与えられる座標を取得する
        ary = input().split(' ')
        x,y = int(ary[0]) , int(ary[1])
        # 座標から文字列を取得する
        ret = string_table_list[x][y]
        # 結果出力用変数に格納する
        result_list.append(ret)
    
    #結果を出力する
    for ret in result_list:
        print(ret)

def get_data_from_nput():
    ary = input().split(' ')
    return int(ary[0]), int(ary[1]), int(ary[2])


#######################
H, W, N = map(int, input().split())
S = [list(input()) for _ in range(H)]
for _ in range(N):
  y, x = map(int, input().split())
  print(S[y][x])