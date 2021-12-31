import os,pathlib
import enum

class FileConst(enum.IntEnum):
    FILE = 1
    DIR = 2
    DIRECTORY = 3
    FOLDER = 4

class Match(enum.IntEnum):
    NONE = 0
    AT_WHOLE = 1
    PART = 2


from posixpath import basename, dirname, splitext
class MyFile_():
    file_name : str
    ext : str
    path : str
    dir_path : str
    compare_mode : int

    def __init__(self,path) -> None:
        self.set_var_file(path)

    def set_file_name(self,file_name):
        """ メンバにファイル名をセットする
        ディレクトリはそのまま
        """ 
        _file_name = os.path.basename(file_name)
        _path = os.path.join(self.dir_path,_file_name)
        self.set_var_file(_path)

    def set_var_file(self,path):
        """ メンバにセットする
        対象形式:dir_path/file_name.ext
        """ 
        self.path = path
        self.compare_mode = Match.AT_WHOLE
        if self._is_file(path):
            # 拡張子ありのファイル名
            self.file_name = os.path.basename(path)
            #
            self.ext = self._get_ext(path)[1]
        #
        self.dir_path = self._get_dir_path(path)

    def _create_path(self,*paths):
        _path = self.dir_path
        for p in paths:
            _path = os.path.join(_path,p)
        return _path
    
    def _get_ext(self,path)->str:
        """拡張子を取得する"""
        ext = os.path.splitext(path)
        return ext

    def _get_basename_without_ext(self,path)->str:
        """拡張子なしのファイル名を取得する"""
        bsename_without_ext = os.path.splitext(os.path.basename(path))[0]
        return bsename_without_ext
    
    def _get_compare_mode(self,mode):
        if mode == Match.NONE:
            ret = self.compare_mode
        elif mode == Match.AT_WHOLE or \
            mode == Match.PART:
            ret = mode
        else:
            ret = self.compare_mode
        return ret
    
    def _get_dir_path_if_exists(self,dir_name,path,match=Match.NONE)->bool:
        """ パス(self.dir_path)にdir_nameが存在するか判定す る
        対象形式:dir_path/file_name.ext
        """ 
        match = self._get_compare_mode(match)
        if match == Match.PART:
            dir_list = self._get_list_dir(path)
            buf:str
            for buf in dir_list:
                if buf.find(dir_name)>0:
                    return buf
            return ''
        else:
            #match == Match.AT_WHOLE
            buf = os.path.join(path,dir_name)
            if os.path.exists(buf):
                return buf
            else:
                return ''

    def _is_exists_dir_path(self,dir_name,path,match=Match.NONE)->bool:
        """ パス(self.dir_path)にdir_nameが存在するか判定す る
        対象形式:dir_path/file_name.ext
        """ 
        match = self._get_compare_mode(match)
        ret = self._get_dir_path_if_exists(dir_name,path,match)
        if ret != '':
            return True
        return False
    
    def _get_dir_path(self,path):
        """ディレクトリパスを取得する
        もし、最後がファイル名なら、ファイル名を除外、
        最後がディレクトリ名なら、除外しない
        """
        if os.path.isfile(path):
            ret_dir = os.path.split(path)[0]
        else:
            #dir
            ret_dir = path
        return ret_dir

    def _is_dir(self,path):
        if os.path.isdir(path):
            return True
        return False
    
    def _is_file(self,path):
        if os.path.isfile(path):
            return True
        return False
    
    def _get_parent_dir(self,path)->str:
        return str(pathlib.Path(path).parent)

    def _get_match_path_in_dir(self,match_value,path,match=Match.NONE):
        """
        path の中(子ディレクトリ含む)に match_value と一致したパスを返す
        戻り値:
        リストを返す:list(str)
        一致したものがあればそこで終了するようにしてある
        検討中、階層指定、子ディレクトリ含むフラグ、ファイルかフォルダか
        """
        match = self._get_compare_mode(match)
        dir_path = self._get_dir_path(path)
        path_list = self._get_file_objects_list(dir_path)
        ret_list = []
        next_dir_list = []
        for p in path_list:
            if self._compare_file(match_value,p,match):
                ret_list.append(p)
            else:
                if os.path.isdir(p):
                    next_dir_list.append(p)
        if len(ret_list) < 1:
            if len(next_dir_list) > 0:
                for d in next_dir_list:
                    ret_list = self._get_match_path_in_dir(match_value,d,match)
                    if len(ret_list) > 0:
                        return ret_list
        return ret_list

    def _compare_file(self,match_value,target:str,mode):
        """文字列を比較する
        """
        if mode == Match.AT_WHOLE:
            if target == match_value:
                return True
            return False
        elif mode == Match.PART:
            if target.find(match_value)>0:
                return True
            return False

    def _get_parent_until_match(self,match_value,path,match=Match.NONE):
        """ match_value と合致するまで親フォルダを取得する"""
        match = self._get_compare_mode(match)
        now_path = path
        while not self._is_root(now_path):
            buf = self._get_dir_path_if_exists(match_value,now_path,match)
            if buf != '':
                return os.path.join( now_path , buf)
            now_path = self._get_parent_dir(now_path)
        print(str(__class__) + ' .get_parent_until_match , not match')
        return path

    def _is_root(self,path):
        """path がルートディレクトリか判定する
        """
        split_path = os.path.splitext(path)
        if len(split_path) <= 1:
            return True
        return False

    def _get_file_objects_list(self,dir_path):
        """ファイル名とディレクトリ名の両方の一覧を取得
        戻り値:list(str)
        """
        files = os.listdir(dir_path)
        return files
    
    def _get_list_file(self,dir_path):
        """ファイル名一覧を取得
        戻り値:list(str)
        """
        files = os.listdir(dir_path)
        files_file = [f for f in files if os.path.isfile(os.path.join(dir_path, f))]
        return files_file
    
    def _get_list_dir(self,dir_path):
        """ディレクトリ名一覧を取得
        戻り値:list(str)
        """
        files = os.listdir(dir_path)
        files_dir = [f for f in files if os.path.isdir(os.path.join(dir_path, f))]
        return files_dir
    
    def _append_to_sys(self,dir_path,on_print=True):
        import sys
        sys.path.append(dir_path)
        if on_print:
            print('sys.path.append = {}'.format(dir_path))

