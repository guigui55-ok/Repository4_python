
from ffmpeg_test1 import Logger
from pathlib import Path
from ffmpeg_common import const_encoding

#他のテキストファイルから
def get_movie_root_path():
    dir_path = r"J:\avidemux_files"
    file_name = r"movie_root_path.txt"
    path = Path(dir_path).joinpath(file_name)
    ret_path = ''
    with open(path, 'r')as f:
        ret_path = f.read().strip()
    print("movie_root_path = {}".format(ret_path))
    return ret_path

# メインファイルパス
def get_movie_info_main_file_path():
    dir_path = r"J:\avidemux_files"
    file_name = r"target_movie_cut_info_list.txt"
    file_name = r"241121_movie.txt"
    path = Path(dir_path).joinpath(file_name)
    print("get_movie_info_main_file_path = {}".format(path))
    return path

class ConstMarker:
    MOVIE_DIR_BEGIN = "***"
    FILE_PATH_BEGIN = "//"


class AnalyzeStatus:
    BEGIN = -1
    NONE = 0
    MOVIE_DIR = 1
    FILE_PATH = 2
    MOVIE_TIME = 3

# メインファイル読み込み、解析
# Dirパス、ファイルパス、時間リスト、オプションを読み込み MovieMainDataのリストにする
def analyze_main_file(logger:Logger, info_main_path:Path)-> 'list[MovieMainData]':
    lines = None
    with open(info_main_path, 'r', encoding=const_encoding)as f:
        lines = f.readlines()

    movie_info_list :'list[MovieMainData]' = []
    # 区切り文字によって、読み取り・解析モードを変えて、モードによってセットする情報を振り分ける
    # 例）***\nディレクトリパス\n//\nファイルパス\n時間リスト（複数行）\n\n***（の繰り返し）
    now_status = AnalyzeStatus.BEGIN
    line_count = 0
    read_movie_dir_path = ""
    read_movie_file_name = ""
    read_movie_time_list_str = ""
    read_add_comment = ""
    is_try_add_data: bool = False
    for line in lines:
        line_count += 1
        ##
        # [データ追加・作成]
        # Movieデータの区切りが来たときに、データをリストに追加する（空データは無視）
        if is_try_add_data:
            before_len = len(movie_info_list)
            _data = create_movie_main_data(
                read_movie_dir_path, read_movie_file_name, read_movie_time_list_str, read_add_comment)
            movie_info_list = add_movie_main_data(movie_info_list, _data)
            logger.info("movie_info_list len = {}".format(len(movie_info_list)))
            is_try_add_data = False
            if before_len < len(movie_info_list):
                read_movie_file_name = ""
                read_movie_time_list_str = ""
                read_add_comment = ""
        ##
        # [モード設定] 区切り文字によって、読み取り解析モードを変更
        if line.startswith(ConstMarker.MOVIE_DIR_BEGIN):
            now_status = AnalyzeStatus.MOVIE_DIR
            is_try_add_data = True
            continue
        elif line.startswith(ConstMarker.FILE_PATH_BEGIN):
            now_status = AnalyzeStatus.FILE_PATH
            is_try_add_data = True
            continue
        ##        
        # [データ読み取り]
        # 空行は読み飛ばし
        if line.strip() == "":
            continue
        # 通常処理
        if now_status == AnalyzeStatus.MOVIE_DIR:
            # 新しいディレクトリに切り替わったら変更
            read_movie_dir_path = Path(line.strip())
            # 読み取ったら一旦アイドル状態に戻す
            now_status = AnalyzeStatus.NONE
            continue
        elif now_status == AnalyzeStatus.FILE_PATH:
            # // → ファイル名 → 次に来るのは時間データなのでモード変更
            read_movie_file_name = line.strip()
            now_status = AnalyzeStatus.MOVIE_TIME
            continue
        elif now_status == AnalyzeStatus.MOVIE_TIME:
            # これは複数行の場合がある
            read_movie_time_list_str += line.strip() 
        else:
            logger.info("想定外のパターン :{}".format(line.strip()))
    return movie_info_list

