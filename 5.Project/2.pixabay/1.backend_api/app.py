from flask import Flask, jsonify, url_for
import random

app = Flask(__name__)

dog_images = [
    "cat.jpg",
    "cat2.jpg",
    "cat3.jpg",
    "cat4.jpg",
    "dog1.jpg",
    "dog2.jpg",
    "fox.jpg",
    "panda.jpg"
]

# http://localhost:5000/static/img/파일명 -> static에 있는 이미지 확인 가능

@app.route('/random-dog')
def random_dog():
    random_img = random.choice(dog_images)
    # image_url = url_for('static', filename=f'img/{random_img}') # 상대경로가 만들어짐
    image_url = url_for('static', filename=f'img/{random_img}', _external=True) # 절대경로 만들기
    return jsonify({"url": image_url})

if __name__ == '__main__':
    app.run(debug=True)
