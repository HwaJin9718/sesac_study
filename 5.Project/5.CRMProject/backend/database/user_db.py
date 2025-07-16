import sqlite3

DATABASE = 'mycrm.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn


def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    # dict 형태로 변환
    users = [dict(u) for u in users]

    return users

