#APIを外部ファイルに記載して、そこから取得する
import load_chaggpt_settings
api_key = load_chaggpt_settings.chatgpt_settting.get_chat_api_key()

import openai
from openai.types import Completion

# APIキーの設定
openai.api_key = 'your-api-key'

# テキスト生成のためのリクエストを作成
response = openai.Completion.create(
    model="text-davinci-003",  # 使用するモデルを指定（最新のモデル名に合わせてください）
    prompt="Tell me a joke.",   # 生成させたいテキストのプロンプト
    max_tokens=50               # 生成するトークンの最大数
)

# 応答の出力
print(response.choices[0].text)