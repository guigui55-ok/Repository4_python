
import sys
import time
from pathlib import Path
import glob
import shutil
import os

path = str(Path(__file__).parent.parent)
sys.path.append(path)
import import_init
from html_log.html_logger import HtmlLogger,BasicLogger


class DirChecker():
    def __init__(self,dir_path:str) -> None:
        self.path = dir_path
        self.path_list = []
        self.observe_target = ''
    def get_now_dir_list(self):
        temp_list = glob.glob(self.path + '/**')
        return temp_list
    def update_list(self):
        temp_list:list = self.get_now_dir_list()
        self.path_list = temp_list.copy()
        return temp_list
    def get_increased_list(self,arg_list:'list[str]'):
        """self.path_list より増えているものがあればリストで取得する"""
        ret_list = []
        for val in arg_list:
            if not val in self.path_list:
                ret_list.append(val)
        return ret_list
    def is_exists(self,path:str):
        if os.path.exists(path):
            return True
        return False
    def get_target_ext(self,ext):
        now_list = self.get_now_dir_list()
        ret = []
        for path in now_list:
            if path.endswith(ext):
                ret.append(path)
        return ret

class ObserberType():
    EXT = 1
    PATH = 2
    FILE_NAME = 3
    DIR_NAME = 4

class DownloadDirectoryObserver():
    """
    TARGET_EXT(.crdownload) があったらダウンロードが終わるまで監視する、
    ダウンロードがストップしたら終了する
    """
    def __init__(self,observe_dir_path:str,logger:BasicLogger) -> None:
        self.dir_path = observe_dir_path
        self.ext = ''
        self.logger:BasicLogger = logger
        #240522
        # ダウンロード対象のファイル拡張子
        # ダウンロード中ファイル[.crdownload]がないときでも、mp4があればダウンロード済みとする
        # （実行前にmp4はすべて移動・削除しておくこと）
        self.target_ext = '.mp4'
        #240522
        # ダウンロード後ファイル拡張子があれば、最初に移動しておく
        # そのためのフォルダ
        self.move_folder_path = Path(self.dir_path).joinpath('download_files')

    def set_conditions(self,value:str):
        self.target_type = value
        self.ext=value

    def init_dir(self):
        """監視対象のext（ダウンロード中）ファイルは消しておく"""
        if self.ext=='':return
        path_list = glob.glob(self.dir_path + '/**')
        for path in path_list:
            if path.endswith(self.ext):
                os.remove(path)
                self._print('removed = {}'.format(Path(path).name))
    
    def init_move_downloaded_file(self):
        """
        監視対象のフォルダに以前のダウンロード後ファイルがあれば移動しておく
            (self.target_ext を含むファイルをすべて[download_files]フォルダに移動する)
        """
        Path(self.move_folder_path).mkdir(exist_ok=True)
        match_files = glob.glob(str(self.dir_path) + '/*' + self.target_ext)
        for matchfile in match_files:
            # shutil.move(str(matchfile), str(self.move_folder_path))
            _move_file(str(matchfile), str(self.move_folder_path))
            self._print('move_file = {}'.format(Path(matchfile).name))

    def _print(self, value):
        print(str(value))
    
    def is_exists_download_file(self,target_path:str):
        if os.path.exists(target_path):
            flag = True
        else:
            flag = False
        self.logger.add_log('is Exists = {} , path = "{}"'.format(flag,target_path))
        return flag
    
    def is_exists_target_download_file_with_ext(self):
        """
        ダウンロード対象の拡張子（self.target_ext=mp4など）が存在するか判定する
        """
        checker = DirChecker(self.dir_path)
        target_list = checker.get_target_ext(self.target_ext)
        if len(target_list)<1:
            self.logger.add_log('target_ext[{}] is len<1'.format(self.target_ext))
            return False
        else:
            self.logger.add_log('target[{}] is Exists({})'.format(
                self.target_ext, len(target_list)))
            return True
        
    def is_exists_download_file_or_temp_file(self):
        """ダウンロード対象のファイル（拡張子が合致したもの）orダウンロード中ファイルがあるか判定する"""
        checker = DirChecker(self.dir_path)
        target_list = checker.get_target_ext(self.ext)
        if len(target_list)<1:
            self.logger.add_log('target[{}] is len<1'.format(self.ext))
            # ダウンロード中ファイル(EndsWiths(self.ext))がない時は、すでにダウンロード済みの場合がある
            # ダウンロード対象の拡張子のファイルがあればダウンロード済みとする
            if self.is_exists_target_download_file_with_ext():
                return True
            else:
                return False
        else:
            target = target_list[0]

    def excute(self):
        # ダウンロードを押した後で実行する
        # ダウンロード中であるか、終わっている前提
        # delete_target_ext(path,TARGET_EXT)
        checker = DirChecker(self.dir_path)
        self.logger.add_log('download folder = {}'.format(self.dir_path))
        # now_list = checker.update_list()
        # no_count = 0
        # begin_wait_limit_times = 30
        # begin_wait = 2
        check_limit_min = 10
        is_passed_loop = False
        # print('check dir path.  path = {}'.format(path))
        target_list = checker.get_target_ext(self.ext)
        if len(target_list)<1:
            self.logger.add_log('target[{}] is len<1'.format(self.ext))
            # ダウンロード中ファイル(EndsWiths(self.ext))がない時は、すでにダウンロード済みの場合がある
            # ダウンロード対象の拡張子のファイルがあればダウンロード済みとする
            if self.is_exists_target_download_file_with_ext():
                return True
            else:
                return False
        else:
            target = target_list[0]

        self.logger.add_log('Start to observe file.  path = {}'.format(target))
        start = time.time()
        before_size = os.path.getsize(target)
        time_log_flag = False
        count = 0
        while checker.is_exists(target):
            passed_time = time.time() - start
            if passed_time > (check_limit_min*60):
                print()
                self.logger.add_log('time passed to limit. passed_time = {}'.format(passed_time))
                break
            if not time_log_flag:
                if int(passed_time) % 5==0:
                    self.logger.add_log('downloading...[{} sec]'.format(count*5))
                    count +=1
                    time_log_flag = True
            else:
                if int(passed_time) % 6==0:
                    time_log_flag = False

            time.sleep(2)
            try:
                now_size = os.path.getsize(target)
                if before_size == now_size:
                    self.logger.add_log('download is stopped')
                    is_passed_loop = True
                    break
            except:
                self.logger.add_log('file size check error.  path = {}'.format(target))
                is_passed_loop = True
        print()
        self.logger.add_log('End to observe file.')
        time.sleep(3)
        flag = self.is_exists_download_file(os.path.splitext(target)[0])
        return flag


def _move_file(src_path, dist_path, exists_rename:bool=True):
    if Path(dist_path).is_dir():
        dist_path_b = Path(dist_path).joinpath(Path(src_path).name)
    else:
        dist_path_b = Path(dist_path)
    if exists_rename:
        if Path(dist_path_b).exists():
            new_file_name = _create_rename_file(dist_path_b)
            dist_path_b = Path(dist_path).joinpath(new_file_name)
    
    shutil.move(str(src_path), str(dist_path_b))
    # _move_file(str(src_path), str(dist_path_b))
    # FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\OK\\Downloads\\download_movie_files\\y2matOn Haul  Transparent Lingerie and Clothes_1440p(1).mp4'
    

import re
def _create_rename_file(path):
    re_ret = re.match(r'$(\d)', Path(path).stem)
    if re_ret!=None:
        buf = re_ret.group()
        num = int(buf)
        num += 1
        new_file_name = Path(path).stem.replace(buf,'')
        new_file_name += '({})'.format(num) + Path(path).suffix
    else:
        new_file_name = Path(path).stem + '(1)' + Path(path).suffix
    return new_file_name