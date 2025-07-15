from app import app
# from app import create_app
from models import db, User

# 해당 파일은 초기화 하기 위해 만든것

# app = create_app()

# DB 사용자 테스트
with app.app_context(): # 위 flask app이 생성되고 초기화 되어 준비가 되었을 때
    db.drop_all() # 모든 테이블 삭제
    db.create_all() # 새로 초기화 -> 테이블 생성

    db.session.add(User(name="Alice", age=30))
    db.session.add(User(name="Bob", age=25))
    db.session.add(User(name="Charlie", age=20))
    db.session.commit()

    # models의 __repr__ 함수 실행
    users = User.query.all()
    print(users)
    
    # models의 __str__ 함수 실행
    for u in User.query.all():
        print(u)

    # print 구문으로 출력
    for u in User.query.all():
        print(u.id, u.name, u.age)
