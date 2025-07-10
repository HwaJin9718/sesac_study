from flask import Flask, send_file, jsonify
# 여기에 cors 라이브러리 추가하여 해결, or 프런트앤드를 여기서 서빙
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_file("4.fetch.html")

@app.route('/data')
def data():
    return jsonify({'result': 'success','message': '안녕하세요 반갑습니다!'})
    # return jsonify({'result':'failure', 'message':'안녕하세요, 반갑습니다.'})

if __name__ == '__main__':
    app.run(debug=True)