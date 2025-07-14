import sqlite3

# DB 접속(연결)
conn = sqlite3.connect('example.db')

# 커서 객체 생성 : DB 접속한 후 내가 작업할 커서 생성
cur = conn.cursor()

# ----------------------

# 데이터 삽입
cur.execute('''
    INSERT INTO users (name, age) VALUES ('Alice', 30)
''')

cur.execute('''
    INSERT INTO users (name, age) VALUES ('Bob', 25)
''')

# 인자로도 값을 받아서 넣을 수 있음
# ? 는 placeholder
# prepared statement 라고 부름, SQL injection 공격을 막는 패던
cur.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Charlie', 40))

# ----------------------

# 커민하여 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()
