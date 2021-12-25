import time
from concurrent.futures import ThreadPoolExecutor
from logging import StreamHandler, Formatter, INFO, getLogger
import import_init
from common_util.log_util.logging_util import intialize_logger_util

import traceback

def init_logger():
    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(Formatter("[%(asctime)s] [%(threadName)s] %(message)s"))
    logger = getLogger()
    logger.addHandler(handler)
    logger.setLevel(INFO)


def task(v):
    getLogger().info("%s start", v)
    time.sleep(1.0)
    getLogger().info("%s end", v)

import common_util.adb_util.adb_common as adb_common
def task2(v,logger):
    try:
        adb_common.swipe(logger,700,500,100,500,400)
        return
    except:
        traceback.print_exc()

def record(logger):
    try:
        filename = 'screenrecord.mp4'
        android_path = '/sdcard/'
        adb_common.screen_record(logger,filename,android_path)
        pc_path = import_init.get_current_dir()
        adb_common.save_file_to_pc_from_android(logger,pc_path,android_path,filename)
        return
    except:
        traceback.print_exc()

def main2():
    logger = import_init.initialize_logger_new()
    for i in range(5):
        task2(i,logger)

def main():
    logger = import_init.initialize_logger_new()
    init_logger()
    getLogger().info("main start")
    import time
    with ThreadPoolExecutor(max_workers=2, thread_name_prefix="thread") as executor:
        executor.submit(record,logger)
        time.sleep(2)
        for i in range(5):
            if i == 1:
                executor.submit(task, i,logger)
            else:
                time.sleep(1)
                executor.submit(task2, i,logger)
        getLogger().info("submit end")
    getLogger().info("main end")


if __name__ == "__main__":
    main()
    # main2()