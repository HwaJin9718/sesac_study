from flask import Flask, render_template

app = Flask(__name__)

# app = Flask(__name__, static_folder="mystatic")
# 1. static 폴더의 이름은 바꿀 수 있으나 굳이 바꿀 필요 없음
# 2. static이라고 폴더명을 정해주면 그곳은 자동으로 외부에 노출된다 (img, html, css, js)
# 3. 그래서 index 안에서 static을 전달할 때 하드코딩해도 동작은 하나 그것보다 url_for('static', ...) 이라고 해서 전달하는게 더 좋은 코딩

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
