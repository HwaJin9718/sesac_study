from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# db 안 쓸 때
users = [] # [{'id' : 1, 'name' : '홍길동', 'age': 30}]
next_id = 1

@app.route('/', methods=['GET', 'POST'])
def index():
    global next_id # 글로벌 변수에 write 시 해당 선언 필요, read 시 불필요
                   # 변수 안에 멤버가 수정될때는 무관함. 
                   # 해당 변수 자체가 변경될때는 global 선언이 필요함.

    if request.method == 'POST':
        # POST 요청 처리
        name = request.form['name']
        age = int(request.form['age'])

        users.append({'id': next_id, 'name': name, 'age': age})
        next_id += 1 # 다음 입력을 위해 자동증가

        return redirect('/') # 추가 완료 시 원래 페이지 호출
    
    # GET 요청 처리

    return render_template('index.html', users=users)

# 내 풀이
# @app.route('/delete/<int:user_id>')
# def delete_user(user_id):
#     # 미션1. users 리스트에서 user_id 를 찾아서 지우기
#     for u in users:
#         if u['id'] == user_id:
#             # users에서 지우기
#             users.remove(u) # 지우고나면 꼭 break 해야함
#     return redirect('/')

# 강사님 풀이
@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    # 미션1. users 리스트에서 user_id 를 찾아서 지우기
    # for i, user in enumerate(users):
    #     if user['id'] == user_id:
    #         print('삭제할 사용자 찾음:', user, i)
    #         del users[i]
    #         break
    
    # 리스트컴프레이션 : 수업용으로 좋으나 실용적이지 않음
    # 왜? 하나 지우려고 모든 리스트를 새로 만들어야함 -> 속도가 느림
    users = [u for u in users if u['id']!= user_id]

    # print('전체목록:', users)

    return redirect('/')

# 내 풀이
# @app.route('/update/<int:user_id>', methods=['GET', 'POST'])
# def update_user(user_id):

#     # users 리스트에서 user_id 를 찾아서 수정
#     # 미션2. get = 수정을 위한 사용자 정보 전달
#     user = []
#     for u in users:
#         if u['id'] == user_id:
#             user = u
        
#     if request.method == 'POST':
#         # 미션3. 실제 수정 코드
#         new_name = request.form['name']
#         new_age = request.form['age']
#         user['name'] = new_name
#         user['age'] = new_age
#         return redirect('/')
    
#     return render_template('/update_user.html', user=user)

# 강사님 풀이
@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):

    global users # 이걸 하지 않더라도 수정은 가능

    # users 리스트에서 user_id 를 찾아서 수정
    # 미션2. get = 수정을 위한 사용자 정보 전달
    user = next((u for u in users if u['id'] == user_id), None)
    print(user)
        
    if request.method == 'POST':

        # 미션3. 실제 수정 코드
        if not user:
            return "사용자를 찾을 수 없습니다", 404
        
        user['name'] = request.form['name']
        user['age'] = int(request.form['age'])

        return redirect('/')
    
    return render_template('/update_user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
