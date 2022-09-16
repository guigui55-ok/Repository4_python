
from lib2to3.pgen2.token import NEWLINE
from typing import Tuple


def check_value_for_send_file(file_path:str)->Tuple[bool,str]:
    try:
        import os
        if os.path.exists(file_path):
            return True,''
        else:
            return False,'path not exists. path='+file_path
    except Exception as e:
        import traceback
        traceback.print_exc()
        return False ,str(e)


def allwed_file(filename,allowed_extensions_list = []):
    # .があるかどうかのチェックと、拡張子の確認
    # OKなら１、だめなら0
    if len(allowed_extensions_list) < 1:
        print('len(allowed_extensions_list) < 1')
        return True
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions_list

def create_tag(value,tag,attribute):
    """ value,p,class="content"  ->  <p class="content">value</p>
    """
    #属性はなければ空文字とする
    if attribute != '':
        attr_new = ' ' + attribute
    else:
        attr_new = ''
    #文字列を作成、連結する
    before_str = '<' + tag + attr_new + '>'
    after_str = '</' + tag + '>'
    ret = before_str + value + after_str
    return ret

def list_to_str(value_list,delimita='\n'):
    ret:str = ''
    for val in value_list:
        ret += str(val) + delimita
    return ret[:-len(delimita)]

def create_tag_li_ul(value_list,ul_attribute):
    """
    文字列のリストから、ul-liの要素を作成する
    value_list, 'class="list" summary="summary_value"'
        ->
        <ul class="list" summary="summary_value">
            <li>value_list[i]</li>
            <li>value_list[i]</li>
            <li>value_list[i]</li>
            ...
        </ul>
    """
    li_value = ''
    for val in value_list:
        buf = create_tag(val,'li','')
        li_value += buf + '\n'
    ul_value = create_tag(li_value,'ul',ul_attribute)
    return ul_value