



DEFAULT_WAIT_TIME = 2
NEW_LINE = '\n'
BAR = '########################################'
import time
import os
import glob
import pathlib
import sys
from pathlib import Path
import shutil

CHROME_DRIVER_PATH = r'C:\Users\OK\source\programs\chromedriver_win32\chromedriver'

path = str(pathlib.Path(__file__).parent.parent)
sys.path.append(path)
import import_init
from html_log.html_logger import HtmlLogger,BasicLogger

class ConstResult():
    OK = 1
    NG = 2
    ERROR = 3
    NOTHING = 4

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
        match_files = glob.glob(str(self.dir_path) + '*' + self.target_ext)
        for matchfile in match_files:
            shutil.move(str(matchfile, str(self.move_folder_path)))
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
        

    def excute(self):
        # ダウンロードを押した後で実行する
        # ダウンロード中であるか、終わっている前提
        # delete_target_ext(path,TARGET_EXT)
        checker = DirChecker(self.dir_path)
        self.logger.add_log('download folder'.format(self.dir_path))
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

import shutil
from movie_downloader_sub import YouTube,DonwloadSite,VdSite
from movie_downloader_sub import get_vd_site_url, get_vd_site_url2

class MovieDownloader():
    def __init__(self) -> None:
        self.logger:HtmlLogger = None
        self.downloader:DonwloadSite=None

    def set_dir(self,dir_path:str,log_dir:str=''):
        self.path = dir_path #linkリストのdir
        self.observer:DownloadDirectoryObserver = None
        self.end_dir_name = 'end'
        self.log_dir_path = log_dir
        self.not_check_db = False



    def set_download_dir_observer(self,observer):
        self.observer = observer
    
    def init_download_dir(self):
        """
        ダウンロードフォルダを初期化する
        （ダウンロード中の拡張子をすべて削除）
         （ダウンロード対象の拡張子をすべて、ダウンロード済みフォルダに移動）
        """
        self.observer.init_dir()
        self.observer.init_move_downloaded_file()
    
    def make_file_list_from_dir(self):
        """対象ディレクトリのlnkリストを作成する"""
        import glob,os
        glob_path = os.path.join(self.path,'*')
        buf_list = glob.glob(glob_path)
        self.lnk_list = self.exact_lnk_path_from_list(buf_list)
        # import pprint
        # print('lnk_list')
        # pprint.pprint(self.lnk_list)
        # print()
    
    def exact_lnk_path_from_list(self,buf_list:'list[str]'):
        import os
        ret = []
        for path in buf_list:
            if os.path.isfile(path):
                if os.path.splitext(path)[1] == '.url':
                    ret.append(path)
        return ret

    def url_is_valid(self,url:str):
        """URLが有効か確認する
        """
        return True
    
    def add_log(self,value:str):
        self.logger.add_log(value)
    
    def print_result(self,flag:int,value:str,url:str=''):
        print()
        self.add_log(BAR)
        if flag==ConstResult.OK:
            self.add_log(value + '   OK')
        if flag==ConstResult.NG:
            self.add_log(value + '   NG')
        if flag==ConstResult.ERROR:
            self.add_log(value + '   ERR')
        if flag==ConstResult.NOTHING:
            self.add_log(value + '   NOTHING')
        if url!='':
            self.add_log('url = {}'.format(url))
        print()
    
    def close_donwloader(self):
        self.downloader.close()

    def path_is_donloaded(self,lnk_path:str):
        import sql_test.sql_for_regist_url as sql_lib
        is_exists_in_db = sql_lib.resist_data_to_mdf_from_url_file(lnk_path)
        # sql_lib.update_times()
        return is_exists_in_db
    def is_exists_path_data_in_db(self,lnk_path:str):
        import sql_test.sql_for_regist_url as sql_lib
        is_exists = sql_lib.is_exists_data_in_db(lnk_path)
        return is_exists
    def regist_link_path_to_db(self,lnk_path:str):
        import sql_test.sql_for_regist_url as sql_lib
        is_registed = sql_lib.regist_url_when_success_download(lnk_path)
        return is_registed

    def wait_for_access_restrictions(self, wait_max=60):
        # アクセス制限　Access restrictions
        print_interval_sec = 10
        for i in range(int(wait_max//print_interval_sec)):
            msg = 'Wait...[Access restrictions] [{} sec]'.format(i*print_interval_sec)
            self.logger.add_log(msg)
            time.sleep(print_interval_sec)

    def download_movie_main(self):
        """lnkが格納されているディレクトリのlnkからURLを読み取り、ダウンロードする。
        終わるまで待って、終わったらlnkを別ディレクトリに移動"""
        for i, path in enumerate(self.lnk_list):
            if not self.not_check_db:
                if self.path_is_donloaded(path):
                    self.add_log('**** path is donloaded.  lnk_path={}'.format(path))
                    # @@@Avlori.com
                    #231124 ダウンロード失敗時にもカウント＋１されて、2回目以降はここでスキップされる
                    # 現状は手動コメントアウトで対応
                    # self.move_link_file_finished(path)
                    # continue
            url = self.get_url_from_link(path)
            # if not self.url_is_valid(url): continue
            self.init_download_dir()
            #########
            # dounload main
            #########
            is_downloading = self.download_movie(url)
            #########
            if self.is_need_observer():
                if is_downloading:
                    is_downloaded = self.wait_until_downloaded()
                    if is_downloaded:
                        self.print_result(ConstResult.OK,'SUCCESS',url)
                    else:
                        self.print_result(ConstResult.NG,'NG',url)
                else:
                    is_downloaded = is_downloading
            else:
                is_downloaded = is_downloading
                if self.download_result():
                    self.print_result(ConstResult.OK,'SUCCESS',url)
                else:
                    self.print_result(ConstResult.NG,'NG',url)

            self.close_donwloader()
            if is_downloaded:
                is_exists = self.is_exists_path_data_in_db(path)
                if not is_exists:
                    is_registed = self.regist_link_path_to_db(path)
                else:
                    is_registed = True
                if is_registed:
                    
                    self.move_link_file_finished(path)
            else:
                self.add_log('is_downloaded = False, skip regist_to_db  , move_link')
            if i!=len(self.lnk_list):
                self.wait_for_access_restrictions(60)
        #End For
        msg = 'processed file_length = {}'.format(len(self.lnk_list))
        self.add_log(msg)
    #End Method download_movie_main

    def move_link_file_finished(self,path):
        """ダウンロードが終わったら、終わった用ディレクトリに移動する"""
        if not os.path.exists(path): return
        end_dir_path = os.path.join(self.path,self.end_dir_name)
        end_dir_path = self.get_end_dir(end_dir_path)
        src_path = path
        file_name = os.path.basename(src_path)
        dist_path = os.path.join(end_dir_path,file_name)
        shutil.move(src_path,dist_path)
    
    def get_end_dir(self,dir_path):
        """lnkを格納するendディレクトリを取得する（無ければ作る）"""
        if os.path.exists(dir_path):
            if os.path.isfile(dir_path):
                os.remove(dir_path)
            else:
                return dir_path
        os.mkdir(dir_path)
        return dir_path
        
    
    def wait_until_downloaded(self):
        """
        ダウンロードが終了するまで待つ
         self.observer.excute
         (DownloadDirectoryObserver)
          ダウンロード中ファイルがなくなるまで待つorダウンロード済みのファイルがあればTrue
           ダウンロード中ファイルが表示されっぱなし=>タイムアウトの場合はFalse
            ダウンロード中ファイル、ダウンロード済みファイルがない場合もFalse
        """
        return self.observer.excute()

    def get_url_from_link(self,lnk_path:str):
        """lnkからURLを取得する"""
        with open(lnk_path, 'r',encoding='utf-8')as f:
            buf = f.read()
        buf = buf.replace(NEW_LINE,'')
        buf = buf.replace('[InternetShortcut]URL=','')
        return buf

    def wait_little(self,wait_time:float=DEFAULT_WAIT_TIME/3):
        self.wait(wait_time)
    def wait_short(self,wait_time:float=DEFAULT_WAIT_TIME/2):
        self.wait(wait_time)
    def wait(self,wait_time=DEFAULT_WAIT_TIME):
        time.sleep(wait_time)
    def wait_long(self,wait_time=DEFAULT_WAIT_TIME*2):
        self.wait(wait_time)

    def download_movie(self,url:str):
        """
        ダウンロードサイトをを開いてURLを入力、STARTをクリックして、動画をWeb上で取得する。
         その後、画面が切り替わったらダウンロードをクリックして、
        ポップアップした要素の（前とは別の）ダウンロードをクリックする。"""
        self.add_log(url)
        is_downloded:bool = False
        chrome_driver_path = CHROME_DRIVER_PATH
        if url.startswith('https://www.youtube.com/'):
            downloader:YouTube = YouTube(chrome_driver_path, self.logger)
        elif url.startswith(get_vd_site_url()) or url.startswith(get_vd_site_url2()):
            downloader:VdSite = VdSite(chrome_driver_path, self.logger)
        else:
            msg = 'ERROR: 未実装のURL種類  url={}'.format(url)
            self.add_log(msg)
            raise Exception(msg)
            downloader:DonwloadSite(chrome_driver_path)
        
        if isinstance(downloader,YouTube) \
        or isinstance(downloader,VdSite)\
        or isinstance(downloader,DonwloadSite):
            downloader:YouTube = downloader
            downloader.set_log_path(self.log_dir_path)
            is_downloded = downloader.excute_download_movie(url)
        self.downloader = downloader
        return is_downloded
    
    def is_need_observer(self):
        return self.downloader.is_need_observer
    def download_result(self):
        return self.downloader.download_result



################################################################################
################################################################################

def text_is_false():
    import pathlib
    path = str(pathlib.Path(__file__).parent.joinpath('is_continue.txt'))
    with open(path,'r',encoding='utf-8')as f:
        buf = f.read()
    if buf[0]=='0':
        return False
    return True

################################################################################
################################################################################
# oberver test
def delete_target_ext(dir_path:str,ext:str):
    path_list = glob.glob(dir_path + '/**')
    for path in path_list:
        if path.endswith(ext):
            os.remove(path)
from lauda import stopwatch
import time
TARGET_EXT  ='.crdownload'
target = ''
def check_dir_test(path = 'F:\ZDOWNLOAD', ext = TARGET_EXT):
    delete_target_ext(path,TARGET_EXT)
    checker = DirChecker(path)
    now_list = checker.update_list()
    no_count = 0
    begin_wait_limit_times = 30
    begin_wait = 2
    check_limit_min = 10
    print('check dir path.  path = {}'.format(path))
    is_passed_loop = False
    while True:
        time.sleep(begin_wait)
        diff_list = checker.get_increased_list(now_list)
        if len(diff_list)<1:
            no_count += 1
            if no_count >= begin_wait_limit_times:
                print()
                print('no_count reached limit')
                break
            else:
                print('.',end='')
                now_list = checker.get_now_dir_list()
        else:
            print()
            # ext = TARGET_EXT
            buf:str=''
            target=''
            for buf in diff_list:
                if buf.endswith(ext):
                    target = diff_list[0]
            if target == '': break
            print('Start to observe file.  path = {}'.format(target))
            start = time.time()
            before_size = os.path.getsize(target)
            while checker.is_exists(target):
                passed_time = time.time() - start
                if passed_time > (check_limit_min*60):
                    print()
                    print('time passed to limit. passed_time = {}'.format(passed_time))
                    break
                if passed_time % 5.0==0:
                    print('.',end='')
                time.sleep(2)
                try:
                    now_size = os.path.getsize(target)
                    if before_size == now_size:
                        print('download is stopped')
                        is_passed_loop = True
                        break
                except:
                    print('file size check error.  path = {}'.format(target))
                    is_passed_loop = True
            print()
            print('End to observe file.')
            is_passed_loop = True
        if is_passed_loop: break
    
    #check
    buf = os.path.splitext(target)[0]
    print(buf)
    if os.path.exists(buf):
        print('is exists = True')
    print('done.')



################################################################################
################################################################################

def main():
    
    # path = r'C:\ZMyFolder\newDoc\新しいfiles\_test_movie'
    # path = r'C:\ZMyFolder\newDoc\新しいfiles\0fashon'
    # path = r'C:\Users\OK\Desktop\0704 you'
    # path = r'C:\Users\OK\Desktop\fas'
    # path = r'C:\Users\OK\Desktop\231123 youel\you'
    path = r'C:\Users\OK\Desktop\240519_el_test'
    if not Path(path).exists():
        raise FileNotFoundError(path)
    #/
    donwload_dir = r'C:\Users\OK\Downloads'
    # donwload_dir = r'J:\ZDOWNLOAD\movie_downloads'
    # 240521  ChromeDriverでダウンロードすると、デフォルトはWindowsのダウンロードフォルダとなる
    # 変更するには別途処理が必要と思われる（未対応）
    # log_dir_path = r'C:\Users\OK\source\repos\test_media_files\selenium_log'
    log_dir_path = r'C:\Users\OK\source\repos\Repository4_python\scraping_test\selenium_utility\__log_selenium\log'
    from html_log.html_logger import HtmlLogger
    html_logger = HtmlLogger('MovieDownloader',log_dir_path)
    downloader = MovieDownloader()
    downloader.logger = html_logger
    downloader.set_dir(path,log_dir_path)

    downloader.not_check_db = True
    downloader.not_check_db = False
    observer = DownloadDirectoryObserver(donwload_dir,html_logger)
    observer.set_conditions(TARGET_EXT)
    downloader.set_download_dir_observer(observer)
    downloader.make_file_list_from_dir()
    #231124
    # ダウンロード失敗時にもカウント＋１されるので、修正が必要
    # 231124
    # selenium_logを実行ごとに別フォルダに区切る（現状は連なっている）
    ##########
    # main
    ##########
    downloader.download_movie_main()
    ##########
    html_logger.finish_to_create_html()



#####################################
# check_dir_test()
if __name__ == '__main__':
    main()



