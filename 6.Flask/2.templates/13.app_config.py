from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_FILE_EXT'] = {'png', 'jpg', 'jpeg', 'gif', 'png'}
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 # 1MB
# 참고 자료 : https://flask-docs-kr.readthedocs.io/ko/latest/patterns/fileuploads.html

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True) # 시작할 때 폴더가 없으면 만들어줘, 이미 있으면 괜찮아!!

def allowed_file(filename):
    # 파일명에 점이 있는지 확인
    if '.' not in filename:
        return False
    
    # 확장자 파트를 오른쪽부터 읽어서 찾아낸다
    ext = filename.rsplit('.', 1)[1].lower()

    # 확장자가 우리의 허용 목록에 있는지 확인한다.
    if ext in app.config['ALLOWED_FILE_EXT']:
        return True
    else:
        return False

def allowed_file_pythonic(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_FILE_EXT']

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER']) # 파일 목록 보여주기
    return render_template('upload.html', files=files)

@app.route('/upload', methods=['post'])
def upload_file():
    print(request.files) # 실제로 파일 내용까지 FileStorage라는 객체의 형태로 파일내용까지 받아옴

    file = request.files['file']
    print(file)

    if file.filename == '':
        return '파일이 올바르게 전송되지 않았습니다.'

    # 비지니스 로직 - 내가 정한 프로세싱 툴들을 여기에 하나 둘 씩 구현

    # 용량이 크면 MAX_CONTENT_LENGTH 가 동작해서 자동으로 예외 발생
    # 이런건 Flask 프레임워크가 자동으로 해줌
    # 다만 오류 메시지가 영어라 내가 원하는 대로(한글) formatting이 필요

    # 1. 사진 파일만 업로드 가능하게 한다.
    if allowed_file_pythonic(file.filename):
        filepath = os.path.join('./', app.config['UPLOAD_FOLDER'], file.filename)
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

# 413이 발생했을 때의 오류 핸들러를 커스텀으로 등록
# 이것이 flask 프레임워크를 잘 사용하는 방법
@app.errorhandler(413)
def too_large(e):
    size_mb = app.config['MAX_CONTENT_LENGTH'] / (1024 * 1024)
    return f"업로드한 파일이 너무 큽니다. 최대 {size_mb}MB 까지만 허용합니다."

if __name__ == '__main__':
    app.run(debug=True)

