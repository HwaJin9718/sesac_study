from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'my-secret-key' 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///session.db'
db = SQLAlchemy(app)

app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db
Session(app)

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

