import csv
import traceback

def write_appnd_csv():
    try:
        data1 = [1,2,3,4]
        data2 = ['c','d','e','f']
        path = get_path()

        with open(path, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data1)
            writer.writerow(data2)
            writer.writerows([data1,data2])

        print('path = ' + path)
        return
    except:
        traceback.print_exc()

def get_path() -> str:
    import pathlib
    file_name = 'test.csv'
    sub_dir = 'test_data'
    path = str(pathlib.Path(__file__).parent.joinpath(sub_dir,file_name))
    return path

def main():
    write_appnd_csv()

if __name__ == '__main__':
    main()