def add_movie_main_data(data_list:'list[MovieMainData]', data: 'MovieMainData') -> 'list[MovieMainData]':
    """
    MovieMainDataのリストにデータをappendする。
    ------
    初回は空データのなるのでスキップ、その他無効なデータがあるときもスキップ
    """
    if not data.is_blank_data():
        data_list.append(data)
    return data_list

def create_movie_main_data(
        dir_path, file_name, time_str, add_comment) -> 'MovieMainData':
    """動画ファイル編集情報クラスを作成する"""
    _data = MovieMainData()
    _data.dir_path = Path(dir_path)
    _data.file_path = _data.dir_path.joinpath(file_name)
    _data.time_str = time_str
    _data.add_comment = add_comment
    # ディレクトリ内のルートではなく、ディレクトリ内の別のサブフォルダにある場合も対応する
    _data.file_path  = find_file_by_name_if_not_exits(_data.dir_path, file_name)
    return _data

from typing import Optional
def find_file_by_name_if_not_exits(base_dir: str, target_filename: str) -> Optional[Path]:
    """
    指定されたディレクトリ配下から、特定のファイル名を探す
    """
    ret_path = Path(base_dir).joinpath(target_filename)
    if ret_path.exists(): 
        return ret_path
    found_path = find_file_by_name(base_dir, target_filename)
    if found_path == None:
        return ret_path
    else:
        return found_path

def find_file_by_name(base_dir: str, target_filename: str) -> Optional[Path]:
    """
    指定されたディレクトリ配下から、特定のファイル名を探す関数（再帰的に検索）

    Parameters:
        base_dir (str): 探索を開始するディレクトリパス
        target_filename (str): 探したいファイル名（例: 'sample.txt'）

    Returns:
        Path or None: 見つかった最初のファイルのパス。見つからなければ None。
    """
    base_path = Path(base_dir)
    for file_path in base_path.rglob(target_filename):
        return file_path  # 最初に見つかった1件のみ返す
    return None

# def analyze_main_file_add_process(logger:Logger, movie_main_info_list:'list[MovieMainData]'):
#     pass
    

class MovieMainData:
    dir_path:Path = None    
    file_path:Path = None
    time_str:str = ''
    time_list:'list[MovieTimeInfo]' = []
    add_comment = ''
    option = 0

    def is_blank_data(self):
        """空データか判定する"""
        if self.dir_path == '':
            return True
        if  self.file_path == '':
            return True
        if  self.time_str == '':
            return True
        return False
    
    def get_log_str(self, num=None):
        ret = ""
        _list = []
        if num != None:
            _list.append("[{:2}]".format(num))            
        _list.append("dir={}".format(self.dir_path))
        _list.append("name={}".format(self.file_path.name))
        _list.append("time={}".format(self.time_str))
        _list.append("comment={}".format(self.add_comment))
        ret = ', '.join(_list)
        return ret

        
    def get_log_str_simple(self, num=None):
        ret = ""
        _list = []
        if num != None:
            _list.append("[{:2}]".format(num))            
        _list.append("dir_name={}".format(self.dir_path.parent.name))
        _list.append("name={}".format(self.file_path.name))
        _list.append("time_str_len={}".format(len(self.time_str)))
        _list.append("comment={}".format(self.add_comment))
        ret = ', '.join(_list)
        return ret

def _output_movie_main_data_list(logger:Logger, movie_main_data_list:'list[MovieMainData]'):
    count = 0
    logger.info("# _output_movie_main_data_list , len={}".format(len(movie_main_data_list)))
    for _data in movie_main_data_list:
        count += 1
        log_str = _data.get_log_str_simple(count)
        logger.info(log_str)


