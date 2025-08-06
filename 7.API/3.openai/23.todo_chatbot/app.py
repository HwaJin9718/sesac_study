from flask import Flask

from route.todo_route import todo_api
from route.chat_route import chat_api

app = Flask(__name__, static_folder='public', static_url_path='')

app.register_blueprint(todo_api, url_prefix="/api/todo")
app.register_blueprint(chat_api, url_prefix="/api/chat")

@app.route('/')
def home():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)
