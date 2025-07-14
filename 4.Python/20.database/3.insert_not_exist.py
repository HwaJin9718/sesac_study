import sqlite3

# DB 접속(연결)
conn = sqlite3.connect('example.db')

# 커서 객체 생성 : DB 접속한 후 내가 작업할 커서 생성
cur = conn.cursor()

# ----------------------

# 데이터 조회
cur.execute('SELECT COUNT(*) FROM users')
count = cur.fetchone()[0]

if count == 0: # 사용자가 없으면 그때 삽입
    # 데이터 삽입
    cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
    cur.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Charlie', 40))
else:
    print('이미 데이터가 존재해서 더이상 삽입하지 않을것임.')
    print('현재 있는 사용자 데이터 갯수:', count)

# ----------------------

# 커민하여 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()
