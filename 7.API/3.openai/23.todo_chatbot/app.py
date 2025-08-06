from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='public', static_url_path='')

# 내 메모 리스트 답을 곳
todos = []

@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/api/todo', methods=['GET'])
def get_todos():
    return jsonify({'error': '아직 구현 전'})


@app.route('/api/todo', methods=['POST'])
def add_todo():
    return jsonify({'error': '아직 구현 전'})


@app.route('/api/todo/<int:todo_id>', methods=['PUT'])
def toggle_todo(todo_id):
    return jsonify({'error': '아직 구현 전'})


@app.route('/api/todo/<int:todo_id>', methods=['DELETE'])
def delete_todos(todo_id):
    return jsonify({'error': '아직 구현 전'})


# 미션1. todo CRUD 완성
# 미션2. 챗봇을 front에 추가하고 /api/chat 을 추가
#        근데 완전히 다른 요청을 한파일에 할거냐?
# 미션2-1. 어떻게 라우트를 분리할까? todo 서비스와 chat 서비스를 분리하자
#        routes를 분리하려면? blueprint 도입
# 미션3. 채팅 아무 말이나 받아서 GPT에게 주고, 요청 받아서 

if __name__ == '__main__':
    app.run(debug=True)
