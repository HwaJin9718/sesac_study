from flask import Blueprint, jsonify, send_from_directory
import backend.database.user_db as db

user_api = Blueprint('user', __name__, static_folder='../../static/pages/user/')

@user_api.route('/')
def get_users_data():
    users = db.get_users()
    # print(users)
    return jsonify({'users' : users})
