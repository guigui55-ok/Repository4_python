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

def test_main():
    _print("test_main")
    pass

def _print(value):
    print(value)

def edit_video_with_avidemux(input_file, output_file, start_time, end_time, format_type="MP4"):
    """
    Avidemuxを使用して動画をカットおよびフォーマット変換する関数
    :param input_file: 編集する動画ファイルのパス
    :param output_file: 編集後の出力ファイルのパス
    :param start_time: カット開始時間（秒単位）
    :param end_time: カット終了時間（秒単位）
    :param format_type: 出力フォーマットの種類（デフォルトはMP4）
    """
    avidemux_script = f"""
    adm = Avidemux()
    adm.loadVideo("{input_file}")
    adm.clearSegments()
    adm.addSegment(0, {start_time * 1000}, {end_time * 1000})
    adm.setContainer("{format_type}")
    adm.save("{output_file}")
    """

    # スクリプトファイルの作成
    with open("avidemux_edit_script.py", "w") as file:
        file.write(avidemux_script)

    # Avidemuxをコマンドラインで実行
    avidemux_exe_path = get_avedemux_exe_path()
    subprocess.run([avidemux_exe_path.__str__(), "--run", "avidemux_edit_script.py"])

from pathlib import Path
if __name__ == "__main__":
    # 使用例
    _print("*****")
    input_file = get_movie_file_path()
    _print(str.format("input_file = {}", input_file))
    
    output_file_name = Path(input_file).name
    output_dir = r"J:\avidemux_files\avidemux_output"
    output_file = Path(output_dir).joinpath(output_file_name)
    start_time = 10  # 開始位置（秒）
    end_time = 60    # 終了位置（秒）
    edit_video_with_avidemux(input_file.__str__(), output_file.__str__(), start_time, end_time)
    _print("Done.")