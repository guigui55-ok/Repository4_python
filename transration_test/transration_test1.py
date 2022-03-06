"""
https://plog.shinmaiblog.com/python-translator/
バージョンが4.0.0-rc1以上

googletransの動作を確認しました。注意点は以下のとおりです。

テキストは最大15kまで
Google翻訳の制限に依存し、このライブラリはいつでも利用可能とは限らない
安定性が必要な場合は有料のGoogle’s official translate APIを使いましょう

pip install googletrans==4.0.0-rc1
"""

from googletrans import Translator

def main():
    try:
        translator = Translator()
        print(translator.translate('Blühe, deutsches Vaterland'))
        print(translator.translate('Blühe, deutsches Vaterland', dest='ja'))
        # Translated(src=de, dest=en, text=Blossom, German fatherland, pronunciation=Blossom, German fatherland)
        translator = Translator()
        message = translator.translate('This is a pen.', src='en', dest='ja')
        print(message.text)
    except:
        bar='######################################################################'
        print(bar)
        import traceback
        traceback.print_exc()

main()
