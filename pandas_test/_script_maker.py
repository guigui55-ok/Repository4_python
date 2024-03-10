"""
手順、確認内容を読み込んで、スクリプトを作成する

処理詳細
エクセルの手順、確認内容を渡して、それぞれの行を読み取り、番号順に振り分ける
 番号のない行は前の番号と一緒にリストに振り分ける
   それぞれの行を手順用、確認用にスクリプト用に変換して
    そして、手順と確認内容の番号が合うように、それぞれ交互に出力する
      これをシナリオに張り付ける
"""

import re
NEW_LINE = '\n'
DEBUG = True
def debug_print(value):
    if DEBUG:
        print(str(value))
class Const():
    MODE_PROC = 1
    MODE_CONFIRM = 2

PROCEDURE_TEXT = "procedure('##$$##')"
CONFIRM_TEXT = "confirm('##$$##')"

class OneStep():
    """ 1つの手順・確認を扱うクラス（複数行あることを想定） """
    def __init__(self) -> None:
        self.step_num:int = 0
        self.lines:'list[str]' = []
        self.script_lines:'list[str]' = []

    def add_text(self, text:str):
        self.lines.append(text)
    
    def print_lines(self):
        for line in self.lines:
            print(line)

    def print_script_lines(self):
        for line in self.script_lines:
            print(line)

class ScriptMaker():
    def __init__(self, mode:int) -> None:
        self.mode = mode
        self.delimita = NEW_LINE
        self.num = 0
        self.step_list:'list[OneStep]'=[]
        self.indent = '    '

    def count_steps(self):
        """手順がいくつあるのかカウント"""
        return len(self.step_list)

    def set_text(self, text:str):
        """
        手順などをセットする

        文字列を改行で区切って、
         各行の最初の文字を判定して、番号ごとにまとめていく
          番号がない行は前の番号と一緒の扱いとする
        """
        lines = text.split(self.delimita)
        now_num = 0
        for i, line in enumerate(lines):
            if line=='':continue
            debug_print('line = ' + line)
            next_num = self._get_step_num_from_line(line, now_num)
            if now_num == next_num:
                #同じなら既存のものの最後に追加する
                one_step = self.step_list[-1]
                one_step.add_text(line)
                debug_print('append line(i={})(step_num={})'.format(i, next_num))
            else:
                #次の番号になったらOneStepClassを追加する
                # 一つと日などの場合は空のOneStepを追加しておく
                if 1<(next_num - now_num):
                    for j in range(now_num+1, next_num):
                        one_step = OneStep()
                        one_step.step_num = j
                        self.step_list.append(one_step)
                        debug_print('add blank step(i={})(step_num={})'.format(i, next_num))
                #/
                one_step = OneStep()
                one_step.step_num = next_num
                buf = self._get_prefix()
                one_step.add_text(buf + line)
                self.step_list.append(one_step)
                debug_print('add step(i={})(step_num={})'.format(i, next_num))
                now_num = next_num

    def get_script_lines_from_step(self, num:int):
        step = self.step_list[num]
        return step.script_lines

    def create_script_from_step_list(self):
        """ 手順の文字列をスクリプトに張り付けるように変換する(ScriptMaker > OneStep) """
        for one_step in self.step_list:
            self._make_script_one_step(one_step)

    def _make_script_one_step(self,one_step:OneStep):
        """ 手順の文字列をスクリプトに張り付けるように変換する(OneStep.lines) """
        # ネストが深くなるので分割しているだけ
        for line in one_step.lines:
            buf = self._make_script_line(line)
            one_step.script_lines.append(buf)
    
    def _make_script_line(self,line:str):
        """ 手順の文字列をスクリプトに張り付けるように変換する(OneStep.lines > line) """
        if self.mode == Const.MODE_PROC:
            base_str = PROCEDURE_TEXT
            # if '※' in line:
            #     pass
        else:
            # Const.MODE_CONFIRM
            base_str = CONFIRM_TEXT
        ret = self.indent + base_str.replace('##$$##', line)
        return ret

    def _get_prefix(self):
        if self.mode == Const.MODE_PROC:
            return '手順'
        else:
            # Const.MODE_CONFIRM
            return '確認'
        
    def _get_step_num_from_line(self, line:str, now_num:int):
        """ 1行から番号を取得する（番号がなければ今のものを返す） """
        re_ret = re.search(r'^\d', line)
        if re_ret!=None:
            ret = re_ret.group()
            return int(ret)
        else:
            return now_num

    def _print_all_lines(self):
        for one_step in self.step_list:
            one_step.print_lines()

    def _print_all_script_lines(self):
        for one_step in self.step_list:
            one_step.print_script_lines()


##################################################

TEST_PROC_TEXT = """
1.手順１を行う
 ※手順１備考
2.手順２を行う
3.手順３を行う
"""

TEST_CONF_TEXT = """
1. 画面1となること
3. 動作３となること
"""

def main():
    #####
    # テキストから手順を番号ごとに分けて、スクリプトソースにするまで
    #####
    #/
    proc_obj = ScriptMaker(Const.MODE_PROC)
    proc_obj.set_text(TEST_PROC_TEXT)
    proc_obj.create_script_from_step_list()
    #/
    conf_obj = ScriptMaker(Const.MODE_CONFIRM)
    conf_obj.set_text(TEST_CONF_TEXT)
    conf_obj.create_script_from_step_list()

    proc_obj._print_all_script_lines()
    conf_obj._print_all_script_lines()
    ###
    # それぞれの手順、確認を番号ごとにまとめる
    ###
    #/
    count = max(
        proc_obj.count_steps(),
        conf_obj.count_steps())
    #/
    ret_str_list = []
    for i in range(count):
        buf_list = proc_obj.get_script_lines_from_step(i)
        ret_str_list.extend(buf_list)
        buf_list = conf_obj.get_script_lines_from_step(i)
        ret_str_list.extend(buf_list)

    print('##########')
    print('出力された結果を張り付ける')
    print('ret_str_list = ')
    print()
    import pprint
    # pprint.pprint(ret_str_list)
    for buf in ret_str_list:
        print(buf)
    print()

if __name__ == '__main__':
    main()