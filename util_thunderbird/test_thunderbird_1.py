import mailbox



import thunderbird_my_setting
def _test():
    mbox_str = "プロファイルフォルダ名/Mail/メールサーバ名/Inbox"
    mbox_str = thunderbird_my_setting.get_thunderbird_mailbox_root_path()
    mail_box = mailbox.mbox(mbox_str + '/Inbox')

    count = 0
    #各メッセージ毎にループする
    #Mailboxクラスのkeys()関数を呼び出してメッセージのキーのリストを受け取り、ループ。
    print('mail_box.keys().length = {}'.format(mail_box.keys().__len__()))
    for key in mail_box.keys():
        a_msg = mail_box.get(key)
        from_str = a_msg.get_from()
        print('[{}]={}, {}, {}'.format(count, key, from_str, a_msg.__len__()))
        head_str = _decode_header(a_msg)
        print('head_str = {}'.format(head_str))
        msg_str = get_message(a_msg)
        print('msg_str = {}'.format(msg_str))
        count+=1
        if count==1:
            print('mail_box type = {}'.format(mail_box.__class__))
            print('a_msg type = {}'.format(a_msg.__class__))
        if 2 < count:
            break

from email.header import decode_header
def _decode_header(a_msg:mailbox.mboxMessage):
    usbj = ''
    for bstr,enc in decode_header(a_msg['Subject']) :
        if enc == None:
            usbj += bstr.decode("ascii", "ignore")
        else:
            usbj += bstr.decode(enc, "ignore")
    return usbj


def get_message(a_msg:mailbox.mboxMessage):
    for aa_msg in a_msg.walk():
        if not 'text' in aa_msg.get_content_type():
            continue #"text"パートでなかったら次のパートへ
        if aa_msg.get_content_charset() :
            a_text = aa_msg.get_payload(decode=True).decode(aa_msg.get_content_charset(), "ignore")
        else:
            if "charset=shift_jis" in str(aa_msg.get_payload(decode=True)):
                #ひとまず シフトJISだけ特別対応。
                a_text = aa_msg.get_payload(decode=True).decode("cp932", "ignore")
            else:
                print ("** Cannot decode.Cannot specify charset ***" + aa_msg.get("From"))
                continue
    return a_text


if __name__ == '__main__':
    print(' ***** ')
    _test() 