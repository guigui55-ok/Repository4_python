import openai
from docopt import docopt

API_KEY = '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'

class AIChat:
    def __init__(self):
        # ※冒頭で作成したopenai の APIキーを設定してください
        openai.api_key = API_KEY

    def response(self, user_input):
        # openai の GPT-3 モデルを使って、応答を生成する
        response = openai.Completion.create(
            engine="text-davinci-002", # text-davinci-003 を指定した方がより自然な文章が生成されます
            prompt=user_input,
            max_tokens=1024,
            temperature=0.5, # 生成する応答の多様性
        )

        # 応答のテキスト部分を取り出して返す
        return response['choices'][0]['text']

def main():

    __doc__ = """
Usage:
    chatgpt.py [--version] [--help]
    chatgpt.py --chat

Options:
    -h --help       ヘルプを表示する。
    --version       バージョンを表示する。
    """

    args = docopt(__doc__)
    # print(args)

    if args['--version']:
        print('AIChat 1.0')
        return

    if args['--chat']:
        # AIChat のインスタンスを作成する
        chatai = AIChat()

        print('>> AIChat: こんにちは、私はchataiです。')

        while True:
            # ユーザーからの入力を受け取る
            user_input = input('>> User: ')

            # ユーザーからの入力が「終了」だった場合にプログラムを終了する
            if user_input == '終了':
                break

            # chataiからの応答を取得する
            response = chatai.response(user_input)
            print('>> AIChat: ' + response)

        print('>> AIChat: いつでもお話ししてくださいね。')


if __name__ == '__main__':
    main()