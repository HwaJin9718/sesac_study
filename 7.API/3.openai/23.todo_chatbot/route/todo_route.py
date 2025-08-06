from flask import Blueprint, request, jsonify

todo_api = Blueprint('todo', __name__)

# 내 메모 리스트 답을 곳
todos = []

next_id = 1 # ToDo 넘버링

# 미션1. todo CRUD 완성
# 미션2. 챗봇을 front에 추가하고 /api/chat 을 추가
#        근데 완전히 다른 요청을 한파일에 할거냐?
# 미션2-1. 어떻게 라우트를 분리할까? todo 서비스와 chat 서비스를 분리하자
#        routes를 분리하려면? blueprint 도입
# 미션3. 채팅 아무 말이나 받아서 GPT에게 주고, 요청 받아서 

@todo_api.route('/', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})


# todo id로 단일 조회
@todo_api.route('/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):

    todo = ''
    for todo in todos:
        if todo['id'] == todo_id:
            todo = todo
            break

    return jsonify({'todo': todo})


@todo_api.route('/', methods=['POST'])
def add_todo():

    global next_id
    todo = request.get_json()
    print('입력된 todo', todo)

    if todo:
        todos.append({'id': next_id, "todo" : todo['textInput']})
        next_id += 1
        return jsonify({'success': 'ToDo 등록 완료'})
    
    elif todo is None or todo.length() == 0:
        return jsonify({'error': 'ToDo 등록이 실패'})


@todo_api.route('/<int:todo_id>', methods=['PUT'])
def toggle_todo(todo_id):
    input_todo = request.get_json()
    print('입력된 todo :', input_todo['todo_text'])

    if input_todo is None:
        return jsonify({'error': 'ToDo 수정 요청값이 없습니다.'})
    
    for todo in todos:
        if todo['id'] == todo_id:
            todo['todo'] = input_todo['todo_text'].strip()
            return jsonify({'success': 'ToDo 수정 완료'})


@todo_api.route('/<int:todo_id>', methods=['DELETE'])
def delete_todos(todo_id):
    delete = False

    for todo in todos:
        if todo['id'] == todo_id:
            # todo 삭제
            todos.remove(todo)
            delete = True
            break
    
    if delete:
        return jsonify({'success': 'ToDo 삭제 완료'})

    return jsonify({'error': 'ToDo 삭제 실패'})

