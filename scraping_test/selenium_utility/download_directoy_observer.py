
import glob,os,time
from html_log.html_logger import BasicLogger

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


class DownloadDirectoryObserver():
    """.crdownload があったらダウンロードが終わるまで監視する、ダウンロードがストップしたら終了する"""
    def __init__(self,observe_dir_path:str,logger:BasicLogger) -> None:
        self.dir_path = observe_dir_path
        self.ext = ''
        self.logger = logger
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
    def add_log(self,value):
        self.add_log(value)
    def is_exists_download_file(self,target_path:str):
        if os.path.exists(target_path):
            flag = True
        else:
            flag = False
        self.add_log('is Exists = {} , path = "{}"'.format(flag,target_path))
        return flag
    def init_move_downloaded_file(self):
        """
        監視対象のフォルダに以前のダウンロード後ファイルがあれば移動しておく
            (self.target_ext を含むファイルをすべて[download_files]フォルダに移動する)
        """
        Path(self.move_folder_path).mkdir(exist_ok=True)
        match_files = glob.glob(str(self.dir_path) + '*' + self.target_ext)
        for matchfile in match_files:
            shutil.move(str(matchfile, str(self.move_folder_path)))
            self._print('move_file = {}'.format(Path(matchfile).name))
    def excute(self):
        # ダウンロードを押した後で実行する
        # ダウンロード中であるか、終わっている前提
        # delete_target_ext(path,TARGET_EXT)
        checker = DirChecker(self.dir_path)
        # now_list = checker.update_list()
        # no_count = 0
        # begin_wait_limit_times = 30
        # begin_wait = 2
        check_limit_min = 10
        is_passed_loop = False
        # self.add_log('check dir path.  path = {}'.format(path))
        target_list = checker.get_target_ext(self.ext)
        if len(target_list)<1:
            self.add_log('target[{}] is len<1 , return'.format(self.ext))
            return False
        else:
            target = target_list[0]

        self.add_log('Start to observe file.  path = {}'.format(target))
        start = time.time()
        before_size = os.path.getsize(target)
        time_log_flag = False
        count = 0
        while checker.is_exists(target):
            passed_time = time.time() - start
            if passed_time > (check_limit_min*60):
                print()
                self.add_log('time passed to limit. passed_time = {}'.format(passed_time))
                break
            if not time_log_flag:
                if int(passed_time) % 5==0:
                    self.add_log('downloading...[{} sec]'.format(count*5))
                    count +=1
                    time_log_flag = True
            else:
                if int(passed_time) % 6==0:
                    time_log_flag = False

            time.sleep(2)
            try:
                now_size = os.path.getsize(target)
                if before_size == now_size:
                    self.add_log('download is stopped')
                    is_passed_loop = True
                    break
            except:
                self.add_log('file size check error.  path = {}'.format(target))
                is_passed_loop = True
        print()
        self.add_log('End to observe file.')
        time.sleep(3)
        flag = self.is_exists_download_file(os.path.splitext(target)[0])
        return flag

DEFAULT_DONLOAD_DIR = r'C:\Users\OK\Downloads'

def main():
    donwload_dir = r'C:\Users\OK\Downloads'
    observer = DownloadDirectoryObserver(donwload_dir)
    flag = observer.excute()
    return flag