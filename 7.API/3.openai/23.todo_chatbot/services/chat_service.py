import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from services import todo_service as todo
import json
from collections import deque

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("API키가 없습니다!!")

# 1. 템플릿 정의
system_template1 = '''
당신은 사용자의 TODO 리스트를 관리해주는 비서입니다.
사용자의 TODO 항목과 질문에 대해서 간결하게 답변해주세요.

[할 일 목록]
{my_todo_list}
'''

system_template2 = """
당신은 사용자의 TODO 리스트를 관리해주는 비서입니다. 
사용자의 TODO 항목과 질문에 대해서 최대한 이모티콘을 많이 사용해서 포악한 동물처럼 어흥~ 또는 멍멍~  형태로 답변해 주세요. 

[할 일 목록]
{my_todo_list}
"""  

system_template3 = """
당신은 사용자의 TODO 리스트를 관리해주는 비서입니다.
당신은 사용자의 질문에 대해서 아래중에 하나를 골라서 action을 선택하고 답변해야 합니다.
사용자의 TODO 항목과 질문에 대해서 간결하게 답변해주세요.

[출력 형식]
{{"action": "add", "item": [항목]}} - 할일을 추가해야 할 때
{{"action": "delete", "item": [항목], "id": [todo 번호]}} - 할일을 안할꺼거나, 잘못 추가했을때
{{"action": "update", "item": [항목], "id": [todo 번호]}} - 할일을 다했거나, 다한일을 다시 해야 할 때
{{"action": "list"}} - 할일을 보여줘야 할 때
{{"action": "nothing"}} - 어떻게 판단해야할지 모를때 또는 TODO 리스트와는 쓸대없는 질문이 들어왔을때

[할 일 목록]
{my_todo_list}
"""

system_template = system_template3
user_template = '{userInput}'
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(user_template)
])

# 2. 모델 정의
llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.7,
    api_key=API_KEY
)

# 3. parser 생성
parser = StrOutputParser()

# 4. 체인 생성
chain = prompt | llm | parser | RunnableLambda(lambda x: x.strip())

# 최대 10개까지 담을 수 있는 자료 구조
HISTORY = deque(maxlen=10) # -> 우리가 history > 10 이런 구조 안써도 됨


def store_history(role, content):
    HISTORY.append({'role': role, 'content' : content})


# gpt 요청 시 prompt랑 history를 같이 보낼 수 있게 해주는 함수
def build_prompt_messages(my_todo_list, userInput):
    """ChatOpenAI용 메시지 리스트 생성"""
    # 시스템 메시지 (TODO 리스트 포함)
    system_content = system_template.format(my_todo_list=my_todo_list)
    prompt = [SystemMessage(content=system_content)]
    
    # 히스토리 추가 
    for hist in HISTORY:
        if hist['role'] == 'user':
            prompt.append(HumanMessage(content=hist['content']))
        elif hist['role'] == 'assistant':
            prompt.append(AIMessage(content=hist['content']))
    
    # 현재 사용자 입력 추가
    prompt.append(HumanMessage(content=userInput))
    
    return prompt


def handle_chatgpt(userInput):

    store_history('user', userInput) # 사용자 저장

    action = ask_chatgpt(userInput)
    result = do_action(action)

    store_history('assistant', result) # 챗봇 응답 저장

    return result


def ask_chatgpt(userInput):
    # print('ask 함수 진입')
    my_todo_list = todo.get_all()

    # history 없는 버전
    # response = chain.invoke({'my_todo_list': my_todo_list, 'userInput': userInput})
    # print('봇 응답값 :', response)

    # action = json.loads(response)
    # print(my_action['action'])
    

    # HISTORY가 포함된 메시지 리스트 생성 -> LangChain 제외
    messages = build_prompt_messages(my_todo_list, userInput) # history 포함된 prompt 생성
    response = llm.invoke(messages) # messages를 넣고 gpt 답변 받기

    # 응답을 파싱하여 JSON으로 변환
    parsed_response = parser.invoke(response).strip() # 받은 답변을 parser를 사용하여 변환
    action = json.loads(parsed_response)

    return action


def do_action(resp_action):
    # print('action 함수 진입')

    action = resp_action.get('action')
    item = resp_action.get('item')
    id = resp_action.get('id')

    result = ''

    if action == 'add':
        # print('add')
        todo_item = {'textInput' : item}
        response = todo.add(todo_item)

        if response:
            result = f"{item}이/가 정상적으로 등록되었습니다."
        else:
            result = f"{item} 등록이 실패했습니다."

    elif action == 'delete':
        # print('delete')
        response = todo.delete(id)

        if response:
            result = f"{item}을/를 삭제했습니다."
        else:
            result = f"{item} 삭제를 실패했습니다."

    elif action == 'list':
        # print('list')
        todos = todo.get_all_to_chat()

        if todos:
            result = f"다음 할 일 들이 있습니다.\n{todos}"
        else:
            result = f"오늘 할 일이 없습니다. 등록해주세요."

    elif action == 'update':
        # print('update')
        response = todo.modify(id)

        if response:
            result = f"{item}을/를 수정했습니다."
        else:
            result = f"{item} 수정을 실패했습니다."

    else:
        result = "잘 이해하지 못했습니다. 다시 한번 말씀해 주세요."

    return result

