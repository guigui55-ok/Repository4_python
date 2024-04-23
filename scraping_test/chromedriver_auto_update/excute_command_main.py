import sys
import subprocess

def excute_command(cmd):
    '''
    コマンドを実行して、結果を取得する
    
    Args:
        param cmd {str}: 実行するコマンド
    
    Returns:
        {list[str]} 標準出力 (行毎).
            各行の後ろにはすべて、改行コード \n があります
    '''
    ret_byte_lines = get_lines(cmd)
    ret_str_lines = cnv_byte_to_str_lines(ret_byte_lines)
    return ret_str_lines



# https://qiita.com/megmogmog1965/items/5f95b35539ed6b3cfa17
def get_lines(cmd):
    '''
    コマンドを実行して、結果を取得する
    
    Args:
        param cmd: str 実行するコマンド.
        rtype: generator
    
    Returns:
        標準出力 (行毎).
    '''
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    str_lines = []
    while True:
        line = proc.stdout.readline()
        if line:
            buf = cnv_byte_to_str(line)
            buf = buf.replace('\r\n','\n')
            str_lines.append(buf)
            yield line

        if not line and proc.poll() is not None:
            break
    return str_lines

# https://python.civic-apps.com/python3-bytes-str-convert/
def cnv_byte_to_str(value)->str:
    try:
        if isinstance(value, str):
            return value
        # if type(value) is type(Bytes): # not define
        ret = value.decode('utf-8')
        return ret
    except Exception as e:
        print(str(e))
        return ''

def cnv_byte_to_str_lines(byte_generator)->'list[str]':
    cmd_result_str_lines = []
    for line in byte_generator:
        buf = cnv_byte_to_str(line)
        buf = buf.replace('\r\n','\n')
        cmd_result_str_lines.append(buf)
    return cmd_result_str_lines

def write_lines(write_file_path, lines):
    with open(str(write_file_path), 'w', encoding='utf-8')as f:
        f.writelines(lines)
    print('lines len = {}'.format(len(lines)))
    # 最初だけ小文字になって、VsCodeコンソールから開けなくなる
    # print('write_file_path = {}'.format(str(write_file_path).capitalize()))
    buf = str(write_file_path)[0].upper()
    buf += str(write_file_path)[1:]
    print('write_file_path = {}'.format(buf))
    from pathlib import Path
    print('write_file_name = {}'.format(Path(str(write_file_path)).name))

def test_excute_command():
    cmd = 'adb shell getevent /dev/input/event2'
    cmd = 'pip install chromedriver-binary'
    cmd = 'pip freeze'
    cmd = 'pip install chromedriver-binary'
    cmd = 'pip install chromedriver-binary-sync'
    # https://qiita.com/QutaPase/items/f895e7f1ba887fa52ce1
    cmd = 'pip install chromedriver-autoinstaller'
    
    cmd = 'dir /B /O-N "C:\Program Files (x86)\Google\Chrome\Application" | findstr "^[0-9].*¥>'
    cmd_result_lines = get_lines(cmd)
    print()
    print()
    print('command = {}'.format(cmd))
    # print('type = {}'.format(type(cmd_result_lines))) # <class 'generator'>
    print('===== result =====')
    # cmd_result_str_lines = []
    cmd_result_str_lines = cnv_byte_to_str_lines(cmd_result_lines)
    for line in cmd_result_str_lines:
        buf = cnv_byte_to_str(line)
        buf = buf.replace('\r\n','\n')
        sys.stdout.write(buf)
    print('=====  end  =====')
    #/
    # 書き込み処理
    from pathlib import Path
    write_dir = Path(__file__).parent
    import datetime
    datetime_str = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    write_file_name = '__sample_' + Path(__file__).name.replace('.py', '_'+datetime_str+'.txt')
    write_file_path = str(write_dir.joinpath(write_file_name))
    write_lines(write_file_path, cmd_result_str_lines)


if __name__ == '__main__':
    test_excute_command()