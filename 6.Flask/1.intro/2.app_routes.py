from flask import Flask

app = Flask(__name__)

@app.route('/') # 사용자가 /(루트)에 접속하면 이 아래 함수를 호출해줘
def home():
    return "<h1>Hello, Flask!</h1>"

@app.route('/user') # 사용자가 /user에 접속하면 이 아래 함수를 호출해줘
def user():
    return "<h1>Hello, User!</h1>"

@app.route('/user/<username>') 
def greet_user(username): # flask 데코레이터에서 정한 변수명, <변수명> 형태로 함수 인자로 전달 해줌
    return f"<h1>Hello, {username}님!</h1>" # 서버사이트 렌더링 (서버에서 필요한 HTML을 그때그떄 만들어 준것)

@app.route('/user/<int:age>') # 내가 따로 지정하지 않으면 문자열, 바꾸고 싶으면 타입 지정 가능
def greet_with_age(age): 
    return f"<h1>Hello, {age}살 아무개님!</h1>"

@app.route('/user/<float:weight>') # 내가 따로 지정하지 않으면 문자열, 바꾸고 싶으면 타입을 지정
def greet_with_weight(weight): 

    # 이렇게 함수 내부에 비지니스 로직 구현하는것
    if weight > 60:
        message = "뚱뚱한"
    elif weight < 40:
        message = "날씬한"
    else:
        message = ""
    
    # 결론은, 원하는 메세지 (결론=결과물) 을 만들어 냄
    return f"<h1>Hello, {weight}Kg {message} 아무개님!</h1>"

@app.route('/user/<name>/<int:age>/<float:weight>')
def greet_user_with_detail(name, age, weight):
    return f"<h1>안녕하세요</h1><h2>사용자 정보</h2><ul><li>이름 : {name}</li><li>나이 : {age}</li><li>몸무게 : {weight}</li></ul>"

@app.route('/product') # 사용자가 /product에 접속하면 이 아래 함수를 호출해줘
def product():
    return "<h1>Hello, Product!</h1>"

if __name__ == "__main__":
    print("여기가 메인 함수")
    # Flask라는 애플리케이션 실행, 사용자의 요청이 올 때까지 대기하고 있음 //5000번 포트가 기본값 -> 수정 가능
    app.run(debug=True) # 디버그 모드 on / 만약에 배포(릴리즈)할 때 디버그 모드를 켜놓으면 오류가 났을 때 오류메시지 디테일을 보여줌 / 꼭 debug=False를 하던 주석을해놓고 커밋하기!!
