
import os 
image_path = os.getcwd()
from pathlib import Path
path = str(Path(__file__).resolve().parent)
path = str(Path(path).resolve().parent)
import sys
sys.path.append(path)
print('sys.path.append')
print(path)

import common_util
