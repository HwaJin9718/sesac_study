from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
# ALLOWED_FILE_EXT = ['png', 'jpg', 'jpeg', 'gif', 'png'] # 리스트
ALLOWED_FILE_EXT = {'png', 'jpg', 'jpeg', 'gif', 'png'} # set - 유닉한 리스트 (리스트와 기능은 동일하지만 좀 더 파이썬스러운 자료구조)

os.makedirs(UPLOAD_FOLDER, exist_ok=True) # 시작할 때 폴더가 없으면 만들어줘, 이미 있으면 괜찮아!!

def allowed_file(filename):
    # 파일명에 .(점)이 있는지 확인
    if '.' not in filename:
        return False
    
    # 확장자 파트를 오른쪽부터 읽어서 찾아낸다
    ext = filename.rsplit('.', 1)[1].lower()

    # 확장자가 우리의 허용 목록에 있는지 확인한다.
    if ext in ALLOWED_FILE_EXT:
        return True
    else:
        return False

def allowed_file_pythonic(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXT

def get_file_size(file):
    pos = file.stream.tell() # 현재 (이전 작업을 고려해서) 현재 파일의 위치를 저장
    file.stream.seek(0, os.SEEK_END) # 파일의 끝으로 가라
    size = file.stream.tell() # 너의 위치(파일의 끝)를 기반으로 크기를 알려줘
    file.stream.seek(pos) # 다시 너의 원래 위치로 가라
    return size

# 미션1. 업로드된 파일 목록 보여주기
# 미션1-2. 각각의 파일명 옆에 삭제 버튼 추가
# 미션1-3. 파일 용량 체크 및 1MB 이상의 파일인 경우 사용자에게 "용량이 너무 큼" 알려준다
# 미션2. 실제로 해당 파일을 삭제

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER) # 파일 목록 보여주기
    return render_template('upload.html', files=files)


@app.route('/upload', methods=['post'])
def upload_file():
    # print(request.form) # 이걸로 하면 파일명만 받아옴
    print(request.files) # 실제로 파일 내용까지 FileStorage라는 객체의 형태로 파일내용까지 받아옴

    file = request.files['file']
    print(file)

    if file.filename == '':
        return '파일이 올바르게 전송되지 않았습니다.'

    # 비지니스 로직 - 내가 정한 프로세싱 툴들을 여기에 하나 둘 씩 구현

    # 2. 용량을 보고 크기가 1MB 보다 크면 허용하지 않는다.
    file_size = get_file_size(file)
    max_size = 1 * 1024 * 1024 # 1MB = 1KB가 1024개인것, 1KB는 1byte가 1024개 인것
    print('파일사이즈:', file_size, max_size, (file_size > max_size))
    if file_size > max_size:
        return '파일 용량이 너무 큽니다. 1MB보다 작은 파일을 올려주세요'

    # 1. 사진 파일만 업로드 가능하게 한다.
    # 확장자를 본다 - jpg, jpeg, png, gif 등등
    if allowed_file_pythonic(file.filename):
        # 파일 저장하기 - 현재 폴더의 upload 안에 받은 파일명으로 저장하기
        filepath = os.path.join('./', UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        # return '파일 업로드에 성공하였습니다.'
        return redirect(url_for('index'))
    else:
        return '하용되지 않는 파일입니다.'


@app.route('/delete/<filename>')
def delete_file(filename):
    filepath = os.path.join('./', 'uploads', filename)

    if os.path.exists(filepath):
        os.remove(filepath)
        # return '파일 삭제가 완료되었습니다.'
        return redirect(url_for('index'))
    else:
        return '해당 파일은 존재하지 않습니다.'


if __name__ == '__main__':
    app.run(debug=True)
