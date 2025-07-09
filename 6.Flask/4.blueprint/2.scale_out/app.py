from flask import Flask, render_template
from user.user_routes import user_bp
from admin.admin_routes import admin_bp
from product.product_routes import product_bp

app = Flask(__name__)

# app에 블루프린트 등록
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(product_bp, url_prefix="/product")

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
