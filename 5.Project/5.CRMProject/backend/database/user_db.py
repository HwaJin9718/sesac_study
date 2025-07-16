import sqlite3

DATABASE = 'mycrm.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn


# 전체 users 조회
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    # dict 형태로 변환
    users = [dict(u) for u in users]

    return users


# 전체 users 조회 + paging 처리
def get_users_paging(current_page, items_per_page):
    offset = (current_page - 1) * items_per_page # 페이지가 이동될 때 몇개째부터 출력할지
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT ? OFFSET ?", (items_per_page, offset))
    users = cursor.fetchall()
    conn.close()

    # dict 형태로 변환
    users = [dict(u) for u in users]

    return users


# 전체 users의 count 조회
def get_user_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    conn.close()

    return user_count


# id로 users 조회
def get_user_by_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE Id=?", (id,))
    user = cursor.fetchone()
    conn.close()

    user = dict(user)

    return user

