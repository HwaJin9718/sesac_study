import sqlite3

DB_FILENAME = 'naver.db'

def connect_db():
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row # sqlite는 원래 튜플로 나옴, 이걸 쓰면 각각의 행이 튜플이 아닌 딕셔너리(dict) 형태로 반환
    return conn


# 테이블 생성
# id : 기본키
# naverid : 네이버에서 받아온 아이디
# username : 네이버에서 받아온 name
# nickname : 네이버에서 받아온 닉네임
# profileimg : 네이버에서 받아온 프로필 이미지
# email : 네이버에서 받아온 이메일
def create_table():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naverid TEXT UNIQUE NOT NULL,
            username TEXT NOT NULL,
            nickname TEXT NOT NULL, 
            profileimg TEXT NOT NULL,
            email TEXT NOT NULL
            )
    ''')

    conn.commit()
    conn.close()


def create_user(naverid, username, nickname, profileimg, email):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (naverid, username, nickname, profileimg, email) VALUES (?, ?, ?, ?, ?)", (naverid, username, nickname, profileimg, email))
    conn.commit()
    conn.close()


def get_user_by_naverid(naverid):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE naverid=?", (naverid, ))
    user = cur.fetchone()

    user = dict(user) if user else []

    conn.close()

    return user


def update_user(id, naverid, username, nickname, profileimg, email):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE users SET naverid=?, username=?, nickname=?, profileimg=?, email=? WHERE id=?", (naverid, username, nickname, profileimg, email, id))
    conn.commit()
    conn.close()

# 테스트 사용자 추가
# create_user('test_naver_id', 'test_name', 'test_nick_name', 'test_profile_image_url', 'test@naver.com')
# create_user('uuid', '송화진', '화진', 'https://ssl.pstatic.net/static/pwe/address/cat.jpg', 'test2@naver.com')
