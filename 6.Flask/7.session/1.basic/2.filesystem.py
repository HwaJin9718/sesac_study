# pip install flask-session

from flask import Flask, session
from flask_session import Session
import os

app = Flask(__name__)
app.secret_key = 'abcd1234' # 아무거나 무방

app.config['SESSION_TYPE'] = 'filesystem' # 실제 서비스는 파일에 저장하는 것 보다는 DB에 session 저장
# 서버에 저장하지 않음, 그 외 filesystem / redis / memchaced / mongod / sqlalchemy 등등
app.config['SESSION_FILE_DIR'] = os.path.join(os.getcwd(), 'my-session')
# app.config['SESSION_FILE_DIR'] = './my-session' # 위 파일 경로 저장한 것과 동일
app.config['SESSION_PERMANENT'] = False # False 일 경우 브라우저가 닫히면 삭제
app.config['SESSION_USE_SIGNER'] = True # 세션 쿠키에 서명 사용 여부

Session(app) # 우리의 앱(app)에 세션 기능을 더함

@app.route('/set-session/<username>')
def set_session(username):
    session['username'] = username
    return '세션이 저장되었습니다.'

@app.route('/get-session')
def get_session():
    if 'username' in session:
        return f"세션 정보 : {session['username']}"
    else:
        return f"저장된 정보가 없습니다."

@app.route('/clear-session')
def del_session():
    session.pop('username', None) # 세션에서 값 삭제
    return f"세션 정보가 삭제되었습니다."

if __name__ == '__main__':
    app.run(debug=True)
