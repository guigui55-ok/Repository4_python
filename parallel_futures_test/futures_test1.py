import time
from concurrent.futures import ThreadPoolExecutor
from logging import StreamHandler, Formatter, INFO, getLogger


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


def main():
    init_logger()
    getLogger().info("main start")
    with ThreadPoolExecutor(max_workers=2, thread_name_prefix="thread") as executor:
        for i in range(5):
            executor.submit(task, i)
        getLogger().info("submit end")
    getLogger().info("main end")


if __name__ == "__main__":
    main()