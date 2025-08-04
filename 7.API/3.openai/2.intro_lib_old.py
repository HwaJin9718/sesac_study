# 구버전 설치 : pip install openai==0.28 
# 삭제 : pip uninstall openai
# pip install openai
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = openai_api_key

# 이건 구버전 코드 0.28
# openai.ChatCompletion 이라고 출발하는 사이트는 일단 보지말기!
# 매우 구버전 API로 지금은 동작 X (openai==0.3.0 이전의 문법)
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages = [
        {'role' : 'user', 'content' : '아무말이나 적어봅시다.'}
    ]
)

print(response['choices'][0]['message']['content'])
