from flask import Flask, send_from_directory, request, jsonify, redirect, url_for
from backend.api.user_api import user_api

app = Flask(__name__)

# blueprint 등록
app.register_blueprint(user_api, url_prefix="/api/user")

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'main.html')

if __name__ == '__main__':
    app.run(debug=True)
