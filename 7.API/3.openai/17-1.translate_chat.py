from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.runnables import RunnableLambda

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 1. 템플릿 정의
prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 변역을 잘 해주는 챗봇 입니다.'),
    ('human', '다음 문장을 영어로 번역하시오\n\n{article}')
])

# 2. 모델 정의
# 너무 창의력이 뛰어나면 아무래도 요약에 대한 정확성이 떨어지니
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.5) 

# 3. parser 생성
parser = StrOutputParser()

# 4. 체인 생성
chain = prompt | llm | parser | RunnableLambda(lambda x: {'translated': x})

# 5. 입력 및 호출
input_text = {
    'article' : '''
    - 애플, 아이폰17 프로 라인업 출시 예정
    - 고성능 이미지 센서, AI 최적화 업그래이드
    - 자 사 설계 커스텀 이미지 센서 도입, 최대 20스톱 다이내믹레인지 구현
    '''
}

result = chain.invoke(input_text)
print('최종결과 : ', result)

