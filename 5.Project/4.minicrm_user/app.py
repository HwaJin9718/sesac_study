from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    # print(f"페이지 : {page}")
    items_per_page = 10 # 10개, 20개, 50개, ...

    # 전체 유저 가져오기
    # users = db.get_users()

    # 페이지 수만큼 유저 가져오기
    users = db.get_users_per_page(page, items_per_page) 

    # 전체 유저수
    user_count = db.get_user_count()
    total_page = user_count // items_per_page 
    # 사용자수가 나눠서 떨어지지 않는 경우라면 total_page 어떻게 해야할까?

    return render_template('index.html', users=users, total_page=total_page)

if __name__ == '__main__':
    app.run(debug=True)
