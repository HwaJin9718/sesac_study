from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import CommaSeparatedListOutputParser

from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

# 1. 프롬프트 생성기 생성
template = '''
    You are a naming consultant. 
    Suggest 5 creative company names for a {company} that makes {product}
    '''

prompt = PromptTemplate(
    input_variables=['company', 'porduct'],
    template=template
)

# 2. 모델 생성
llm = OpenAI()

# 3. 출력 parser 생성
parser = StrOutputParser()
parser_csv = CommaSeparatedListOutputParser()

# 4. 결과를 도출한다 (위의 생성기들을 연결 prompt -> llm -> output)
inputs = {'company': 'high-tech startup', 'product': 'mobile games'}
filled_prompt = prompt.format(**inputs)
llm_output = llm.invoke(filled_prompt)
print(f'output & csv parser 전\n{llm_output}') # output & csv parser 전

result_str = parser.invoke(llm_output)
result_csv = parser_csv.invoke(llm_output)


print(f'일반 문자열\n{result_str}')
print(f'\n\nCSV 리스트\n{result_csv}')

# 여기까지는 우리가 사용할건 아님 13번 항목 체이닝이 우리가 쓸 것
