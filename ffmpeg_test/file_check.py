from pathlib import Path
from ffmpeg_common import const_encoding

def _get_check_file_path():
    file_name = "end_file_list.txt"
    file_list_text_file_path = Path(__file__).parent.joinpath(file_name)
    return file_list_text_file_path


def is_exists_path_in_file_list_text(check_file_path)-> bool:
    check_file_path = Path(check_file_path)
    file_list_text_file_path = _get_check_file_path()
    lines = []
    with open(str(file_list_text_file_path), 'r', encoding=const_encoding)as f:
        lines = f.readlines()
    if _is_exists_in_list(lines, str(check_file_path)):
        return True
    else:
        return False

def _is_exists_in_list(check_list :'list[str]', target_value:str)->bool:
    for check_value in check_list:
        if check_value == target_value:
            return True
    return False

def append_file_path(file_path):
    file_list_text_file_path = _get_check_file_path()
    with open(str(file_list_text_file_path), 'a', encoding=const_encoding)as f:
        f.write(str(file_path))



