from flask import Flask, url_for, request, send_from_directory, jsonify, redirect
import os

app = Flask(__name__)

images = [
    {"filename" : "cat.jpg", "keywords" : ["cat", "animal", "pet", "cute", "baby"]},
    {"filename" : "cat2.jpg", "keywords" : ["cat", "animal", "pet", "two", "baby", "sleep"]},
    {"filename" : "cat3.jpg", "keywords" : ["cat", "animal", "pet", "eye"]},
    {"filename" : "cat4.jpg", "keywords" : ["cat", "animal", "pet", "hand", "cute"]},
    {"filename" : "dog1.jpg", "keywords" : ["dog", "animal", "pet", "smile"]},
    {"filename" : "dog2.jpg", "keywords" : ["dog", "animal", "pet", "eye"]},
    {"filename" : "fox.jpg", "keywords" : ["fox", "animal", "eye", "big ear"]},
    {"filename" : "panda.jpg", "keywords" : ["panda", "animal", "eat", "hand"]},
]

app.config['UPLOAD_FOLDER'] = 'static/img'
app.config['ALLOWED_FILE_EXT'] = {'png', 'jpg', 'jpeg', 'gif', 'png'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file_pythonic(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_FILE_EXT']

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/search')
def search():
    query = request.args.get("q", "").lower()
    results = []
    
    for item in images:
        
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static', filename=f'img/{item["filename"]}')
            results.append(image_url)

    return jsonify({"url": results}) # 순수 backend 개발자는 여기까지

@app.route('/admin')
def admin():
    return send_from_directory(app.static_folder, 'admin.html')

@app.route('/api/images')
def get_images():
    file_path = "static/img/"
    return jsonify({"images": images, "path": file_path})

@app.route('/api/upload', methods=["POST"])
def upload():

    file = request.files['file']
    keywords = request.form.get('keywords')
    # print(keywords)

    if file.filename == '':
        return '파일이 올바르게 전송되지 않았습니다.'
    
    # 1. 사진 파일만 업로드 가능하게 한다.
    if allowed_file_pythonic(file.filename):
        filepath = os.path.join('./', app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # 리스트에 해당 값 저장
        if keywords:
            keywords_list = [keyword.strip() for keyword in keywords.split(',')]
        else:
            keywords_list = []

        images.append({ "filename" : file.filename  ,  "keywords" : keywords_list })

        return redirect(url_for('admin'))
        # return send_from_directory(app.static_folder, 'admin.html')
    else:
        return '하용되지 않는 파일입니다.'


@app.route('/api/modify', methods=["POST"])
def keywords_modify():

    filename = request.form.get('filename')
    new_keywords = request.form.get('keywords')

    if new_keywords:
        keywords_list = [keyword.strip() for keyword in new_keywords.split(',')]
    else:
        keywords_list = []

    for img in images:
        if img["filename"] == filename:
            img["keywords"] = keywords_list
            break

    return redirect(url_for('admin'))
    # return send_from_directory(app.static_folder, 'admin.html')


@app.route('/api/remove/<filename>')
def remove(filename):

    filepath = os.path.join('./', 'static/img', filename)

    if os.path.exists(filepath):
        # 실제 이미지 삭제
        os.remove(filepath)
        
        # 리스트에서 filename 삭제
        for img in images[:]:
            if img["filename"] == filename:
                images.remove(img)

        return redirect(url_for('admin'))
        # return send_from_directory(app.static_folder, 'admin.html')
    else:
        return '해당 파일은 존재하지 않습니다.'

# @app.route('/api/upload', methods=["POST"])
# def upload():
#     return 'upload 호출'

# @app.route('/api/modify')
# def keywords_modify():
#     return 'modify 호출'

# @app.route('/api/remove')
# def remove():
#     return 'remove 호출'

if __name__ == '__main__':
    app.run(debug=True)
