import import_init
import traceback

def test_file():
    try:
        print('-------------------------')
        import file_class
        file = file_class.MyFile(__file__)
        base_dir = 'Repository4_python'
        file.move_to_parent_until_match('Repository4_python')
        file.move_child_dir('common_util')
        file.print_path()
        return
    except:
        traceback .print_exc()

test_file()