import sqlite3

# db에 접속하는 함수
MY_DATABASE = 'users.db'

def connect_db():
    conn = sqlite3.connect(MY_DATABASE)
    conn.row_factory = sqlite3.Row # sqlite는 원래 튜플로 나옴, 이걸 쓰면 각각의 행이 튜플이 아닌 딕셔너리(dict) 형태로 반환
    return conn

# 테이블 생성 함수
def create_table():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL, 
            age INTEGER NOT NULL
            )
            ''')

    conn.commit()
    conn.close()

# 데이터 삽입 함수
def insert_user(name, age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("INSERT INTO users(name, age) VALUES (?, ?)", (name, age))

    conn.commit()
    conn.close()

# 데이터 조회 함수
def get_users():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    conn.commit()
    conn.close()

    return rows

def get_users_by_name(name):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE name=?", (name,))
    user = cur.fetchone()

    conn.commit()
    conn.close()

    return user

def get_users_by_id(id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE id=?", (id,))
    user = cur.fetchone()

    conn.commit()
    conn.close()

    return user

# 데이터 수정 함수
def update_user_age(name, new_age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("UPDATE users SET age=? WHERE name=?", (new_age, name))

    conn.commit()
    conn.close()

def update_user(id, new_name, new_age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("UPDATE users SET name=?, age=? WHERE id=?", (new_name, new_age, id))

    conn.commit()
    conn.close()

# 데이터 삭제 함수
def delete_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE name=?", (name,))

    conn.commit()
    conn.close()

def delete_user_by_age(age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE age=?", (age,))

    conn.commit()
    conn.close()

def delete_user_by_id(id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE id=?", (id,))

    conn.commit()
    conn.close()
