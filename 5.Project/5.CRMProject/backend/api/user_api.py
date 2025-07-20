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
    total_page = 0 

    if user_count % items_per_page == 0:
        total_page = user_count // items_per_page
    else:
        total_page = (user_count // items_per_page) + 1

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
    total_page = 0 

    if user_count % items_per_page == 0:
        total_page = user_count // items_per_page
    else:
        total_page = (user_count // items_per_page) + 1

    return jsonify({'users' : users, 'total_page' : total_page})


# 검색 및 페이징 처리 시 user 페이지 이동
@user_api.route('/search/page/<int:page>')
def get_users_search_paging(page):
    # 다른 페이지로 이동시 페이징 처리된 main.html로 이동
    return send_from_directory(current_app.static_folder, 'main.html')


# 검색 및 페이징 처리 시 user 데이터 전달
@user_api.route('/search')
def users_search():

    current_page = 1 # 처음 1 페이지 고정
    items_per_page = 20 # 한페이지의 item 개수
    users = []
    user_count = 0
    total_page = 0

    search_name = request.args.get('name')
    search_gender = request.args.get('gender')

    if search_name and search_gender:
        users = db.get_user_by_name_and_gender(search_name, search_gender, current_page, items_per_page)
        user_count = db.get_user_by_name_and_gender_count(search_name, search_gender)
    elif search_name:
        users = db.get_user_by_name(search_name, current_page, items_per_page)
        user_count = db.get_user_by_name_count(search_name)
    elif search_gender:
        users = db.get_user_by_gender(search_gender, current_page, items_per_page)
        user_count = db.get_user_by_gender_count(search_gender)

    if user_count % items_per_page == 0:
        total_page = user_count // items_per_page
    else:
        total_page = (user_count // items_per_page) + 1

    return jsonify({'users' : users, 'total_page' : total_page})


@user_api.route('/search/<int:page>')
def users_search_page(page):

    current_page = page # 현재 페이지
    items_per_page = 20 # 한페이지의 item 개수
    users = []
    user_count = 0
    total_page = 0

    search_name = request.args.get('name')
    search_gender = request.args.get('gender')

    if search_name is not None and search_gender is not None and search_name.strip() and search_gender.strip():
        users = db.get_user_by_name_and_gender(search_name, search_gender, current_page, items_per_page)
        user_count = db.get_user_by_name_and_gender_count(search_name, search_gender)
    elif search_name is not None and search_name.strip():
        users = db.get_user_by_name(search_name, current_page, items_per_page)
        user_count = db.get_user_by_name_count(search_name)
    elif search_gender is not None and search_gender.strip():
        users = db.get_user_by_gender(search_gender, current_page, items_per_page)
        user_count = db.get_user_by_gender_count(search_gender)

    if user_count % items_per_page == 0:
        total_page = user_count // items_per_page
    else:
        total_page = (user_count // items_per_page) + 1

    return jsonify({'users' : users, 'total_page' : total_page, 'search_name': search_name, 'search_gender': search_gender})


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


# 상세 페이지의 order 데이터 전달
@user_api.route('/info/order/<id>')
def get_order_by_user_id_data(id):
    orders = db.get_order_by_user_id(id)
    return jsonify({'orders' : orders})


# 상세 페이지의 store 데이터 전달
@user_api.route('/info/store/<id>')
def get_store_by_user_id_data(id):
    stores = db.get_store_top5_by_user_id(id)
    return jsonify({'stores' : stores})


# 상세 페이지의 item 데이터 전달
@user_api.route('/info/item/<id>')
def get_item_by_user_id_data(id):
    items = db.get_item_top5_by_user_id(id)
    return jsonify({'items' : items})

