import subprocess
import subprocess
from subprocess import PIPE

def print_result_run(ret):
    print('print_result.ret = ')
    print(ret)
    print("return code: {}".format(ret.returncode))
    print("ret.stdout = " + ret.stdout) #char配列　ret.stdout[0] == 'C'
    print("ret.stderr = " + ret.stderr)
    print("captured stdout: {}".format(ret.stdout.decode()))
    print("captured stderr: {}".format(ret.stderr.decode()))

def print_result_call(ret):
    print('print_result.ret = ')
    print(ret)
    # print("return code: {}".format(ret.returncode))
    # print("ret.stdout = " + ret.stdout) #char配列　ret.stdout[0] == 'C'
    # print("ret.stderr = " + ret.stderr)
    # print("captured stdout: {}".format(ret.stdout.decode()))
    # print("captured stderr: {}".format(ret.stderr.decode()))


def subproc_call():
    try:
        print('\n\n*** subproc_call')
        import os
        path = os.getcwd() + '\\' + 'subproc_called.py'
        # result = subprocess.call(path, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE,
        #     universal_newlines=True)
        # result = subprocess.call(path,shell=True,capture_output=True,text=True)
        result = subprocess.call(path,shell=True,capture_output=True)
        #print('result = ' + str(result))
        if result != 0:            
            # エラー時の処理
            print('subproc error')
        else:
            print('subproc success')
        print_result_call(result)
    except:
        import traceback
        traceback.print_exc()

def subproc_run():
    try:
        print('\n\n*** subproc_run')
        import os
        path = os.getcwd() + '\\' + 'subproc_called.py'
        result = subprocess.run(path, shell=True,capture_output=True,text=True)
        # result = subprocess.run(path, shell=True,capture_output=True)
        if result.returncode != 0:            
            # エラー時の処理
            print('subproc error')
        else:
            print('subproc success')
        #print('result = ' + str(result))
        #print('result.returncode  = ' + str(result.returncode ))
        print_result_run(result)
    except:
        import traceback
        traceback.print_exc()

def main():
    print(__file__)
    subproc_run()
    subproc_call()

if __name__ == '__main__':main()