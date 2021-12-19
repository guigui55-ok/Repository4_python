
import traceback
import sys

def test_sys_args():
    try:

        print(sys.argv)
        buf:list = sys.argv
        buf.append('append_value')
        sys.argv
        print(sys.argv)

        return
    except:
        traceback.print_exc()

test_sys_args()
