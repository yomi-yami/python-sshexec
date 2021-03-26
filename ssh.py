#!coding: utf-8
# ssh接続で利用するため、pipでもいいがインストール
# >conda install paramiko 

import paramiko
from optparse import OptionParser

# ssh接続しコマンドを実行する。
def exex_ssh(hostname, username, password):
    with paramiko.SSHClient() as ssh:
        # 初回ログイン時に「Are you sure you want to continue connecting (yes/no)?」と
        # きかれても問題なく接続できるように。
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # ssh接続
        ssh.connect(hostname, port=22, username=username, password=password)

        # コマンド実行
        stdin, stdout, stderr = ssh.exec_command('cd ./Docker; ls -al')

        # コマンド実行後に標準入力が必要な場合
        # stdin.write('password\n')
        # stdin.flush()

        # 実行結果を表示
        for o in stdout:
            print('[std]', o, end='')
        for e in stderr:
            print('[err]', e, end='')

def yes_no_input():
    while True:
        choice = input("処理を続行しますか？ [Y/N]: ").lower()
        if choice in ['y']:
            return True
        elif choice in ['n']:
            return False


if __name__ == '__main__':
    parser = OptionParser(usage="%prog <hostname> <username> <password>")
    (options, args) = parser.parse_args()
    if len(args) != 3:
        parser.error("引数が3つではありません。 <hostname> <username> <password>")

    hostname,username,password = args
    # 引数の出力
    print ("lhostname: " + hostname)
    print ("username: " + username)
    print ("password: " + password)
    print ("linuxへssh接続しXXを実行します。")

    if not yes_no_input():
        sys.exit()

    exex_ssh(hostname, username, password)
    # input("Enterキーを押すと終了します")