class MyFile(MyFile_):
    def __init__(self, path) -> None:
        super().__init__(path)

    def get_path_if_arg_nothing(self,arg_path:str):
        if arg_path == '':
            return self.path
        else:
            return arg_path
    def get_ext(self, path='') -> str:
        _path = self.get_path_if_arg_nothing(path)
        return super()._get_ext(_path)
    
    def get_basename_without_ext(self, path='') -> str:
        _path = self.get_path_if_arg_nothing(path)
        return super()._get_basename_without_ext(path=_path)
    
    def is_exists_dir_path(self, dir_name, path='', match=Match.NONE) -> bool:
        match = self._get_compare_mode(match)
        _path = self.get_path_if_arg_nothing(path)
        return super()._is_exists_dir_path(dir_name, _path, match=match)
    
    def get_dir_path(self, path=''):
        _path = self.get_path_if_arg_nothing(path)
        return super()._get_dir_path(_path)
    
    def is_dir(self, path=''):
        _path = self.get_path_if_arg_nothing(path)
        return super()._is_dir(_path)
    
    def is_file(self, path=''):
        _path = self.get_path_if_arg_nothing(path)
        return super()._is_file(_path)
    
    def get_parent_dir(self, path='') -> str:
        _path = self.get_path_if_arg_nothing(path)
        return super()._get_parent_dir(_path)

    def move_parent_dir(self):
        path = self.get_parent_dir()
        self.set_var_file(path)
    
    def move_dir_from_self(self,*child_dir_names):
        """サブディレクトリに移動する(複数指定可能、可変引数)
        """
        for d in child_dir_names:
            self.move_child_dir(d)

    def move_child_dir(self,child_dir_name=''):
        """サブディレクトリに移動する
        """
        # match = self._get_compare_mode(0)
        match = Match.AT_WHOLE
        dir_path_new = self.get_dir_path(self.path)
        dir_list = self.get_list_dir_(dir_path_new)
        ret = ''
        if len(dir_list) < 1:
            print(str(__class__) + ' : move_child_dir : nothing sub dir , return')
            return
        if child_dir_name != '':
            for d in dir_list:
                if self._compare_file(child_dir_name,d,match):
                    p = os.path.join(dir_path_new,d)
                    self.set_var_file(p)
                    return
            else:
                print(str(__class__) + ' : move_child_dir : not match sub dir [{}] , return'.format(child_dir_name))
        else:
            for d in dir_list:
                self.set_var_file(d)
                return


    
    def get_match_path_in_dir(self, match_value, path='', mode=Match.AT_WHOLE):
        _path = self.get_path_if_arg_nothing(path)
        return super()._get_match_path_in_dir(match_value, _path, mode)

    def compare_file_(self, match_value, target: str, mode):
        return super()._compare_file(match_value, target, mode)
    
    def get_parent_until_match(self, match_value, path='', mode=Match.AT_WHOLE):
        _path = self.get_path_if_arg_nothing(path)
        return super()._get_parent_until_match(match_value, _path, mode)

    def move_to_parent_until_match(self, match_value, mode=Match.AT_WHOLE):
        _path = self.get_parent_until_match(match_value,self.path,mode)
        self.set_var_file(_path)

    def get_file_objects_list(self, dir_path=''):
        _path = self.get_path_if_arg_nothing(dir_path)
        _path = self._get_dir_path(_path)
        return super()._get_file_objects_list(_path)
    
    def is_root(self, path='')->bool:
        _path = self.get_path_if_arg_nothing(path)
        return super().is_root_(_path)
    
    def get_list_file_(self, dir_path=''):
        _path = self.get_path_if_arg_nothing(dir_path)
        _path = super()._get_dir_path(_path)
        return super()._get_list_file(_path)
    
    def get_list_dir_(self, dir_path=''):
        _path = self.get_path_if_arg_nothing(dir_path)
        _path = self._get_dir_path(_path)
        return super()._get_list_dir(_path)
    
    def append_to_sys(self, on_print=True):
        dir_path = self.get_dir_path(self.path)
        return super()._append_to_sys(dir_path, on_print=on_print)

    def print_path(self):
        print('print_path = ' + self.path)