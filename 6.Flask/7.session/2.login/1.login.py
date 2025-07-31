from flask import Flask, render_template, request, redirect, url_for
from flask import session

app = Flask(__name__)
app.secret_key = 'this-is-my-important-password'

users = [
    {'name' : 'Alice', 'id' : 'alice', 'pw' : 'alice'},
    {'name' : 'Bob', 'id' : 'bob', 'pw' : 'bob'},
    {'name' : 'Charlie', 'id' : 'charlie', 'pw' : 'charlie'},
]

# 미션1. 로그인 된 사용자는 dashboard.html 을 만들어서 "안녕하세요 OOO님 <-- 세션에 있는 정보 활용"
# 미션2. /에 접속해서 로그인된 사용자면 바로 dashboard로 보내기
# 미션3. 로그아웃 구현 "안녕하세요 OOO님" 밑에 줄에 "로그아웃" 추가 a href로 /logout 

@app.route('/', methods=['GET', 'POST'])
def index():

    session_user = session.get('user')
    if session_user:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')
        # print(id, password)

        # 사용자 목록 매칭 확인
        user = next((u for u in users if u['id'] == id and u['pw'] == password), None)
        
        if user:
            session['user'] = user # 로그인한 사용자 정보 세션에 저장
            return redirect(url_for('profile'))
        else:
            return '로그인에 실패하였습니다.'
        
    return render_template('index.html')


@app.route('/profile')
def profile():
    user = session.get('user') # 해당 정보는 로그인 시 저장한 세션 정보
    if user:
        # return f'당신은 아까 왔던 사용자 군요, {user}'
        return render_template('dashboard.html', user=user)
    else:
        # return f'로그인이 안된 사용자 입니다.'
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    user = session.get('user')
    print(user)

    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        for u in users:
            if u['id'] == user['id']:
                u['name'] = name
                u['pw'] = password
        
        user = next((u for u in users if u['id'] == user['id'] and u['name'] == name and u['pw'] == password), None)

        session['user'] = user

        return render_template('dashboard.html', user=user)

    if user:
        return render_template('update.html', user=user)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)