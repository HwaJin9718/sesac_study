# pip install langchain -> 기본
# openai 사 모델과 연동 : langchain_openai -> pip install langchain_openai
# claude 사 모델과 연동 : langchain_claude -> pip install langchain_claude
# gemini 사 모델과 연동 : langchain_gemini -> pip install langchain_gemini

import os
from dotenv import load_dotenv

# from langchain.llms import OpenAI # 구버전 API 호출
from langchain_openai import OpenAI # 신버전 API

load_dotenv()

# llm = OpenAI(api_key=api_key) # 우리는 기본값을 넣어서 쓸거라 api key 넣지 않아도 됨
# llm = OpenAI() # 기본값

# gpt-3.5-turbo-instruct가 기본값 -> 2024.01
# text-davinci-003 -> deprecated 된 모델 2024.01 -> 한마디로 이전에 사용하던것, 이전에 발행된 책을 보면 해당 내용으로 나와얐음

# gpt-3.5-turbo-instruct -> 시키는 모델, 문장 완성형 모델
# gpt-3.5-turbo -> 채팅, 사용자와 인터렉션, QA 모델


# print(llm) # 만들어 놓은 모델 (기본 모델) 출력
# Params: {'model_name': 'gpt-3.5-turbo-instruct', 'temperature': 0.7, 'top_p': 1, 'frequency_penalty': 0, 'presence_penalty': 0, 'n': 1, 'seed': None, 'logprobs': None, 'max_tokens': 256}


# prompt = '오늘 점심에 먹을 메뉴는'
# result = llm.invoke(prompt)
# print(result)


llm = OpenAI(max_tokens=1000) # 최대 답변 token을 1000개로 설정 , 단어랑 토근은 다른거!!

prompt = '인공지능이란'
result = llm.invoke(prompt)
print(result)
