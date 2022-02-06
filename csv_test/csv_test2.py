import csv
from fileinput import filename
import pprint

def write_appnd_csv():
    try:
        data1 = [1,2,3,4]
        data2 = ['c','d','e','f']
        path = get_path()

        with open(path, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data1)
            writer.writerow(data2)

        print('path = ' + path)

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
    write_appnd_csv()
main()