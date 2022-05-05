

import glob
import pathlib

def main():
    path = __file__
    path = str(pathlib.Path(__file__).parent.parent)

    files = glob.glob(path + '/*.py')
    print()
    print('----------')
    for file in files:
        print('  ' + file)


if __name__ == '__main__':
    main()