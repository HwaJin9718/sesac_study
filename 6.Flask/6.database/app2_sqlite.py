from flask import Flask, render_template, request, redirect
import database as db

app = Flask(__name__)

# 미션. uesrs.append가 아니라 db를 사용해서 db.insert_user 등등으로 수정
db.create_table() # 최초의 DB 생성

# 이거 처음에 초기화 1번만 하도록 하는거
# @app.before_first_request
# def initialise():
#     print('나는 언제 찍힐까?')
#     db.create_table()

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # POST 요청 처리
        name = request.form['name']
        age = int(request.form['age'])
        print(f"이름 : {name}, 나이: {age}")

        db.insert_user(name, age)

        return redirect('/') # 추가 완료 시 원래 페이지 호출
    
    # GET 요청 처리
    users = db.get_users() # dict로 변환 가능한 row 포멧으로 나와서 그냥 쓸 수 있음
    return render_template('index.html', users=users)

# 내 풀이
# @app.route('/delete/<int:user_id>')
# def delete_user(user_id):
#     # 미션1. users 리스트에서 user_id 를 찾아서 지우기
#     user = db.get_users_by_id(user_id)

#     if user:
#         db.delete_user_by_id(user_id)

#     return redirect('/')

# 강사님 풀이
@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    # 수업용으로 좋고, 실용적이지 않음. 왜? 하나 지울려고 모든 리스트를 새로 만들어야 함. 속도가 느림
    db.delete_user_by_id(user_id)
    return redirect('/')

# 내 풀이
# @app.route('/update/<int:user_id>', methods=['GET', 'POST'])
# def update_user(user_id):

#     # users 리스트에서 user_id 를 찾아서 수정
#     # 미션2. get = 수정을 위한 사용자 정보 전달
#     user = db.get_users_by_id(user_id)
        
#     if request.method == 'POST':

#         # 미션3. 실제 수정 코드
#         if not user:
#             return "사용자를 찾을 수 없습니다", 404
        
#         name = request.form['name']
#         age = int(request.form['age'])

#         db.update_user(user_id, name, age)

#         return redirect('/')
    
#     return render_template('/update_user.html', user=user)

@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = db.get_user_by_id(user_id)
    if not user:
        return "사용자를 찾을 수 없습니다.", 404
    
    if request.method == 'POST':
        # 미션3. POST = 실제 수정하는 코드
        name = request.form['name']
        age = int(request.form['age'])
        
        db.update_user_by_id(user_id, name, age)
        return redirect('/')
        
    return render_template('update_user.html', user=user)


if __name__ == '__main__':
    # db.create_table()
    # print('나는 언제 찍힐까?') # debug 모드에서는 이게 두번 실행됨 -> 오류 발생할 수 있음
    app.run(debug=True)