import ffmpeg_common
from ffmpeg_common import MovieTimeInfo
def create_time_info_list(logger:Logger, time_str:str) -> 'list[MovieTimeInfo]':
    """
    時間文字列から、開始時間・終了時間を取得して、MoveTimeInfoリストにする
    """
    time_str_base = time_str  #動画時間
    logger.info('time_str_base = {}'.format(time_str_base))
    time_col = ffmpeg_common.MovieTimeInfoCollection()
    time_col.set_time_list_by_str(time_str_base)
    time_info_list :'list[MovieTimeInfo]' = time_col.info_list
    return time_info_list

def _analyze_time_str(logger:Logger, mov_data_list: list[MovieMainData] ):
    # Analyze Convert
    count = 0
    for _data in mov_data_list:
        count += 1
        _data.time_list = create_time_info_list(logger, _data.time_str)
    # Log
    count = 0
    for _data in mov_data_list:
        count += 1
        # logger.info("{:2}: {}".format(count, MovieTimeInfo.get_log_str(_data.time_list)))
        logger.info("==========")
        logger.info("dir = {}".format(str(_data.dir_path)) + " , filename = {}".format(str(_data.file_path.name)))
        logger.info("{:2}: {}".format(count, MovieTimeInfo.get_log_timedelta(_data.time_list)))
        # break
    return 
################################################################################
################################################################################
import datetime
def _test_main():
    log_filename = datetime.datetime.now().strftime("__test_%y%m%d_%H%M%S.log")
    log_path = Path(__file__).parent.joinpath(log_filename)
    logger = Logger(log_path)
    # 情報ファイル読み込み
    # 動画情報がすべて記載されているファイル
    movie_info_main_path = get_movie_info_main_file_path()

    ##
    ## [機能]
    ##
    # すべての行を解析して、movieMainDataのリストを作成
    # MoveMainDataのデータ構成は（フォルダ、ファイル名、時間リスト、オプション・コメント）
    # エラー情報の場合はフラグで管理
    # エラーパターン（時間がない、フォルダ名がない、ファイル名がない、時間リストで不具合がある）
    #（ファイルパスが存在しない）

    # [メイン部]
    movie_main_data_list:list[MovieMainData] = analyze_main_file(logger, movie_info_main_path)
    _output_movie_main_data_list(logger, movie_main_data_list)

    # 時間例外パターン
    # 連なったパターン：0-3.30-8.17 →これは 0-3.30、3.30-8.17 にする
    # 空行
    # 開始時間省略パターン： -1.34
    # 開始時間がゼロのみ： 0-1.34
    # 対象の時間がない場合：'x', 'xxx'
    # すべての時間を対象： 0--,  0- 
    # ※数字が1つもない場合はスキップする？
    _analyze_time_str(logger, movie_main_data_list)

    logger.info("##### cut_movie_main")
    #成功ファイルリスト（and 無視リスト）は処理を除外する
    import file_check
    import ffmpeg_test1
    import traceback
    count = 0
    for movie_main_data in movie_main_data_list:
        count += 1
        is_exists_in_check_list = file_check.is_exists_path_in_file_list_text(movie_main_data.file_path)
        if is_exists_in_check_list :
            logger.info("is_exists = True , path = {}".format(movie_main_data.file_path))
            continue
        #変換処理
        is_success = ffmpeg_test1.cut_movie_main(logger, movie_main_data.file_path, movie_main_data.time_list)
        # try:
        #     ffmpeg_test1.cut_movie_main(logger, movie_main_data.file_path, movie_main_data.time_list)
        # except Exception as e:
        #     logger.info("==========")
        #     logger.info("cut_movie_main error")
        #     logger.info("{}:{}".format(str(type(e)), str(e)))
        #     logger.info(traceback.format_exc())
        #     logger.info("===")
            
        #成功ファイルリスト（成功したら追記、存在するファイルパスは追記しない）
        if is_success:
            file_check.append_file_path(movie_main_data.file_path)


if __name__ == "__main__":
    print("\n*****")
    _test_main()
    print("\n")