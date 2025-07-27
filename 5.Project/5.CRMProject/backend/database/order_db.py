import sqlite3

DATABASE = 'mycrm.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn


# 전체 order 조회
def get_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()

    # dict 형태로 변환
    orders = [dict(o) for o in orders]

    return orders


# 전체 orders 조회 + paging 처리
def get_orders_paging(current_page, items_per_page):
    offset = (current_page - 1) * items_per_page # 페이지가 이동될 때 몇개째부터 출력할지
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders LIMIT ? OFFSET ?", (items_per_page, offset))
    orders = cursor.fetchall()
    conn.close()

    # dict 형태로 변환
    orders = [dict(o) for o in orders]

    return orders


# 전체 orders의 count 조회
def get_order_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM orders")
    order_count = cursor.fetchone()[0]
    conn.close()

    return order_count


# order 에서 id 클릭하고 들어가
# -> orderitems 테이블에서 order_id로 검색하면 나오는 내용 + item_name 까지 같이 나옴
# order_item 에서 order_id 클릭하고 들어가
# -> orders 테이블에서 id로 검색하면 나오는 내용

# id로 orders 조회
def get_order_by_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE Id=?", (id,))
    order = cursor.fetchone()
    conn.close()

    order = dict(order)

    return order


# user_id로 검색한 orders 목록
def get_orders_by_user_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(r'''
                    select S.Name as StoreName, O.OrderAt as OrderAt
                    from orders O
                            left join stores S on O.StoreId = S.Id
                            left join orderitems OI on O.id = OI.OrderId
                    where O.UserId = ?
                    group by S.Id, strftime('%Y-%m-%d', O.OrderAt)
                    order by O.OrderAt
                    ''', (id, ))
    orders = cursor.fetchall()
    conn.close()

    if orders:
        # dict 형태로 변환
        orders = [dict(o) for o in orders]
    else:
        orders = []
    
    return orders


# 주문 생성
def create_order(order_id, order_at, store_id, user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                    insert into orders (Id, OrderAt, StoreId, UserId)
                    values (?, ?, ?, ?)
                    ''', (order_id, order_at, store_id, user_id))
    conn.commit()
    conn.close()

