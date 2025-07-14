import sqlite3

# DB 접속(연결)
conn = sqlite3.connect('example.db')

# 커서 객체 생성 : DB 접속한 후 내가 작업할 커서 생성
cur = conn.cursor()

# ----------------------

# 데이터 삭제
cur.execute('DELETE FROM users WHERE name="Alice"')

# 인자를 한가지만('Bob') 넣는 경우 이것이 튜플인지, () 단일 인자를 말한건지, (1==1) 이런 형태의 Ture/False를 계산하려는건지 모름
# 그래서 단일 인자일 때 튜플을 강제로 표현하기 위해서 빈 콤마를 넣어줌 -> ('값',)
cur.execute('DELETE FROM users WHERE name=?', ('Bob', )) 

# ----------------------

# 커민하여 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()