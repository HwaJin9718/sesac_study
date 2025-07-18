import sqlite3

DATABASE = 'mycrm.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn


# 전체 item 조회
def get_items():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()

    # dict 형태로 변환
    items = [dict(i) for i in items]

    return items


# 전체 item 조회 + paging 처리
def get_items_paging(current_page, items_per_page):
    offset = (current_page - 1) * items_per_page # 페이지가 이동될 때 몇개째부터 출력할지
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items LIMIT ? OFFSET ?", (items_per_page, offset))
    items = cursor.fetchall()
    conn.close()

    # dict 형태로 변환
    items = [dict(i) for i in items]

    return items


# 전체 item의 count 조회
def get_item_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM items")
    item_count = cursor.fetchone()[0]
    conn.close()

    return item_count


# id로 item 조회
def get_item_by_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE Id=?", (id,))
    item = cursor.fetchone()
    conn.close()

    item = dict(item)

    return item


# type으로 item 조회
def get_item_by_type(type, current_page, items_per_page):
    offset = (current_page - 1) * items_per_page # 페이지가 이동될 때 몇개째부터 출력할지
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE Type=? LIMIT ? OFFSET ?", (type, items_per_page, offset))
    items = cursor.fetchall()
    conn.close()

    items = [dict(i) for i in items]

    return items


# type으로 조회된 item의 count 
def get_store_by_name_count(type):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM items WHERE Type=?", (type,))
    item_count = cursor.fetchone()[0]
    conn.close()

    return item_count

