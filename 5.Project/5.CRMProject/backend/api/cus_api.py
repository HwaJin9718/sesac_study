from flask import Blueprint, jsonify, send_from_directory, request
import backend.database.user_db as user_db

cus_api = Blueprint('cus', __name__, static_folder='../../static/pages/cus/')

@cus_api.route('/')
def cus_page():
    return send_from_directory(cus_api.static_folder, 'customer.html')


@cus_api.route('/membership', methods=['POST'])
def membership():
    return

