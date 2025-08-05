import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI()

history = []

def ask_chatgpt(user_input):
    # 페르소나 - 가상의 인물을 만들어서, 그 역할을 시킴

    # 프롬프트 설정
    # gpt_systemprompt = {'role':'system', 'content': 'You are a helpful assistant.'}
    # gpt_systemprompt = {'role':'system', 'content': '당신은 사용자의 질문에 잘 답변을 해주는 챗봇입니다.'}
    # gpt_systemprompt = {'role':'system', 'content': '당신은 일급 호텔의 요리사 입니다.'}
    gpt_systemprompt = {'role':'system', 'content': '당신은 동내 분식집의 주방장 입니다.'}

    gpt_question = {'role' : 'user', 'content' : user_input}

    if (len(history) == 0):
        history.append(gpt_systemprompt)

    history.append(gpt_question)
    print('----- 실제로 우리가 GPT에게 던지는 메시지 ------\n----- 질문 시작 -----\n')
    print(history)
    print('----- 대화 내용 -----')

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages = history,
        temperature=1.0
    )

    gpt_response = {'role' : 'assistant', 'content' : response.choices[0].message.content}
    history.append(gpt_response)

    return gpt_response['content']

while True:
    user_input = input('[YOU] : ')

    if user_input in ['exit', 'quit', '종료', '그만', '끝']:
        print('대화를 종료합니다.')
        break

    print('[챗봇응답] : ', ask_chatgpt(user_input))
