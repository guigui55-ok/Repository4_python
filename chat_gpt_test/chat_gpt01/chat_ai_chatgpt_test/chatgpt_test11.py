
import load_chaggpt_settings
api_key = load_chaggpt_settings.chatgpt_settting.get_chat_api_key()
# import os
# api_key = os.environ['OPENAI_API_KEY']

from openai import OpenAI
from openai.types import Completion

client = OpenAI(
  api_key=api_key,  # this is also the default, it can be omitted
)

prompt = 'ChatGPTについて簡単に説明してください。'

completion:Completion = client.completions.create(
    model='curie',
    prompt=prompt)
print(completion.choices[0].text)
print(dict(completion).get('usage'))
print(completion.model_dump_json(indent=2))

# # 非同期クライアント
# from openai import AsyncOpenAI

# client = AsyncOpenAI()
# completion = await client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

import openai
openai.api_key = api_key
# all client options can be configured just like the `OpenAI` instantiation counterpart
openai.base_url = "https://..."
openai.default_headers = {"x-foo": "true"}

completion = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.choices[0].message.content)

# このライブラリをAzure OpenAIで使用するには、クラスAzureOpenAIの代わりにクラスを使用しますOpenAI