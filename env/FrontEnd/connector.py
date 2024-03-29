from flask import (Flask, render_template,
                   request, redirect,
                   url_for, session, g)                     # Import flask library to create web application
from env.BackEnd.orders import UsersData                    # Import created class UserData
from env.BackEnd.businesses import User                     # Import created class User
from env.BackEnd.item import Item                           # Import created class Item
from datetime import timedelta                              # Import time to create invoices timestamp
import datetime                                             # Import time to create invoices timestamp

app = Flask(__name__)                                       # Create flask link for the application
app.secret_key = '498hfg2rn29'                              # Required secret key for the app
app.permanent_session_lifetime = timedelta(minutes=10)      # Time which will take to close inactive session

users = []                                                  # List of users
users.append(User(business='seller', email='first@gmail.com', password='FirstPassword', ewallet='WTDsdg43f23g2'))
users.append(User(business='seller', email='second@gmail.com', password='SecondPassword', ewallet='f343f34f34f'))
users.append(User(business='buyer', email='third@gmail.com', password='ThirdPassword', ewallet='3f4d3d33f3f'))
users.append(User(business='buyer', email='forth@gmail.com', password='ForthPassword', ewallet='WTDsd34f3f3g43f23g2'))
items = []                                                  # List of items
items.append(Item(item_id='1', seller='first@gmail.com', description='Metal', quantity=20, price=300, date='02/12/21'))
items.append(Item(item_id='2', seller='first@gmail.com', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='3', seller='first@gmail.com', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='4', seller='first@gmail.com', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='5', seller='first@gmail.com', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='6', seller='first@gmail.com', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='7', seller='first@gmail.com', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='8', seller='first@gmail.com', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='9', seller='first@gmail.com', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='10', seller='second@gmail.com', description='Coal', quantity=10, price=199, date='02/12/21'))
items.append(Item(item_id='11', seller='second@gmail.com', description='Iron', quantity=1000, price=50, date='02/12/21'))
orders = []                                                 # List of invoices
orders.append(UsersData(seller='first@gmail.com', buyer='third@gmail.com', seller_wallet='WTDsdg43f23g2', buyer_wallet='3f4d3d33f3f', item='Metal', quantity=20, price=300, date='02/12/21'))
orders.append(UsersData(seller='first@gmail.com', buyer='two@gmail.com', seller_wallet='WTDsdg43f23g2', buyer_wallet='WTDsd34f3f3g43f23g2', item='Metal', quantity=20, price=300, date='02/12/21'))
orders.append(UsersData(seller='second@gmail.com', buyer='third@gmail.com', seller_wallet='f343f34f34f', buyer_wallet='3f4d3d33f3f', item='Metal', quantity=20, price=300, date='02/12/21'))


@app.before_request
def before_request():                                       # Function executed automatically
    if 'user_id' in session:                                # Establish the session with user's accreditation
        user = [x for x in users if x.email == session['user_id']][0]
        g.user = user
        global items
        global orders                                       # Establish global variables


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():                                                # Main web page redirection
    return render_template('index.html')                    # Render created Index page


@app.route('/login', methods=['GET', 'POST'])
def login():                                                # Redirect to login page which finds user's account
    if request.method == 'POST':                            # If button is activated with attribute POST
        session.permanent = True
        session.pop('user_id', None)                        # Clear the session
        email = request.form['email']
        password = request.form['password']                 # Get user's inputs
        user = [x for x in users if x.email == email][0]    # looks for user's input in the list
        if user and user.password == password:              # If both user's inputs already exist and match
            session['user_id'] = user.email                 # Establish the session with user's username
            return redirect(url_for('add'))
        return redirect(url_for('index'))
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():                                             # Function to create account
    global n_email
    global n_ewallet
    global n_password                                       # Establish global variables
    if request.method == 'POST':
        n_email = request.form['email']
        n_ewallet = request.form['ewallet']
        n_password = request.form['password']
        n_password2 = request.form['password2']             # Get user's inputs
        if n_password == n_password2:
            for credit in users:
                if n_email == credit.email \
                        or n_password == credit.password \
                        or n_ewallet == credit.ewallet:     # If one of the user's inputs already exist in the list
                    print("Email, Password or Ewallet Already Used")
                    return redirect(url_for('register'))
            return redirect(url_for('choice'))
        else:
            return redirect(url_for('register'))
    return render_template('register.html')


