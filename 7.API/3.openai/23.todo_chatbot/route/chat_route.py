from flask import Blueprint, request, jsonify

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

chat_api = Blueprint('chat', __name__)

# 1. 템플릿 정의
template = '{userInput}'
prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(template)
])

# 2. 모델 정의
llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.7
)

# 3. parser 생성
parser = StrOutputParser()

# 4. 체인 생성
chain = prompt | llm | parser | RunnableLambda(lambda x: x.strip())


@chat_api.route('/', methods=['POST'])
def sk_chatgpt():
    userInput = request.get_json()['userInput']
    print('사용자 입력값 :', userInput)

    response = chain.invoke({'userInput': userInput})
    print('봇 응답값 :', response)

    return jsonify({'response': response})

