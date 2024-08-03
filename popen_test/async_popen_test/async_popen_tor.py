import subprocess
import threading
from pathlib import Path
import psutil
import os
import time
import signal

if __name__ == '__main__':
    import sys
    path = str(Path(__file__).parent.parent.parent)
    sys.path.append(path)
    from logger_simple.simple_logger_main import SimpleLogger as Logger

def run_command(logger:Logger, cmd):
    logger.info('run_command = {}'.format(cmd))
    proc = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    # logger.info('proc.stdout = {}'.format(proc.stdout))
    # stdoutとstderrを取得
    stdout, stderr = proc.communicate()
    # 結果をログに記録
    if stdout:
        logger.info('stdout = {}'.format(stdout))
    if stderr:
        logger.error('stderr = {}'.format(stderr))
    

def execute_dotest_and_write_to_file(logger:Logger, cmd, output_file, pid_file):
    '''
    コマンドを実行し、結果をファイルに出力する（非同期）

    Args:
        cmd (str): 実行するコマンド
        output_file (str): 出力ファイルのパス
    '''
    def __run_command():
        logger.info('# execute_dotest_and_write_to_file')
        logger.info('cmd = {}'.format(cmd))
        logger.info('output_file = {}'.format(output_file))
        with open(output_file, 'w', encoding='utf-8') as f:
            proc = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            logger.info('str(proc.pid) = {}'.format(str(proc.pid)))
            # プロセスIDをファイルに書き込む
            with open(pid_file, 'w') as pidf:
                pidf.write(str(proc.pid))
            # 出力をファイルに書き込む
            for line in proc.stdout:
                f.write(line)
                f.flush()
            # proc.wait()  # プロセスが終了するまで待つ
    #########
    logger.info('threading.Thread  __run_command')
    thread = threading.Thread(target=__run_command)
    logger.info('thred.start before')
    thread.start()
    logger.info('thred.start after')

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

def _test_start_command_tor(logger:Logger):
    # # 動作テスト
    # #/
    # # テスト用コマンド
    # cmd = "dotest"
    # script_file = str(Path(__file__).parent.joinpath('do_test.py'))
    # cmd = "python {} 10".format(script_file)
    cmd = r"C:\Users\OK\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe"
    output_file_name = "__test_command_output.txt"
    output_file_path = str(Path(__file__).parent.joinpath(output_file_name))
    logger.info('*****')
    execute_dotest_and_write_to_file(logger, cmd, output_file_path, _pid_file_path)

def test_stop_command(logger:Logger):
    logger.info('# test_stop_command')
    with open(_pid_file_path, 'r') as f:
        pid = int(f.read())
    try:
        process = psutil.Process(pid)
        if process.is_running():
            process.terminate()  # プロセスを終了
            process.wait()  # プロセスが終了するまで待つ
            logger.info(f"Process {pid} has been terminated.")
        else:
            logger.info(f"Process {pid} is not running.")
    except psutil.NoSuchProcess:
        logger.info(f"No process with PID {pid} found.")

def restart_tor(logger:Logger):
    test_stop_command(logger)
    #/
    cmd = r'taskkill /IM tor.exe /F'
    run_command(logger, cmd)
    #/
    _test_start_command_tor(logger)
    logger.info('restart_tor Done.')

if __name__ == '__main__':
    logger = Logger()
    logger.info('\n*****')
    restart_tor(logger)
