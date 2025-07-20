import sqlite3

DATABASE = 'mycrm.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn


# 전체 store 조회
def get_stores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores")
    stores = cursor.fetchall()
    conn.close()

    # dict 형태로 변환
    stores = [dict(s) for s in stores]

    return stores


# 전체 stores 조회 + paging 처리
def get_stores_paging(current_page, items_per_page):
    offset = (current_page - 1) * items_per_page # 페이지가 이동될 때 몇개째부터 출력할지
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores LIMIT ? OFFSET ?", (items_per_page, offset))
    stores = cursor.fetchall()
    conn.close()

    # dict 형태로 변환
    stores = [dict(s) for s in stores]

    return stores


# 전체 stores의 count 조회
def get_store_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM stores")
    store_count = cursor.fetchone()[0]
    conn.close()

    return store_count


# id로 stores 조회
def get_store_by_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores WHERE Id=?", (id,))
    store = cursor.fetchone()
    conn.close()

    store = dict(store)

    return store


# name으로 store 조회
def get_store_by_name(name, current_page, items_per_page):
    offset = (current_page - 1) * items_per_page # 페이지가 이동될 때 몇개째부터 출력할지
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores WHERE Name LIKE ? LIMIT ? OFFSET ?", ('%' + name + '%', items_per_page, offset))
    stores = cursor.fetchall()
    conn.close()

    stores = [dict(s) for s in stores]

    return stores


# name으로 조회된 store의 count 
def get_store_by_name_count(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM stores WHERE Name LIKE ?", ('%' + name + '%',))
    store_count = cursor.fetchone()[0]
    conn.close()

    return store_count


# store id로 store의 월간 매출액 조회
def get_store_month_revenue_by_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                    select strftime('%Y-%m', O.OrderAt) as Month, sum(I.UnitPrice) as Revenue, count(I.Id) as Count
                    from orders O
                            left join orderitems OI on O.Id = OI.OrderId
                            left join items I on OI.ItemId = I.Id
                    where O.StoreId = ?
                    group by strftime('%Y-%m', O.OrderAt);
                    ''', (id, ))
    month_revenues = cursor.fetchall()
    conn.close()

    store_revenues = [dict(r) for r in month_revenues]

    return store_revenues


