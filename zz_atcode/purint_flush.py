
import sys

def main():
    print('test')
    # sys.stdout.write('test3\n')
    # \033[1Dでカーソルを一つ左に動かし、\033[Kでカーソルから行末まで削除しています。
    # buf =''
    # for _ in range(5):
    #     buf +='\033[1D'
    # buf += "\033[K"
    # print(buf)
    # sys.stdout.flush()
    # sys.stdout.flush()
    # print("abc\033[1D\033[K")
    print('\033[2A')
    print('test2')


if __name__ == '__main__':
    main()