from flask import Flask, url_for, request, send_from_directory, jsonify

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
    return jsonify({"images": images}, {"path": file_path})

@app.route('/api/upload', methods=["POST"])
def upload():
    return 'upload 호출'

@app.route('/api/modify')
def keywords_modify():
    return 'modify 호출'

@app.route('/api/remove')
def remove():
    return 'remove 호출'

if __name__ == '__main__':
    app.run(debug=True)
