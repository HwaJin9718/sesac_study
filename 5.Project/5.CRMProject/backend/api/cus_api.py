import uuid
from datetime import datetime

from flask import Blueprint, jsonify, send_from_directory, request
import backend.database.user_db as user_db
import backend.database.order_db as order_db
import backend.database.item_db as item_db

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
    return orders


# 특정 고객의 특정 달의 상품 목록
@cus_api.route('/order/<id>/<month>')
def get_order_item(id, month):
    items = item_db.get_items_by_user_id_and_order_at(id, month)
    return items


# 주문페이지 이동
@cus_api.route('/orderpage')
def order_page():
    return send_from_directory(cus_api.static_folder, 'order_page.html')

