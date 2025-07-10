from flask import Flask, url_for, request, send_from_directory, jsonify
from flask_cors import CORS
# pip install flask-cors

app = Flask(__name__)
CORS(app)  # 나의 서버에 누구든지 와서 정보를 요청할수 있음.

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

@app.route('/search')
def sss():
    return send_from_directory(app.static_folder, 'search.html')

@app.route('/api/search')
def search():
    query = request.args.get("q", "").lower()
    results = []
    
    for item in images:
        
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static', filename=f'img/{item["filename"]}')
            results.append(image_url)

    return jsonify({"url": results}) # 순수 backend 개발자는 여기까지

if __name__ == '__main__':
    app.run(debug=True)
