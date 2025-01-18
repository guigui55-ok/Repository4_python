import ffmpeg_common
import traceback
from pathlib import Path

class Logger:
    def info(self, value):
        print(value)

class FfmpegUtil:
    def __init__(self) -> None:
        pass
    
    def _print(self, value):
        print(value)
    
    def _print_ex(self, ex: Exception, value):
        self._print(value)
        self._print(ex.__class__.__name__ + ": " + str(ex))
        self._print(traceback.format_exc())

    def cut_time_only(self, write_path, movie_path, ss, t):
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
        except Exception as e:
            self._print_ex(e, f"Error occurred while cutting the video: {movie_path}")

# 使用例
# ffmpeg_util = FfmpegUtil()
# ffmpeg_util.cut_time_only('output.mp4', 'input.mp4', '00:01:00', '00:00:30')


# 予定　
# 0--　で最初から最後まで　


import ffmpeg
def _test_main():
    logger = Logger()
    movie_path = ffmpeg_common.get_movie_path()
    print('movie_path = {}'.format(movie_path))
    time_str_base = ffmpeg_common.get_movie_time()
    print('time_str_base = {}'.format(time_str_base))
    time_list = ffmpeg_common.MovieTimeInfoCollection()
    time_list.set_time_list_by_str(time_str_base)

    video_info = ffmpeg.probe(movie_path)
    # print('video_info')
    # print(video_info)
    ffmpeg_util = FfmpegUtil()
    logger.info('-----')
    time_info:ffmpeg_common.MovieTimeInfo = None
    count = 1
    for time_info in time_list.info_list:
        logger.info('##########')
        logger.info('count = {}'.format(count))
        buf = 'path={}'.format(Path(movie_path).name, )
        buf += ', ss={}'.format(time_info.begin_time)
        buf += ', t={}'.format(time_info.end_time)
        logger.info(buf)
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

if __name__ == '__main__':
    print('*****')
    _test_main()