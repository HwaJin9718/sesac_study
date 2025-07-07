from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '050-1234-5678'},
    {'name': 'Alice', 'age': 35, 'mobile': '050-5555-5678'},
    {'name': 'Bob', 'age': 30, 'mobile': '050-2222-5678'},
    {'name': 'Charlie', 'age': 35, 'mobile': '050-3333-5678'},
    {'name': 'David', 'age': 30, 'mobile': '050-4444-5678'},
]

# 미션1. 이름과 나이로 검색 / 이름 or 나이 or 둘다

@app.route('/')
def home():
    name = request.args.get('name')
    age = request.args.get('age')
    phone = request.args.get('phone')

    print(f"이름 : {name}, 나이 : {age}")

    filtered_users = users

    # for u in users:
    #     if name and age:
    #         # if ( u['name'].lower() == name.lower() ) and ( u['age'] == int(age) ):
    #         #     filtered_users = [u]
    #         #     break
    #         if u['name'].lower() == name.lower():
    #             name_check = [u]
    #             if u['age'] == int(age):
    #                 age_check = [u]
    #                 if name_check == age_check:
    #                     filtered_users = [u]
    #                     break
    #     elif name:
    #         if u['name'].lower() == name.lower():
    #             filtered_users = [u]
    #             break
    #     elif age:
    #         if u['age'] == int(age):
    #             filtered_users = [u]
    #             break

    
    # 강사님 코드
    # 이런 로직을 어떻게 이렇게 하나하나 비교 안하고 할 수 없을까?
    # 설계적으로 논리적으로 좋지 않음 // 왜? 항목의 제곱수로 늘어나는 조합에 대한 비교가 필요
    # 제곱수가 아니고 그냥 그 항목의 갯수만큼
    # 0 0 0
    # 0 0 1
    # 0 1 0
    # 0 1 1
    # 1 0 0
    # 1 0 1
    # 1 1 0
    # 1 1 1
    
    if name and age:
        print("이름과 나이 둘다 검색")
        filtered_users = [u for u in users if u['name'].lower() == name.lower() and u['age'] == int(age)]
    elif name:
        filtered_users = [u for u in users if u['name'].lower() == name.lower()]
    elif age:
        filtered_users = [u for u in  users if u['age'] == int(age)]

    
    # phone 까지 포함했을 때 경우의 수 -> if 문으로 작성해야 하는 것 2^3 = 8가지
    # if name and age and phone:
    #     filtered_users = [u for u in users if u['name'].lower() == name.lower() and u['age'] == int(age)]
    # elif name and age:
    #     filtered_users = [u for u in users if u['name'].lower() == name.lower() and u['age'] == int(age)]
    # elif name and phone:
    #     filtered_users = [u for u in users if u['name'].lower() == name.lower() and u['age'] == int(age)]
    # elif age and phone:  # 여기서 부터 아래까지가 일단...
    #     filtered_users = [u for u in users if u['name'].lower() == name.lower() and u['age'] == int(age)]
    # elif name:
    #     filtered_users = [u for u in users if u['name'].lower() == name.lower()]
    # elif age:
    #     filtered_users = [u for u in users if u['age'] == int(age)]
    
    print(filtered_users)
    return render_template('index5.html', users=filtered_users) 

if __name__ == '__main__':
    app.run(debug=True)
