import csv
import pprint

def test_csv_dict_make():
    try:
        labels = ['a','b','c']
        nums = [1,2,3]
        path = get_path()
        w_nums = []
        n = 0
        with open(path, 'a') as f:
            writer = csv.DictWriter(f, labels)
            writer.writeheader()
            for i in range(10):
                n += 10
                w_nums = {labels[0]:nums[0]+n, labels[1]:nums[1]+n, labels[2]:nums[2]+n}
                writer.writerow(w_nums)

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
    test_csv_dict_make()
main()