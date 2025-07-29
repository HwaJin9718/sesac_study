function membership() {

    const input_name = document.querySelector('input[name="name"]').value;
    const input_gender = document.querySelector('select[name="gender"]').value;
    const input_birthdate = document.querySelector('input[name="birthdate"]').value;
    const input_address = document.querySelector('input[name="address"]').value;

    const formData = new FormData();
    formData.append('name', input_name);
    formData.append('gender', input_gender);
    formData.append('birthdate', input_birthdate);
    formData.append('address', input_address);

    // console.log('이름:', formData.get('name'));
    // console.log('성별:', formData.get('gender'));
    // console.log('생년월일:', formData.get('birthdate'));
    // console.log('주소:', formData.get('address'));

    fetch('/api/cus/membership', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(create_user => {
            alert(`계정이 생성되었습니다. ${create_user.create_user.Id}`);
            window.location.href = '/';
        })
}

document.getElementById('membership').addEventListener('submit', (e) => {
    e.preventDefault(); // form의 기본 submit 동작 방지
    membership()
})

document.getElementById('back-login').addEventListener('click', () => {
    window.location.href = '/';
})
