
import os


remote_host = os.getenv('REMOTE_HOST')
print('remote_host = {}'.format(remote_host))


import socket

def print_remote_machine_info(remote_host):
    """
    リモートのIPアドレスを表示する
    """
    #https://hiron.hatenablog.jp/entry/2014/07/18/112858
    try:
        print("IP address: %s" % socket.gethostbyname(remote_host))
    except Exception as e:
        print("%s: %s" % (remote_host, e))


if __name__ == '__main__':
    print_remote_machine_info(remote_host='www.google.co.jp')

    # https://qiita.com/tatsuya-k_net/items/666b0f39c14b8cbd4417
    import requests
    ip = '14.9.131.160'
    # ホスト名取得
    host = socket.gethostname()
    print('hostname: ' + host)

    # ローカルIPアドレスを取得
    pip = socket.gethostbyname(host)
    print('pip: ' + pip)  # 192.168.○○○.○○○

    # グローバルIPアドレスを取得
    gip = requests.get('https://ifconfig.me').text
    print('gip: ' + gip)  # グローバルIPアドレス
