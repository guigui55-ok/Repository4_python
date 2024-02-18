# https://camp.trainocate.co.jp/magazine/python-excel-advanced/
"""

https://camp.trainocate.co.jp/magazine/python-excel-advanced/

pip install xlwings


"""

import xlwings
import openpyxl

def test1():
    """
    エクセルファイルを開いて マクロを作成からの処理を実行、ファイルを保存して終了する
    ----
    エラーが発生する
    マクロが実行されない
    """
    app = xlwings.App()
    # file_path = './FileIO.xlsb'
    # file_path = './python_test.xltm'
    file_path = 'python_test1.xlsm'
    # wb = app.books.open(file_path)
    # keep_vba=Trueで作成したマクロを保存する（？）
    wb = openpyxl.load_workbook('./Excelサンプル2.xlsm', keep_vba=True)

    # pg=wb.macro('CommandButton1_Click')
    pg = wb.macro('TestMacro')
    pg()
    
    wb.save(file_path)
    
    wb.close()
    app.quit()

    """
    (-2147352567, '例外が発生しました。', (0, 'Microsoft Office Excel', "マクロ ''FileIO.xlsb'!CommandButton1_Click' を実行できません。このブックでマクロが使用できないか、またはすべてのマクロが無効になっている可能性があります。", 'C:\\Program Files (x86)\\Microsoft Office\\Office12\\1041\\XLMAIN11.CHM', 0, -2146827284), None)

    pywintypes.com_error: (-2147352567, '例外が発生しました。', (0, 'Microsoft Office Excel', "マクロ ''python_test1'!CommandButton1_Click' を実行できません。このブックでマクロが使用できないか、またはすべてのマクロが無効になってい
    る可能性があります。", 'C:\\Program Files (x86)\\Microsoft Office\\Office12\\1041\\XLMAIN11.CHM', 0, -2146827284), None)

    """

def test2():
    """
    エクセルファイルに画像を張り付けて保存
    ----
    ファイルが破損する
    """
    img = openpyxl.drawing.image.Image('sample.jpg')

    file_path = 'python_test1.xlsm'
    wb = openpyxl.load_workbook(file_path)
    sheet = wb['Sheet1']

    img.anchor = 'A1'
    sheet.add_image(img)

    wb.save(file_path)
    wb.close()
    """
    Excelでファイル 'python_test1.xlsm' を開くことができません。ファイル形式またはファイル拡張子が正しくありません。ファイルが破損しておらず、ファイル拡張子とファイル形式が一致していることを確認してください。
    """
    return


if __name__ == '__main__':
    # test1()
    test2()

