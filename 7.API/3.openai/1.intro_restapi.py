from dotenv import load_dotenv
import os
import requests

load_dotenv()

OPEN_API_KEY = os.getenv('OPENAI_API_KEY')

# 기본 질문
response = requests.post('https://api.openai.com/v1/responses', 
              json={
                  'model' : 'gpt-4o',
                #   'input' : 'Write a one-sentence bedtime story about a unicorn'
                  'input' : '잠자리에 들기 전에 양에 대해 스토리를 한문장 말해주시오.'
              }, 
              headers={
                  'Content-Type' : 'application/json',
                  'Authorization' : f'Bearer {OPEN_API_KEY}',
              }
            )

response_data = response.json()

# response_data > output > content > text

# output = response_data['output']
# content = output[0]
# content = content['content']
# text = content[0]
# text = text['text']
# print(text)

print(response_data['output'][0]['content'][0]['text'])


# 채팅?
response = requests.post('https://api.openai.com/v1/chat/completions', 
              json={
                  'model' : 'gpt-4o',
                  'messages' : [
                    #   {'role': 'user', 'content': '잠자리에 들기 전에 양에 대해 스토리를 한문장 말해주시오.'}
                      {"role":"user", "content": "어떤 옵션이 있다고?? 다시 말해줘"}
                  ]
              }, 
              headers={
                  'Content-Type' : 'application/json',
                  'Authorization' : f'Bearer {OPEN_API_KEY}',
              }
            )

response_data = response.json()
print(response_data['choices'][0]['message']['content'])
