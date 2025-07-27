import uuid
from datetime import datetime

from flask import Blueprint, jsonify, send_from_directory, request
import backend.database.user_db as user_db
import backend.database.order_db as order_db
import backend.database.item_db as item_db
import backend.database.store_db as store_db
import backend.database.order_item_db as order_item_db

cus_api = Blueprint('cus', __name__, static_folder='../../static/pages/cus/')

@cus_api.route('/')
def cus_page():
    return send_from_directory(cus_api.static_folder, 'customer.html')


# 고객 회원 가입
@cus_api.route('/membership', methods=['POST'])
def membership():

    name = request.form.get('name')
    gender = request.form.get('gender')
    birthdate = request.form.get('birthdate')
    address = request.form.get('address')
    # print(f"사용자 form 입력값 : {name}, {gender}, {birthdate}, {address}")

    id = str(uuid.uuid4())
    age = (datetime.now() - datetime.strptime(birthdate, "%Y-%m-%d")).days // 365

    user_db.create_user(id, name, gender, age, birthdate, address)
    create_user = user_db.get_user_by_id(id)

    return jsonify({'create_user': create_user})


# 특정 고객 주문 목록
@cus_api.route('/order/<id>')
def get_orders_by_user_id(id):
    orders = order_db.get_orders_by_user_id(id)
    return jsonify({'orders': orders})


# 특정 고객의 특정 달의 상품 목록
@cus_api.route('/order/<id>/<month>')
def get_order_item(id, month):
    items = item_db.get_items_by_user_id_and_order_at(id, month)
    return jsonify({'items': items})


# 주문페이지 이동
@cus_api.route('/orderpage')
def order_page():
    return send_from_directory(cus_api.static_folder, 'order_page.html')


# 매장 타입 전달
@cus_api.route('/orderpage/type')
def get_store_type():
    types = store_db.get_store_type()
    return jsonify({'types': types})


# 타입에 맞는 이름 전달
@cus_api.route('/orderpage/name/<type>')
def get_store_name(type):
    names = store_db.get_store_name(type)
    return jsonify({'names': names})


# 상품명 전달
@cus_api.route('/orderpage/item')
def get_item():
    items = item_db.get_items()
    return jsonify({'items': items})


# 상품 주문
@cus_api.route('/orderpage/order', methods=['POST'])
def create_order():
    order_id = str(uuid.uuid4())
    order_at = datetime.now().replace(microsecond=0) # 마이크로 초 제거한 년-월-일 시:분:초
    store_id = request.form.get('store_id')
    user_id = request.form.get('user_id')

    order_db.create_order(order_id, order_at, store_id, user_id)

    items = request.form.getlist('items')
    for item in items:
        order_item_id = str(uuid.uuid4())
        order_item_db.create_order_item(order_item_id, order_id, item)

    create_order = order_db.get_order_by_id(order_id)
    create_order_item = order_item_db.get_order_item_by_order_id(order_id)

    create_result = False
    if create_order and create_order_item:
        create_result = True

    return jsonify({'create_result': create_result})

