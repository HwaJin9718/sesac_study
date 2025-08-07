# 내 메모 리스트 담을 곳

# _ 가 붙으면 내부 변수, 
# 외부에서 직접 가져다 쓸 수 없음 -> 자바에서 public private 등등
_todos = []
_next_id = 1 # ToDo 넘버링


def get_all():
    todos_dict = [{'id': todo['id'], 'todo': todo['todo'], 'done': todo['done']} for todo in _todos]
    return todos_dict


def get_all_to_chat():
    todos_fommat = "\n".join([
        f"{t['id']}. {t['todo']} [{'완료' if t['done'] else '미완료'}]" for t in _todos
    ])
    return todos_fommat


def get_one(todo_id):
    todo_result = ''
    for todo in _todos:
        if todo['id'] == todo_id:
            todo_result = todo
            break
    return dict(todo_result)


def add(todo):
    global _next_id
    try:
        _todos.append({'id': _next_id, "todo" : todo['textInput'], 'done' : False})
        _next_id += 1
        return True
    except Exception as e:
        print(f"오류 발생: {e}")
        return False


def modify(todo_id):
    modify = False

    for todo in _todos:
        if todo['id'] == todo_id:
            todo['done'] = not todo['done']
            modify = True
        
    if modify:
        return modify # True
    else:
        return modify # False


def delete(todo_id):
    delete = False

    for todo in _todos:
        if todo['id'] == todo_id:
            # todo 삭제
            _todos.remove(todo)
            delete = True
            break

    if delete:
        return delete # True
    else:
        return delete # False

