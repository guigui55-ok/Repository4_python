# inputの代わりに、1文字ずつ入力を受け取る関数を用意。
# try の中はWindows用、except の中はLinux用
try:
    from msvcrt import getch
except ImportError:
    import sys
    import tty
    import termios
    def getch():

            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                return sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)

def input_char_special_proc(key:int):
    pass

def input_char_main(special_class):
    print('*****  input_char_main  *****')
    # Unicode制御文字のエイリアス
    EOT = 3
    TAB = 9
    ESC = 27
    stack = ''
    # メインループ
    while True:
        key = ord(getch())
        if key == EOT:
            break
        elif key == TAB:
            print('keydown TAB')
        elif key == ESC:
            # key = ord(getch())
            print()
            print('------------------------------')
            if special_class != None:
                special_class.excute(stack)
                print('==============================')
            stack = ''
        else:
            message = f'{chr(key)}'
            print(message ,end='')
            if key == 13:
                print()
                # print('------------------------------')
                if stack == 'exit()':
                    break
                # stack = ''
            else:
                stack += message

if __name__ == '__main__':
    input_char_main(None)