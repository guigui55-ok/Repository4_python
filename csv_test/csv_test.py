import csv
from fileinput import filename
import pprint

def write_csv_test():
    try:
        data1 = [0,1,2]
        data2 = ['a','b','c']
        path = get_path()

        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(data1)
            writer.writerow(data2)

        print('path = ' + path)

        return
    except:
        import traceback
        traceback.print_exc()

def read_csv_test():
    try:
        path = get_path()
        print('path = ' + path)

        with open(path) as f:
            data = f.read()

        print('-------------')
        print(data)
        return
    except:
        import traceback
        traceback.print_exc()


def get_path()->str:
    import pathlib,os
    file_name = 'test.csv'
    sub_dir = 'test_data'
    path = os.path.join(pathlib.Path(__file__).parent,sub_dir,file_name)
    return path

def main():
    # write_csv_test()
    read_csv_test()
main()