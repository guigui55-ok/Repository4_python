# VSCode�̃p�X���w��
$vscodePath = "C:\Users\OK\AppData\Local\Programs\Microsoft VS Code\Code.exe"

# �J�������f�B���N�g���̃p�X
$directoryPath = "C:\Users\OK\source\repos\Repository4_python\scraping_test"

# VSCode�Ńf�B���N�g�����J��
Start-Process -FilePath $vscodePath -ArgumentList $directoryPath
