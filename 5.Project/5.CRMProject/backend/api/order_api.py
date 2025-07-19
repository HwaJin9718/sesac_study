from flask import Blueprint, jsonify, send_from_directory
import backend.database.order_db as db

order_api = Blueprint('order', __name__, static_folder='../../static/pages/order/')

# order 페이지 이동
@order_api.route('/')
def order_page():
    return send_from_directory(order_api.static_folder, 'order.html')


# order 데이터 전달
@order_api.route('/data')
def get_orders_data():

    # 페이징 처리
    current_page = 1 # 기본 페이지
    items_per_page = 20 # 한페이지의 item 개수

    orders = db.get_orders_paging(current_page, items_per_page)
    order_count = db.get_order_count()
    total_page = 0

    if order_count % items_per_page == 0:
        total_page = order_count // items_per_page
    else:
        total_page = (order_count // items_per_page) + 1


    return jsonify({'orders' : orders, 'total_page' : total_page})


# 페이지 이동 시 order 페이지 이동
@order_api.route('/<int:page>')
def get_orders_paging(page):
    return send_from_directory(order_api.static_folder, 'order.html')


# 페이징 처리 및 order 데이터 전달
@order_api.route('/page/data/<int:page>')
def get_orders_paging_data(page):

    # 페이징 처리
    current_page = page # 현재 페이지
    items_per_page = 20 # 한페이지의 item 개수

    orders = db.get_orders_paging(current_page, items_per_page)
    order_count = db.get_order_count()
    total_page = 0

    if order_count % items_per_page == 0:
        total_page = order_count // items_per_page
    else:
        total_page = (order_count // items_per_page) + 1


    return jsonify({'orders' : orders, 'total_page' : total_page})


# order 상세 페이지 이동
@order_api.route('/<id>')
def order_info_page(id):
    return send_from_directory(order_api.static_folder, 'order_info.html')


# 상세페이지 order 데이터 전달
@order_api.route('/info/<id>')
def get_order_by_id_date(id):
    order = db.get_order_by_id(id)
    return jsonify({'order' : order})
