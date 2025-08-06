from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify
from openai import OpenAI

load_dotenv()

# app = Flask(__name__, static_folder='static', static_url_path='static') 
# 우리는 public으로 폴더명을 작성 -> 기본이 static 이기 때문에 폴더 명시
# 파일을 호출할 때 static으로 불러와야 하는데 그거 안하려고 url 없앰
app = Flask(__name__, static_folder='public', static_url_path='')

# openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
# 위처럼 불러와도 됨 우리는 기본값 쓸거라 그냥 하기처럼 쓴거
openai = OpenAI()

# 사용자 후기를 저장할 DB
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


# 미션1. 리뷰 내용을 백엔드에 저장하고 프론트에 불러와서 DOM에 하나하나 랜더링하면서 그려준다
# 미션2. /api/ai-summary에 요청을 하면, 그때 요약을 시킨다
@app.route('/api/reviews', methods=['GET'])
def get_review():
    return jsonify({'reviews': reviews})


@app.route('/api/ai-summary', methods=['GET'])
def get_ai_summary():
    target_lang = request.args.get('lang', 'ko')
    print('언어: ', target_lang)

    # 미션1. front에서 보낸 언어 '코드값'으로 원하는 언어 매핑
    # 미션2. 그걸 기반으로 GPT에게 해당 언어로 요약 요청
    #       하나의 프롬프트로 할지, 아니면 두번의 스탭으로 나눠서(1. 요약, 2. 번역) 할지 고민

    if not reviews:
        return jsonify({'summary': '리뷰가 없습니다.', 'averageRating' : 0.0})
    
    average_rating = sum(r['rating'] for r in reviews) / len(reviews)
    reviews_text = '/n'.join([f"별점: {r['rating']}, 내용: {r['opinion']}" for r in reviews])

    print('리뷰내용 통합: ', reviews_text)

    # 리뷰 요약
    # try catch 로 오류 체크 필요, key가 없거나, 돈이 떨어졌거나, 서버가 죽었거나, 등등 이유로 요청에 실패할수 있음.
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{
            'role': 'user',
            'content': f'다음 리뷰목록을 기반으로 간결하게 한줄로 요약해 주세요.\n\n {reviews_text}'
        }] # 어떻게 이문장을 잘 만들것이냐? -> 이게 프롬프트 엔지니어링
    )

    summary = response.choices[0].message.content.strip()
    print('요약리뷰내용: ', summary)

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

    # 리뷰 번역
    lang_response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{
            'role': 'user',
            'content': f'다음 요약 리뷰를 다음 언어로 번역해 주세요.\n\n언어: {language} \n\n요약리뷰: {summary}'
        }],
        temperature=0.2
    )

    lang_summary = lang_response.choices[0].message.content.strip()
    print('번역 요약리뷰내용: ', lang_summary)

    return jsonify({'summary': lang_summary, 'averageRating': average_rating})


if __name__ == '__main__':
    app.run(debug=True)

