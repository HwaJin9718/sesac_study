from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
import requests
import os
import json

load_dotenv()

app=Flask(__name__)

KAKAO_REST_API_KEY=os.getenv("KAKAO_REST_API_KEY")
KAKAO_CLIENT_SECRET=os.getenv("KAKAO_CLIENT_SECRET")
KAKAO_REDIRECT_URI=os.getenv("KAKAO_REDIRECT_URI")

@app.route('/')
def index():
    kakao_auth_url = {
        # 카카오 로그인 주소 엔드 포인트 확인, 필요한 입력값 확인
    }

    return render_template('index.html')


@app.route('/auth/kakao/callback')
def callback():
    code = request.args.get('code')
    print('코드값 :', code)

    token_url = {
        # 카카오에게 코드 검증 후 토큰 발급받을 엔드포인트 입력 및 입력값 확인
    }

    # 성공했으면? 사용자 정보 요청
    user_info_url = {
        # 사용자 정보 가져오기 위한 엔드 포인트
    }

    user_info = requests.get() # 위의 변수와 인자값들 채워넣기

    # 로그인 성공
    print(user_info)
    return "로그인 성공" # 어디로 보낼지 알아서 처리


@app.route('/profile')
def profile():
    # 위에 내용 다 끝나면 사용자 정보 저장하고 수정하고 등등 기능 추가
    user  = []
    return render_template('profile.html', user=user)


# 로그아웃 추가

if __name__ == '__main__':
    app.run(debug=True)

