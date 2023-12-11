import openai

# APIキーの設定
openai.api_key = 'your-api-key'

# ChatGPTモデルを使用してテキストを生成する
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # 使用するモデルを指定
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ]
)

# 応答の出力
print(response.choices[0].message['content'])