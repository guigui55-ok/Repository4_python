import sys,pathlib,os
target = 'Repository4_python'
path = str(pathlib.Path(__file__).parent)
while True:
    path = str(pathlib.Path(path).parent)
    if os.path.basename(path) == target:
        sys.path.append(path)
        print(path)
    if len(path)<4:break

import common_utility