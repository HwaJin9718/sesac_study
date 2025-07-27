import sqlite3

DATABASE = 'mycrm.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn


# 전체 order item 조회
def get_order_items():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orderitems")
    orderitems = cursor.fetchall()
    conn.close()

    # dict 형태로 변환
    orderitems = [dict(o) for o in orderitems]

    return orderitems


# 전체 order item 조회 + paging 처리
def get_order_items_paging(current_page, items_per_page):
    offset = (current_page - 1) * items_per_page # 페이지가 이동될 때 몇개째부터 출력할지
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orderitems LIMIT ? OFFSET ?", (items_per_page, offset))
    orderitems = cursor.fetchall()
    conn.close()

    # dict 형태로 변환
    orderitems = [dict(o) for o in orderitems]

    return orderitems


# 전체 order item의 count 조회
def get_order_item_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM orderitems")
    orderitem_count = cursor.fetchone()[0]
    conn.close()

    return orderitem_count


# order 에서 id 클릭하고 들어가
# -> orderitems 테이블에서 order_id로 검색하면 나오는 내용 + item_name 까지 같이 나옴
# order_item 에서 order_id 클릭하고 들어가
# -> orders 테이블에서 id로 검색하면 나오는 내용
# id로 orders 조회
def get_order_item_by_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                   select OI.Id as Id, OI.OrderId as OrderId, OI.ItemId as ItemId, I.Name as Name
                   from orderitems OI
                            left join items I on OI.ItemId = I.Id
                   WHERE OI.OrderId = ?''', (id,))
    orderitems = cursor.fetchall()
    conn.close()

    orderitems = [dict(o) for o in orderitems]

    return orderitems


# order item 생성
def create_order_item(order_item_id, order_id, item_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                    insert into orderitems (Id, OrderId, ItemId)
                    values (?, ?, ?)
                    ''', (order_item_id, order_id, item_id))
    conn.commit()
    conn.close()


# order id로 orderitems 조회
def get_order_item_by_order_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orderitems WHERE OrderId=?", (id,))
    orderitems = cursor.fetchall()
    conn.close()

    # dict 형태로 변환
    orderitems = [dict(o) for o in orderitems]

    return orderitems

