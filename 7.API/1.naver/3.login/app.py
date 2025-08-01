from flask import Flask, render_template, redirect, request, session, url_for
from dotenv import load_dotenv
import os
import requests
# request : 클라이언트가 나한테 요청할 때 값을 담아오는 것
# requests : 내가 다른 서버에 요청을 보낼 때

# TODO: sqlite 와 연동해서.. 사용자 정보 저장하기..

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SESSION_SECRET")

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")
NAVER_REDIRECT_URI = os.getenv("NAVER_REDIRECT_URI")

@app.route('/')
def index():
    user = session.get('user')
    return render_template('index.html', user=user)


# 내 사이트에서 네이버 로그인 시도 시 진행
@app.route('/login/naver/')
def login_naver():

    # 실제 네이버 로그인 인증 할 주소
    auth_url = (
        f"https://nid.naver.com/oauth2.0/authorize?"
        f"response_type=code&client_id={NAVER_CLIENT_ID}"
        f"&redirect_uri={NAVER_REDIRECT_URI}&state=xyz"
    )

    return redirect(auth_url)


# 네이버 로그인(인증) 완료 후 내 사이트로 돌아올 때 end point
@app.route('/naver/callback')
def naver_callback():
    code = request.args.get('code') # 네이버 서버에서 인증 성공 시 준 값
    state = request.args.get('state') # 내 서버에서 갔다온건지 확인용 문장 / 내가 보낸 state 내 글자 확인
    print(f"code: {code}, state: {state}")

    # 인증 토큰 요청 : 고객이 가져온 코드가 네이버에서 발급된 내용이 맞는지 확인하기 위한 것
    # (code를 검증 후 일치할 경우 네이버 서버 토큰 전달)
    token_url = (
        f"https://nid.naver.com/oauth2.0/token?"
        f"grant_type=authorization_code&client_id={NAVER_CLIENT_ID}"
        f"&client_secret={NAVER_CLIENT_SECRET}&code={code}&state={state}"
    )

    token_response = requests.get(token_url).json()
    print(token_response)
    access_token = token_response.get('access_token')

    # 사용자가 제대로 인증하고 온 것 확인 완료
    # 네이버 서버에게 해당 사용자의 정보 요청

    headers = {'Authorization': f'Bearer {access_token}'}
    profile = requests.get('https://openapi.naver.com/v1/nid/me', headers=headers).json()

    print('최종적으로 받아온 사용자의 정보 : ', profile)

    # TODO: 우리의 DB(sqlite3)에 이 사용자가 있는지 확인, 있으면 그 정보 가져와서 세션에 저장
    # 사용자가 없으면 새롭게 DB에 삽입
    # 이걸 더 확장하면?? 사용자가 없으면 회원가입 페이지로 이동, 그 후 주소, 전화번호 등 추가정보를 입력받아서 DB에 저장
    
    # 해당 정보를 내 세션에 저장하기
    session['user'] = profile['response']

    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.clear() # 해당 회원의 모든 session 정보 삭제
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
