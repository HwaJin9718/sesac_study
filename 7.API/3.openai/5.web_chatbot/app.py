from flask import Flask, request, send_from_directory, jsonify

from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()

app = Flask(__name__)

client = OpenAI()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    print(data)
    # time.sleep(3)
    userInput = data['userInput']
    chatbot_reponse = ask_chatgpt(userInput)

    return jsonify({'response' : f'{chatbot_reponse}'})


# 이전 대화 내용 저장할 공간
history = [] 
# 이런식으로 글로벌 변수로 해서 대화내용을 저장하면 사용자가 많을 때 대화 내용이 섞이고 새로운 사용자가 와도 이전 다른 사용자와의 대화를 인식해서 답변
# 실제로 만들 때는 사용자별로 대화 내용을 분리해서 넣어야 함


def ask_chatgpt(user_input):
    # 문의 내용 history에 저장
    history.append({'role': 'user', 'content' : user_input})

    response = client.chat.completions.create(
        model='gpt-3.5-turbo', # gpt-4o-mini
        # messages = [
        #     {'role': 'user', 'content': user_input}
        # ]
        messages = history,
        temperature=1.0 # 0으로 가까워 질수록 창의성이 줄어듬 -> 딱딱하고 균일화된 답변을 함
        # 만약 내 웹서비스가 의료/법률 관련된 내용이면 0.0 처럼 정확도에 가까운 값을 넣음
        # 작명/소설이라면 창의성이 높은 1.0, 1.1, 1.2 처럼 높이면 됨
    )

    chatgpt_response = response.choices[0].message.content

    # 응답 내용 history에 저장
    history.append({'role': 'assistant', 'content' : chatgpt_response})

    if len(history) > 10:
        # history에 저장될 때에는 고객 문의, GPT 답변 2가지가 저장
        # 그렇기 때문에 삭제할 때 2개씩 삭제되어야 총 대화 개수를 10개로 유지할 수 있다
        history.pop(0) # 가장 오래된 내용 하나 삭제
        history.pop(0) # 가장 오래된 내용 하나더 삭제
        # 리스트 슬라이싱으로도 가능
        # history[2:] # 슬라이싱 문법 [start:stop:step]에서 step이 음수면 역순으로 진행

    print(history)
    print('대화 내용 길이:', len(history))

    return chatgpt_response


if __name__ == '__main__':
    app.run(debug=True)

