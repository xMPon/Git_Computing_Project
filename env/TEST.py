#  this creates the items
@app.route('/create-item', methods=['GET', 'POST'])
def create_item():
    if request.method == 'POST' and 'newitem' in request.form:
        if 'loggedin' in session:
            item_message = request.form['newitem']
            item_date = datetime.utcnow().isoformat()
            item_by = session['username']
        else:
            return render_template('index.html')
        # need to create add items for the inventory
    return redirect(url_for('index'))


@app.route('/item/<item_id>', methods=['GET', 'POST'])
def item(item_id):
    session['current_page'] = 'item'
    session['item_id'] = item_id
    login_status = '0'
    if 'loggedin' in session:
        login_status = '1'
    data = get_item_page_data(item_id=int(item_id))
    return render_template('item.html', login_status=login_status, data=data)


#  import all flask libraries required
from wtforms.validators import (InputRequired,
                                DataRequired,
                                EqualTo,
                                Email,
                                Length)
from wtforms import (StringField,
                     PasswordField,
                     Form)

#  unused because of complexity and time consumption

class RegistrationForm(Form):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(min=4, max=40)])
    wallet = StringField('wallet', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=80)])
    password2 = PasswordField('password2', validators=[DataRequired(), EqualTo('password')])


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' \
            and 'email' in request.form \
            and 'ewallet' in request.form \
            and 'password' in request.form \
            and form.validate():
        email = form.email.data
        ewallet = sha256_crypt.encrypt(str(form.ewallet.data))
        password = sha256_crypt.encrypt(str(form.password.data))
        if email in users.email:
            return False
        elif len(email) < 5:
            return False
        else:
            users.emails.append(email)
            print(users.mails)
            return render_template('profile.html')
            return True
    return render_template('register.html')


def validate_email():
    emails = []
    while True:
        email = input("your email")
        if email in emails:
            print("email already used")
            return False
        elif len(email) < 5:
            print("Email is not valid 1")
            return False
        else:
            print("Your email seems fine")
            emails.append(email)
            print(emails)
            return True
validate_email()

if email in email:
    return False
elif len(email) < 5:
    return False
else:
    users.emails.append(email)
    print(users.mails)
    return render_template('choice.html')
    return True



#### working register
# import all flask libraries required
from datetime import timedelta
from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   url_for,
                   session,
                   g)
from env.BackEnd.businesses import User
from env.BackEnd.orders import UsersData


app = Flask(__name__)
app.secret_key = '498hfg2rn29'
app.permanent_session_lifetime = timedelta(minutes=10)

users = []
users.append(User(business='seller', email='n@a', password='p', ewallet='WTDsdg43f23g2'))
users.append(User(business='buyer', email='o@a', password='p', ewallet='3f4d3d33f3f'))
users.append(User(business='buyer', email='two@gmail.com', password='pass3', ewallet='WTDsd34f3f3g43f23g2'))
print(users)

orders = []
orders.append(UsersData(transaction_id='1',
                        seller='n@a',
                        buyer='o@a',
                        seller_wallet='WTDsdg43f23g2',
                        buyer_wallet='3f4d3d33f3f',
                        item='Metal',
                        quantity=20,
                        price=300.90,
                        date=''))
print(orders)


@app.before_request
def before_request():
    if 'user_id' in session:
        user = [x for x in users if x.email == session['user_id']][0]
        g.user = user


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
            if user.business == 'buyer':
                return redirect(url_for('buyer'))
            elif user.business == 'seller':
                return redirect(url_for('seller'))
            else:
                # this leads to broken page as it won't load the data from the list
                # try to pass the information and add business type in /choice
                return render_template('choice.html', email=email, password=password)
        return redirect(url_for('index'))
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_email = request.form['email']
        new_ewallet = request.form['ewallet']
        new_password = request.form['password']
        new_password2 = request.form['password2']
        if new_password == new_password2:
            def keep():
                return new_email, new_ewallet, new_password
            return render_template('choice.html')
        else:
            return render_template('register.html')
    return render_template('register.html')


@app.route('/choice', methods=['GET', 'POST'])
def choice():
    if request.method == 'POST':
        new_email, new_password, new_ewallet = keep()
        #  ...if check the list for email and business = "" (dead link from login)
        if request.form['submit_button'] == 'buyer':
            users.append(User(business='buyer',
                              email=new_email,
                              password=new_password,
                              ewallet=new_ewallet))
            session['user_id'] = new_email
            return redirect(url_for('buyer'))
        elif request.form['submit_button'] == 'seller':
            users.append(User(business='seller',
                              email=new_email,
                              password=new_password,
                              ewallet=new_ewallet))
            print(users)
            session['user_id'] = new_email
            return redirect(url_for('seller'))
        else:
            return render_template('choice.html')
    return render_template('choice.html')


@app.route('/buyer', methods=['GET', 'POST'])
def buyer():
    if not g.user:
        return redirect(url_for('index'))
    return render_template('buyer.html')


@app.route('/seller', methods=['GET', 'POST'])
def seller():
    if not g.user:
        return redirect(url_for('index'))
    return render_template('seller.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if not g.user:
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if not g.user:
        return redirect(url_for('index'))
    return render_template('profile.html')


@app.route('/history', methods=['GET', 'POST'])
def history():
    if not g.user:
        return redirect(url_for('index'))
    return render_template('history.html')


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
