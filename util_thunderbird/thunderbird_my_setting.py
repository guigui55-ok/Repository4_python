

def get_thunderbird_mailbox_root_path():
    file_path = r'C:\Users\OK\source\repos\test_media_files\_any_setting\thunderbird_path.txt'
    with open(file_path, 'r')as f:
        buf = f.readline()
    return buf
    