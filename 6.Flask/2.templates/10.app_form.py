from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['get'])
def index():
    return render_template('form.html')

@app.route('/submit', methods=['post'])
def submit():
    # name = request.args.get('name') # 이건 GET 파라미터(아규먼트 = argements)를 받는 방식
    name = request.form.get('name') # POST 로 form(폼) 에 전달된 것 중 name이 키 인 것을 주시오
    age = request.form.get('age') # POST 로 form(폼) 에 전달된 것 중 age가 키 인 것을 주시오

    print(request.form)
    print(name)
    
    return f"안녕하세요 {age} 세 {name} 님"

if __name__ == '__main__':
    app.run(debug=True)
