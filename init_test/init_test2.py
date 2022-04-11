"""
import init_test
を読み込んだ時、__initは読み込まれるか

"""
import init_test

def main():
    print('** main')
    print('    ' + __name__)

if __name__ == '__main__':
    main()