
from pathlib import Path
encoding_def = 'utf8'

def get_target_movie_file_text():
    dir_path = r"J:\avidemux_files"
    file_name = r"target_movie_file.txt"
    path = Path(dir_path).joinpath(file_name)
    return path

def get_movie_path():
    rpath = get_target_movie_file_text()    
    with open(rpath , "r", encoding=encoding_def)as f:
        ret = f.readline()
    return ret

def get_target_movie_time_text():
    dir_path = r"J:\avidemux_files"
    file_name = r"target_movie_time.txt"
    path = Path(dir_path).joinpath(file_name)
    return path

def get_movie_time():
    rpath = get_target_movie_time_text()    
    with open(rpath , "r", encoding=encoding_def)as f:
        ret = f.read()
    ret = ret.replace("\n", "")
    return ret

def get_write_dir_path():
    dir_path = r"J:\avidemux_files\ffmpeg_output"
    return Path(dir_path)

def get_write_path(movie_path, add):
    dist_dir = get_write_dir_path()
    dist_path = dist_dir.joinpath(Path(movie_path).name)
    new_file_path = get_new_file_name(dist_path, add)
    return new_file_path

"""
既存パスのファイル名にaddを加えて、新しいパスを取得する
新しいファイル名filename + add が存在する場合、
新しいファイル名 ＋ _数字 としてファイル名を変更して処理を継続する。
以降、新しいファイル名も存在する場合は数字部分をカウントアップして、ファイルが存在しないようになるまで処理を続ける。
"""
# from pathlib import Path
import re
def get_new_file_name(file_path: str, add: str) -> Path:
    """既存パスのファイル名にaddを加えて、新しいパスを取得する"""
    original_path = Path(file_path)
    new_file_name = original_path.stem + add + original_path.suffix
    new_file_path = original_path.parent / new_file_name
    
    # 数字付きファイル名が必要な場合
    count = 1
    while new_file_path.exists():
        # ファイル名の最後が既に "_数字" であるかを確認し、カウントアップ
        match = re.match(rf"^(.*{re.escape(add)})(_(\d+))?{re.escape(original_path.suffix)}$", new_file_path.name)
        if match:
            base_name = match.group(1)
            count = int(match.group(3)) + 1 if match.group(3) else 1
            new_file_name = f"{base_name}_{count}{original_path.suffix}"
        else:
            new_file_name = original_path.stem + add + f"_{count}" + original_path.suffix
        
        new_file_path = original_path.parent / new_file_name

    return new_file_path




class ConstMovieTime:    
    RESULT_SUCCESS = 1
    RESULT_FAILED = -1
    ERR_PYPHEN_NONE = -2
    ERR_LIST_LENGTH_IS_SINGLE = -2

"""
以下の時間設定を読み込んで、1つのファイルに複数の動画編集を行う
例）
0-3.11 - 5.38,  6.10  ,7.05-8.55

1.基本フォーマット
（ハイフンつなぎで対になった時間を設定する）
[開始時間]-[終了時間]
書式：m:s/m:ss 0.0/0.00
※1桁の数字の0は許容する（0.00）と同じにする
2.hh:mm:ss/ h:m:s も許容する
3.コンマでつなげて、複数の時間区間を設定できる
4.間の空白は無視する
5.書式以外の場合は無視する
6.値が足りないときも無視する

"""
import re
from datetime import timedelta

