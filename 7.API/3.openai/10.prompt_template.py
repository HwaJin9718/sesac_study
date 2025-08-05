from langchain_core.prompts import PromptTemplate

template = 'You are a naming consultant. Suggest a name for a company that makes {product}'

prompt = PromptTemplate(
    input_variables=['porduct'],
    template=template
)

filled_prompt = prompt.format(product='icecream')
print(filled_prompt)

filled_prompt = prompt.format(product='cookie')
print(filled_prompt)

filled_prompt = prompt.format(product='smartphone')
print(filled_prompt)

test_products = [
    'mobile games',
    'robot toys',
    'electrical bike',
    'camping goods',
    'programming language education'
]

from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

# llm = OpenAI()
llm = ChatOpenAI()

for product in test_products:
    result = prompt.format(product=product)
    print(f'[{product}] : [{result}]')

    # 미션1. 만들어진 프롬프트를 llm.invoke 로 호출

    # response = llm.invoke(result)

    message = [
        SystemMessage(content='당신은 회사 이름을 창의적으로 잘 만드는 작명가 입니다.'),
        HumanMessage(content=result)
    ]

    response = llm.invoke(message)

    print('생성된 이름 :', response.content.strip('"'))


