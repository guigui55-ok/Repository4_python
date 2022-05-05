
# from distutils.file_util import move_file

from datetime import datetime, timedelta
from inspect import isfunction
import pathlib,os

from lauda import stopwatchcm

import import_init
DEBUG_TRACE = 1
DEBUG_DEBUG = 2
DEBUG_MODE = DEBUG_DEBUG
NEW_LINE = '\n'
SHOW_PROGRESS = False


from common_utility.file_util.count_up_file_name import move_file,copy_file,FileControlMode

class SimpleLogger():
    def __init__(self,dir_path,log_file_name='app.log') -> None:
        import os
        if os.path.isdir(dir_path):
            self.dir_path = dir_path
        else:
            self.dir_path = os.path.dirname(dir_path)
        self.log_file_name = log_file_name
        #ログをとったときにコンソールにも出力する
        self.is_print_when_loged = True
    
    def info(self,value):
        if self.is_print_when_loged:
            print(str(value))
        self.write_log(value + '\n')
    
    def info_no_print(self,value):
        self.write_log(value + '\n')
        
    def write_log(self,value):
        write_path = os.path.join(self.dir_path,self.log_file_name)
        with open(write_path,'a',encoding='utf-8')as f:
            f.write(str(value))

class StopWatch():
    def __init__(self) -> None:
        self.start_time = 0
        self.end_time = 0
    def start(self):
        import datetime
        self.start_time = datetime.datetime.now()
        print('StopWatch Start.')
    def stop(self):
        import datetime
        self.end_time = datetime.datetime.now()
        self.result:datetime.timedelta = self.end_time - self.start_time
        print(type(self.result))
        print('StopWatch Stop.')
    def get_h_m_s(self,timedelta):
        import datetime
        if isinstance(timedelta,datetime.timedelta):
            td = timedelta
            m, s = divmod(td.seconds, 60)
            h, m = divmod(m, 60)
        elif isinstance(timedelta,datetime.datetime):
            dt = timedelta
            m = dt.min
            s = dt.second
            h = dt.hour
        else:
            raise Exception('argument is invalid')
        return h, m, s
    def get_start_time_str(self):
        ret = self.get_time_str(self.start_time)
        return ret

    def get_time_str(self,td:timedelta):
        import datetime
        hour,min,sec = self.get_h_m_s(td)
        if isinstance(td,datetime.timedelta):
            msec = str(td.microseconds)
        elif isinstance(td,datetime.datetime):
            msec = 0        
        ret = '{}:{}:{}.{}'.format(hour,min,sec,msec)
        return ret

    def get_result_str(self):
        ret = self.get_time_str(self.result)
        return ret


def sub():
    sw = StopWatch()
    sw.start()
    import time
    time.sleep(3.3)
    sw.stop()
    print(sw.get_result_str())


def main():
    target_path = r'C:\Users\OK\source\repos\Repository4_python\cv2_test1\comp_ex_test\image'
    sort_dir = os.path.join(str(pathlib.Path(__file__).parent),'comp_dir')



    logger = SimpleLogger(sort_dir)
    sw = StopWatch()
    sw.start()
    logger.info('start_time:' + sw.get_start_time_str())

    if not os.path.exists(sort_dir):
        os.mkdir(sort_dir)
    comp_path = target_path
    jpg_path_list = get_file_path_list(target_path,'jpg')
    #excute
    excute_comp_pic(jpg_path_list,sort_dir,logger)
    sw.stop()
    logger.info(sw.get_result_str())
    return

def save_all_pics(path_list:'list[str]',sort_dir:str,logger_):
    logger = get_logger(logger_)
    count = 0
    cv2img_list:'list[Cv2Image]' = []
    logger.info('reading path_list')
    for base_path in path_list:
        cv2img = read_image(base_path)
        cv2img.img_to_gray()
        cv2img.resize_keep_raito(0.5)

        cv2img_list.append(cv2img)
        count += 1
        if count % 200 == 0:
            logger.info('reading count[{} / {]}]'.format(count,len(cv2img_list)))
        # logger.info('[{} / {}]'.format(count,len(path_list)))
        # logger.info('base_now_path = ')
        # logger.info(base_path)
        # print(cv2img_list.__sizeof__())
    logger.info('read count = {}'.format(count))
    return cv2img_list


