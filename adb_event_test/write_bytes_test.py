


def write_byetes(data:bytes,file_name):
    f = open(file_name, 'wb')
    f.write(data)
    f.close()

from contextlib import nullcontext
import traceback

def main():
    try:
        file_name = 'test_write_bytes.bin'
        data = b'00000000' # 30303030
        data = b'\x00' # 00
        #data = None # TypeError: a bytes-like object is required, not 'NoneType'
        write_byetes(data,file_name)
        print(file_name)
    except:
        traceback.print_exc()

main()