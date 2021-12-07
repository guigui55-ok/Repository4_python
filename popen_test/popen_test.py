
import subprocess
import traceback
# from subprocess import PIPE

def popen_test():
    try:
        file = './popen_out.txt'
        cmd = 'python popen_test.py'
        cmd = 'popen_test.py' # おわらない
        cmd = 'loop_test.py'
        # サブプロセスをスタート
        # proc = subprocess.Popen(cmd, shell=True, stdout=file, stderr=file, text=True)
        proc = subprocess.Popen(cmd, shell=True, text=True)

        import time
        # time.sleep(3)
        import loop_test
        # loop_test.loop_method(__file__)
        
        # サブプロセスの完了を待つ
        # ここではsleepしている60秒待たされる
        result = proc.communicate()

        stdout = result[0]
        stderr = result[1]

        print('STDOUT: {}'.format(stdout))
        print('STDERR: {}'.format(stderr))
        # STDOUT: hoge.py
        # STDERR: ls: aaaa: No such file or directory
    except:
        print(traceback.print_exc())

def main():
    popen_test()

main()