from flask import Flask, send_from_directory, request, url_for, jsonify

app = Flask(__name__)

todoList = []

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'todo_restapi.html')

@app.route('/addTodo', methods=["POST"])
def add_todo():
    return 'addTodo 서버 접속 완료'

@app.route('/deleteTodo', methods=["DELETE"])
def delete_todo():
    return 'deleteTodo 서버 접속 완료'

if __name__ == '__main__':
    app.run(debug=True)
