

def other_test():
    try:
        import os
        pid = os.getpid()
        print(str(type(pid)))
        print(pid)
    except:
        import traceback
        print(traceback.print_exc())

other_test()

import sys
print(sys.__stdin__)
sys.__stdout__ = 'aa'