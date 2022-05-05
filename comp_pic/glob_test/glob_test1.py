

import glob

def main():
    path = __file__


    files = glob.glob(path)
    print()
    print('----------')
    for file in files:
        print('  ' + file)


if __name__ == '__main__':
    main()