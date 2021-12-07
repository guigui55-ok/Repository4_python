
import time

# module_name = 'take_in_var_target : '

def loop_method(value:str):
    def _print(val):
        print(module_name + ' : ' + str(val))
    try:
        import os
        if value != '':
            if os.path.exists(value):
                buf = os.path.basename(value)
            else:
                buf = value
            module_name = buf
        else:
            module_name = os.path.basename(__file__)
        _print('loop_method')
        start = time.time()
        before = start
        limit = 5
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

def main():
    # loop_method('')
    import sys
    sys.stdout.write( 'loop_test stdout')
    import time
    time.sleep(3)
    sys.stdout.write( 'loop_test stdout2')
    sys.stdout.flush()


if __name__ == '__main__':
    main()

