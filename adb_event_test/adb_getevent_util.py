
import common_util.file_util.file_general as file_general
import common_util.adb_util.adb_common as adb_common

from adb_getevent_io import AdbEvent,AdbEventWriter,cnv_adb_event_str_to_hex
# from adb_getevent_util import read_to_ffffff_or_eof

def adb_sendevents_main(
    logger,
    event_lines:list,
    pc_dir_path:str,
    binary_file_name:str,
    android_sd_dir_path:str,
    dev_input_event:str):
    """
    以下機能のメイン関数
    実行関数は adb_sendevents で実行する
    機能：
    /dev/input/event* へ イベントデータをバイナリファイルを転送して、
    タッチ、スワイプなどの操作を行う
    ※備考
    PC 内の getevent ファイル (pc_dir_path \ binary_file_name)を、
    Android SD カード内のパス(android_sd_dir_path) へコピーして
    その後、adb shell cat コマンドで dev/enput/event* へ転送する
    ・　getevent ファイルは、adb shell getevent の形式と同じもの
    """
    # ファイルを読み込む

    # 読み込んだリストから、type,code,valueを読み込む
    import os
    adb_events = []
    count = 0
    for line in event_lines:
        # print(line[:-1])
        e_type,e_code,e_value = cnv_adb_event_str_to_hex(line[:-1])
        e = AdbEvent(e_type,e_code,e_value,count)
        adb_events.append(e)
        count+=1
    # ファイル名、パスをセットする
    bin_name = binary_file_name
    bin_file_path =  os.path.join(pc_dir_path,bin_name)
    # ファイルが存在していたら削除する
    if os.path.exists(bin_file_path):
        os.remove(bin_file_path)
        logger.info('adb_sendevents : remove file. file = ' + bin_file_path)
    # bin ファイルに書き込み
    writer = AdbEventWriter(bin_file_path)
    data:AdbEvent
    i = 0
    for data in adb_events:
        i+=1
        data.print_data(i) # debug
        writer.write_adb_event_data(data)
    # 一度 sdcard へ bin ファイルをコピーする（権限問題回避のため）
    android_path = android_sd_dir_path + '/' + binary_file_name
    flag = adb_common.push(logger, bin_file_path, android_path)
    if not flag:
        logger.exp.error('adb push failed , return')
        return False
    # さらにsdard から本体へコピーする（イベントを実行する）
    # cmd = 'adb shell "cat /sdcard/event.bin > /dev/input/event2"'
    cmd = 'adb shell "cat ' + android_path + ' > ' + dev_input_event + '"'
    flag = adb_common.excute_command(logger,cmd)

def adb_sendevents(
    logger,
    pc_read_getevent_dir:str,
    pc_read_getevent_file_name:str,
    pc_binary_dir_path:str,
    binary_file_name:str,
    android_sd_dir_path:str,
    dev_input_event:str,
    interval_sec:int=1):
    """
    /dev/input/event* へ イベントデータをバイナリファイルを転送して、
    タッチ、スワイプなどの操作を行う
    ※1
    PC 内の getevent ファイル (read_getevent_dir \ read_getevent_file_name)を、
    バイナリ変換して PC (pc_binary_dir_path \ binary_file_name) 内に作成。
    その後、Android SD カード内のパス(android_sd_dir_path) へコピー (push) してから
    adb shell cat コマンドで dev/enput/event* へ転送する
    ※2
    getevent ファイルは、adb shell getevent の形式と同じもの
    """
    import os
    read_file_path = os.path.join(pc_read_getevent_dir,pc_read_getevent_file_name)
    # read file
    read_lines = file_general.read_line_file(logger,read_file_path)
    # print('len(read_lines) = ' + str(len(read_lines)))
    if len(read_lines)<1:
        logger.exp.error('adb_sendevents , len(read_lines)<1 , return')
        return
    # excute
    import time
    pos = 0
    while(pos<len(read_lines)):
        pos,lines = read_to_ffffff_or_eof(logger,read_lines,pos)
        adb_sendevents_main(
            logger,
            lines,
            pc_binary_dir_path,
            binary_file_name,
            android_sd_dir_path,
            dev_input_event)
        time.sleep(interval_sec)
        pos = pos + 1
    return

def read_to_ffffff_or_eof(logger,lines:list,start=0):
    """
    adb shell getevent で取得したデータの一区切りを読み込む
    adb のイベント ffffffff から後ろ2行までが一区切り
    """
    i:int
    ret_list = []
    if len(lines) < 1:
        logger.exp.error('read_to_ffffff_or_eof , len(lines) < 1: , return')
        return start,ret_list
    if start > (len(lines)-1):
        logger.exp.error('read_to_ffffff_or_eof , start > (len(lines)-1): , return')
        return start, ret_list
    to_last = 0
    for i in range(len(lines))[start:]:
        value:str = lines[i]
        if value.find('ffffffff') >= 0:
            ret_list.append(value)
            to_last = 3
        else:                
            ret_list.append(value)
            if to_last > 0:
                to_last -= 1
                if to_last == 1:
                    break
        # eof
        if i == (len(lines)-1):
            break
    return i, ret_list

