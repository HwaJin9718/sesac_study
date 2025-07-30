from flask import Blueprint, jsonify, request, session
import backend.database.user_db as db

login_api = Blueprint('login', __name__)

@login_api.route('/user', methods=['POST'])
def login_user():
    login_result = False

    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')
    # print(f"입력한 아이디: {user_id}, 입력한 비밀번호: {user_pw}")

    user = db.get_user_by_id(user_id)

    if user and user_pw:
        session['user'] = user # 세션에 user 정보 추가
        login_result = True

    return jsonify({'message': login_result, 'user': user})


@login_api.route('/admin', methods=['POST'])
def login_admin():
    login_result = False

    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')
    # print(f"입력한 아이디: {user_id}, 입력한 비밀번호: {user_pw}")

    user = db.get_user_by_id(user_id)
    # print(f"admin 검색된 user : {user}")

    if user['Id'] == 'admin' and user_pw == 'admin':
        session['user'] = user # 세션에 admin 정보 추가
        login_result = True

    return jsonify({'message': login_result})
