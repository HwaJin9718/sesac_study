import db_crud_sqlite as db
# import db_crud_mysql as db
# import db_crud_postgresql as db

# from db_crud_sqlite import (
#     create_table, 
#     insert_user, 
#     update_user_age, 
#     get_users, 
#     get_users_by_name, 
#     delete_user_by_name, 
#     delete_user_by_age, 
#     delete_user_by_id
# )

def main():
    # 테이블 생성
    # create_table()
    db.create_table()

    # 데이터 삽입
    # insert_user('Alice', 30)
    db.insert_user('Alice', 30)
    # insert_user('Bob', 25)
    db.insert_user('Bob', 25)
    # insert_user('Charlie', 35)
    db.insert_user('Charlie', 35)

    # 데이터 조회
    print('데이터 목록:')
    users = db.get_users()
    # users = get_users()
    for user in users:
        print(user)
    
    # 데이터 수정
    db.update_user_age('Alice', 32)
    # update_user_age('Alice', 32)

    # 수정 후 데이터 조회
    print('Alice 수정 후 조회:')
    user = db.get_users_by_name('Alice')
    # user = get_users_by_name('Alice')
    print(user)

    # 데이터 삭제 name
    db.delete_user_by_name('Bob')
    # delete_user_by_name('Bob')
    print('Bob 삭제 후 조회:')
    user = db.get_users_by_name('Bob')
    # user = get_users_by_name('Bob')
    print(user)

    print("전체 데이터 목록:")
    users = db.get_users()
    # users = get_users()
    for user in users:
        print(user)
    
    db.delete_user_by_name('Alice')
    # delete_user_by_name('Alice')
    print('Alice 삭제 후 조회:')
    user = db.get_users_by_name('Alice')
    # user = get_users_by_name('Alice')
    print(user)
    
    # 데이터 삭제 age
    db.delete_user_by_age(30)
    # delete_user_by_age(30)
    print('나이 30 삭제 후 조회:')
    user = db.delete_user_by_age(30)
    # user = delete_user_by_age(30)
    print(user)

    # 데이터 삭제 id
    db.delete_user_by_id(3)
    # delete_user_by_id(3)
    print('아이디 3 삭제 후 조회:')
    user = db.delete_user_by_id(3)
    # user = delete_user_by_id(3)
    print(user)

    print('전체 데이터 목록:')
    users = db.get_users()
    # users = get_users()
    for user in users:
        print(user)

if __name__ == '__main__':
    main()
