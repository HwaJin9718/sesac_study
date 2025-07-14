import sqlite3

# DB 접속(연결)
conn = sqlite3.connect('example.db')

# 커서 객체 생성 : DB 접속한 후 내가 작업할 커서 생성
cur = conn.cursor()

# ----------------------

# 데이터 조회
cur.execute('''
    SELECT * FROM users
''')

# 조회 결과 가져오기
rows = cur.fetchall() # fetchall() - 모든 행 다 가져오기
# print(rows) # 전체를 다 출력

for row in rows:
    print(row) # 한줄 씩 출력

print('-' * 10)

# 데이터 조회
cur.execute('''
    SELECT * FROM users
''')

rows = cur.fetchone()
print(rows)

print('-' * 10)

# 데이터 조회 fetchall
cur.execute('SELECT COUNT(*) FROM users')
rows = cur.fetchall() # count로 값은 하나인데 fetchall 사용하여 리스트에 굳이 담을거냐?
print(rows)

# 데이터 조회 fetchone
cur.execute('SELECT COUNT(*) FROM users')
rows = cur.fetchone() # 하나의 값을 받아왔으나 결과 튜플
print(rows)

# 데이터 조회 fetchone 첫번째 항목
cur.execute('SELECT COUNT(*) FROM users')
rows = cur.fetchone()[0] # 하나의 값을 받아와서 첫번째 항목 가져오기
print(rows)

# ----------------------

# 커민하여 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()
