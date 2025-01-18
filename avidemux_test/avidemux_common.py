

from pathlib import Path

def get_movie_file_path():
    root_path = r"J:\avidemux_files\target_movie_file.txt"
    with open(root_path,"r", encoding="utf8")as f:
        read_buf = f.readline()
    path = read_buf
    if not Path(path).exists():
        raise FileNotFoundError(path)
    return Path(path)


def get_avedemux_exe_path():
    path = r"C:\Program Files\Avidemux 2.8 VC++ 64bits\avidemux.exe"
    return Path(path)

def test_main():
    _print("test_main")
    pass

def _print(value):
    print(value)

if __name__ == '__main__':
    _print(" ##### ")
    test_main()
    
    


