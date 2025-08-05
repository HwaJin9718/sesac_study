from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate # 이전까지 배운 것
from langchain_core.prompts import ChatPromptTemplate # 지금부터 배울 것
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.runnables import RunnableLambda

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 1. 프롬프트 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content='You are a naming consultant for new companies'),
    HumanMessage(content='What is a good name for a {company} that makes {product}?')
])

# 아래는 현업에서 많이 쓰는 축약형
# prompt_short = ChatPromptTemplate.from_messages([
#     ('system', 'You are a naming consultant for new companies'),
#     ('human', 'What is a good name for a {company} that makes {product}?'')
# ])

# 2. 모델 생성
llm = ChatOpenAI(model='gpt-3.5-turbo') # chat 모델 중 하나 고르면 됨

# 3. parser 생성
parser = StrOutputParser()

# 4. 입력값 정의하고 invoke로 호출 -> 총 3줄
# message = ''
# response = llm.invoke(message)
# output = parser.invoke(response)

# 위 여러줄의 문장을 LCEL 체이닝으로 처리
# chain = prompt | llm # parser 넣기 전 -> 출력 형태가 긴 형태의 json 형태로 보기 어려움
# 최종결과:  content='"Crafty Creations Co." for a company that makes handmade products.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 15, 'prompt_tokens': 34, 'total_tokens': 49, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-C169QuBDZAmQddBCQ9tvsORhktB9p', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='run--3de7e16a-89fe-4953-8611-fd29c6c1eadc-0' usage_metadata={'input_tokens': 34, 'output_tokens': 15, 'total_tokens': 49, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

# chain = prompt | llm | parser
# 최종결과:  Sure, I'd be happy to help! Can you provide me with more details about the company and the product?

chain = prompt | llm | parser | RunnableLambda(lambda x: {'response': x})

inputs = {'company': 'high-tech startup', 'product': 'electrical automobile'}
result = chain.invoke(inputs)

print('최종결과:', result)



