
from pathlib import Path
import shutil
# いきなりサブフォルダは作成できない
# FileNotFoundError: [WinError 3] 指定されたパスが見つかりません。: 'c:\\Users\\OK\\source\\repos\\Repository4_python\\excel_test\\test\\test_b'
path = Path(__file__).parent.joinpath('test')
path.mkdir(exist_ok=True)

path = path.joinpath('test_b')
path.mkdir(exist_ok=True)