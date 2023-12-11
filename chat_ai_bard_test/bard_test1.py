import os
from bardapi import Bard
from dotenv import load_dotenv

print()
print('*****')

load_dotenv()

token = os.environ['COOKIE_TOKEN']
print('token = {}'.format(token))
bard = Bard(token=token)
prompt="LLMとはなんですか?"
response = bard.get_answer(prompt)['content']
print(response)