from flask import Flask

from routes.todo_routes import todo_bp
from routes.chat_routes import chat_bp

app = Flask(__name__, static_folder='public', static_url_path='')

app.register_blueprint(todo_bp, url_prefix="/api/todo")
app.register_blueprint(chat_bp, url_prefix="/api/chat")

@app.route('/')
def home():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)
