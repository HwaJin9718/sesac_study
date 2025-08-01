from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
# SQLAlchemy 공식 문서 : https://docs.sqlalchemy.org/en/20/

engine = create_engine('sqlite:///users.db')

Base = declarative_base()

# 테이블 설계 - 객체 설계
# 사용자 "모델" 정의

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

# ----------------------
# CRUD 함수 만들기

def create_user(session, name:str, age:int) -> User:
    # 구현, 위 프로토타입을 보고 적절한 타입/변수 리턴하기
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    return new_user

def get_users(session) -> list[User]:
    # 인자 안받고 사용자 리스트 리턴
    return session.query(User).all()

def get_user_by_id(session, user_id:int) -> User|None:
    # 사용자 ID 받아서 사용자 반환, 사용자 없을 수 있음
    # return session.query(User).filter_by(id=user_id).first() # -> 이렇게도 할 수 있음
    return session.get(User, user_id) # SQLalchemy 2.x 버전부터 새롭게 등장

def update_user_age(session, user_id:int, new_age:int) -> bool:
    # 사용자 아이디와 나이를 받아서, 나이 업데이트하기
    # 그냥 객체에 값만 설정하면 자동으로 쓰임 (물론 sess.commit() 했을 때)
    user = session.get(User, user_id)

    if not user:
        return False
    
    user.age = new_age
    session.commit()

    return True

def delete_user_by_id(session, user_id:int) -> bool:
    # 사용자를 삭제하고 성공 시 True 리턴
    user = session.get(User, user_id)

    if not user:
        return False
    
    session.delete(user)
    session.commit()

    return True

def delete_user_by_name(session, user_name:str) -> int:
    # 사용자를 삭제하고 성공 시 삭제한 사용자 수를 리턴
    users = session.query(User).filter_by(name=user_name).all()

    if not users:
        return 0
    
    for u in users:
        session.delete(u)

    session.commit()

    return len(users)

# ----------------------

if __name__ == '__main__':
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    with Session() as sess:

        # 1. 사용자 생성
        alice = create_user(sess, "Alice", 30)
        bob = create_user(sess, "Bob", 25)
        print(f"추가된 사용자 ID: {alice.id}, {bob.id}")

        # 2. 사용자 조회
        user1 = get_user_by_id(sess, alice.id)
        print(f"조회한 사용자 정보: {user1.name, user1.age}")

        user2 = get_user_by_id(sess, bob.id)
        print(f"조회한 사용자 정보: {user2.name, user2.age}")

        # 3. 정보 수정
        update_alice = update_user_age(sess, alice.id, 29)
        print(f"업데이트 성공실패 여부 확인: {update_alice}")

        # 4. 사용자 모두 조회
        users = get_users(sess)
        for u in users:
            print(f"아이디: {u.id}, 이름: {u.name}, 나이: {u.age}세")

        # 5. 사용자 삭제
        delete_alice = delete_user_by_id(sess, alice.id)
        print(f"Alice 삭제 성공실패 여부 : {delete_alice}")

        del_user_count = delete_user_by_name(sess, bob.name)
        print(f"Bob 이라는 사용자를 모두 삭제한 개수 : {del_user_count}")

        # 6. 최종 사용자 목록
        users = get_users(sess)
        for u in users:
            print(f"아이디: {u.id}, 이름: {u.name}, 나이: {u.age}세")
