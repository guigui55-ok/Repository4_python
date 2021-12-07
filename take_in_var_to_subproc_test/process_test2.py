import time
import subprocess

module_name = 'process_test2 : '
def _print(val):
    print(module_name + str(val))

def loop_method():
    try:
        _print(' main')
        start = time.time()
        before = start
        limit = 20
        count = 0
        while(True):
            now = time.time()
            if (now - before) >= 1:
                _print('pass 1sec. ' + str(count))
                before = time.time()
                count += 1
            
            if (now - start) >= limit:
                _print('(now - start) >= '+ str(limit) +' , break')
                break
        ### end while
        _print(' done.')
        return
    except:
        import traceback
        _print('except : ')
        print(traceback.print_exc())
        return

# https://www.delftstack.com/ja/howto/python/python-run-another-python-script/
def main():
    try:
        # loop_method()
        file_name = 'take_in_var_target.py'
        # 別の Python スクリプトで Python スクリプトを実行
        # exec(open(file_name).read())
        subprocess.call(file_name,shell=True)

        # run
        # popen プロセスの終了を待機しない
    except:
        import traceback
        _print('except : ')
        print(traceback.print_exc())

main()