
def allwed_file(filename,allowed_extensions_list = []):
    # .があるかどうかのチェックと、拡張子の確認
    # OKなら１、だめなら0
    if len(allowed_extensions_list) < 1:
        print('len(allowed_extensions_list) < 1')
        return True
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions_list