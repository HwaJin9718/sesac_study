from flask import Blueprint, jsonify, send_from_directory, request, current_app
# current_app : main.html 접근을 위해 app에 있는 static 폴더로 접근 필요
# from app import app 시 순환 참조 오류 발생, 현재 활성화된 app을 가져오기 위해 current_app 사용
import backend.database.user_db as db

user_api = Blueprint('user', __name__, static_folder='../../static/pages/user/')

#  처음 user 데이터 전달
@user_api.route('/')
def get_users_data():

    # 페이징 처리
    current_page = 1 # 기본 페이지
    items_per_page = 20 # 한페이지의 item 개수

    users = db.get_users_paging(current_page, items_per_page)
    user_count = db.get_user_count()
    total_page = user_count // items_per_page 

    # users = db.get_users()
    # print(users)
    return jsonify({'users' : users, 'total_page' : total_page})


# 페이징 처리 시 user 페이지 이동
@user_api.route('/<int:page>')
def get_users_paging(page):
    # 다른 페이지로 이동시 페이징 처리된 main.html로 이동
    return send_from_directory(current_app.static_folder, 'main.html')


# 페이징 처리 시 user 데이터 전달
@user_api.route('/page/<int:page>')
def get_users_paging_data(page):

    # 페이징 처리
    current_page = page # 현재 페이지
    items_per_page = 20 # 한페이지의 item 개수

    users = db.get_users_paging(current_page, items_per_page)
    user_count = db.get_user_count()
    total_page = user_count // items_per_page 

    return jsonify({'users' : users, 'total_page' : total_page})


# user 상세 페이지 이동
@user_api.route('/<id>') # id str로 지정 : string:
def user_info_page(id):
    return send_from_directory(user_api.static_folder, 'user_info.html')


# 상세페이지 user 데이터 전달
@user_api.route('/info/<id>')
def get_user_by_id_date(id):
    # print('받아온 id :', id)
    user = db.get_user_by_id(id)
    # print(user)
    return jsonify({'user' : user})

