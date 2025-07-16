from flask import Blueprint, jsonify, send_from_directory
import backend.database.user_db as db

user_api = Blueprint('user', __name__, static_folder='../../static/pages/user/')

@user_api.route('/')
def get_users_data():
    users = db.get_users()
    # print(users)
    return jsonify({'users' : users})

@user_api.route('/<id>') # id str로 지정 : string:
def user_info_page(id):
    return send_from_directory(user_api.static_folder, 'user_info.html')

@user_api.route('/info/<id>')
def get_user_by_id_date(id):
    print('받아온 id :', id)
    user = db.get_user_by_id(id)
    # print(user)
    return jsonify({'user' : user})
