from flask import Flask, render_template, request, jsonify, session, flash, redirect, url_for
from flask_mail import Mail, Message

from dotenv import load_dotenv
import os
import random

load_dotenv()

app = Flask(__name__)
app.secret_key = 'abce1234'

app.config['MAIL_SERVER'] = os.getenv('NAVER_MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('NAVER_MAIL_PORT')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('NAVER_EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('NAVER_PASSWORD')

mail = Mail(app)

users = []

@app.route('/')
def signup():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():

    id = request.form.get('id')
    pw = request.form.get('pw')
    print(f'아이디 : {id}, 비밀번호 : {pw}')

    if not users:
        flash('등록된 사용자가 없습니다. 먼저 회원가입을 해주세요.', 'warning')
        return render_template('index.html')

    login_success = False
    for u in users:
        if (u['id'] == id) and (u['password'] == pw):
            flash('로그인이 성공했습니다.', 'success')
            login_success = True
            break

    if not login_success:
        flash('ID/PW가 일치하지 않습니다.', 'danger')
    
    return redirect(url_for('signup'))


@app.route('/membership', methods=['GET', 'POST'])
def membership():
    
    if request.method == 'POST':
        id = request.form.get('id')
        pw = request.form.get('pw')
        email = request.form.get('email')
        code = request.form.get('code')
        email_verify = request.form.get('email_verify')
        code_verify = request.form.get('code_verify')

        print(f'아이디 : {id}, 비밀번호 : {pw}, 이메일 : {email}, 인증코드 : {code}, 이메일 인증 여부 : {email_verify}, 코드 인증 여부 : {code_verify}')

        if (email_verify != 'true') or (code_verify != 'true'):
            flash('이메일 인증과 인증코드를 입력해주세요.', 'danger')
            return render_template('membership.html')
        
        id_exists = False
        for u in users:
            if u['id'] == id:
                id_exists = True

        if id_exists:
            flash('해당 ID를 사용할 수 없습니다. 다시 입력해주세요.', 'warning')
            return redirect(url_for('membership'))
            
        user = {'id' : id, 'password' : pw, 'email' : email}
        users.append(user)
        flash('회원가입이 완료되었습니다. 로그인해주세요.', 'success')

        return redirect(url_for('signup'))

    else:
        return render_template('membership.html')


@app.route('/send-code', methods=['POST'])
def send_code():
    email = request.form.get('email') # 사용자로 부터 받아오기

    code = random.randint(000000, 999999)
    print(f'random 코드 : {code}')

    msg = Message('SeSAC 인증 코드', sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = f"SeSAC 인증코드 : {code} 입니다."

    # result = False

    try:
        mail.send(msg)
        session['send_code'] = str(code)
        # result = True
        # flash('메일 전송이 성공했습니다. 발송된 메일 내 인증코드를 입력해주세요.', 'success')
        return jsonify({
            'result': True,
            'message': '메일 전송이 성공했습니다. 발송된 메일 내 인증코드를 입력해주세요.',
            'type': 'success'
        })
    except Exception as e:
        # result = False
        # flash(f'메일 전송 중 오류가 발생했습니다. 재시도 해주세요. 오류 내용 : {e}', 'warning')
        return jsonify({
            'result': False,
            'message': f'메일 전송 중 오류가 발생했습니다. 재시도 해주세요. 오류 내용 : {e}',
            'type': 'warning'
        })

    # return jsonify({'result': result})


@app.route('/verify-code', methods=['POST'])
def verify_code():
    input_code = request.form.get('code')
    session_code = session.get('send_code', None)
    print(f'입력된 code : {input_code}, 세션에 저장되 코드 : {session_code}')

    result = False

    if (input_code == session_code):
        # result = True
        # flash('인증에 성공했습니다.', 'success')
        return jsonify({
            'result': True,
            'message': '인증에 성공했습니다.',
            'type': 'success'
        })
    else:
        # result = False
        # flash('인증에 실패했습니다. 다시 시도해주세요.', 'danger')
        return jsonify({
            'result': False,
            'message': '인증에 실패했습니다. 다시 시도해주세요.',
            'type': 'danger'
        })

    # return jsonify({'result': result})


@app.route('/password-search')
def password_search():
    return render_template('password_search.html')


if __name__ == '__main__':
    app.run(debug=True)

