from flask import Flask, jsonify, url_for, render_template, request, redirect
import os

app = Flask(__name__)

# 글로벌 변수
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

@app.route('/')
def index():
    query = request.args.get("q", "").lower()
    results = []

    for item in images:
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static', filename=f'img/{item["filename"]}')
            results.append(image_url)

    return render_template('index.html', query=query, results=results)

@app.route('/admin')
def admin():
    return render_template('admin.html', images=images)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('image')
    keywords = request.form.get('keywords')

    if file:
        filename = file.filename
        filepath = os.path.join('static', 'img', filename)
        file.save(filepath)
        images.append({'filename':filename, 'keywords' : keywords.lower().split(',')})

    return redirect(url_for('admin'))

@app.route('/update/<filename>', methods=['POST'])
def update_keywords(filename):
    new_keywords = request.form.get('keywords')
    for i in images:
        if i["filename"] == filename:
            i["keywords"] = [word.strip() for word in new_keywords.lower().split(',') if len(word.strip())]
            break
    
    return redirect(url_for('admin'))

@app.route('/delete/<filename>')
def delete_image(filename):
    print(f"삭제할 파일 : {filename}")
    # 글로벌 변수를 읽어가는건 문제되지 않으나 수정 시 global로 설정해줘야만 해당 변수 안의 내용 수정가능
    global images 

    # 삭제할 항목 제외, 나머지 다시 넣기
    images = [
        img
        for img in images
        if img["filename"] != filename
    ]

    # 실제로 이미지 삭제
    filepath = os.path.join('static', 'img', filename)
    if os.path.exists(filepath):
        # os.remove(filepath) # 실제 지우지는 않을거야!
        print(f"{filename} 파일 지웠다고 치자")

    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
