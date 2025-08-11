document.addEventListener('DOMContentLoader', async () => {
    loadFileList();
})

async function loadFileList() {
    const fileList = document.getElementById('fileList');

    const response = await fetch('/file-list');
    const data = await response.json();

    console.log(data.file_list)

    fileList.innerHTML = data.file_list.map(fn => 
        `<li>
            ${fn} <button data-file="${fn}" class="delete-btn">삭제</button>
        </li>`
    ).join(''); // 리스트 순회 시 기본값 [oo,oo,oo]을 '' 공백으로 연결

    fileList.addEventListener('click', async (e) => {
        if (!e.target.matches('.delete-btn')) return;

        const filename = e.target.dataset.file;
        console.log('삭제하려고 함: ', filename)

        // if (!confirm(`${filename}을 정말 삭제하시겠습니까?`)) return;

        const response = await fetch(`/files/${filename}`, {method: 'DELETE'})
        const result = await response.json()
        console.log('요청한 결과 : ', result.message)

        loadFileList();
    })
}

async function uploadFile() {
    // 파일 업로드
    console.log('UPLOAD 실행')

    const fileInput = document.getElementById('fileInput');
    
    const formData = new FormData();

    for (i=0; i < fileInput.files.length; i++) {
        const file = fileInput.files[i];
        // console.log(file)
        formData.append('file', file);
    }

    // const file = fileInput.files[0];
    // console.log(file)

    // const formData = new FormData();
    // formData.append('file', file);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    alert(result.message)

    loadFileList();
}

async function askQuestion() {
    // 질문
    const questionInput = document.getElementById('questionInput');
    const question = questionInput.value;

    const response = await fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({question})
    })

    const data = await response.json()
    const answer = document.getElementById('answer');
    answer.innerHTML = data.message
}
