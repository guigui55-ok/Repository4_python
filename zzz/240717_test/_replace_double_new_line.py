


from pathlib import Path
def _test_main():
    enc = 'utf8'
    # enc = 'sjis'
    file_name = 'log.txt'
    dir_path_str = r'C:\Users\OK\Desktop'
    # dir_path_str = r'C:\Users\OK\source\repos\Learning\learning_python\scraping_tool\scraping_main\__test_data'
    rpath = str(Path(dir_path_str).joinpath(file_name))
    with open(rpath, 'r', encoding=enc, errors='ignore')as f:
        read_buf = f.read()
    #/
    count = read_buf.count('\n\n')
    print('count = {}'.format(count))
    read_buf = read_buf.replace('\n\n', '\n')
    #/
    # file_name = 'log_w.txt'
    wpath = str(Path(dir_path_str).joinpath(file_name))
    with open(wpath, 'w', encoding=enc)as f:
        f.write(read_buf)
    print('wpath = {}'.format(wpath))


if __name__ == '__main__':
    _test_main()