def excute_comp_pic(path_list:'list[str]',sort_dir:str,logger_):
    """
    以前のものでは時間がかかるため変更
    以前のものは980ファイルで1h43mくらい、せめて10mくらいにはしたい
    変更点
    save_all_picsで比較の前にすべてのイメージを取得するようにした
     メモリが増えないように、グレースケールで、サイズは読み込んだあと半分にした
      そのままだと、メモリが980ファイルで800MBくらいになった（リソースモニターで確認）
    グレースケールで一致したら、再度rgbで読み込み詳細に比較
     これで一致したら指定フォルダに移動とする
    →6m30sとなる
    コンソール出力調整
    →5m39s

    """
    debug_print()
    logger = get_logger(logger_)
    
    cv2img_list = save_all_pics(path_list,sort_dir,logger)

    logger.info('===========')
    logger.info('comparing image path_list')
    count = 0
    comp_cv2img:Cv2Image = Cv2Image()
    for base_cv2img in cv2img_list:
        count += 1
        if count % 200 == 0:
            logger.info('comparing count[{} / {]}]'.format(count,len(cv2img_list)))
        print_progress('.',True)
        if not os.path.exists(base_cv2img.path):
            continue
        # #read file
        # base_cv2img = read_image(base_path)
        if cl_img_is_none(base_cv2img):
            continue
        logger.info_no_print('----------')
        logger.info_no_print('[{} / {}]'.format(count,len(cv2img_list)))
        logger.info_no_print('base_now_path = ')
        logger.info_no_print(base_cv2img.path)

        print_image_info(base_cv2img,-1,True)
        is_skip=True
        
        for comp_cv2img in cv2img_list:
            #debug
            # tempb = 'comp_test_size_big.jpg'
            # tempa = 'comp_test_low_qt.jpg'
            # if os.path.basename(base_path)==tempa and os.path.basename(comp_path)==tempb:
            #     pass
            if not os.path.exists(comp_cv2img.path):
                continue
            if not os.path.exists(base_cv2img.path):
                break
            #一度行った比較はスキップする
            print_progress('.')
            if not is_skip:
                #comp read file
                # comp_cv2img = read_image(comp_cv2img.path)
                if cl_img_is_none(comp_cv2img):
                    continue
                # is_match = cv2_image_comp.is_same_image(None,base_cv2img.img,comp_cv2img.img)
                # resize
                # comp_cv2img.resize_by_image_keep_ratio(base_cv2img.img)
                threshold = 0.5
                threshold = 0.99
                comp_val = cv2_image_comp.get_compareist_value(
                    None,base_cv2img.img,comp_cv2img.img)
                comp_val2 = 0
                if comp_val >= threshold:
                    # grayスケールで一致したら、カラーで精密に比較する
                    base_cv2img_rgb = read_image(base_cv2img.path)
                    comp_cv2img_rgb = read_image(comp_cv2img.path)
                    comp_val2 = cv2_image_comp.get_compareist_value(
                        None,base_cv2img_rgb.img,comp_cv2img_rgb.img)

                if comp_val2 >= threshold:
                    if base_cv2img_rgb.is_big_more_than_self_image(comp_cv2img_rgb.img):
                        logger.info('* base_move')
                        new_path = move_file(base_cv2img_rgb.path,sort_dir)
                        print_move_file_to_log(logger,comp_cv2img_rgb.path,new_path,comp_val)
                        print_image_info(comp_cv2img_rgb,comp_val,True)
                        comp_cv2img_rgb.dispose()
                        del comp_cv2img_rgb
                        continue
                    elif base_cv2img_rgb.is_same_size_other_image(comp_cv2img_rgb.img):
                        new_path = move_file(comp_cv2img_rgb.path,sort_dir)
                        print_move_file_to_log(logger,new_path,base_cv2img_rgb.path,comp_val)
                    else:
                        new_path = move_file(comp_cv2img_rgb.path,sort_dir)
                        print_move_file_to_log(logger,new_path,base_cv2img_rgb.path,comp_val)
                    comp_cv2img_rgb.dispose()
                    del comp_cv2img_rgb
                    base_cv2img_rgb.dispose()
                    del base_cv2img_rgb
                    debug_print()
                    print_image_info(comp_cv2img_rgb,comp_val)
                else:
                    if comp_val >= threshold:
                        logger.info('not match in 2nd check')
                        logger.info('   ' + base_cv2img.path)
                        logger.info('   ' + comp_cv2img.path)

            
            #一度行った比較はスキップする
            #base_path と同じ配列を使用しているので
            #以下の条件までは比較済み→スキップする
            if base_cv2img.path == comp_cv2img.path:
                print_progress('/')
                is_skip = False
        # debug_print()
        # print('***** test break')
        # break

