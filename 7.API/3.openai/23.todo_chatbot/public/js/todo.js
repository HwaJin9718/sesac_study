// /api/todo에 CRUD 기능 추가
// GET /api/todo
// POST /api/todo
// PUT /api/todo/${id}
// DELETE /api/todo/${id}

document.addEventListener('DOMContentLoaded', () => {
    getTodos();
    closeModifyModal();
})

const todoForm = document.getElementById('todo-form')
todoForm.addEventListener('submit', createTodo);

const todoList = document.getElementById('todo-list')
todoList.addEventListener('click', (e) => {
    e.preventDefault()

    if (e.target.classList.contains('modify')) {
        const todo_id = e.target.id
        getTodo(todo_id)
        // modifyTodo(todo_id)
    } else {
        const todo_id = e.target.id
        deleteTodo(todo_id)
    }
})

async function getTodos() {
    const response = await fetch('/api/todo')
    const todos = await response.json()
    console.log('서버응답:', todos)

    if (todos) {
        displayTodos(todos.todos)
    }
}

async function getTodo(todo_id) {
    const response = await fetch(`/api/todo/${todo_id}`)
    const todo = await response.json()
    console.log('서버응답:', todo)

    if (todo) {
        openModifyModal(todo.todo)
    }
}

function displayTodos(todos) {
    // 조회 시 이전 todo list 제거 후 새로 등록
    todoList.querySelectorAll('li').forEach(li => li.remove())

    todos.forEach(todo => {
        console.log(todo) // {id: 1, todo: '숙제'}
        const new_li = document.createElement('li')
        // new_li.textContent = todo.todo
        new_li.innerHTML = `${todo.todo} <a class="modify" id="${todo.id}" href="">수정</a> | <a class="delete" id="${todo.id}" href="">삭제</a>`

        todoList.appendChild(new_li)
        
    })
}

async function createTodo() {
    const textInput = document.getElementById('text-input').value.trim();

    if (!textInput) return;

    const response = await fetch('/api/todo', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({textInput})
    })
    const result = await response.json()
    console.log('POST result', result)

    if (result.error) {
        alert('ToDo 등록이 실패했습니다. 다시 시도해 주세요')
    }

    // 등록 성공 시 ToDo 목록 조회 호출
    getTodos();
}

// 모달 창 띄우기
function openModifyModal(todo) {
    document.getElementById('todo-id').value = todo.id;
    document.getElementById('todo-text').value = todo.todo;
    document.getElementById('modify-modal').style.display = 'block';
}

// 모달창 닫기
function closeModifyModal() {
    document.getElementById('modify-modal').style.display = 'none';
}

const modal = document.getElementById('modify-body')
modal.addEventListener('submit', () => {
    const todo_id = document.getElementById('todo-id').value
    const todo_text = document.getElementById('todo-text').value
    // const todo = {'todo_id' : todo_id, 'todo_text': todo_text}
    modifyTodo(todo_id, todo_text);
})

async function modifyTodo(todo_id, todo_text) {
    // 수정
    const response = await fetch(`/api/todo/${todo_id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({todo_text})
    })
    const result = await response.json()
    if (result.error) {
        alert('ToDo 수정이 실패했습니다. 다시 시도해 주세요')
    }

    // 수정 성공 시 ToDo 목록 조회 호출
    getTodos();
}

async function deleteTodo(todo_id) {
    // 삭제
    const response = await fetch(`/api/todo/${todo_id}`, {
        method: 'DELETE'
    })
    const result = await response.json()
    if (result.error) {
        alert('ToDo 삭제가 실패했습니다. 다시 시도해 주세요')
    }

    // 삭제 성공 시 ToDo 목록 조회 호출
    getTodos();
}
