from enum import Enum

class const(Enum):
    ENCODING_UTF_8 = 'UTF-8'
    ENCODING_SHIFT_JIS = 'shift_jis'
    ENCODING_DEFAULT = 'UTF-8'
    
class file_io():
    path = ''
    encoding = const.ENCODING_UTF_8.value
    logger = None
    # -----------------------------------------------
    def __init__(
        self,
        logger,
        path,
        encoding = const.ENCODING_DEFAULT.value
    ) -> None:
        self.path = path
        self.encoding = encoding
        self.logger = logger
    # -----------------------------------------------
    
    # -----------------------------------------------
    def write_append(
        self,
        data,
        path = '',
        encoding = const.ENCODING_UTF_8.value
    ) -> bool:
        write_path = ''
        # 引数の path を優先する
        if (path != '')&(path != None):
            write_path = path
        else:
            # 引数の path がなければ、self.path をチェックする
            if (self.path != '')&(self.path != None):
                write_path = self.path
            else:
                self.logger.info('path is nothing.')
                return False
        write_encoding = ''
        # 引数の encoding を優先する
        if encoding != const.ENCODING_DEFAULT.value:
            write_encoding = encoding
        else:
            # 引数が default のとき、self.encoding をチェックする
            if self.encoding != const.ENCODING_DEFAULT.value:
                write_encoding = self.encoding
            else:
                write_encoding = const.ENCODING_DEFAULT.value
        # ファイルに書きこむ
        with open(write_path, "a",encoding=write_encoding) as f:
            f.write(data)
        return True

    # -----------------------------------------------
    def read(
        self,
        path='',
        encoding=const.ENCODING_DEFAULT.value
    ) -> str:
        read_path = ''
        # 引数の path を優先する
        if (path != '')&(path != None):
            read_path = path
        else:
            # 引数の path がなければ、self.path をチェックする
            if (self.path != '')&(self.path != None):
                read_path = self.path
            else:
                self.logger.info('path is nothing.')
                return False
        read_encoding = ''
        # 引数の encoding を優先する
        if encoding != const.ENCODING_DEFAULT.value:
            read_encoding = encoding
        else:
            # 引数が default のとき、self.encoding をチェックする
            if self.encoding != const.ENCODING_DEFAULT.value:
                read_encoding = self.encoding
            else:
                read_encoding = const.ENCODING_DEFAULT.value
        # ファイルに書きこむ
        with open(read_path, "r",encoding=read_encoding) as f:
            data = f.read()
        return data
