import sqlite3

DATABASE = 'mycrm.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# ------- user ------------

def get_user_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    conn.close()

    return user_count


def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    return users


def get_users_per_page(page, count):
    offset_pos = (page - 1) * count
    print(f"page : {page}, offset_pos : {offset_pos}")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT ? OFFSET ?", (count, offset_pos))
    users = cursor.fetchall()
    conn.close()

    return users

# ------- store ------------

def get_stores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores")
    stores = cursor.fetchall()
    conn.close()

    return stores


def get_stores_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM stores WHERE Name LIKE ?", ('%' + name + '%', ))
    stores = cursor.fetchall()
    conn.close()

    return stores
