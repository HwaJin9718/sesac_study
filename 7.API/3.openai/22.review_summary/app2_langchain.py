from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify

from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

app = Flask(__name__, static_folder='public', static_url_path='')

# 1. 템플릿 정의 -> 프롬프트 템플릿 만들기
# 리뷰 요약
summary_template = '다음 리뷰목록을 기반으로 간결하게 한줄로 요약해 주세요.\n\n {reviews_text}'
summary_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('당신은 문장 요약 전문가입니다.'),
    HumanMessagePromptTemplate.from_template(summary_template)
])

# 리뷰 번역
translate_template = '다음 한국어 요약 리뷰를 {language}로 번역해 주세요. 대신 {language}가 한국어인 경우에는 리뷰 내용을 출력해주세요.\n\n요약 리뷰: {summary}'
translate_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('당신은 문장 번역 전문가입니다.'),
    HumanMessagePromptTemplate.from_template(translate_template)
])

# 강사님꺼
# summary_prompt = PromptTemplate.from_template(
#     """다음 목록을 기반으로 간결한 요약을 작성하시오.

# 리뷰목록:
# {reviews_text}
# """
# )

# translate_prompt = PromptTemplate.from_template(
#     """다음 한국어 문장을 기반으로 {target_lang_name} 으로 번역하시오.
    
# {summary_ko}
# """
# )


# 2. 모델 정의
llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.7
)

# 3. 체인 생성
summary_chain = summary_prompt | llm | RunnableLambda(lambda x: x.content.strip())
translate_chain = translate_prompt | llm | RunnableLambda(lambda y: y.content.strip())

# 강사님
# summary_chain = summary_prompt | llm
# translate_chain = translate_prompt | llm

# 최종 원하는 체인 -> 한가지 체인으로 다 할 수 있는것!! -> 지금은 요약 따로 번역 따로 체인 구성
# summary_then_translate_chain = (
#     {"summary_ko": summary_prompt | llm | RunnableLambda(lambda m: m.content),
#      "target_lang_name": RunnablePassthrough() }
#     #  "target_lang_name": RunnableLambda(lambda x: x["target_lang_name"]) }
#     | translate_prompt
#     | llm
#     | RunnableLambda(lambda m: m.content)
# )

reviews = []

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    rating = data.get('rating')
    opinion = data.get('opinion')
    print(f'점수 : {rating}, 리뷰 : {opinion}')

    reviews.append({'rating': rating, 'opinion' : opinion})

    return jsonify({'message' : '성공적으로 저장됨'})


@app.route('/api/reviews', methods=['GET'])
def get_review():
    return jsonify({'reviews': reviews})


@app.route('/api/ai-summary', methods=['GET'])
def get_ai_summary():

    if not reviews:
        return jsonify({'summary': '리뷰가 없습니다.', 'averageRating' : 0.0})
    
    average_rating = sum(r['rating'] for r in reviews) / len(reviews)
    reviews_text = '/n'.join([f"별점: {r['rating']}, 내용: {r['opinion']}" for r in reviews])
    print('리뷰내용 통합: ', reviews_text)
    
    target_lang = request.args.get('lang', 'ko')
    print('언어: ', target_lang)

    languages = [
        {'id': 'ko', 'lang': '한국어'},
        {'id': 'en', 'lang': '영어'},
        {'id': 'ja', 'lang': '일본어'},
        {'id': 'zh', 'lang': '중국어'},
        {'id': 'fr', 'lang': '프랑스어'},
        {'id': 'it', 'lang': '이탈리아어'}
    ]

    language = ''
    for lang in languages:
        if target_lang == lang['id']:
            language = lang['lang']

    print('확인된 언어 :', language)

    # 리뷰 요약
    summary_response = summary_chain.invoke({'reviews_text': reviews_text})
    # summary_response = summary_chain.invoke({'reviews_text': reviews_text}).content
    print('요약리뷰내용: ', summary_response)

    # 리뷰 번역
    translate_response = translate_chain.invoke({'language' : language, 'summary' : summary_response})
    # translate_response = translate_chain.invoke({'language' : language, 'summary' : summary_response}).content
    print('번역 요약리뷰내용: ', translate_response)

    # 한번에 두가지를 체이닝해서 호출하기
    # response_translated = summary_then_translate_chain.invoke({
    #     "reviews_text": reviews_text,
    #     "target_lang_name": lang_name
    # })

    return jsonify({'summary': translate_response, 'averageRating': average_rating})


if __name__ == '__main__':
    app.run(debug=True)

