from flask import Flask, send_from_directory, request, jsonify, redirect, url_for
from backend.api.user_api import user_api
from backend.api.store_api import store_api
from backend.api.item_api import item_api
from backend.api.order_api import order_api
from backend.api.order_item_api import order_item_api
from backend.api.login_api import login_api

app = Flask(__name__)

# blueprint 등록
app.register_blueprint(user_api, url_prefix="/api/user")
app.register_blueprint(store_api, url_prefix="/api/store")
app.register_blueprint(item_api, url_prefix="/api/item")
app.register_blueprint(order_api, url_prefix="/api/order")
app.register_blueprint(order_item_api, url_prefix="/api/order_item")
app.register_blueprint(login_api, url_prefix="/api/login")

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'login.html')

if __name__ == '__main__':
    app.run(debug=True)
