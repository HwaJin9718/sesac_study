from flask import Flask, session

app = Flask(__name__)
# 세션 암호를 위한 키 (서버에서 관리/암호화/복호화 진행 -> 즉 외부에 노출되면 안됨!!)
app.secret_key = 'my-secret-key' 

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

# cmd 에서 했을 때!!
# (base) D:\study\SeSAC\sesac_study>curl 127.0.0.1:5000/get-session
# 저장된 정보가 없습니다.
# (base) D:\study\SeSAC\sesac_study>curl 127.0.0.1:5000/set-session/user1
# 세션이 저장되었습니다.
# (base) D:\study\SeSAC\sesac_study>curl 127.0.0.1:5000/get-session
# 저장된 정보가 없습니다.
# (base) D:\study\SeSAC\sesac_study>curl 127.0.0.1:5000/set-session/user1 -c cookie.txt
# (base) D:\study\SeSAC\sesac_study>curl 127.0.0.1:5000/set-session/user1 --cookie-jar cookie.txt # 위랑 동일한 코드 줄이면 위에꺼
# 세션이 저장되었습니다.
# (base) D:\study\SeSAC\sesac_study>curl 127.0.0.1:5000/get-session
# 저장된 정보가 없습니다.
# (base) D:\study\SeSAC\sesac_study>curl 127.0.0.1:5000/get-session -b cookie.txt
# (base) D:\study\SeSAC\sesac_study>curl 127.0.0.1:5000/get-session --cookie cookie.txt # 위랑 동일한 코드 줄이면 위에꺼
# 세션 정보 : user1
