from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # app.py에서 db.init_app(app) 로 초기화 시켰기 때문에 app은 불필요
# db = SQLAlchemy(app) 

# 사용자 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
