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

    if user:
        user = dict(user)
    else:
        user = []

    return user


# name으로 user 조회
def get_user_by_name(name, current_page, items_per_page):
    offset = (current_page - 1) * items_per_page # 페이지가 이동될 때 몇개째부터 출력할지
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE Name LIKE ? LIMIT ? OFFSET ?", ('%' + name + '%', items_per_page, offset))
    users = cursor.fetchall()
    conn.close()

    users = [dict(u) for u in users]

    return users

# name으로 조회된 user의 count 
def get_user_by_name_count(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE Name LIKE ?", ('%' + name + '%',))
    user_count = cursor.fetchone()[0]
    conn.close()

    return user_count


# gender로 user 조회
def get_user_by_gender(gender, current_page, items_per_page):
    offset = (current_page - 1) * items_per_page # 페이지가 이동될 때 몇개째부터 출력할지
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE Gender=? LIMIT ? OFFSET ?", (gender, items_per_page, offset))
    users = cursor.fetchall()
    conn.close()

    users = [dict(u) for u in users]

    return users


# gender로 조회된 user의 count 
def get_user_by_gender_count(gender):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE Gender=?", (gender,))
    user_count = cursor.fetchone()[0]
    conn.close()

    return user_count


# name, gender로 user 조회
def get_user_by_name_and_gender(name, gender, current_page, items_per_page):
    offset = (current_page - 1) * items_per_page # 페이지가 이동될 때 몇개째부터 출력할지
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE Name LIKE ? AND Gender=? LIMIT ? OFFSET ?", ('%' + name + '%', gender, items_per_page, offset))
    users = cursor.fetchall()
    conn.close()

    users = [dict(u) for u in users]

    return users


# name, gender로 조회된 user의 count 
def get_user_by_name_and_gender_count(name, gender):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE Name LIKE ? AND Gender=?", ('%' + name + '%', gender))
    user_count = cursor.fetchone()[0]
    conn.close()

    return user_count


# user id로 조회된 주문내역 
def get_order_by_user_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE UserId=?", (id, ))
    orders = cursor.fetchall()
    conn.close()

    orders = [dict(o) for o in orders]

    return orders


# user id로 조회한 매장 top 5
def get_store_top5_by_user_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                    select S.Name as Name, count(S.Name) as Count
                    from users U
                            left join orders O on U.Id = O.UserId
                            left join stores S on O.StoreId = S.Id
                    where U.Id = ?
                    group by S.Id
                    order by Count DESC, S.Id limit 5
                    ''', (id, ))
    stores = cursor.fetchall()
    conn.close()

    stores = [dict(s) for s in stores]

    return stores


# user id로 조회한 주문 상품명 top 5
def get_item_top5_by_user_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                    select I.Name as Name, count(I.Name) as Count
                    from users U
                            left join orders O on U.Id = O.UserId
                            left join orderitems OI on O.Id = OI.OrderId
                            left join items I on OI.ItemId = I.Id
                    where U.Id = ?
                    group by I.Id
                    order by Count DESC, I.Id
                    limit 5
                    ''', (id, ))
    items = cursor.fetchall()
    conn.close()

    items = [dict(i) for i in items]

    return items


def create_user(id, name, gender, age, birthdate, address):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                    insert into users (Id, Name, Gender, Age, Birthdate, Address)
                    values (?, ?, ?, ?, ?, ?)
                    ''', (id, name, gender, age, birthdate, address))
    conn.close()

