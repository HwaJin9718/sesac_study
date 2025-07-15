from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # app.py에서 db.init_app(app) 로 초기화 시켰기 때문에 app은 불필요
# db = SQLAlchemy(app) 

# 사용자 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    # 객체를 print로 출력할 때의 포멧 정의하는 함수 , 개발자 디버깅용
    def __repr__(self):
        return f"출력 <User {self.id} {self.name} {self.age}>"
    
    # 객체를 문자열로 출력 - string casting, print 로 출력 시 해당 포멧으로 나옴
    def __str__(self):
        return f"문자열 변환 <User {self.id} {self.name} {self.age}>"
