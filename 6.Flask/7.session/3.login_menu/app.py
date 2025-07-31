from flask import Flask, render_template, request, redirect, url_for
from flask import session

app = Flask(__name__)
app.secret_key = 'sesac'

users = [
    {'name' : '새싹', 'id' : 'sesac', 'pw' : 'sesac'}
]

items = [
    {'id' : 'prod-001', 'name' : '사과', 'price' : 1000},
    {'id' : 'prod-002', 'name' : '딸기', 'price' : 3000},
    {'id' : 'prod-003', 'name' : '오렌지', 'price' : 5000},
    {'id' : 'prod-004', 'name' : '바나나', 'price' : 2500},
]

# carts = []

@app.route('/')
def home():
    user = session.get('user')
    return render_template('index.html', user=user)


@app.route('/user')
def user():
    user = session.get('user')
    if user:
        return render_template('user.html', user=user)
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')

        user = next((u for u in users if u['id'] == id and u['pw'] == password), None)

        if user:
            session['user'] = user # 로그인한 사용자 정보 세션에 저장
            return redirect(url_for("user"))
        else:
            error = "ID 또는 비밀번호가 올바르지 않습니다."
            return render_template('login.html', error=error)


    return render_template('login.html')


@app.route('/logout')
def logout():
    # 로그아웃을 두번 누르면 user가 없기때문에 key error가 생김, 코드 죽는걸 방지하기 위해 None 반환
    session.pop('user', None) 
    return redirect(url_for('home'))


@app.route('/product')
def product():
    user = session.get('user')
    return render_template('product.html', user=user, items=items)


@app.route('/cart')
def cart():
    user = session.get('user')
    carts = session.get('carts', []) # carts session 없을 경우 빈 dict 반환
    # print(carts)

    # items의 복사본 생성 (원본에 영향 주지 않음)
    item_list = []
    for i in items:
        item_copy = i.copy()  # 각 상품을 복사
        item_copy['qty'] = 0     # qty 초기화
        item_list.append(item_copy)

    # 장바구니에 있는 상품 수량 + (기본은 0)
    for c in carts:
        for i in item_list:
            if c['id'] == i['id']:
                i['qty'] += 1
    
    for i in reversed(item_list):
        if i['qty'] == 0:
            item_list.remove(i)

    session['carts'] = item_list

    carts = session.get('carts')

    if user:
        return render_template('cart.html', user=user, carts=carts)
    else:
        return render_template('cart.html', user=None)


# 강사님 코드
# @app.route('/cart')
# def view_cart():
#     user = session.get('user')
#     if not user:
#         return render_template("cart.html", user=None, items=items, error="로그인 후 사용할 수 있습니다.")
    
#     cart = session.get("cart", {}) # 카트가 없으면 {} 빈 dict를 반환하겠다.
    
#     cart_items = []
#     for item_id, item_qty in cart.items():
#         item = next((i for i in items if i['id'] == item_id), None)
#         if item:
#             a_item = item.copy()
#             a_item["qty"] = item_qty
#             cart_items.append(a_item)
    
#     return render_template("cart.html", user=user, cart=cart_items)


@app.route('/add-to-cart')
def add_to_cart():
    user = session.get('user')
    item_id = request.args.get('id')
    # print(item_id)

    # for i in items:
    #     if i['id'] == item_id:
    #         carts.append(i)
    #         print(carts)

    if 'carts' not in session:
        session['carts'] = [] # 빈 리스트로 초기화
        for i in items:
            if i['id'] == item_id:
                session['carts'].append(i)
                break
    else:
        carts = session['carts']
        for i in items:
            if i['id'] == item_id:
                # print(i)
                carts.append(i)
                session['carts'] = carts
                break
    
    carts = session.get('carts')
    # print(carts)

    return render_template('product.html', user=user, items=items)


# 강사님 코드
# @app.route('/add_to_cart', methods=["POST"])
# def add_to_cart():
#     user = session.get('user')
#     if not user:
#         return render_template("product.html", user=None, items=items, error="로그인 후 사용할 수 있습니다.")
    
#     item_id = request.form.get('item_id')
#     print("담기요청한 상품코드: ", item_id)
    
#     if "cart" not in session:
#         # session["cart"] = []  # prod-001, prod-002, prod-001, prod-001
#         session["cart"] = {}  # key, value  {"prod-001": 1}
        
#     cart = session["cart"] # 빈 카트를 가져오거나, 이전에 담은 카드...
    
#     if item_id in cart:  # 이전에 내 카트에 이 상품이 있어??
#         cart[item_id] += 1
#     else:
#         cart[item_id] = 1
        
#     session["cart"] = cart
    
#     return render_template("product.html", user=user, items=items, message=f"{item_id} 가 담겼습니다.")


@app.route('/del-to-cart')
def del_to_cart():
    user = session.get('user')
    carts = session.get('carts')
    item_id = request.args.get('id')
    # print(item_id)

    for c in carts:
        if c['id'] == item_id:
            carts.remove(c)
            break
    
    session['carts'] = carts

    return render_template('cart.html', user=user, carts=carts)


@app.route('/all-del')
def all_del_to_cart():
    user = session.get('user')
    session.pop('carts', None)
    return render_template('cart.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
