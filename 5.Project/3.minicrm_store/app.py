from flask import Flask, render_template, request
import database as db

app = Flask(__name__)
# blueprint 활용하여 route를 나눌 수 있음

@app.route('/')
def index():
    
    q = request.args.get('q', '').strip()

    if q:
        stores = db.get_stores_by_name(q)
    else:
        stores = db.get_stores()

    print(stores)
    
    return render_template('index.html', stores=stores, search=q)

@app.route('/search')
def search():
    q = request.args.get('q')
    print(f"검색값 : {q}")
    stores = db.get_stores_by_name(q)
    return render_template('index.html', stores=stores)

if __name__ == '__main__':
    app.run(debug=True)
