
import time

module_name = 'take_in_var_target : '
def _print(val):
    print(module_name + str(val))

def main():
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

main()