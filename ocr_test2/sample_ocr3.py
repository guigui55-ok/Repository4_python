

"""
# https://qiita.com/ryome/items/16fc42854fe93de78a23
pip install pytesseract Pillow


Tesseractのインストール
https://github.com/UB-Mannheim/tesseract/wiki
tesseract-ocr-w64-setup-5.3.3.20231005.exe (64 bit)

■ 環境変数にパスを入れる。
C:\Program Files\Tesseract-OCR

"""
from PIL import Image
import pytesseract
# Load the image from file
image_path = '/mnt/data/sample_db_image.png'
image_path = r'C:\Users\OK\Pictures\sample_db_image.png'
image = Image.open(image_path)

# Use tesseract to do OCR on the image
text = pytesseract.image_to_string(image, lang='jpn')

print(text)


"""

Traceback (most recent call last):
  File "C:\Program Files\Python\Python310\lib\site-packages\pytesseract\pytesseract.py", line 255, in run_tesseract
    proc = subprocess.Popen(cmd_args, **subprocess_args())
  File "C:\Program Files\Python\Python310\lib\subprocess.py", line 966, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "C:\Program Files\Python\Python310\lib\subprocess.py", line 1435, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
  File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydev_bundle\pydev_monkey.py", line 901, in new_CreateProcess
    return getattr(_subprocess, original_name)(app_name, cmd_line, *args) 
FileNotFoundError: [WinError 2] 指定されたファイルが見つかりません。      

During handling of the above exception, another exception occurred:       

Traceback (most recent call last):
  File "C:\Program Files\Python\Python310\lib\runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Program Files\Python\Python310\lib\runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy\__main__.py", line 39, in <module>
    cli.main()
  File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy/..\debugpy\server\cli.py", line 430, in main       
    run()
  File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy/..\debugpy\server\cli.py", line 284, in run_file   
    runpy.run_path(target, run_name="__main__")
  File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 321, in run_path
    return _run_module_code(code, init_globals, run_name,
  File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 135, in _run_module_code
    _run_code(code, mod_globals, init_globals,
  File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 124, in _run_code
    exec(code, run_globals)
  File "c:\Users\OK\source\repos\Repository4_python\ocr_test2\sample_ocr3.py", line 21, in <module>
    text = pytesseract.image_to_string(image, lang='jpn')
  File "C:\Program Files\Python\Python310\lib\site-packages\pytesseract\pytesseract.py", line 423, in image_to_string
    return {
  File "C:\Program Files\Python\Python310\lib\site-packages\pytesseract\pytesseract.py", line 426, in <lambda>
    Output.STRING: lambda: run_and_get_output(*args),
  File "C:\Program Files\Python\Python310\lib\site-packages\pytesseract\pytesseract.py", line 288, in run_and_get_output
    run_tesseract(**kwargs)
  File "C:\Program Files\Python\Python310\lib\site-packages\pytesseract\pytesseract.py", line 260, in run_tesseract
    raise TesseractNotFoundError()
pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
PS C:\Users\OK\source\repos\Repository4_python\ocr_test2> 

"""

"""
C:\Users\OK>tesseract --version
tesseract v5.0.0-rc1.20211030
 leptonica-1.78.0
  libgif 5.1.4 : libjpeg 8d (libjpeg-turbo 1.5.3) : libpng 1.6.34 : libtiff 4.0.9 : zlib 1.2.11 : libwebp 0.6.1 : libopenjp2 2.3.0
 Found AVX2
 Found AVX
 Found FMA
 Found SSE4.1
 Found libarchive 3.5.0 zlib/1.2.11 liblzma/5.2.3 bz2lib/1.0.6 liblz4/1.7.5 libzstd/1.4.5
 Found libcurl/7.77.0-DEV Schannel zlib/1.2.11 zstd/1.4.5 libidn2/2.0.4 nghttp2/1.31.0


 
"""