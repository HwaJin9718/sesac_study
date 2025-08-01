import sqlite3
import hashlib

DB_FILENAME = 'users.db'

# 테스트 가능하도록 DB 초기화
conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# 테이블 생성
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        name TEXT NOT NULL
        )
''')

# 테스트 사용자 추가
hash_pw1 = hash_password('password1')
hash_pw2 = hash_password('password2')

cur.execute("INSERT INTO users (username, password, name) VALUES (?, ?, ?)", ('user1', hash_pw1, 'UserName1'))
cur.execute("INSERT INTO users (username, password, name) VALUES (?, ?, ?)", ('user2', hash_pw2, 'UserName2'))

conn.commit()
conn.close()
