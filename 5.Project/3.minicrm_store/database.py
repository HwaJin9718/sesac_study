import sqlite3

DATABASE = 'mycrm.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    # 미션1-1. DB로부터 가져온 내용을 dict 변환하는 방법
    conn.row_factory = sqlite3.Row
    return conn

def get_stores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores")
    stores = cursor.fetchall()
    conn.close()

    # 프린트로 할 때 진행
    # stores = [dict(s) for s in stores]

    # 미션1-2. 미션 1-1을 안했다면 여기에서 튜플형 데이터를 dict형으로 변환
    # stores_dict = []
    # for s in stores:
    #     stores_dict.append({
    #         'Id' : s[0],
    #         'Name' : s[1],
    #         'Type' : s[2],
    #         'Address' : s[3]
    #     })
    # 한줄짜리 코드
    # stores_dict = [{'Id':s[0], 'Name':s[1], 'Type':s[2], 'Address':s[3]} for s in stores]
    
    # return stores_dict
    return stores

def get_stores_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM stores WHERE Name LIKE %?%", (name)) # 오류 발생
    cursor.execute("SELECT * FROM stores WHERE Name LIKE ?", ('%' + name + '%', ))
    stores = cursor.fetchall()
    conn.close()

    return stores
