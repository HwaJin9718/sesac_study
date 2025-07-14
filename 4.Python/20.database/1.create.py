import sqlite3

# DB 접속(연결)
conn = sqlite3.connect('example.db')

# 커서 객체 생성 : DB 접속한 후 내가 작업할 위치(커서) 생성
cur = conn.cursor()

# 커서를 중심으로 DB 입출력 진행
cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL, 
            age INTEGER NOT NULL
            )
            ''')

# 커민하여 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()
