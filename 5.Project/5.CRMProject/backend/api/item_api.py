from flask import Blueprint, jsonify, send_from_directory, request
import backend.database.item_db as db

item_api = Blueprint('item', __name__, static_folder='../../static/pages/item/')

# item 페이지 이동
@item_api.route('/')
def item_page():
    return send_from_directory(item_api.static_folder, 'item.html')


# store 데이터 전달
@item_api.route('/data')
def get_items_data():

    # 페이징 처리
    current_page = 1 # 기본 페이지
    items_per_page = 20 # 한페이지의 item 개수

    items = db.get_items_paging(current_page, items_per_page)
    item_count = db.get_item_count()
    total_page = 0

    if item_count % items_per_page == 0:
        total_page = item_count // items_per_page
    else:
        total_page = (item_count // items_per_page) + 1


    return jsonify({'items' : items, 'total_page' : total_page})


# 페이지 이동 시 item 페이지 이동
@item_api.route('/<int:page>')
def get_items_paging(page):
    return send_from_directory(item_api.static_folder, 'item.html')


# 페이징 처리 및 item 데이터 전달
@item_api.route('/page/data/<int:page>')
def get_items_paging_data(page):

    # 페이징 처리
    current_page = page # 현재 페이지
    items_per_page = 20 # 한페이지의 item 개수

    items = db.get_items_paging(current_page, items_per_page)
    item_count = db.get_item_count()
    total_page = 0

    if item_count % items_per_page == 0:
        total_page = item_count // items_per_page
    else:
        total_page = (item_count // items_per_page) + 1


    return jsonify({'items' : items, 'total_page' : total_page})


# 검색 시 item 페이지 이동
@item_api.route('/search/<int:page>')
def get_items_search_paging(page):
    return send_from_directory(item_api.static_folder, 'store.html')


# 검색 시 item 데이터 전달
@item_api.route('/search')
def get_items_search_data():

    current_page = 1 # 처음 1 페이지 고정
    items_per_page = 20 # 한페이지의 item 개수
    items = []
    item_count = 0
    total_page = 0

    search_type = request.args.get('type')

    if search_type:
        items = db.get_item_by_type(search_type, current_page, items_per_page)
        item_count = db.get_store_by_name_count(search_type)
    
    if item_count % items_per_page == 0:
        total_page = item_count // items_per_page
    else:
        total_page = (item_count // items_per_page) + 1

    return jsonify({'items' : items, 'total_page' : total_page})


# 검색 및 페이지 이동 시 item 데이터 전달
@item_api.route('/search/page/<int:page>')
def get_items_search_data_and_page(page):

    current_page = page # 현재 페이지
    items_per_page = 20 # 한페이지의 item 개수
    items = []
    item_count = 0
    total_page = 0

    search_type = request.args.get('type')

    if search_type is not None and search_type.strip():
        items = db.get_store_by_name(search_type, current_page, items_per_page)
        item_count = db.get_store_by_name_count(search_type)
    
    if item_count % items_per_page == 0:
        total_page = item_count // items_per_page
    else:
        total_page = (item_count // items_per_page) + 1

    return jsonify({'items' : items, 'total_page' : total_page, 'search_type': search_type})


# item 상세 페이지 이동
@item_api.route('/<id>')
def item_info_page(id):
    return send_from_directory(item_api.static_folder, 'item_info.html')


# 상세페이지 item 데이터 전달
@item_api.route('/info/<id>')
def get_item_by_id_date(id):
    item = db.get_item_by_id(id)
    return jsonify({'item' : item})