class MovieTimeInfo:
    def __init__(self) -> None:
        self.begin_time_str = ''
        self.end_time_str = ''
        self.begin_time:timedelta = None
        self.end_time:timedelta = None

    def time_is_invalid(self):
        if self.begin_time == None:
            return True
        if self.end_time == None:
            return True
        return False

    def get_start_sec(self):
        return self.begin_time.total_seconds()

    def get_length_sec(self):
        ret = self.end_time.total_seconds() - self.begin_time.total_seconds()
        return ret

    def _print(self, value):
        print(value)

    def set_value(self, time_str: str):
        """ 文字列 [開始時間-終了時間] を受け取って 開始、終了時間を設定する """
        # 空白を削除し、ハイフンで分割
        time_str = time_str.replace(' ', '')
        # ピリオドはコロンに置き換え
        time_str = time_str.replace('.', ':')
        if '-' not in time_str:
            msg = 'Invalid format: Time string must contain a hyphen. [{}]'.format(time_str)
            # raise ValueError(msg)
            self._print(msg)
            return ConstMovieTime.ERR_PYPHEN_NONE
        buf_list = time_str.split('-')        
        if len(buf_list) != 2:
            msg = 'Invalid format: Time string must have exactly one hyphen and two parts.'
            msg += ' [{}]'.format(time_str)
            # raise ValueError(msg)
            self._print(msg)
            return ConstMovieTime.ERR_LIST_LENGTH_IS_SINGLE
        self.begin_time_str = buf_list[0]
        if self.begin_time_str == '0':
            self.begin_time_str = '0:0'
        self.end_time_str = buf_list[1]
        # それぞれの時間文字列を timedelta に変換
        self.begin_time = self.convert_time_str_to_timedelta(self.begin_time_str)
        self.end_time = self.convert_time_str_to_timedelta(self.end_time_str)
        return ConstMovieTime.RESULT_SUCCESS

    def convert_time_str_to_timedelta(self, single_time_str):
        """ 時間文字列を timedelta に変換する """
        if not self.time_format_is_valid(single_time_str):
            raise ValueError(f"Invalid time format: '{single_time_str}'")
        if len(single_time_str)==1 and single_time_str=='0':
            single_time_str = '0:0'
        time_parts = single_time_str.split(':')
        if len(time_parts) == 2:  # mm:ss or m:ss or m:s
            minutes, seconds = map(int, time_parts)
            return timedelta(minutes=minutes, seconds=seconds)
        elif len(time_parts) == 3:  # hh:mm:ss or h:mm:ss or h:m:s
            hours, minutes, seconds = map(int, time_parts)
            return timedelta(hours=hours, minutes=minutes, seconds=seconds)
        else:
            raise ValueError(f"Invalid time format: '{single_time_str}'")

    def time_format_is_valid(self, single_time_str):
        """ mm:ss, m:ss, m:s か hh:mm:ss, h:mm:ss, h:m:ss ,h:m:s の判定を行う """
        if len(single_time_str)==1 and single_time_str=='0':
            return True
        # 正規表現で時間フォーマットを判定 [0:0]
        pattern = r'^(\d+:\d{1,2}:\d{1,2}|\d{1,2}:\d{1,2})$'
        is_match = bool(re.match(pattern, single_time_str))
        if is_match:
            return True
        # コロンではなくピリオドでも可能とする [0.0]
        pattern = r'^(\d+\.\d{1,2}\.\d{1,2}|\d{1,2}\.\d{1,2})$'
        is_match = bool(re.match(pattern, single_time_str))
        return is_match        
    
    def get_time_delta_str(self):
        """ begin と endのtimeDeltaを文字列で取得する（確認用） """
        begin_str = self.begin_time.__str__()
        end_str = self.end_time.__str__()
        ret = str.format('{}-{}', begin_str, end_str)
        ret = '{}-{}'.format(begin_str, end_str)
        return ret


# # 使用例
# try:
#     time_info = MovieTimeInfo()
#     time_info.set_value("0:15-1:45")
#     print("Begin time:", time_info.begin_time)
#     print("End time:", time_info.end_time)
# except ValueError as e:
#     print(e)



class MovieTimeInfoCollection:
    info_list = []
    time_str_base = ''
    def set_time_list_by_str(self, time_str:str):
        """ 読み取り元time_str を MovieTimeInfoに変換する """
        self.time_str_base = time_str
        time_str = time_str.replace('\n', '')
        # 余計な記号は消してもよいかも（検討）
        #
        #スペース3つも区切りに追加 241123
        time_str_list:'list[str]' = time_str.replace('   ', ',')
        #文字列をコンマで区切って、値の変換処理をする（それぞれ対になるように変換）
        time_str_list:'list[str]' = time_str.split(',')
        for i in range(len(time_str_list)-1):            
            time_str_list[i] = time_str_list[i].strip()
            time_str_b = convert_hyphen_separated_string(time_str_list[i])
            time_str_list[i] = time_str_b
        
        #変換処理によって、split',' のリスト要素の中に 「0-3.11, 3.11-5.38」が作られるので
        #もう一度結合して、splitする
        str_time_b = ','.join(time_str_list)
        print('cnv_time_str = {}'.format(str_time_b))
        time_str_list_b :'list[str]' = str_time_b.split(',')

        for time_str_buf in time_str_list_b:
            info = MovieTimeInfo()
            info.set_value(time_str_buf)
            buf = info.get_time_delta_str()
            print('time_buf = {}'.format(buf))
            self.info_list.append(info)


"""
ハイフンで区切られた文字列が与えられて、
区切った後の文字列値が2つ以上の場合は、
それぞれが対になるようにする。

■文字列　変換例
例1　（ハイフンで区切られた文字列が3つの場合）
　変換前）0.00-3.11 - 5.38
　変換後）0.00-3.11,3.11-5.38
　　（ハイフンで区切られた文字列が2つ以上の場合は、それぞれ対になるようにする）
例2　（ハイフンで区切られた文字列が3つの場合）
　変換前）0.00-3.11 - 5.38 - 6.11
　変換後）0.00-3.11, 3.11-5.38, 5.38-6.11
例3　6.11-8.5
（ハイフンで区切られた文字列が2つの場合は何もしない）
"""
def convert_hyphen_separated_string(input_string):
    """ハイフンで区切られた文字列が与えられて、
区切った後の文字列値が2つ以上の場合は、
それぞれが対になるようにする。
    """
    # ハイフンで文字列を分割し、各要素をトリムする
    parts = [part.strip() for part in input_string.split('-') if part.strip()]
    
    # パーツの数が2以下の場合はそのまま返す
    if len(parts) <= 2:
        return input_string
    
    # 変換後のリストを作成
    converted = [f"{parts[i]}-{parts[i + 1]}" for i in range(len(parts) - 1)]
    
    # カンマで連結して返す
    return ', '.join(converted)
