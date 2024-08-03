"""

【Python】PythonでPowerShellのコマンドを利用する
"""

import subprocess

def _test_main():
    cmd = "powershell -Command Get-Date"
    cmd = 'powershell wget https://api.ipify.org'
    cmd = 'powershell torsocks wget https://api.ipify.org'
    cmd = 'torsocks wget https://api.ipify.org'
    # nbtstat -A "IPアドレス"
    ip = '14.9.131.160'
    cmd = 'nbtstat -A "{}"'.format(ip)
    # https://rainbow-engine.com/domain-from-address-revdns/#google_vignette
    # ipアドレス逆引き
    cmd = 'nslookup "{}"'.format(ip)
    proc = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
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
    