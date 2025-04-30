import copy
# 駒が最初に置かれた場所が上から何行目か表す整数 H
# 左から何列目かを表す整数 W
# 移動回数を表す整数 K
h,w,k = map(int, input().split())

BAN_SIZE_X = 9
BAN_SIZE_Y = 9
LOG_OUTPUT = False

# LoggerClass
class Logger:
    is_output = LOG_OUTPUT
    def info(self, value):
        if self.is_output:
            print(value)

# 2つの値を扱う
class Point:
    #x = 0 
    #y = 0
    def __init__(self, _x =0, _y =0):
        self.x=_x
        self.y=_y
    def is_enable(self):
        if self.x >= 0 and self.y >= 0:
            return True
        else:
            return False
    def is_under(self, check_point:'Point'):
        if self.x < check_point.x and self.y < check_point.y:
            return True
        else:
            return False
    def is_same(self, check_point:'Point'):
        if self.x == check_point.x and self.y == check_point.y:
            return True
        else:
            return False
        

# 駒の動きと、移動判定などをする
class KomaAbs:
    # 盤のサイズ
    ban_size : Point = Point()
    # 駒の効き
    move_enable_list: 'list(Point)' = []
    # 現在の位置リスト
    now_pos_list: 'list(Point)' = []
    # 移動した履歴
    moved_pos_list: 'list(Point)' = []
    # 次に移動するリスト（一時保管用）
    next_pos_list : 'list(Point)' = []
    # 
    logger:'Logger' = None
    
    def __init__(self, width, height):
        self.ban_size = Point(width , height)
    
    # 与えられている、現在の位置リストと駒の効きから「次の移動するリスト」を算出
    def calc_move_enable(self):
        self.next_pos_list = []
        next_list_buf =[]
        for now_pos in self.now_pos_list:
            next_list_buf = []
            for move_pos in self.move_enable_list:
                #print_pos_list(self.logger, [move_pos], "calc_pos ")
                check_pos = self._calc_move_enable_single(now_pos, move_pos)
                # 計算した駒の位置が有効な位置なら、次の移動リストに追加
                if check_pos.is_enable():
                    if check_pos.is_under(self.ban_size):
                        #next_list_buf.append(check_pos)
                        point_list_append_not_same(next_list_buf, check_pos)
            logger.info("**")
            print_pos_list(self.logger, [now_pos], "now_pos ")
            print_pos_list(self.logger, next_list_buf, "next_list_buf ")
            #self.next_pos_list.extend(next_list_buf)
            point_list_extend_not_same(self.next_pos_list, next_list_buf)
    
    #算出した次に移動するリストから、次に移動するリストの重複を除去
    def update_moved_pos_list(self):
        if len(self.moved_pos_list) < 1:
            self.moved_pos_list = self.next_pos_list
            return
        self.moved_pos_list = point_list_remove_same_value(self.next_pos_list)
        print_pos_list(self.logger, self.moved_pos_list, "self.moved_pos_list  ")
    
    #算出した次に移動するリストから、現在の位置リストを更新
    def update_now_pos_list_to_next(self):
        self.now_pos_list = self.next_pos_list
        
    #計算処理
    def _calc_move_enable_single(self, now_pos:Point, move_pos:Point):
        return Point( now_pos.x + move_pos.x,  now_pos.y + move_pos.y)

# 駒を動かすときに「変身していない、変身済み」のパターンを作っておく
# 0＝変身済みしていない、1=変身済み
patterns = []
for i in range(k):
    buf_a = ["0" for _ in range(k - i)]
    buf_b = ["1" for _ in range(i)]
    buf = ''.join(buf_a) + ''.join(buf_b)
    patterns.append(buf)

#PointListの重複する値を削除
def point_list_remove_same_value(point_list : 'list(Point)'):
    new_list = []
    for i, point_value in enumerate(point_list):
        is_same_pos = False
        if i ==0:
            new_list.append(point_value)
            continue
        for check_value in point_list[:i-1]:
            if point_value.is_same(check_value):
                is_same_pos = True
                break
        if not is_same_pos:
            new_list.append(point_value)
    return new_list
    
# 重複しない場合、Pointリストに追加
def point_list_append_not_same(point_list:'list(Point)', add_point:'Point'):
    for p in point_list:
        if p.is_same(add_point):
            return point_list
    point_list.append(add_point)
    return point_list
        
# PointListに重複しない値のみを追加
def point_list_extend_not_same(point_list_a : 'list(Point)', point_list_b : 'list(Point)'):
    add_list = []
    for point_b in point_list_b:
        is_same_value = False
        for point_a in point_list_a:
            if point_b.is_same(point_a):
                is_same_value = True
                break
        if not is_same_value:
            add_list.append(point_b)
    point_list_a.extend(add_list)
    return point_list_a
        
# 確認用
def print_pos_list(logger:'Logger', point_list:'list(Point)', comment=""):
    l = []
    for p in point_list:
        l.append(f'[{p.x}, {p.y}]')
    logger.info(comment + ', '.join(l))

##########
# [方針]
# 最初に、サイズ、コマの動きをセットする
# 次に、現在の位置をセットする。
# 現在の位置から、コマの動きを加算し、動ける場所リストを「現在の位置リスト」に格納
# そして、「現在の位置リスト」で「次の位置リスト」で更新する。
# （次の位置リストは、重複不可）
# 最終な次の位置リストが回答となる
# ※「駒が変身したか」は別フラグで管理をして、変身したら、move_enable_listを入れ替える

##########
## 処理部メイン

logger = Logger()
koma = KomaAbs(BAN_SIZE_X,BAN_SIZE_Y)
# 駒Aの効きを設定
move_enable_list_a = [
    Point(-1, -1),
    Point(0 ,-1),
    Point(1, -1),
    Point(-1, 1),
    Point(1,1)]
# 駒Aの効きを設定
move_enable_list_b = [
    Point(-2, 1),
    Point(2,-1)]
# 駒の開始位置
now_pos_list_buf =[Point(w-1,h-1)]
koma.logger = logger

all_pos_list = []
for i, pattern in enumerate(patterns):
    logger.info('i:{}, pat={}'.format(i, pattern))
    #if i != 1:
    #    continue
    koma.now_pos_list = now_pos_list_buf
    for hensin in pattern:
        # 変身するかどうか
        move_enable_list_buf = move_enable_list_a
        if hensin == "1":
            move_enable_list_buf = move_enable_list_b
        koma.move_enable_list = move_enable_list_buf
        # 計算
        koma.calc_move_enable()
        logger.info("---")
        print_pos_list(logger, koma.next_pos_list, "koma.next_pos_list ")
        koma.update_moved_pos_list()
        koma.update_now_pos_list_to_next()
        logger.info("koma.moved_pos_list len={}".format(len(koma.moved_pos_list)))
        print_pos_list(logger, koma.moved_pos_list, "koma.moved_pos_list ")
    all_pos_list.extend(koma.next_pos_list)

#重複を削除
ret_pos_list = point_list_remove_same_value(all_pos_list)

# 結果出力
print(len(ret_pos_list))
