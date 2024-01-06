

import pytesseract
from pathlib import Path

image_path = r'C:\Users\OK\Pictures\sample_db_image.png'
if not Path(image_path).exists():
    raise FileNotFoundError(image_path)

try:
    print(pytesseract.image_to_string(image_path))  # 'example.png'は存在している画像ファイル名に置き換えてください
except pytesseract.TesseractError as e:
    print(e)

# """

# Traceback (most recent call last):
#   File "C:\Program Files\Python\Python310\lib\site-packages\pytesseract\pytesseract.py", line 255, in run_tesseract
#     proc = subprocess.Popen(cmd_args, **subprocess_args())
#   File "C:\Program Files\Python\Python310\lib\subprocess.py", line 966, in __init__
#     self._execute_child(args, executable, preexec_fn, close_fds,
#   File "C:\Program Files\Python\Python310\lib\subprocess.py", line 1435, in _execute_child
#     hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
#   File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydev_bundle\pydev_monkey.py", line 901, in new_CreateProcess
#     return getattr(_subprocess, original_name)(app_name, cmd_line, *args) 
# FileNotFoundError: [WinError 2] 指定されたファイルが見つかりません。      

# During handling of the above exception, another exception occurred:       

# Traceback (most recent call last):
#   File "C:\Program Files\Python\Python310\lib\runpy.py", line 196, in _run_module_as_main
#     return _run_code(code, main_globals, None,
#   File "C:\Program Files\Python\Python310\lib\runpy.py", line 86, in _run_code
#     exec(code, run_globals)
#   File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy\__main__.py", line 39, in <module>
#     cli.main()
#   File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy/..\debugpy\server\cli.py", line 430, in main       
#     run()
#   File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy/..\debugpy\server\cli.py", line 284, in run_file   
#     runpy.run_path(target, run_name="__main__")
#   File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 321, in run_path
#     return _run_module_code(code, init_globals, run_name,
#   File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 135, in _run_module_code
#     _run_code(code, mod_globals, init_globals,
#   File "c:\Users\OK\.vscode\extensions\ms-python.python-2023.22.1\pythonFiles\lib\python\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 124, in _run_code
#     exec(code, run_globals)
#   File "c:\Users\OK\source\repos\Repository4_python\ocr_test2\check_tesseract.py", line 11, in <module>
#     print(pytesseract.image_to_string(image_path))  # 'example.png'は存在 
# している画像ファイル名に置き換えてください
#   File "C:\Program Files\Python\Python310\lib\site-packages\pytesseract\pytesseract.py", line 423, in image_to_string
#     return {
#   File "C:\Program Files\Python\Python310\lib\site-packages\pytesseract\pytesseract.py", line 426, in <lambda>
#     Output.STRING: lambda: run_and_get_output(*args),
#   File "C:\Program Files\Python\Python310\lib\site-packages\pytesseract\pytesseract.py", line 288, in run_and_get_output
#     run_tesseract(**kwargs)
#   File "C:\Program Files\Python\Python310\lib\site-packages\pytesseract\pytesseract.py", line 260, in run_tesseract
#     raise TesseractNotFoundError()
# pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
# """