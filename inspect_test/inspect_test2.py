
# https://qiita.com/ymko/items/b46d32b98f013f06d805
# """
#   File "c:\Users\OK\.vscode\extensions\ms-python.python-2022.16.1\pythonFiles\lib\python\debugpy\__main__.py", line 39, in <module>  
#     cli.main()
# """
import inspect
import os

def location(depth=0):
  frame = inspect.currentframe().f_back
  buf = os.path.basename(frame.f_code.co_filename), frame.f_code.co_name, frame.f_lineno
  return buf

def get_source_info(depth=0):
  frame = inspect.currentframe().f_back
  file = os.path.basename(frame.f_code.co_filename)
  f_name = frame.f_code.co_name
  line = frame.f_lineno
  buf = 'FILE "{}", line {}, in  {}'.format(file, line, f_name)
  return buf

def func1():
  print(get_source_info())

def main():
  print(get_source_info())
  func1()

if __name__ == '__main__':
  main()
  exit(0)