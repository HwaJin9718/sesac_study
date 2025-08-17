# 소셜 로그인
from dotenv import load_dotenv
from flask import Flask, request, redirect, url_for, session, jsonify
import requests
import os
from flask_cors import CORS

load_dotenv()

app=Flask(__name__)
app.secret_key = os.getenv("SESSION_SECRET")
CORS(app, origins=[
    'http://127.0.0.1:5000',  # 백엔드
    'http://127.0.0.1:3000'   # 프론트엔드
])

KAKAO_CLIENT_ID=os.getenv("KAKAO_REST_API_KEY")
KAKAO_CLIENT_SECRET=os.getenv("KAKAO_CLIENT_SECRET")
KAKAO_REDIRECT_URI=os.getenv("KAKAO_REDIRECT_URI")

users = []

@app.route('/')
def index():
    return app.send_static_file('index.html')


# 내 사이트에서 카카오 로그인 시도 시 진행
@app.route('/login/kakao')
def login_kakao():

    # 실제 네이버 로그인 인증 할 주소
    auth_url = (
        f'https://kauth.kakao.com/oauth/authorize?'
        f'response_type=code&client_id={KAKAO_CLIENT_ID}'
        f'&redirect_uri={KAKAO_REDIRECT_URI}&scope=profile_nickname,profile_image'
    )

    return redirect(auth_url)


@app.route('/auth/kakao/callback')
def kakao_callback():
    code = request.args.get('code')
    # print('코드값 :', code)

    if not code:
        return '인가 코드가 없습니다.', 400

    token_url = 'https://kauth.kakao.com/oauth/token'

    headers = {'Content-Type' : 'application/x-www-form-urlencoded;charset=utf-8'}

    # 인가 코드 발급 요청에 필요한 파라미터 구성
    token_data = {
        'grant_type': 'authorization_code', # 인증 방식 고정값
        'client_id': KAKAO_CLIENT_ID,
        'redirect_uri': KAKAO_REDIRECT_URI,
        'client_secret': KAKAO_CLIENT_SECRET,
        'code': code
    }

    # 카카오에게 코드 검증 후 토큰 발급받을 엔드포인트 입력 및 입력값 확인
    token_res = requests.post(token_url, headers=headers, data=token_data).json()
    # print(token_res)
    access_token = token_res.get('access_token') # access_token 확인

    # 성공 시 사용자 정보 요청
    # 사용자 정보 가져오기 위한 엔드 포인트
    user_info_url = 'https://kapi.kakao.com/v2/user/me'
    headers = {'Authorization': f'Bearer {access_token}', 'Content-Type' : 'application/x-www-form-urlencoded;charset=utf-8'}
    user_info = requests.get(user_info_url, headers=headers).json()
    print('최종적으로 받아온 사용자의 정보 : ', user_info)

    # 로그인 성공
    kakao_id = user_info['id']
    properties = user_info['properties']

    for user in users:
        if user['id'] == kakao_id:
            session['user'] = user
            return redirect(url_for('profile'))
    
    new_user = {'id' : str(kakao_id), 'nickname' : properties['nickname'], 'image' : properties['profile_image']}
    users.append(new_user)
    
    # 해당 정보를 내 세션에 저장하기
    session['user'] = new_user

    return redirect(url_for('profile'))


@app.route('/profile')
def profile():
    user = session.get('user')

    if not user:
        return redirect(url_for('index'))

    # return render_template('profile.html', user=user)
    return app.send_static_file('profile.html')


@app.route('/user-data')
def user_data():
    user = session.get('user')
    return jsonify({'user' : user})


@app.route('/modify', methods=['GET', 'POST'])
def modify():
    parm_id = request.args.get('id')
    session_user = session.get('user')
    print(f'parm_id : {parm_id}, parm_id 타입 : {type(parm_id)}, user : {session_user}')

    if request.method == 'POST':
        id = request.form.get('kakaoid')
        nickname = request.form.get('nickname')
        profileimg = request.form.get('profileimg')

        for user in users:
            if user['id'] == id:
                user['nickname'] = nickname
                break

        modify_user = {'id' : id, 'nickname' : nickname, 'image' : profileimg}

        # 해당 정보를 내 세션에 저장하기
        session['user'] = modify_user

        return redirect(url_for('profile'))
    
    if session_user['id'] == parm_id:
        print('if 문 진입 완료')
        return app.send_static_file('update.html')
    else:
        return app.send_static_file('index.html')


@app.route('/modify-data', methods=['GET'])
def modify_data():
    user = session.get('user')

    return jsonify({'user' : user})


# 로그아웃 추가
@app.route('/logout')
def logout():
    session.clear() # 해당 회원의 모든 session 정보 삭제
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
