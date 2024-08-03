buf = r'I:/BACKUP\\bkup220502\\ZMyFolder\\newDoc\\新しいDOC\\PC系IT系\\2019 企画-開発\\要件定義\\新しいフォルダー\\新しいフォルダー\\'

buf = buf.replace("\\\\", "\\")
buf = buf.replace(':/', ':\\')
buf = buf.replace('\n', '')

print()
print('\n*****')
print(buf)