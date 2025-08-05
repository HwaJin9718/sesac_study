from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify

from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

app = Flask(__name__)

llm1 = OpenAI(temperature=1.3)
llm2 = ChatOpenAI(temperature=0.9)


# Completion 모델
# 실행 명령어 : 
# curl -X POST http://127.0.0.1:5000/api/name -H "Content-Type: application/json" -d "{\"product\": \"laptop\"}"
# curl -X POST 127.0.0.1:5000/api/name -H "Content-Type: application/json" -d "{\"product\": \"laptop\"}"
@app.route('/api/name', methods=['POST'])
def generate_name():
    data = request.get_json()
    product = data.get('product', None)

    # prompt = f'What is a good company name that makes {product}?'
    # 각자 프롬프트를 잘 만들어서, 언제나 한글 회사명으로 1개만 주어지게 한다.
    # prompt = f'판매하는 상품({product})을 보고 그에 어울리는 회사명을 1개 만들어줘. 단, 회사명은 한글로 만들어줘야 해.'
    # prompt = f'판매하는 상품({product})을 보고 그에 어울리는 회사명을 1개 만들어줘.'
    prompt = f"다음 상품을 만드는 창의 적인 회사 이름을 1개만 작성해줘. 상품명: {product}"

    result = llm1.invoke(prompt)
    names = result.strip()

    return jsonify({'product': product, 'name': names})


# chat 모델
# 실행 명령어 : 
# curl -X POST http://127.0.0.1:5000/api/name2 -H "Content-Type: application/json" -d "{\"product\": \"laptop\"}"
# curl -X POST 127.0.0.1:5000/api/name2 -H "Content-Type: application/json" -d "{\"product\": \"laptop\"}"
@app.route('/api/name2', methods=['POST'])
def generate_name2():
    data = request.get_json()
    product = data.get('product', None)

    # prompt = f'판매하는 상품({product})을 보고 그에 어울리는 회사명을 1개 만들어줘. 단, 회사명은 한글로 만들어줘야 해.'
    # prompt = f'판매하는 상품({product})을 보고 그에 어울리는 회사명을 1개 만들어줘.'
    prompt = f"다음 상품을 만드는 창의 적인 회사 이름을 1개만 작성해줘. 상품명: {product}"

    messages = [
        SystemMessage(content='당신은 회사 이름을 창의적으로 잘 만드는 작명가 입니다.'),
        HumanMessage(content=prompt)
    ]

    result = llm2.invoke(messages)
    names = result.content.strip('"')

    return jsonify({'product': product, 'name': names})


if __name__ == '__main__':
    app.run(debug=True)

