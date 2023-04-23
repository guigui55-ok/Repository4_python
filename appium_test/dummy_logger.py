


import os
import logging
from typing import Any
import pathlib

class DummyLogger(logging.Logger):
    def __init__(self, name: str, level: int = -1) -> None:
        file_name = os.path.basename(name)
        self.flush = True
        self.log_dir = None

        if level == -1:
            self.dummy_mode = True
        else:
            self.dummy_mode = False
            # nameがパスの時ディレクトリがなければ作成
            if not pathlib.Path(name).exists():
                if not pathlib.Path(name).is_dir():
                    path = str(pathlib.Path(name).parent)
                else:
                    path = str(pathlib.Path(name))
                os.mkdir(path)
            super().__init__(file_name, level)
            # ログファイルハンドラを作成し、ログレベルを設定
            file_handler = logging.FileHandler(name)
            file_handler.setLevel(level)
            # フォーマットを設定し、ハンドラに適用
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            # ロガーにハンドラを追加
            self.addHandler(file_handler)

    # def _log(self, level: int, msg: str, *args: Any, **kwargs: Any) -> None:
    #     if self.dummy_mode:
    #         print(msg, flush=self.flush)
    #     else:
    #         super()._log(level, msg, *args, **kwargs)
    def _log(self, level: int, msg: str, *args: Any, **kwargs: Any) -> None:
        print(msg, flush=self.flush)
        if self.dummy_mode:
            pass
        else:
            super()._log(level, msg, args, *args, **kwargs)  # 修正された行

    def info(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.INFO, msg, *args, **kwargs)

    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.DEBUG, msg, *args, **kwargs)

    def warning(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.WARNING, msg, *args, **kwargs)

    def error(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.ERROR, msg, *args, **kwargs)

    def critical(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log(logging.CRITICAL, msg, *args, **kwargs)

"""
230415
pythonでロガークラス（クラス名：DummyLogger）を作成したいです。
以下の条件に従ってソースを出力してください。
条件
DummyLoggerはテキストなどにはなにも出力せず、コンソールにのみ出力する
python のライブラリlogging.Loggerを継承する
モードを2つ用意して、1つは上記logging.Loggerを通常通り使用する（Normalモード）、
　　2つ目はDummyLoggerを使用する（Dummyモード）
__init__の引数は以下のようにLoggerと似たものにする（_levelの初期値は-1）
  (def __init__(self, name: str, level: _Level = -1) -> None:)
__init__ の第2引数_Levelが-1の時は、Dummyモードとする
__init__ の第1引数name がpathの時には、
  そのパスのファイル名だけをsuper().__init__のnameにわたし、Normalモードで実行する
Dummyモードの場合、Logger.info, Logger.debug などのログを出力するメソッドは、printで置き換えること
また、上記のprintではクラスにメンバ変数flushを設置して、print(value,flush=self.flush)のようにして、制御できるようにする

__init__ の第1引数name がpathの時には、そのパスにログファイルを出力するようにする。
"""



import os
from pathlib import Path
from dummy_logger import DummyLogger

def main():
    # Dummyモードのテスト
    print("Testing Dummy Mode:")
    dummy_logger = DummyLogger("dummy", level=-1)
    dummy_logger.debug("Dummy Debug")
    dummy_logger.info("Dummy Info")
    dummy_logger.warning("Dummy Warning")
    dummy_logger.error("Dummy Error")
    dummy_logger.critical("Dummy Critical")

    print("\nTesting Normal Mode:")
    # Normalモードのテスト
    log_path = Path(__file__).parent.joinpath('logger_test.log')
    normal_logger = DummyLogger(str(log_path), level=logging.DEBUG)
    normal_logger.debug("Normal Debug")
    normal_logger.info("Normal Info")
    normal_logger.warning("Normal Warning")
    normal_logger.error("Normal Error")
    normal_logger.critical("Normal Critical")
    print("\nTesting Normal Mode:")
    print(f"Log file has been created at: {log_path}")

    # Normalモードのテスト
    log_path = Path(__file__).parent.joinpath('log').joinpath('logger_test.log')
    # log_path = 'log/logger_test.log'
    normal_logger = DummyLogger(str(log_path), level=logging.DEBUG)
    normal_logger.debug("Normal Debug")
    normal_logger.info("Normal Info")
    normal_logger.warning("Normal Warning")
    normal_logger.error("Normal Error")
    normal_logger.critical("Normal Critical")


if __name__ == "__main__":
    main()