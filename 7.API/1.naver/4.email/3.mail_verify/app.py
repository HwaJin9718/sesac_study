from flask import Flask, render_template, request, jsonify, session
from flask_mail import Mail, Message # pip install flask-mail

from dotenv import load_dotenv
import os
import random

load_dotenv

app = Flask(__name__)
app.secret_key = 'abce1234'

app.config['MAIL_SERVER'] = os.getenv('NAVER_MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('NAVER_MAIL_PORT')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('NAVER_EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('NAVER_PASSWORD')

mail = Mail(app)

@app.route('/')
def signup():
    return render_template('index.html')


@app.route('/send-code', methods=['POST'])
def send_code():
    email = request.form.get('email') # 사용자로 부터 받아오기
    # print(f'이메일 : {email}')

    # 미션1. 6자리 랜덤값 만들기
    # 미션1-1. 세션에 우리의 랜덤 코드 등 저장해서 각 회원별 코드 받아올 수 있게
    code = random.randint(000000, 999999)
    # code = str(random.randint(000000, 999999))
    print(f'random 코드 : {code}')

    msg = Message('SeSAC 회원가입 인증 코드', sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = f"SeSAC 인증코드 : {code} 입니다."

    result = ''

    try:
        mail.send(msg)
        session['send_code'] = str(code)
        result = '메일 전송이 성공했습니다. 발송된 메일 내 인증코드를 입력해주세요.'
    except Exception as e:
        result = '메일 전송 중 오류가 발생했습니다.'
        result += f'오류 내용 : {e}'
        result += '재시도 해주세요'

    return jsonify({'result': result})


# 강사님 코드
# @app.route('/send-code', methods=['POST'])
# def send_code():
#     email = request.json.get('email') # 사용자로부터 받아오기
#     print('입력한 이메일: ', email)
    
#     # 미션1. 6자리 숫자 랜덤값 만들기
#     code = str(random.randint(100000, 999999))
    
#     # 미션1-1. 세션에 우리의 랜덤 코드...
#     session['auth_code'] = code
#     print('발송한 코드는: ', code)

#     msg = Message("회원가입 인증 코드", sender=app.config['MAIL_USERNAME'], recipients=[email])
#     msg.body = f"인증 코드: {code}"
#     mail.send(msg)

#     return jsonify({"message": "인증 코드가 전송되었습니다."})


@app.route('/verify-code', methods=['POST'])
def verify_code():
    input_code = request.form.get('code')
    session_code = session.get('send_code', None)
    print(f'입력된 code : {input_code}, 세션에 저장되 코드 : {session_code}')

    result = ''

    # 미션2. 내가 보낸 코드와 일치/불일치 여부 확인 -> 결과 전송
    # 미션2-1. 저장된 세션에서 코드 가져와서 사용자 입력, 내가 저장해둔거랑 같은지 확인
    
    # input_code와 session_code 값이 동일하더라도 타입이 다르면 false가 됨
    if (input_code == session_code):
        result = '인증에 성공했습니다.'
    else:
        result = '인증에 실패했습니다. 다시 시도해주세요.'

    return jsonify({'result': result}) # return jsonify({'message': '인증 실패'})


# 강사님 코드
# @app.route('/verify-code', methods=['POST'])
# def verify_code():
#     # 미션2. 내가 보낸 코드와 같은지 확인하고
#     code = request.json.get('code') # 사용자로부터 받아오기
    
#     # 미션2-1. 저장된 세션으로부터 코드 가져와서.. 사용자 입력, 내가 저장해둔거랑 같은지 확인..
#     stored_code = session.get('auth_code', None)
    
#     print(f"저장된 코드값: {stored_code}, 사용자 입력: {code}")
#     if (stored_code == code):
#         return jsonify({"message": "인증성공"})

#     return jsonify({"message": "인증실패"})


if __name__ == '__main__':
    app.run(debug=True)

