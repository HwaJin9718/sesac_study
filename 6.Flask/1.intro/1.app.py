# pip install flask

from flask import Flask

app = Flask(__name__)

@app.route('/') # 사용자가 /(루트)에 접속하면 이 아래 함수를 호출해줘
def home():
    return "<h1>Hello, Flask!</h1>"

if __name__ == '__main__':
    print("여기가 메인 함수")
    # Flask라는 애플리케이션 실행, 사용자의 요청이 올 때까지 대기하고 있음 //5000번 포트가 기본값 -> 수정 가능
    app.run() 
    # Flask 서버는 이 자체로는 대용량의 트래픽, 수많은 사용자의 요청을 핸들링 하도록 만들어 진 것은 아님 -> FastAPI 서버 등은 이걸 다 포함
    # unicorn uvicorn 이런게 대용량 트래픽 처리가 가능한 앞단의 서비스 / 요청 받은걸 flask로 전달
