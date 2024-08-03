import subprocess
import threading
import time
from pathlib import Path

def execute_dotest_and_write_to_file(cmd, output_file):
    '''
    テスト用コマンドを実行し、結果をファイルに出力する

    Args:
        cmd (str): 実行するコマンド
        output_file (str): 出力ファイルのパス
    '''
    print('*execute_dotest_and_write_to_file')
    with open(output_file, 'w', encoding='utf-8') as f:
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        # 別スレッドで出力をファイルに書き込む
        def read_output():
            for line in proc.stdout:
                f.write(line)
                f.flush()

        thread = threading.Thread(target=read_output)
        thread.start()

        thread.join()  # スレッドが終了するのを待つ
        print(list(proc.stdout))
        proc.wait()  # プロセスが終了するのを待つ

def process_b(output_file):
    '''
    処理B: dotestの出力を書き込んでいるファイルのパスを出力する

    Args:
        output_file (str): 出力ファイルのパス
    '''
    print(f"The output file path is: {output_file}")

def main():
    print('\n*****')
    cmd = "dotest"  # テスト用コマンド
    from pathlib import Path
    script_file = str(Path(__file__).parent.joinpath('do_test.py'))
    cmd = "python {} 30".format(script_file)
    #/
    output_file_name = "__test_dotest_output.txt"  # 出力ファイルのパス
    output_file = str(Path(__file__).parent.joinpath(output_file_name))

    # サブプロセスでdotestを実行
    dotest_thread = threading.Thread(target=execute_dotest_and_write_to_file, args=(cmd, output_file))
    dotest_thread.start()

    # メインプロセスで処理Bを実行
    process_b(output_file)

    dotest_thread.join()  # dotestの実行が完了するのを待つ

if __name__ == '__main__':
    main()
