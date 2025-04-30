# 縦 H 個、横 W 個
h,w = map(int, input().split())

# 山のデータを取得（リストの1行が横軸）
map_data_horizon = []
for i in range(h):
    map_data_horizon.append(input())

# 扱いやすいように縦横変換（1行が縦軸のリストへ変換）
map_data_vertical = []
for i in range(w):
    buf = ""
    for j in reversed(range(h)):
        buf += map_data_horizon[j][i]
    map_data_vertical.append(buf)
    
##
## それぞれの行の1つ目をチェックして、山の区切りがあるか判定しながら、現在の山のサイズを加算していく
## 区切りがあった場合は、計算中の山データを格納、別の新しい山データを作成する
## （最大サイズ500×500）
##
#それぞれの山のサイズリスト
mountain_size_list = [00] 
# 現在のサイズ 
now_size = 0

for i in range(w):
    now_line = map_data_vertical[i]
    #
    # 1つ目がゼロの時は山が区切られている
    #
    if now_line[0] == "0":
        # 加算済みのデータがあれば、リストへ格納
        if now_size > 0:
            mountain_size_list.append(now_size)
        now_size = 0
    #
    #サイズを加算していく
    #
    now_size += now_line.count("1")
    
# 最後に計算している山をリストへ追加
if now_size > 0 :
    mountain_size_list.append(now_size)

# 結果出力
# 一番サイズが大きい山を出力
print(max(mountain_size_list))
