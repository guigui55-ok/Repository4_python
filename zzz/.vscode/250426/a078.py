# coding: utf-8
### Input
input_count = int(input())

### Constants
LOG_OUTPUT = False
LOOP_MAX_COUNT = 10
DOT_CHAR = "."

### クラス定義
# LoggerClass
class Logger:
    is_output = LOG_OUTPUT
    def info(self, value):
        if self.is_output:
            print(value)

# 2つの値を扱う
class Point:
    def __init__(self, _x =0, _y =0):
        self.x=_x
        self.y=_y

# ブロックTable
class BlockTable:
    logger = None
    block_lines = []
    current_pos:Point = None
    block_flag_manager = None
    pos_cals = None
    
    def __init__(self):
        current_pos = Point()
    
    def add_block_data(self, input):
        self.block_lines.append(input)
    
    def set_flags(self):
        self.block_flag_manager = BlockFlagsManager()
        self.block_flag_manager.resize(self.block_lines)
        self.block_flag_manager.init_value(self.block_lines)
        self.pos_cals = PositionCalcrator()
        self.pos_cals.resize(self.block_lines)
        
    def check_same_block(self):
        x_max = len(self.block_lines[0])
        y_max = len(self.block_lines)
        for y, b_line in enumerate(self.block_lines):
            # すべてチェックして、左右上下同じなら、消去フラグerase_main=True
            # 壁の時も対応
            for x, b_char in enumerate(b_line):
                current_pos = Point(x, y)
                
                if x+1 < x_max:
                    check_pos = Point(x+1, y)
                    if self.is_same_value(current_pos, check_pos):
                        self.block_flag_manager.flag_lines[y][x].is_same_right = True
                else:
                    self.block_flag_manager.flag_lines[y][x].is_same_right = True
                if x-1 >= 0:
                    check_pos = Point(x-1, y)
                    if self.is_same_value(current_pos, check_pos):
                        self.block_flag_manager.flag_lines[y][x].is_same_left = True
                else:
                    self.block_flag_manager.flag_lines[y][x].is_same_left = True
                if y+1 < y_max:
                    check_pos = Point(x, y+1)
                    if self.is_same_value(current_pos, check_pos):
                        self.block_flag_manager.flag_lines[y][x].is_same_bottom = True
                else:
                    self.block_flag_manager.flag_lines[y][x].is_same_bottom = True
                if y-1 >= 0:
                    check_pos = Point(x, y-1)
                    if self.is_same_value(current_pos, check_pos):
                        self.block_flag_manager.flag_lines[y][x].is_same_top = True
                else:
                    self.block_flag_manager.flag_lines[y][x].is_same_top = True
                
                if self.block_flag_manager.flag_lines[y][x].is_erase_able():
                    self.block_flag_manager.flag_lines[y][x].is_erase_main = True
                    if x+1 < x_max:
                        if self.block_flag_manager.flag_lines[y][x].is_same_right:
                            self.block_flag_manager.flag_lines[y][x+1].is_erase_main = True
                    if x-1 >= 0:
                        if self.block_flag_manager.flag_lines[y][x].is_same_left:
                            self.block_flag_manager.flag_lines[y][x-1].is_erase_main = True
                    if y-1 >= 0:
                        if self.block_flag_manager.flag_lines[y][x].is_same_top:
                            self.block_flag_manager.flag_lines[y-1][x].is_erase_main = True
                    if y+1 < y_max:
                        if self.block_flag_manager.flag_lines[y][x].is_same_bottom:
                            self.block_flag_manager.flag_lines[y+1][x].is_erase_main = True
        return
        # log（デバッグ用）
        log_lines = []
        for flag_lines in self.block_flag_manager.flag_lines:
            log = ""
            for flag in flag_lines:
                if flag.is_erase_horizon:
                    log += "1"
                else:
                    log += "0"
            log_lines.append(log)
        self.logout_table_other(log_lines)
    ################################################################################
    ################################################################################
        
    def is_same_value(self, current_pos:Point, check_pos:Point):
        char_a = self._get_char(current_pos)
        char_b = self._get_char(check_pos)
        if char_a == DOT_CHAR or char_b == DOT_CHAR:
            return False
        ret = False
        if char_a == char_b:
            ret= True
        else:
            ret= False
        return ret
        #self.logger.info("[{},{}-{},{}]={}".format(current_pos.x, current_pos.y, char_a, char_b ,ret))
        
    def _get_char(self, pos:Point):
        if pos.y < 0 or pos.x < 0 :
            return ""
        return self.block_lines[pos.y][pos.x]
        
    def erase_block(self):
        erase_count = 0
        for y, b_line in enumerate(self.block_lines):
            for x, b_char in enumerate(b_line):
                #logger.info("{},{} = {}".format(y,x,  self.block_flag_manager.flag_lines[y][x].is_erase_main))
                if self.block_flag_manager.flag_lines[y][x].is_erase_main:
                    self.block_lines[y] = self._replace_char(self.block_lines[y], x , DOT_CHAR)
                    erase_count += 1
        return erase_count            
        
                    
    def _replace_char(self, value:str, pos:int , char:str):
        buf_list = list(value)
        buf_list[pos] = char
        return "".join(buf_list)
                    
    def down_block(self):
        work_block_lines = conret_table_for_block_down(self.block_lines)
        # 文字列を左詰めにして、余った右側を"."で埋める
        length = len(work_block_lines[0])
        for i in range(len(work_block_lines)):
            buf = work_block_lines[i].replace(DOT_CHAR, "")
            work_block_lines[i] = buf.ljust(length, DOT_CHAR)
        self.block_lines = convert_table_for_block_down_reverse(work_block_lines)
        #self.logout_table_other(self.block_lines)
        
    ################################################################################
        
    def logout_table_other(self, block_lines:'list(str)'):
        self.logger.info("---------")
        for i, line in enumerate(block_lines):
            self.logger.info("[{}] {}".format(i, line))
            
    def logout_table(self):
        self.logger.info("---------")
        for i, line in enumerate(self.block_lines):
            self.logger.info("[{}] {}".format(i, line))
            
    def logout_table_result(self):
        for i, line in enumerate(self.block_lines):
            print(line)
    
