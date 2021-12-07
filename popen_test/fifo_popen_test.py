from sys import tracebacklimit
import time
import subprocess
from subprocess import PIPE
import traceback
from types import TracebackType

# # named_pipeという名前の名前付きパイプを作成
# $ mkfifo named_pipe

# def popen_test():
#     try:
#         s = 'aiueo'
#         proc = subprocess.Popen("cat {} | cat -n; sleep 60".format('named_pipe'), shell=True, stdout=PIPE, stderr=PIPE, text=True)
#         with open('named_pipe', 'w') as fifo:
#             fifo.write(s)

#         # サブプロセスが処理終わるまでの間に、並列で別の重い処理
#         time.sleep(30)

#         # サブプロセスの完了を待つ
#         result = proc.communicate()
#         (stdout, stderr) = (result[0], result[1])
#         print('STDOUT: {}'.format(stdout)
#         # STDOUT:  1  aiueo
#     except:
#         print(traceback.print())
