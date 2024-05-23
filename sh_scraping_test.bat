@echo off
echo Starting the script...
set "vscodePath=C:\Users\OK\AppData\Local\Programs\Microsoft VS Code\Code.exe"
set "directoryPath=C:\Users\OK\source\repos\Repository4_python\scraping_test"

;echo VSCode Path: %vscodePath%
;echo Directory Path: %directoryPath%

REM start によりbatファイルのプロセスのバックグラウンドでvscodeが実行される。
REM コンソールを閉じてもvscodeは閉じられない。
REM start /B "" "%vscodePath%" "%directoryPath%"
REM start "%vscodePath%" "%directoryPath%" REM起動しない
REM start /min "" "%vscodePath%" "%directoryPath%"
REM start /i "" "%vscodePath%" "%directoryPath%"
start /b "" "%vscodePath%" "%directoryPath%"

;echo VSCode has been launched.
;echo Press any key to exit...
;pause > nul
