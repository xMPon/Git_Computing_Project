# import all flask libraries required
from flask import (Flask, render_template,
                   request, redirect,
                   url_for, session, g)
from env.BackEnd.orders import UsersData
from env.BackEnd.businesses import User
from env.BackEnd.item import Item
from datetime import timedelta
import datetime

app = Flask(__name__)
app.secret_key = '498hfg2rn29'
app.permanent_session_lifetime = timedelta(minutes=10)

users = []
users.append(User(business='seller', email='a@a', password='a', ewallet='WTDsdg43f23g2'))
users.append(User(business='seller', email='b@b', password='b', ewallet='f343f34f34f'))
users.append(User(business='buyer', email='o@o', password='o', ewallet='3f4d3d33f3f'))
users.append(User(business='buyer', email='two@gmail.com', password='pass3', ewallet='WTDsd34f3f3g43f23g2'))
items = []
items.append(Item(item_id='1', seller='a@a', description='Metal', quantity=20, price=300, date='02/12/21'))
items.append(Item(item_id='2', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='3', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='4', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='5', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='6', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='7', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='8', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='9', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='10', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='11', seller='b@b', description='Coal', quantity=10, price=199, date='02/12/21'))
items.append(Item(item_id='12', seller='b@b', description='Iron', quantity=1000, price=50, date='02/12/21'))
orders = []
orders.append(
    UsersData(seller='a@a', buyer='o@o', seller_wallet='WTDsdg43f23g2',
              buyer_wallet='3f4d3d33f3f', item='Metal', quantity=20, price=300, date='02/12/21'))
orders.append(
    UsersData(seller='a@a', buyer='two@gmail.com', seller_wallet='WTDsdg43f23g2',
              buyer_wallet='WTDsd34f3f3g43f23g2', item='Metal', quantity=20, price=300, date='02/12/21'))
orders.append(
    UsersData(seller='b@b', buyer='o@o', seller_wallet='f343f34f34f',
              buyer_wallet='3f4d3d33f3f', item='Metal', quantity=20, price=300, date='02/12/21'))


@app.before_request
def before_request():
    if 'user_id' in session:
        user = [x for x in users if x.email == session['user_id']][0]
        g.user = user
        global items
        global orders


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        session.pop('user_id', None)
        email = request.form['email']
        password = request.form['password']
        user = [x for x in users if x.email == email][0]
        if user and user.password == password:
            session['user_id'] = user.email
            return redirect(url_for('add'))
        return redirect(url_for('index'))
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    global n_email
    global n_ewallet
    global n_password
    if request.method == 'POST':
        n_email = request.form['email']
        n_ewallet = request.form['ewallet']
        n_password = request.form['password']
        n_password2 = request.form['password2']
        if n_password == n_password2:
            for credit in users:
                if n_email == credit.email \
                        or n_password == credit.password \
                        or n_ewallet == credit.ewallet:
                    print("Email, Password or Ewallet Already Used")
                    return redirect(url_for('register'))
            return redirect(url_for('choice'))
        else:
            return redirect(url_for('register'))
    return render_template('register.html')


@app.route('/choice', methods=['GET', 'POST'])
def choice():
    if request.method == 'POST':
        #  ...if check the list for email and business = "" (dead link from login)
        if request.form['submit_button'] == 'buyer':
            users.append(User(business='buyer',
                              email=n_email,
                              password=n_password,
                              ewallet=n_ewallet))
            session['user_id'] = n_email
            return redirect(url_for('profile'))
        elif request.form['submit_button'] == 'seller':
            users.append(User(business='seller',
                              email=n_email,
                              password=n_password,
                              ewallet=n_ewallet))
            session['user_id'] = n_email
            return redirect(url_for('profile'))
        else:
            return render_template('choice.html')
    return render_template('choice.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if not g.user:
        return redirect(url_for('index'))
    elif request.method == 'POST' and g.user.business == 'seller':
        item_id_new = [n.item_id for n in items][-1] + 1
        seller = g.user
        description = request.form['description']
        quantity = int(request.form['quantity'])
        price = int(request.form['price'])
        date = datetime.datetime.now()
        date = date.strftime("%x")
        items.append(Item(item_id=item_id_new,
                          seller=seller,
                          description=description,
                          quantity=quantity,
                          price=price,
                          date=date))
        return render_template('add.html', item=items, order=orders)
    elif request.method == 'POST' and g.user.business == 'buyer':
        retrieve_id = int(request.form['retrieve_id'])
        seller = request.form['seller']
        buyer = g.user
        buyer_wallet = g.user.ewallet
        seller = [x for x in users if x.email == seller][0]
        seller_wallet = seller.ewallet
        description = request.form['description']
        stock_quantity = int(request.form['stock_quantity'])
        price = int(request.form['price'])
        buy_quantity = int(request.form['buy_quantity'])
        price = int(buy_quantity * price)
        date = datetime.datetime.now()
        date = date.strftime("%x")
        if buy_quantity > stock_quantity:
            print("Order is too big")
            return redirect(url_for('add'))
        else:
            orders.append(UsersData(seller=seller,
                                    buyer=buyer,
                                    seller_wallet=seller_wallet,
                                    buyer_wallet=buyer_wallet,
                                    item=description,
                                    quantity=buy_quantity,
                                    price=price,
                                    date=date))
            new_quantity = stock_quantity - buy_quantity
            for x in items:
                if x.item_id == retrieve_id:
                    x.quantity = new_quantity
        return render_template('add.html', item=items, order=orders)
    else:
        return render_template('add.html', item=items, order=orders)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if not g.user:
        return redirect(url_for('index'))
    return render_template('profile.html')


@app.route('/history', methods=['GET', 'POST'])
def history():
    if not g.user:
        return redirect(url_for('index'))
    return render_template('history.html', order=orders)


@app.route('/out')
def out():
    session.pop('user_n', None)
    session.clear()
    return redirect(url_for('index'))


@app.errorhandler(404)  # error 404 handler, redirect to this page and back
def page_not_found_404():
    return render_template("404.html")


@app.errorhandler(405)  # error 405 handler, redirect to this page and back
def page_not_found_405():
    return render_template("405.html")


@app.errorhandler(500)  # error 500 handler, redirect to this page and back
def page_not_found_500():
    return render_template("500.html")


if __name__ == '__main__':
    app.run(debug=True)  # delete debugging when finished
    app.run(use_reloader=True)
