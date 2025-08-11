import os
from flask import Flask, request, jsonify
from vectorstore import initialize_vector_db, create_vector_db, delete_file_from_vector
from chatbot import initialize_llm, answer_question

app = Flask(__name__, static_url_path='')

DATA_DIR = './DATA'

# 미션1. 파일 여러개 업로드
# 미션2. 현재 등록된 파일 목록 보여주기

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': '파일이 없습니다.'}), 404
    
    # file = request.files['file']
    # file_path = ''
    # if file:
    #     file_path = os.path.join(DATA_DIR, file.filename)
    #     file.save(file_path)

    # 받아온 문서를 백터DB에 추가한다.
    # store = create_vector_db(file_path)

    # if store:
    #     return jsonify({'message': '파일이 성공적으로 업로드 되었습니다.'}), 200
    # else:
    #     return jsonify({'message': '파일이 UPLOAD 되었으나, DB가 정상적으로 생성되지 못했습니다.'}), 500
    
    files = request.files.getlist('file')
    create_count = 0
    if files:
        for file in files:
            file_path = os.path.join(DATA_DIR, file.filename)
            file.save(file_path)

            # 받아온 문서를 백터DB에 추가한다.
            store = create_vector_db(file_path)

            if store:
                create_count += 1
            else:
                jsonify({'message': '파일이 UPLOAD 되었으나, DB가 정상적으로 생성되지 않았습니다.'}), 500
    
    if create_count > 0:
        return jsonify({'message': '파일이 성공적으로 업로드 되었습니다.'}), 200
    else:
        return jsonify({'message': '파일이 UPLOAD 되었으나, DB가 정상적으로 생성되지 않았습니다.'}), 500


@app.route('/ask', methods=['POST'])
def chatbot():
    data = request.get_json()
    question = data.get('question', '')

    response = answer_question(question)

    if response:
        return jsonify({'message': f'챗봇 답변 : {response}'}), 200
    else:
        return jsonify({'message': '챗봇 답변을 받지 못했습니다.'}), 500


@app.route('/file-list')
def get_file_list():

    # file_names = []
    # for filename in os.listdir(DATA_DIR):
    #     file_names.append(filename)

    file_names = [f for f in os.listdir(DATA_DIR) if os.path.isfile(os.path.join(DATA_DIR, f))]

    return jsonify({'file_list' : file_names})


@app.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    # vector DB 에서 삭제
    delete_file_from_vector(filename)

    # 물리적인 삭제
    path = os.path.join(DATA_DIR, filename)

    if os.path.exists(path):
        os.remove(path)

    return jsonify({'message' : f'{filename}을 삭제하였습니다.'})


if __name__ == '__main__':
    initialize_vector_db()
    initialize_llm()
    app.run(debug=True)
