function login() {

    const user_id = document.querySelector('input[name="user_id"]').value;
    const user_pw = document.querySelector('input[name="user_pw"]').value;

    const formData = new FormData();
    formData.append('user_id', user_id);
    formData.append('user_pw', user_pw);

    fetch(`/api/login/admin`, {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(result => {
            // console.log(result.message)
            if (result.message === true) {
                window.location.href = '/api/user';
            } else {
                alert('입력한 아이디/비밀번호가 맞지 않습니다.')
            }
        })
}

document.getElementById('login_form').addEventListener('submit', (e) => {
    e.preventDefault(); // form의 기본 submit 동작 방지
    login()
})

document.getElementById('user-button').addEventListener('click', () => {
    window.location.href = '/';
})

document.getElementById('admin-button').addEventListener('click', () => {
    window.location.href = '/admin';
})
