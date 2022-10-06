import subprocess
from subprocess import PIPE

import os
import pathlib
def test_main():
    ## 非同期 15s
    py_file_name = 'input_test.py'
    py_file_name = 'while_loop_test.py'
    abs_path = 'subproc_async_test/' + py_file_name
    proc = subprocess.Popen(['python', abs_path], stdout=PIPE, stderr=PIPE)
    print('非同期処理でsub.pyを実行中')
    print('結果が帰ってくるまでの間にやりたいことができるよ')
    print('非同期')
    try:
        # タイムアウトは15秒以上の処理だった場合
        outs, errs = proc.communicate(timeout=3)
    except subprocess.SubprocessError:
        proc.kill()
        outs, errs = proc.communicate()
    print('outs = {}'.format(outs.decode('utf-8').split('\n')))
    print('errs = {}'.format(errs.decode('utf-8').split('\n')))

if __name__ == '__main__':
    test_main()