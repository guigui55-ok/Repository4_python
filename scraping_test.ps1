# VSCodeのパスを指定
$vscodePath = "C:\Users\OK\AppData\Local\Programs\Microsoft VS Code\Code.exe"

# 開きたいディレクトリのパス
$directoryPath = "C:\Users\OK\source\repos\Repository4_python\scraping_test"

# VSCodeでディレクトリを開く
Start-Process -FilePath $vscodePath -ArgumentList $directoryPath
