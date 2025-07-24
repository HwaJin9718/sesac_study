from flask import Blueprint, jsonify, send_from_directory, request
import backend.database.user_db as user_db
import uuid
from datetime import datetime

cus_api = Blueprint('cus', __name__, static_folder='../../static/pages/cus/')

@cus_api.route('/')
def cus_page():
    return send_from_directory(cus_api.static_folder, 'customer.html')


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

