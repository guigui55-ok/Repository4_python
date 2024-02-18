"""
エクセルから読み込んで合計

外部データ連携
"""

r"""
textインポート
https://xtech.nikkei.com/it/pc/article/NPC/20060214/229255/

「データ」メニューの「外部データの取り込み」をポイントし「テキストファイルのインポート」をクリックする

エクセルに外部データ連携をして、テキストを書き換える

外部データ更新VBA
https://ittrip.xyz/vba/excel-vba-data-source-auto-update

Sub UpdateDataSource()
    ThisWorkbook.RefreshAll
End Sub
"""

r"""
エクセル側では以下のVBAでデータソース(参照しているテキストファイル)をボタンで更新する

Private Sub UpdateDataSource_Click()
    Dim filePath As String
    filePath = "C:\Users\OK\source\repos\Repository4_python\excel_test\test_ref.txt" ' テキストファイルのパスを指定
    UpdateOrCreateQueryTable "my sheet", filePath, "A2"
End Sub



Sub UpdateOrCreateQueryTable(sheetName As String, filePath As String, destination As String)
    'Args: destination: 開始アドレスの文字列（例："A2"）
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets(sheetName) ' 対象のワークシートを指定

    Dim qt As QueryTable
'    Dim filePath As String
'    filePath = "C:\path\to\your\file.txt" ' テキストファイルのパスを指定

    Dim found As Boolean
    found = False

    ' 既存のQueryTableを探す
    For Each qt In ws.QueryTables
        If qt.Connection = "TEXT;" & filePath Then
            found = True
            Exit For
        End If
    Next qt

    If found Then
        ' 既存のQueryTableを更新
        qt.Refresh
        ' 作成済みのクエリを消した後ファイルを再度開かないと、Queryが存在していることになる。
'        Debug.Print ("Refresh Query")
    Else
        ' 新しいQueryTableを追加
        Set qt = ws.QueryTables.Add( _
            Connection:="TEXT;" & filePath, _
            destination:=ws.Range(destination))

        With qt
            .TextFilePlatform = 65001 ' または必要に応じて別のエンコーディング
            .TextFileParseType = xlDelimited
            .TextFileTabDelimiter = True
            .Refresh
        End With
'        Debug.Print ("Create Query")
    End If
End Sub
"""


from excel_data import ExcelSheetDataUtil

from pathlib import Path
print('*外部データ連携済みのテキストを書き換え')
text_path = Path(__file__).parent.joinpath('test_ref.txt')
with open(str(text_path), 'r', encoding='utf-8')as f:
    lines = f.readlines()

# 2行目には数値のみしかない想定
lines[1] = str( int(lines[1].strip()) + 1 ) + '\n'
with open(str(text_path), 'w', encoding='utf-8')as f:
    f.writelines(lines)
print('write text value = {}'.format(lines[1]))

print('*セルを読み取って合計')
# file_name = 'myworkbook.xlsx'
file_name = 'myworkbook.xlsm'
file_path = Path(__file__).parent.joinpath(file_name)
### 書き込み処理するときは念のためバックアップ
import shutil
back_path = Path(__file__).parent.joinpath('back')
back_path.mkdir(exist_ok=True)
shutil.copy(file_path, back_path)
###
sheet_name = 'my sheet'
ex_data = ExcelSheetDataUtil(file_name, sheet_name, data_only=False)

title = '■textファイル参照テスト'
ex_data.set_address_by_find(title, debug=False)
if not ex_data.address_is_valid(ex_data.address):
    raise Exception('Not found value(address={})'.format(ex_data.address))
print('begin_address = {}'.format(ex_data.address))

ex_data.move_address(1,0)
title = ex_data.get_value()
ex_data.move_address(1,0)
value = ex_data.get_value()
print('title, value = {}, {}'.format(title, value))

# print(ex_data.get_value('C1'))
