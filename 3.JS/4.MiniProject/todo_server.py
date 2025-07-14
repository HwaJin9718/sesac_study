from flask import Flask, send_from_directory, request, redirect, url_for, jsonify

app = Flask(__name__)

todoList = []

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'todo_restapi.html')

@app.route('/getTodo')
def get_todo():
    return todoList

@app.route('/addTodo', methods=["POST"])
def add_todo():
    todo = request.form.get('userInput')

    if todo:
        todoList.append({ "todos" : todo})
        return redirect(url_for('index'))
    elif todo is None or todo.length() == 0:
        return 'ToDo 등록이 실패하였습니다.'


@app.route('/deleteTodo', methods=["DELETE"])
def delete_todo():
    return 'deleteTodo 서버 접속 완료'

if __name__ == '__main__':
    app.run(debug=True)
