from flask import Flask, jsonify 
# from flask import jsonify # json 화 시킨다

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '050-1234-5678'},
    {'name': 'Bob', 'age': 30, 'mobile': '050-2222-5678'},
    {'name': 'Charlie', 'age': 35, 'mobile': '050-3333-5678'},
]

@app.route('/')
def index():
    return jsonify(users)

@app.route('/user/<name>')
def get_user_by_name(name):
    print("이름", name)
    
    user = None
    for u in users:
        if name.lower() == u['name'].lower():  # 입력값, DB값 소문자로 변환하여 비교
            user = u
            break  # 반복문을 중단
        
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404


# 삽질하는 중...
# @app.route('/user/<name>')
# def get_user_by_name(name):
    # 이름이 일치하는지
    # for/if 구문을 통해서 입력받은 name이 실제로 위에 users에서 존재하는지
    # print("이름 : ", name)
    # print("타입 : ", type(name))

    # if isinstance(name, str):
    #     for u in users:
    #         if name.lower() == u['name'].lower(): # 입력값, DB값 소문자로 변환하여 비교
    #             print("매칭")
    #             user = u
    #             break

    # elif isinstance(int(name), int):
    #     for u in users:
    #         if int(name) == u['age']:
    #             user = u
    #             break

    # if user:
    #     return jsonify(user)
    # else:
    #     return jsonify({'error': 'User not found'}), 404
    
@app.route('/user/<int:age>')
def get_user_by_age(age):
    # 나이로 검색
    print("나이 : ", age)

    user = None
    for u in users:
        if age == u['age']: # 함수의 인자값을 숫자로 변경하거나 DB 값을 
            user = u
            break

    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404
    

if __name__ == "__main__":
    app.run(debug=True, port=5000)