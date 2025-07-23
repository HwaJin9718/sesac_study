from flask import Blueprint, jsonify, request
import backend.database.user_db as db

login_api = Blueprint('login', __name__) # 

@login_api.route('/')
def login():
    login_result = False

    user_id = request.args.get('user_id')
    user_pw = request.args.get('user_pw')
    # print(f"입력한 아이디: {user_id}, 입력한 비밀번호: {user_pw}")

    if user_id and user_pw:
        login_result = True

    return jsonify({'message': login_result})
