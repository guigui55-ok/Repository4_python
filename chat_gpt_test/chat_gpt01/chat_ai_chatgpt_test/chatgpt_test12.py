#APIを外部ファイルに記載して、そこから取得する
import load_chaggpt_settings
api_key = load_chaggpt_settings.chatgpt_settting.get_chat_api_key()

from openai import OpenAI
from openai.types import Completion

client = OpenAI(api_key=api_key)
prompt = 'ChatGPTについて簡単に説明してください。'

completion:Completion = client.completions.create(
    model='curie',
    prompt=prompt)
print(completion.choices[0].text)
print(dict(completion).get('usage'))
print(completion.model_dump_json(indent=2))