@app.route('/choice', methods=['GET', 'POST'])
def choice():                                               # Assign user type to the account
    if request.method == 'POST':
        if request.form['submit_button'] == 'buyer':        # First type = buyer
            users.append(User(business='buyer',
                              email=n_email,
                              password=n_password,
                              ewallet=n_ewallet))           # Append the user's input in the list
            session['user_id'] = n_email
            return redirect(url_for('profile'))
        elif request.form['submit_button'] == 'seller':     # Second type = seller
            users.append(User(business='seller',
                              email=n_email,
                              password=n_password,
                              ewallet=n_ewallet))           # Append the user's input in the list
            session['user_id'] = n_email
            return redirect(url_for('profile'))
        else:
            return render_template('choice.html')
    return render_template('choice.html')


@app.route('/add', methods=['GET', 'POST'])
def add():                                                  # Add function for both user's
    if not g.user:
        return redirect(url_for('index'))
    elif request.method == 'POST' and g.user.business == 'seller':
        item_id_new = [n.item_id for n in items][-1] + 1
        seller = g.user                                     # Get the user's username
        description = request.form['description']
        quantity = int(request.form['quantity'])
        price = int(request.form['price'])                  # User's inputs
        date = datetime.datetime.now()                      # item's creation timestamp
        date = date.strftime("%x")                          # conversion
        items.append(Item(item_id=item_id_new,
                          seller=seller,
                          description=description,
                          quantity=quantity,
                          price=price,
                          date=date))                       # Add user's inputs to the list
        return render_template('add.html', item=items, order=orders)
    elif request.method == 'POST' and g.user.business == 'buyer':
        retrieve_id = int(request.form['retrieve_id'])
        seller = request.form['seller']
        buyer = g.user
        buyer_wallet = g.user.ewallet                       # Retrieve user's information
        seller = [x for x in users if x.email == seller][0]
        seller_wallet = seller.ewallet
        description = request.form['description']
        stock_quantity = int(request.form['stock_quantity'])
        price = int(request.form['price'])                  # Get user's inputs
        buy_quantity = int(request.form['buy_quantity'])
        price = int(buy_quantity * price)
        date = datetime.datetime.now()
        date = date.strftime("%x")
        if buy_quantity > stock_quantity:                   # If user's input is to big then don't process it
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
                                    date=date))             # Create invoice on the list
            new_quantity = stock_quantity - buy_quantity    # Update the item quantity
            for x in items:
                if x.item_id == retrieve_id:
                    x.quantity = new_quantity               # Update the item on the list
                if x.quantity == 0:
                    items.remove(x)                         # Delete the item
        return render_template('add.html', item=items, order=orders)
    else:
        return render_template('add.html', item=items, order=orders)


@app.route('/change', methods=['GET', 'POST'])
def change():
    if not g.user:
        return redirect(url_for('index'))
    elif request.method == 'POST' and g.user.business == 'seller':
        updated_id = int(request.form['updated_id'])        # User's inputs
        updated_description = request.form['updated_description']
        updated_quantity = int(request.form['updated_quantity'])
        updated_price = int(request.form['updated_price'])
        updated_date = datetime.datetime.now()
        updated_date = updated_date.strftime("%x")          # Update the time
        for x in items:
            if x.item_id == updated_id:
                x.description = updated_description
                x.quantity = updated_quantity
                x.price = updated_price
                x.date = updated_date
            if x.quantity == 0 or x.price == 0:             # Delete the item if quantity = 0
                items.remove(x)
        return render_template('add.html', item=items)
    return render_template('add.html', item=items)


@app.route('/profile', methods=['GET', 'POST'])
def profile():                                              # Display user's account information
    if not g.user:
        return redirect(url_for('index'))
    return render_template('profile.html')


@app.route('/history', methods=['GET', 'POST'])
def history():                                              # Display user's invoices
    if not g.user:
        return redirect(url_for('index'))
    return render_template('history.html', order=orders)


@app.route('/out')
def out():                                                  # Function to close the user's session
    session.pop('user_n', None)
    session.clear()
    return redirect(url_for('index'))


@app.errorhandler(404)                                      # error 404 handler, redirect to this page and back
def page_not_found_404(e):
    return render_template("404.html")


@app.errorhandler(405)                                      # error 405 handler, redirect to this page and back
def page_not_found_405(e):
    return render_template("405.html")


@app.errorhandler(500)                                      # error 500 handler, redirect to this page and back
def page_not_found_500(e):
    return render_template("500.html")


if __name__ == '__main__':
    app.run()
    app.run(use_reloader=True)
