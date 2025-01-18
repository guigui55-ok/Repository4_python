
import subprocess

def get_movie_file_path():
    root_path = r"J:\avidemux_files\target_movie_file.txt"
    with open(root_path,"r", encoding="utf8")as f:
        read_buf = f.readline()
    path = read_buf
    if not Path(path).exists():
        raise FileNotFoundError(path)
    return Path(path)

def get_avedemux_exe_path():
    path = r"C:\Program Files\Avidemux 2.8 VC++ 64bits\avidemux.exe"
    return Path(path)

def get_avedemux_exe_path_cli():
    path = r"C:\Program Files\Avidemux 2.8 VC++ 64bits\avidemux_cli.exe"
    return Path(path)

def get_avedemux_exe_dir_path():
    path = r"C:\Program Files\Avidemux 2.8 VC++ 64bits"
    return Path(path)

def test_main():
    _print("test_main")
    pass

def _print(value):
    print(value)


NEW_LINE = '\n'
def cut_only(input_file, output_file, start_time, end_time):

    dir_path = get_avedemux_exe_dir_path()
    buf = ''
    buf += '@echo off' + NEW_LINE
    buf += str.format('cd "{}"', dir_path) + NEW_LINE
    # buf += '    avidemux3_cli --load "%%f" --video-codec x264 --audio-codec AAC --save "%%~nf_output.mp4" --output-format MP4'
    buf += str.format('avidemux_cli --load "{}"', input_file)
    buf += str.format(' --start {}', start_time)
    buf += str.format(' --end {}', end_time)
    buf += str.format(' --save "{}"', output_file)
    buf += NEW_LINE

    avidemux_script = buf
    # スクリプトファイルの作成・実行
    make_bat_file_and_execute(avidemux_script)


def edit_video_with_avidemux(input_file, output_file, start_time, end_time, format_type="MP4"):
    """
    Avidemuxを使用して動画をカットおよびフォーマット変換する関数
    """
    buf = "avidemux3_cli --load <入力ファイル> --save <出力ファイル> --output-format <フォーマット>"


    dir_path = get_avedemux_exe_dir_path()
    buf = ''
    buf += '@echo off' + NEW_LINE
    buf += str.format('cd "{}"', dir_path) + NEW_LINE
    # buf += '    avidemux3_cli --load "%%f" --video-codec x264 --audio-codec AAC --save "%%~nf_output.mp4" --output-format MP4'
    buf += str.format('avidemux_cli --load "{}"', input_file)
    buf += str.format(' --start {}', start_time)
    buf += str.format(' --end {}', end_time)
    buf += str.format(' --video-codec {}', 'x264')
    buf += str.format(' --audio-codec {}', 'AAC')
    buf += str.format(' --save "{}"', output_file)
    buf += str.format(' --output-format {}', format_type)
    buf += NEW_LINE

    avidemux_script = buf
    # avidemux_script = f"""
    # adm = Avidemux()
    # adm.loadVideo(r"{input_file}")
    # adm.clearSegments()
    # adm.addSegment(0, {start_time * 1000}, {end_time * 1000})
    # adm.setContainer("{format_type}")
    # adm.save(r"{output_file}")
    # """
    # スクリプトファイルの作成・実行
    make_bat_file_and_execute(avidemux_script)


def make_bat_file_and_execute(bat_write_str):
    # スクリプトファイルの作成・実行
    enc = 'utf-8'
    enc = 'sjis'
    with open("avidemux_auto.bat", "w", encoding=enc) as file:
        file.write(bat_write_str)

    # Avidemuxをコマンドラインで実行
    avidemux_exe_path = get_avedemux_exe_path_cli()
    # subprocess.run([str(avidemux_exe_path), "--run", "avidemux_auto.bat"])
    subprocess.run(["avidemux_auto.bat"])



from pathlib import Path
if __name__ == "__main__":
    # 使用例
    _print("*****")
    input_file = get_movie_file_path()
    _print(str.format("input_file = {}", input_file))
    
    # output_file_name = Path(input_file).name
    import datetime
    date_str = datetime.datetime.now().strftime('_%y%m%d_%H%M%S')
    output_file_name = Path(input_file).stem + date_str + Path(input_file).suffix
    output_dir = r"J:\avidemux_files\avidemux_output"
    output_file = Path(output_dir).joinpath(output_file_name)
    start_time = 418500000  # 開始位置（frameNumber）
    end_time = 720500000    # 終了位置（frameNumber）
    # adm.markerA = 418500000
    # adm.markerB = 720500000
    start_time = '00:00.00.000'
    end_time = '00:12.00:500'
    # edit_video_with_avidemux(input_file.__str__(), output_file.__str__(), start_time, end_time)
    cut_only(input_file.__str__(), output_file.__str__(), start_time, end_time)
    _print("Done.")
