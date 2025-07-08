from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
# ALLOWED_FILE_EXT = ['png', 'jpg', 'jpeg', 'gif', 'png'] # 리스트
ALLOWED_FILE_EXT = {'png', 'jpg', 'jpeg', 'gif', 'png'} # set - 유닉한 리스트 (리스트와 기능은 동일하지만 좀 더 파이썬스러운 자료구조)

os.makedirs(UPLOAD_FOLDER, exist_ok=True) # 시작할 때 폴더가 없으면 만들어줘, 이미 있으면 괜찮아!!

def allowed_file(filename):
    # 파일명에 점이 있는지 확인
    if '.' not in filename:
        return False
    
    # 확장자 파트를 오른쪽부터 읽어서 찾아낸다
    ext = filename.rsplit('.', 1)[1].lower()

    # 확장자가 우리의 허용 목록에 있는지 확인한다.
    if ext in ALLOWED_FILE_EXT:
        return True
    else:
        False

def allowed_file_pythonic(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXT


@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['post'])
def upload_file():
    # print(request.form) # 이걸로 하면 파일명만 받아옴
    print(request.files) # 실제로 파일 내용까지 FileStorage라는 객체의 형태로 파일내용까지 받아옴

    file = request.files['file']
    print(file)

    if file.filename == '':
        return '파일이 올바르게 전송되지 않았습니다.'

    # 비지니스 로직 - 내가 정한 프로세싱 툴들을 여기에 하나 둘 씩 구현

    # 1. 사진 파일만 업로드 가능하게 한다.
    # 확장자를 본다 - jpg, jpeg, png, gif 등등
    if allowed_file_pythonic(file.filename):
        # 파일 저장하기 - 현재 폴더의 upload 안에 받은 파일명으로 저장하기
        filepath = os.path.join('./', UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return '파일 업로드에 성공하였습니다.'
    else:
        return '하용되지 않는 파일입니다.'

    # 파일 저장하기 - 현재 폴더의 upload 안에 받은 파일명으로 저장하기
    # filepath = os.path.join('./', UPLOAD_FOLDER, file.filename)
    # file.save(filepath)

    # return '파일 받았음'

if __name__ == '__main__':
    app.run(debug=True)

