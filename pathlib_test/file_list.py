

import glob
from pathlib import Path
import os

def _test_main():
    path = r'O:\iso'

    paths = glob.glob(path + '/*', recursive=True)
    print('*****\n')
    for path in paths:
        print(os.path.basename(path))
    print('======')

if __name__ == '__main__':
    _test_main()