from common_utility.cv2_image.cv2_image_util import Cv2Image


def print_move_file_to_log(logger_,base_path:str,move_path:str,threshold=-1):
    logger = get_logger(logger_)
    msg = '    '
    if threshold > 0:
        msg += '[threshold={}]'.format(threshold)
    import os
    logger.info('base_path=')
    logger.info(base_path)
    logger.info('move_file=')
    logger.info(move_path)
    logger.info(msg)
    # print('{} {}'.format(path,msg))

def print_move_file(base_path:str,move_path:str,threshold=-1):
    msg = '    '
    if threshold > 0:
        msg += '[threshold={}]'.format(threshold)
    import os
    print('base_path=')
    print(base_path)
    print('move_file=')
    print(move_path)
    print(msg)
    # print('{} {}'.format(path,msg))

def print_image_info(cv2img:Cv2Image,threshold=-1,is_full_path:bool=False):
    msg = '    '
    # if threshold > 0:
    #     msg += '[threshold={}]'.format(threshold)
    msg += '[w,h={},{}]'.format(cv2img.width(),cv2img.height())
    # print(msg)
    import os
    # if is_full_path:
    #     path = cv2img.path
    # else:
    #     path = os.path.basename(cv2img.path)
    # print(path)
    # print(msg)
    # print('{} {} {}'.format(path,NEW_LINE,msg))

def get_logger(logger):
    ret_logger:SimpleLogger = logger
    return ret_logger

import common_utility.cv2_image.cv2_image_comp as cv2_image_comp
import common_utility.cv2_image.cv2_image_util as cv2_image_util
def read_image(path):
    cv2img = Cv2Image(path)
    return cv2img

import numpy
def img_is_none(img):
    if isinstance(img,numpy.ndarray):
        if len(img) < 1:
            return True
    else:
        if img == None:
            return True
    return False

def cl_img_is_none(cl_cv2img:Cv2Image):
    is_none = img_is_none(cl_cv2img.img)
    if is_none:
        debug_print('[none] '+ cl_cv2img.path)
    return is_none

def get_file_path_list(path:str,ext:str):
    import glob
    value = path + '/*.' + ext
    file_list = glob.glob(value)
    if DEBUG_MODE < DEBUG_DEBUG:
        print()
        print('----------')
        for file in file_list:
            print('  ' + file)
    return file_list

def debug_print(value='',end=None):

    if DEBUG_MODE >= DEBUG_TRACE:
        if end == None:
            print(value)
        else:
            print(value,end=end)


def print_progress(value,is_show:bool=SHOW_PROGRESS):
    if is_show:
        debug_print(value,end='')

if __name__ == '__main__':
    main()
    # sub()