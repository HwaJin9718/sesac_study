from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

from langchain_openai import OpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 1. 템플릿 정의
template = '다음 수신자에게 주제의 내용에 해당하는 회사의 공식 이메일 형태로 작성해주세요.\n\n수신자: {recipient}\n\n주제: {topic}'
prompt = PromptTemplate(input_variables=['recipient', 'topic'], template=template)

# 2. 모델 정의
# 메일을 작성하는 것이니 창의력이 높아도 괜춘
# max_tokens은 기본값이 256 -> 메일 본문이 길어질 수 있으니 max_tokens 수정
llm = OpenAI(temperature=1.0, max_tokens=1000) 

# 3. 체인 생성
chain = prompt | llm
# chain = prompt | llm | StrOutputParser()

# 4. 입력 및 호출
input_text = {
    # 'recipient' : '마케팅팀', 'topic' : '신제품 출시를 위한 전략'
    # 'recipient' : '인사팀', 'topic' : '버그를 많이 만드는 개발자 해고'
    'recipient' : 'CEO', 'topic' : '회사의 중요 인재인 개발자를 해고시킨 인사팀장 해고'
}

result = chain.invoke(input_text)
print('최종결과 : ', result)

