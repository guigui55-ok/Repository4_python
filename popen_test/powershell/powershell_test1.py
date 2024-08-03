"""

【Python】PythonでPowerShellのコマンドを利用する
https://qiita.com/Broccolingual/items/7b57824272116a22caf0
"""
import os
def register_task(task_name, batch_path):
    ps_cmd = f"schtasks /create /tn {task_name} /tr {batch_path} /sc onlogon /delay 0000:30 /rl highest"
    os.system(f"powershell -Command {ps_cmd}")

def _test_main():
    cmd = "powershell -Command Get-Date"
    # os.system(cmd)
    print('------')
    import subprocess
    # result = subprocess.check_output([cmd])#Error
    # result = subprocess.Popen(cmd)
    # print(result) #<Popen: returncode: None args: 'powershell -Command Get-Date'>
    print('------')
    proc = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    # logger.info('proc.stdout = {}'.format(proc.stdout))
    # stdoutとstderrを取得
    stdout, stderr = proc.communicate()
    # 結果をログに記録
    if stdout:
        buf = str(stdout).strip()
        print('stdout = {}'.format(buf))
    if stderr:
        print('stderr = {}'.format(stderr))
    print('Done.')

if __name__ == "__main__":
    print('\n*****')
    _test_main()
    