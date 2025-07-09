from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 미션1. 사용자 목록 완성
# 미션2. 로그인 시 ID/PW 일치 체크
# 미션3. 맞으면 로그인 성공 페이지로 이동 (안녕하세요 OOO님)
#        실패 시, 로그인 실패라고 출력
# 사용자 목록
users = [
    # 사용자 이름, 아이디, 암호 -> 3명 이상의 사용자 만들기 // dict : key, value 형태
    {'name' : 'HwaJinSong', 'id' : 'genie', 'pw' : 'genie'},
    {'name' : 'Alice', 'id' : 'qwerasdf', 'pw' : 'qwer1234'},
    {'name' : 'Bob', 'id' : 'asdfqwer', 'pw' : 'asdf1234'},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # post에 대한 처리
        # user = request.form['name']
        # print(f"입력된 이름은 : {user}")

        id = request.form['id']
        pw = request.form['pw']
        # print(f"ID : {id}, PW : {pw}")

        # 강사님 코드
        # user = None

        # 일반적인 for / if 구문
        # for u in user:
        #     if u['id'] == id and u['pw'] == pw:
        #         user = u
        #         break

        # 좀 더 pythonic 하게 짜면!!
        user = next((u for u in users if u['id'] == id and u['pw'] == pw), None)
        print(f"검색된 사용자: {user}")

        if user:
            error = None
        else:
            error = "ID/PW 가 올바르지 않습니다."

        # return redirect(url_for("user", user=user))
        # return render_template('user.html', user=user)
        return render_template('user.html', user=user, error=error)

        # 내 코드
        # user_check = users
        # print(f"ID 확인 전 user_check : {user_check}")
        # if id:
        #     user_check = [u for u in user_check if id == u['id']]
        #     print(f"ID 확인 후 user_check : {user_check}")
        #     if pw:
        #         user_check = [u for u in user_check if pw == u['pw']]
        #         print(f"PW 확인 후 user_check : {user_check}")
        #         # print(f"User : {user_check}")
        #         return render_template('user.html', user=user_check)
        #         # return redirect(url_for("user", user=user_check))
        #     else:
        #         return '아이디 비밀번호가 일치하지 않습니다. 다시 확인해주세요'
        # else:
        #     return '아이디 비밀번호가 일치하지 않습니다. 다시 확인해주세요'

    else:
        # post가 아닐 때 처리, 즉 get일 때의 처리
        return render_template('login.html')

@app.route('/user')
@app.route('/user/<user>')
def user(user=None): # 초기값 할당
    if user:
        error = None
    else:
        error = "ID/PW가 일치하지 않습니다."
    
    print('프런트전달전: ', user)

    return render_template('user.html', user=user, error=error)

@app.route('/product')
def product():
    return render_template('product.html')

if __name__ == '__main__':
    app.run(debug=True)