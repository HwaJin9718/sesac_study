from flask import Flask, jsonify, url_for, render_template, request

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get("q", "").lower()
    results = []
    for item in images:
        # found = False
        # for keyword in item["keywords"]:
        #     if query in keyword:
        #         found = True
        #         # break # 이미지 하나만 찾을 때 쓰기
        # if found:
        #     image_url = url_for('static', filename=f'img/{item["filename"]}')
        #     results.append(image_url)
        
        # pythonic하게 한줄로
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static', filename=f'img/{item["filename"]}')
            results.append(image_url)

    # return jsonify({"url": results}) # 순수 backend 개발자는 여기까지
    return render_template("result.html", query=query, results=results)

@app.route('/admin')
def admin():
    file_path = "static/img/"
    return render_template("admin.html", images=images, path=file_path)

@app.route('/upload', methods=["POST"])
def upload():
    return 'upload 호출'

@app.route('/modify')
def keywords_modify():
    return 'modify 호출'

@app.route('/remove')
def remove():
    return 'remove 호출'

if __name__ == '__main__':
    app.run(debug=True)
