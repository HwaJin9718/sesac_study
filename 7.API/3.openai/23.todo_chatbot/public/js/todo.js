// /api/todo에 CRUD 기능 추가
// GET /api/todo
// POST /api/todo
// PUT /api/todo/${id}
// DELETE /api/todo/${id}

document.addEventListener('DOMContentLoaded', () => {
    loadTodos();
    closeModifyModal();
})

const todoForm = document.getElementById('todo-form')
todoForm.addEventListener('submit', (e) => {
    e.preventDefault();
    createTodo();
});

const todoList = document.getElementById('todo-list')
todoList.addEventListener('click', (e) => {
    e.preventDefault()

    if (e.target.classList.contains('modify')) {
        // console.log('수정 진입')
        const todo_id = e.target.id
        // getTodo(todo_id)
        modifyTodo2(todo_id);
    } else {
        // console.log('삭제 진입')
        const todo_id = e.target.parentElement.id
        deleteTodo(todo_id)
    }
})

async function loadTodos() {
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

        // 중요!! - 입력값 검증!!!
        // 시큐어 코딩을 고려했을 때 innerHTML으로 출력하는것은 좋지 않음
        // 이렇게 하면 사용자가 태그를 입력했을 때 그게 그대로 적용됨
        // 이걸 방지하려면 DOM을 직접 그려주는 것 : createElement -> 컨텐츠만 텍스트로 추가
        // 아니면 최소한의 방어책으로 사용자 입력값을 검증
        new_li.innerHTML = `<span class="${todo.done ? 'done' : ''}"><a class="modify" id="${todo.id}" href="">${escapeHTML(todo.todo)}</a></span> |<a class="delete" id="${todo.id}" href=""><i class="bi bi-trash"></i></a>`

        todoList.appendChild(new_li)
        
    })
}

// 사용자 입력값 검증
function escapeHTML(str) {
    // <> 태그 적용 안되게 처리
    return String(str)
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
}

async function createTodo() {
    const textInputElement = document.getElementById('text-input');
    const textInput = textInputElement.value.trim();

    if (!textInput) return;

    // 입력값 제거
    textInputElement.value = '';

    // try catch 문으로 예외(에러)처리 필요
    const response = await fetch('/api/todo', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({textInput})
    })
    const result = await response.json()
    console.log('POST result', result)
    
    // response와 result를 동시에 try catch를 할 수 있음. 단, 각각 예외처리 하는것이 더 좋은 코드
    // try {
    //     const response = await fetch('/api/todo', {
    //         method: 'POST',
    //         headers: { 'Content-Type': 'application/json' },
    //         body: JSON.stringify({textInput})
    //     })
    // } catch (err) {
    //     console.error('서버 요청 실패: ', err)
    // }

    // try {
    //     const result = await response.json()
    //     console.log('POST result', result)
    // } catch (err) {
    //     console.error('데이터 파싱 실패: ', err)
    // }

    // if (result.error) {
    //     alert('ToDo 등록이 실패했습니다. 다시 시도해 주세요')
    // }

    // 등록 성공 시 ToDo 목록 조회 호출
    loadTodos();
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
    loadTodos();
}

async function modifyTodo2(todo_id) {
    // 수정
    const response = await fetch(`/api/todo/${todo_id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' }
    })
    const result = await response.json()
    if (result.error) {
        alert('ToDo 수정이 실패했습니다. 다시 시도해 주세요')
    }

    // 수정 성공 시 ToDo 목록 조회 호출
    loadTodos();
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
    loadTodos();
}
