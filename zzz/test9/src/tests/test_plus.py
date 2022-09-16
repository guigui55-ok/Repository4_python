import pathlib,sys
parent_dir = str(pathlib.Path(__file__).parent.parent.parent)
sys.path.append(parent_dir)
print('sys.path.append : {}'.format(parent_dir))

from src.plus import plusplus

def test_plus():
    assert plusplus(1,2) == 100

if __name__ == '__main__':
    test_plus()