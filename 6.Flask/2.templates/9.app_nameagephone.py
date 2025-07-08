from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '050-1234-1234'},
    {'name': 'Alice', 'age': 35, 'mobile': '050-5555-1234'},
    {'name': 'Bob', 'age': 30, 'mobile': '050-2222-5678'},
    {'name': 'Charlie', 'age': 35, 'mobile': '050-3333-5678'},
    {'name': 'David', 'age': 30, 'mobile': '050-4444-5678'},
]

@app.route('/')
def home():
    name = request.args.get('name')
    age = request.args.get('age')
    phone = request.args.get('phone')

    print(f"이름 : {name}, 나이 : {age}, 전화번호 : {phone}")

    filtered_users = users
    
    # 강사님 코드
    # 이런 로직을 어떻게 이렇게 하나하나 비교 안하고 할 수 없을까?
    # 항목의 제곱수로 늘어나는 조합에 대한 비교가 필요하므로 설계적으로 논리적으로 좋지 않음
    
    # 제곱수가 아니고 그냥 그 항목의 갯수만큼 비교하는 방식 필요
    # 전체목록 (100) -> 이름과 나이
    # 1. 전체목록 (100) -> 이름비교
    # 2. 이름매칭(30) -> 나이비교
    # 3. 나이매칭(5)

    if name:
        # 이름으로 비교하기
        # 이름으로 필터링이 끝난 결과가 filtered_users 안에 들어감
        filtered_users = [u for u in filtered_users if name.lower() == u['name'].lower()]

    
    if age:
        # 나이로 비교하기
        # 나이로 필터링이 끝난 결과가 filtered_users 안에 들어감
        filtered_users = [u for u in filtered_users if int(age) == u['age']] 

    if phone:
        # 전화번호로 비교하기
        # 전화번호로 필터링이 끝난 결과가 filtered_users 안에 들어감
        # in 을 사용하여 전화번호의 일부 검색도 가능(뒷 4자리 등)
        filtered_users = [u for u in filtered_users if phone in u['mobile']]

    return render_template('index9.html', users=filtered_users)

if __name__ == '__main__':
    app.run(debug=True)