# 位置計算用
class PositionCalcrator:
    table_size :Point = Point()
    def __init__(self):
        pass
    def resize(self, block_lines:'list(str)'):
        h = len(block_lines)
        w = 0
        if len(block_lines) > 0:
            w = len(block_lines[0])
        table_size = Point( w, h )
    def get_right_pos(self, current_pos: Point):
        return Point(current_pos.x + 1, current_pos.y)
    

# BlockFlagを2次元配列で扱う
class BlockFlagsManager:
    flag_lines : 'list(list(BlockFlag))' = []
    def __init__(self):
        pass
    
    def resize(self, block_lines:'line(str)'):
        # テーブルデータの大きさから作成する
        for line in block_lines:
            buf = [BlockFlag(DOT_CHAR) for _ in range(len(line))]
            self.flag_lines.append(buf)

    def init_value(self, block_lines:'line(str)'):
        for i, line in enumerate(block_lines):
            for j, block_char in enumerate(line):
                self.flag_lines[i][j] = BlockFlag(block_char)


# ブロックの状態を管理
class BlockFlag:
    is_erase_main = False
    is_same_right = False
    is_same_left = False
    is_same_bottom = False
    is_same_top = False
    is_nothing = True
    
    def __init__(self, block_value:str):
        if block_value == ".":
            self.is_nothing = True
        else:
            self.is_nothing = False
    
    def is_erase_able(self):
        flag_list = [self.is_same_right, self.is_same_left, self.is_same_top, self.is_same_bottom]
        if flag_list.count(True) >= 4:
            return True
        else:
            return False
        

### 関数
# 列を逆順にして、行列変換する（落下処理をしやすいように変換）（右に90度回転）
# 以下のように変換する
# .15.
# 222.
# 3..3
# 4..4
# ↓
# 432.
# ..21
# ..25
# 43..
def conret_table_for_block_down(block_lines: 'list(str)'):
    # 1×1以上を想定
    ret_list = []
    for i in range(len(block_lines[0])):
        new_line = ""
        for line in reversed(block_lines):
            new_line += line[i]
        ret_list.append(new_line)
    return ret_list

# 上記の逆（左に90度回転）
def convert_table_for_block_down_reverse(block_lines: 'list(str)'):
    ret_list = []
    for i in reversed(range(len(block_lines[0]))):
        new_line = ""
        for line in block_lines:
            new_line += line[i]
        ret_list.append(new_line)
    return ret_list
    

###
# ブロックは取得したままの値（文字列配列）で扱う
# (0,0)がブロックの左上

###
# メイン
logger = Logger()
block_table = BlockTable()
block_table.logger = logger

# データをセット
for _ in range(input_count):
    block_table.add_block_data(input())

#for i, line in enumerate(block_table.block_lines):
#    logger.info("[{}] {}".format(i, line))

loop_count = 0
while True:
    logger.info("# loop_count = {}".format(loop_count))
    block_table.current_pos = Point(0,0)
    block_table.set_flags()
    block_table.block_flag_manager.init_value(block_table.block_lines)
    
    # 隣接するブロックかを判定（右隣か左隣に同じ数字があるか）LR
    block_table.check_same_block()
    # ブロックを消去する
    erased_count = 0
    erased_count = block_table.erase_block()
    logger.info("erased_count = {}".format(erased_count))
    # ブロックを落下
    block_table.down_block()
    # log
    block_table.logout_table()
    #break
    if erased_count == 0:
        break
    #
    if loop_count >= LOOP_MAX_COUNT:
        break
    loop_count += 1



### 結果出力
block_table.logout_table_result()