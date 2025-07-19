from flask import Blueprint, jsonify, send_from_directory
import backend.database.order_item_db as db

order_item_api = Blueprint('order_item', __name__, static_folder='../../static/pages/order_item/')

# order_item 페이지 이동
@order_item_api.route('/')
def order_item_page():
    return send_from_directory(order_item_api.static_folder, 'order_item.html')


# order_item 데이터 전달
@order_item_api.route('/data')
def get_order_items_data():

    # 페이징 처리
    current_page = 1 # 기본 페이지
    items_per_page = 20 # 한페이지의 item 개수

    order_items = db.get_order_items_paging(current_page, items_per_page)
    order_item_count = db.get_order_item_count()
    total_page = 0

    if order_item_count % items_per_page == 0:
        total_page = order_item_count // items_per_page
    else:
        total_page = (order_item_count // items_per_page) + 1


    return jsonify({'order_items' : order_items, 'total_page' : total_page})


# 페이지 이동 시 order_item 페이지 이동
@order_item_api.route('/<int:page>')
def get_order_items_paging(page):
    return send_from_directory(order_item_api.static_folder, 'order_item.html')


# 페이징 처리 및 order_item 데이터 전달
@order_item_api.route('/page/data/<int:page>')
def get_order_items_paging_data(page):

    # 페이징 처리
    current_page = page # 현재 페이지
    items_per_page = 20 # 한페이지의 item 개수

    order_items = db.get_order_items_paging(current_page, items_per_page)
    order_item_count = db.get_order_item_count()
    total_page = 0

    if order_item_count % items_per_page == 0:
        total_page = order_item_count // items_per_page
    else:
        total_page = (order_item_count // items_per_page) + 1


    return jsonify({'order_items' : order_items, 'total_page' : total_page})


# order_item 상세 페이지 이동
@order_item_api.route('/<id>')
def order_item_info_page(id):
    return send_from_directory(order_item_api.static_folder, 'order_item_info.html')


# 상세페이지 order_item 데이터 전달
@order_item_api.route('/info/<id>')
def get_order_item_by_id_date(id):
    order_item = db.get_order_item_by_id(id)
    return jsonify({'order_item' : order_item})
