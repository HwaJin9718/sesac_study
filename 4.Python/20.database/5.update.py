import sqlite3

# DB 접속(연결)
conn = sqlite3.connect('example.db')

# 커서 객체 생성 : DB 접속한 후 내가 작업할 커서 생성
cur = conn.cursor()

# ----------------------

# 데이터 수정
cur.execute('UPDATE users SET age=10 WHERE name="Alice"')

cur.execute('UPDATE users SET age=? WHERE id=?', (50, 1))

# ----------------------

# 커민하여 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()
