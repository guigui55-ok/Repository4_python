@echo off
echo Starting the script...
set "vscodePath=C:\Users\OK\AppData\Local\Programs\Microsoft VS Code\Code.exe"
set "directoryPath=C:\Users\OK\source\repos\Repository4_python\scraping_test"

;echo VSCode Path: %vscodePath%
;echo Directory Path: %directoryPath%

REM start �ɂ��bat�t�@�C���̃v���Z�X�̃o�b�N�O���E���h��vscode�����s�����B
REM �R���\�[������Ă�vscode�͕����Ȃ��B
REM start /B "" "%vscodePath%" "%directoryPath%"
REM start "%vscodePath%" "%directoryPath%" REM�N�����Ȃ�
REM start /min "" "%vscodePath%" "%directoryPath%"
REM start /i "" "%vscodePath%" "%directoryPath%"
start /b "" "%vscodePath%" "%directoryPath%"

;echo VSCode has been launched.
;echo Press any key to exit...
;pause > nul
