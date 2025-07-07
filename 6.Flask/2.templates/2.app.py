from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    users = ['Alice', 'BOb', 'Charlie', 'David', 'Eve']
    return render_template('index2.html', names=users) # HTML 파일안에 이 names 라는 key에 users라는 값을 담아 보낼거다.


if __name__ == '__main__':
    app.run(debug=True)