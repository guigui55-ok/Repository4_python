
print(__file__[__file__[:__file__.rfind('\\')-1].rfind('\\'):])


# from __init__ import common_function,CommonClass
from imports import common_function,CommonClass

def main():
    common_function()
    cl = CommonClass()
    cl.excute()
    
    return

if __name__ == '__main__':
    main()