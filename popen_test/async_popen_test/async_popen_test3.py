import subprocess
import threading
import time
from pathlib import Path
import os
import signal
import psutil

def execute_dotest_and_write_to_file(cmd, output_file, pid_file):
    '''
    コマンドを実行し、結果をファイルに出力する（非同期）

    Args:
        cmd (str): 実行するコマンド
        output_file (str): 出力ファイルのパス
    '''
    def run_command():
        print('*execute_dotest_and_write_to_file')
        with open(output_file, 'w', encoding='utf-8') as f:
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            print('str(proc.pid) = {}'.format(str(proc.pid)))
            # プロセスIDをファイルに書き込む
            with open(pid_file, 'w') as pidf:
                pidf.write(str(proc.pid))

            # 出力をファイルに書き込む
            for line in proc.stdout:
                f.write(line)
                f.flush()
            proc.wait()  # プロセスが終了するまで待つ

    thread = threading.Thread(target=run_command)
    thread.start()

def process_b(output_file):
    '''
    処理B: dotestの出力を書き込んでいるファイルのパスを出力する

    Args:
        output_file (str): 出力ファイルのパス
    '''
    print(f"The output file path is: {output_file}")

def execute_command_async_with_dump(cmd:str, stdout_filepath, pid_file):
    command_value = ['python', '-c', f'import os; os.system("{cmd}")']
    dotest_proc = subprocess.Popen(command_value, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pid = dotest_proc.pid
    with open(pid_file, 'w') as f:
        f.write(str(pid))

import pickle
def pickle_dump(bin_file_path, obj):
    with open(bin_file_path, 'wb') as f:
        pickle.dump(obj, f)

def pickle_load(bin_file_path):
    with open(bin_file_path, 'rb') as f:
        obj = pickle.load(f)
    return obj

_pid_file_name  = '__test_pid_file.txt'
_pid_file_path  = str(Path(__file__).parent.joinpath(_pid_file_name))

def _test_start_command():
    # 動作テスト
    #/
    # テスト用コマンド
    cmd = "dotest"
    script_file = str(Path(__file__).parent.joinpath('do_test.py'))
    cmd = "python {} 10".format(script_file)
    output_file_name = "__test_dotest_output.txt"
    output_file_path = str(Path(__file__).parent.joinpath(output_file_name))
    print('\n*****')
    execute_dotest_and_write_to_file(cmd, output_file_path, _pid_file_path)

def test_stop_command():
    print('# test_stop_command')
    with open(_pid_file_path, 'r') as f:
        pid = int(f.read())
    try:
        process = psutil.Process(pid)
        if process.is_running():
            process.terminate()  # プロセスを終了
            process.wait()  # プロセスが終了するまで待つ
            print(f"Process {pid} has been terminated.")
        else:
            print(f"Process {pid} is not running.")
    except psutil.NoSuchProcess:
        print(f"No process with PID {pid} found.")

if __name__ == '__main__':
    print('\n*****')
    print('os.getpid = {}'.format(os.getpid()))
    _test_start_command()
    import time
    time.sleep(4)  # ここでコマンドが終了しないように適切な時間を設定
    test_stop_command()
