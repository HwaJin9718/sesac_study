# pip install flask-sqlalchemy

from flask import Flask, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db' 
db.init_app(app) # 초기화

# def create_app():
#     app = Flask(__name__)
#     # 이게 실행되면 instance 폴더가 생성됨 -> 거기에 db 파일 만들어짐
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db' 
#     db.init_app(app) # 초기화
#     return app

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    age = int(request.form.get('age'))

    # 필요한 에러체크를 더 넣는게 좋음 - 중복사용자/누락된 데이터 등등(지금은 생략)
    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/') # redirect(url_for('index')) 가 좀 더 나은 코드이기는 함

@app.route('/delete/<int:id>')
def delete_user(id):
    user = db.session.get(User, id)

    if user:
        db.session.delete(user)
        db.session.commit()
    else:
        # 사용자 없으면 팝업을 띄우는것 -> 이건 따로 배워야함 일단 지금은 안배웠으니 pass
        print('사용자 없음: ', id)
    
    return redirect('/')

@app.route('/modify/<int:id>', methods=['GET', 'POST'])
def modify_user(id):
    user = db.session.get(User, id)

    if request.method == 'POST':
        new_name = request.form.get('name')
        new_age = int(request.form.get('age'))
        print(f"새로운 이름 : {new_name}, 새로운 나이 : {new_age}")

        user.name = new_name
        user.age = new_age
        db.session.commit()
        
        return redirect(url_for('index'))

    return render_template('modify.html', user=user)

if __name__ == '__main__':
    # app = create_app()
    app.run(debug=True)
