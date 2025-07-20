from flask import Blueprint, jsonify, send_from_directory, request
import backend.database.store_db as db

store_api = Blueprint('store', __name__, static_folder='../../static/pages/store/')

# store 페이지 이동
@store_api.route('/')
def store_page():
    return send_from_directory(store_api.static_folder, 'store.html')


# store 데이터 전달
@store_api.route('/data')
def get_stores_data():

    # 페이징 처리
    current_page = 1 # 기본 페이지
    items_per_page = 20 # 한페이지의 item 개수

    stores = db.get_stores_paging(current_page, items_per_page)
    store_count = db.get_store_count()
    total_page = 0

    if store_count % items_per_page == 0:
        total_page = store_count // items_per_page
    else:
        total_page = (store_count // items_per_page) + 1


    return jsonify({'stores' : stores, 'total_page' : total_page})


# 페이지 이동 시 store 페이지 이동
@store_api.route('/<int:page>')
def get_stores_paging(page):
    return send_from_directory(store_api.static_folder, 'store.html')


# 페이징 처리 및 store 데이터 전달
@store_api.route('/page/data/<int:page>')
def get_stores_paging_data(page):

    # 페이징 처리
    current_page = page # 현재 페이지
    items_per_page = 20 # 한페이지의 item 개수

    stores = db.get_stores_paging(current_page, items_per_page)
    store_count = db.get_store_count()
    total_page = 0

    if store_count % items_per_page == 0:
        total_page = store_count // items_per_page
    else:
        total_page = (store_count // items_per_page) + 1


    return jsonify({'stores' : stores, 'total_page' : total_page})


# 검색 시 store 페이지 이동
@store_api.route('/search/<int:page>')
def get_stores_search_paging(page):
    return send_from_directory(store_api.static_folder, 'store.html')


# 검색 시 store 데이터 전달
@store_api.route('/search')
def get_stores_search_data():

    current_page = 1 # 처음 1 페이지 고정
    items_per_page = 20 # 한페이지의 item 개수
    stores = []
    store_count = 0
    total_page = 0

    search_name = request.args.get('name')

    if search_name:
        stores = db.get_store_by_name(search_name, current_page, items_per_page)
        store_count = db.get_store_by_name_count(search_name)
    
    if store_count % items_per_page == 0:
        total_page = store_count // items_per_page
    else:
        total_page = (store_count // items_per_page) + 1

    return jsonify({'stores' : stores, 'total_page' : total_page})


# 검색 및 페이지 이동 시 store 데이터 전달
@store_api.route('/search/page/<int:page>')
def get_stores_search_data_and_page(page):

    current_page = page # 현재 페이지
    items_per_page = 20 # 한페이지의 item 개수
    stores = []
    store_count = 0
    total_page = 0

    search_name = request.args.get('name')

    if search_name is not None and search_name.strip():
        stores = db.get_store_by_name(search_name, current_page, items_per_page)
        store_count = db.get_store_by_name_count(search_name)
    
    if store_count % items_per_page == 0:
        total_page = store_count // items_per_page
    else:
        total_page = (store_count // items_per_page) + 1

    return jsonify({'stores' : stores, 'total_page' : total_page, 'search_name': search_name})


# store 상세 페이지 이동
@store_api.route('/<id>')
def store_info_page(id):
    return send_from_directory(store_api.static_folder, 'store_info.html')


# 상세페이지 store 데이터 전달
@store_api.route('/info/<id>')
def get_store_by_id_date(id):
    store = db.get_store_by_id(id)
    return jsonify({'store' : store})


# 상세페이지 월간 매출액 데이터 전달
@store_api.route('/info/month/revenue/<id>')
def get_store_month_revenue_by_id_data(id):
    store_revenues = db.get_store_month_revenue_by_id(id)
    return jsonify({'store_revenues' : store_revenues})


# 상세페이지 특정 월의 일간 매출액 데이터 전달
@store_api.route('/info/day/revenue/<id>')
def get_store_day_revenue_by_id_data(id):
    search_month = request.args.get('month')
    # print('검색한 달 :', search_month)
    store_revenues = db.get_store_day_revenue_by_id_and_month(id, search_month)
    return jsonify({'store_revenues' : store_revenues})


# 상세 페이지의 user 데이터 전달
@store_api.route('/info/user/<id>')
def get_users_by_id_data(id):
    users = db.get_users_visit_top10_by_id(id)
    return jsonify({'users' : users})

