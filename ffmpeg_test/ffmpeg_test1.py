import ffmpeg_common
import traceback
from pathlib import Path

class Logger:
    log_path:Path = None
    encoding = 'utf-8'

    def __init__(self, log_path = None):
        if log_path != None:
            self.log_path = Path(str(log_path))

    def info(self, value):
        print(value)
        self._write_file(value)

    def _write_file(self,value):
        if self.log_path == None :return
        if not Path(self.log_path).exists(): return
        with open(self.log_path, "a", encoding=self.encoding) as f:
            f.write(value + "\n")
    
import subprocess
import json
import os
from datetime import timedelta

class FfmpegUtil:
    logger = None

    def __init__(self) -> None:
        pass
    
    def _print(self, value):
        print(value)
        if self.logger != None:
            self.logger.info(value)
    
    def _print_ex(self, ex: Exception, value):
        self._print(value)
        self._print(ex.__class__.__name__ + ": " + str(ex))
        self._print(traceback.format_exc())

    def cut_time_only(self, write_path, movie_path, ss, t)->bool:
        """ 指定した時間をカットして、別ファイルに出力する """
        try:
            movie_path_str = str(movie_path)
            write_path_str = str(write_path)
            # 入力ストリームの設定
            stream = ffmpeg.input(movie_path_str, ss=ss, t=t)
            # # 出力ストリームの設定
            # stream = ffmpeg.output(stream, write_path_str)
            # 出力ストリームの設定 (無劣化でコピー)
            stream = ffmpeg.output(stream, write_path_str, **{'c:v': 'copy', 'c:a': 'copy'})
            # 処理の実行
            ffmpeg.run(stream)
            return True
        except Exception as e:
            self._print_ex(e, f"Error occurred while cutting the video: {movie_path}")
            self._print("cut_time_only error")
            self._print("filename={}, ss={}, t={}".format(Path(movie_path).name, ss, t))
            self._print("read_path={}".format(movie_path))
            self._print("write_path={}".format(movie_path))
            self._print("---")
            return False

    def get_video_duration_hhmmss(self, file_path: str) -> str:
        """
        指定された動画ファイルの再生時間を hh:mm:ss 形式で取得する。

        Args:
            file_path (str): 動画ファイルのパス

        Returns:
            str: 再生時間（hh:mm:ss 形式）。取得できない場合は "00:00:00"
        """
        if not os.path.exists(file_path):
            print("File Not Found:", file_path)
            return "00:00:00"

        try:
            # ffprobe を使って動画の duration を取得
            result = subprocess.run(
                ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
                '-show_entries', 'format=duration', '-of', 'json', file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            info = json.loads(result.stdout)
            duration_sec = float(info['format']['duration'])

            # 秒数を hh:mm:ss に変換
            hours = int(duration_sec // 3600)
            minutes = int((duration_sec % 3600) // 60)
            seconds = int(duration_sec % 60)

            return f"{hours:02}:{minutes:02}:{seconds:02}"
        except Exception as e:
            print("get_video_duration_hhmmss error:", e)
            return "00:00:00"
        

    def hhmmss_to_timedelta(self, hhmmss: str) -> timedelta:
        """
        hh:mm:ss 形式の文字列を timedelta に変換する。

        Args:
            hhmmss (str): "hh:mm:ss" 形式の時間文字列

        Returns:
            timedelta: 対応する timedelta オブジェクト
        """
        try:
            h, m, s = map(int, hhmmss.split(":"))
            return timedelta(hours=h, minutes=m, seconds=s)
        except Exception as e:
            print("hhmmss_to_timedelta error:", e)
            return timedelta(0)
    
# 使用例
# ffmpeg_util = FfmpegUtil()
# ffmpeg_util.cut_time_only('output.mp4', 'input.mp4', '00:01:00', '00:00:30')

# 0--　で最初から最後まで　

def log_out_movie_path_and_time(logger:Logger, count, movie_path, time_info: 'ffmpeg_tool1.MovieTimeInfo'):
        # log
        logger.info('##########')
        buf = '[t_cnt = {}] '.format(count)
        buf += 'path={}'.format(Path(movie_path).name, )
        buf += ', ss(begin)={}'.format(time_info.begin_time)
        buf += ', t(length)={}'.format(time_info.end_time)
        logger.info(buf)

import ffmpeg_tool1
def cut_movie_main(
        logger:Logger,
        movie_path:Path,
        movie_time_info_list:'list[ffmpeg_tool1.MovieTimeInfo]')->bool:
    is_success = False
    ffmpeg_util = FfmpegUtil()
    time_list_count = 0
    for time_info in movie_time_info_list:        
        time_list_count += 1
        # log
        logger.info('##########')
        log_out_movie_path_and_time(logger, time_list_count, movie_path, time_info)
        # check exists
        if not Path(movie_path).exists():
            logger.info("# movie path is not exists(movie_path={})".format(movie_path))
            return
        #/ 例外の時間書式対応
        if time_info.end_time_str == '' and ( '--' in time_info.read_str):
            end_time_str = ffmpeg_util.get_video_duration_hhmmss(str(movie_path))
            duration_td = ffmpeg_util.hhmmss_to_timedelta(end_time_str)
            time_info.end_time = duration_td
            logger.info("change_time {} -> {}".format(time_info.read_str, end_time_str))
        #/ 時間チェック
        if time_info.time_is_invalid():
            msg = 'time_is_Invalid = {}'.format(time_info.get_time_delta_str())
            logger.info(msg)
            continue
        #/ path
        write_path = ffmpeg_common.get_write_path(movie_path, '_'+str(time_list_count))
        buf = 'write_path={}'.format(Path(write_path).name)
        logger.info(buf)
        # cut movie main
        # ss：開始秒、ｔ：長さ秒
        start_sec = time_info.get_start_sec()
        time_length = time_info.get_length_sec()
        cut_result = ffmpeg_util.cut_time_only(write_path, movie_path, ss=start_sec, t=time_length)
        # result flag
        if time_list_count == 1: is_success = cut_result
        is_success = cut_result and is_success
        if not is_success:
            log_out_movie_path_and_time(logger, time_list_count, movie_path, time_info)
        logger.info("[t_cnt={}] wpath={}".format( time_list_count, str(write_path)))
    logger.info('Done.')
    return is_success

import ffmpeg
def _test_main_old1():
    """
    ffmpegで動画切り取りテスト（1動画ファイル、複数カット）
    （動画パスと動画時間[複数]はファイルから読み込み）
    """
    logger = Logger()
    movie_path = ffmpeg_common.get_movie_path() #動画パス
    logger.info('movie_path = {}'.format(movie_path))
    if not Path(movie_path).exists():
        logger.info("# movie path is not exists(movie_path={})".format(movie_path))
        return
    time_str_base = ffmpeg_common.get_movie_time() #動画時間
    logger.info('time_str_base = {}'.format(time_str_base))
    time_list = ffmpeg_common.MovieTimeInfoCollection()
    time_list.set_time_list_by_str(time_str_base)

    video_info = ffmpeg.probe(movie_path)
    # logger.info('video_info')
    # logger.info(video_info)
    ffmpeg_util = FfmpegUtil()
    logger.info('-----')
    time_info:ffmpeg_common.MovieTimeInfo = None
    count = 1
    for time_info in time_list.info_list:
        logger.info('##########')
        logger.info('count = {}'.format(count))
        buf = 'path={}'.format(Path(movie_path).name)
        buf += ', begin={}'.format(time_info.begin_time)
        buf += ', end={}'.format(time_info.end_time)
        logger.info(buf)
        #/
        if time_info.end_time_str == '':
            pass
        #/
        if time_info.time_is_invalid():
            msg = 'time_is_Invalid = {}'.format(time_info.get_time_delta_str())
            logger.info(msg)
            continue
        #/
        write_path = ffmpeg_common.get_write_path(movie_path, '_'+str(count))
        buf = 'write_path={}'.format(Path(write_path).name)
        logger.info(buf)
        # ss：開始秒、ｔ：長さ秒
        start_sec = time_info.get_start_sec()
        time_length = time_info.get_length_sec()
        ffmpeg_util.cut_time_only(write_path, movie_path, ss=start_sec, t=time_length)
        # break #デバッグ用（1回のみ実行）
        count += 1
    logger.info('Done.')


def _test_main():
    """
    ffmpegで動画切り取りテスト（1動画ファイル、複数カット）
    （動画パスと動画時間[複数]はファイルから読み込み）
    """
    logger = Logger()
    # movie_path = ffmpeg_common.get_movie_path() #動画パス
    movie_path = ffmpeg_common.get_movie_path_for_test() #動画パス
    logger.info('movie_path = {}'.format(movie_path))
    if not Path(movie_path).exists():
        logger.info("# movie path is not exists(movie_path={})".format(movie_path))
        return
    # time_str_base = ffmpeg_common.get_movie_time() #動画時間
    time_str_base = ffmpeg_common.get_movie_time_for_test() #動画時間    
    logger.info('time_str_base = {}'.format(time_str_base))
    time_list = ffmpeg_common.MovieTimeInfoCollection()
    time_list.set_time_list_by_str(time_str_base)

    # video_info = ffmpeg.probe(movie_path)
    # logger.info('video_info')
    # logger.info(video_info)
    cut_movie_main(logger, movie_path, time_list.info_list)


if __name__ == '__main__':
    print('*****')
    _test_main()