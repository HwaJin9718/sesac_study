from flask import Blueprint, request, jsonify
from services import todo_service as svc
# 하기처럼 함수를 직접 호출할 수 있으나 함수가 많으면 import가 너무 길어지니 위 방식 사용
# from services.todo_service import get_all, get_one, add, modify, delete

todo_bp = Blueprint('todo', __name__)

# 미션1. todo CRUD 완성
# 미션2. 챗봇을 front에 추가하고 /api/chat 을 추가
#        근데 완전히 다른 요청을 한파일에 할거냐?
# 미션2-1. 어떻게 라우트를 분리할까? todo 서비스와 chat 서비스를 분리하자
#        routes를 분리하려면? blueprint 도입
# 미션3. 채팅 아무 말이나 받아서 GPT에게 주고, 요청 받아서 

@todo_bp.route('', methods=['GET'])
def get_todos():
    todos = svc.get_all()
    return jsonify({'todos': todos})


# todo id로 단일 조회
@todo_bp.route('/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):

    result = svc.get_one(todo_id)

    if result:
        return jsonify({'todo': result})
    else:
        return jsonify({'error': 'ToDo 조회이 실패'})


@todo_bp.route('/', methods=['POST'])
def add_todo():

    todo = request.get_json()
    print('입력된 todo', todo)

    if todo is None or len(todo) == 0:
        return jsonify({'error': '입력된 ToDo가 없습니다.'})

    if svc.add(todo):
        return jsonify({'success': 'ToDo 등록 완료'})
    else:
        return jsonify({'error': 'ToDo 등록 실패'}) 


# todo 내용 수정
# @todo_bp.route('/<int:todo_id>', methods=['PUT'])
# def toggle_todo(todo_id):
#     input_todo = request.get_json()
#     print('입력된 todo :', input_todo['todo_text'])

#     if input_todo is None:
#         return jsonify({'error': 'ToDo 수정 요청값이 없습니다.'})
    
#     for todo in todos:
#         if todo['id'] == todo_id:
#             todo['todo'] = input_todo['todo_text'].strip()
#             return jsonify({'success': 'ToDo 수정 완료'})
        

# todo done 여부 수정
@todo_bp.route('/<int:todo_id>', methods=['PUT'])
def toggle_todo(todo_id):

    result = svc.modify(todo_id)

    if result:
        # return jsonify({'success': f"ToDo {todo_id}번 {todo['done']} 처리 완료"})
        return jsonify({'success': f"ToDo {todo_id}번 처리 완료"})
    
    return jsonify({'error': 'ToDo 수정 실패'})


@todo_bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todos(todo_id):
    
    result = svc.delete(todo_id)

    if result:
        return jsonify({'success': 'ToDo 삭제 완료'})

    return jsonify({'error': 'ToDo 삭제 실패'})

