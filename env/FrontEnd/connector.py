# import all flask libraries required
from passlib.hash import sha256_crypt
from datetime import timedelta
from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   url_for,
                   session,
                   g)

# from env.FrontEnd.register import RegistrationForm
# from env.SupplyChain.businesses import User

app = Flask(__name__)
app.secret_key = '498hfg2rn29'
app.permanent_session_lifetime = timedelta(minutes=10)


class User:
    def __init__(self, n, business, email, password, ewallet):
        self.users = []
        self.n = n
        self.business = business
        self.email = email
        self.password = password
        self.ewallet = ewallet

    def __repr__(self):
        return f'<User:{self.email}>'


users = []
users.append(User(n=1, business='seller', email='new@gmail.com', password='pass', ewallet='WTDsdg43f23g2'))
users.append(User(n=2, business='buyer', email='one@gmail.com', password='pass2', ewallet='3f43f3f'))
users.append(User(n=3, business='buyer', email='twat@gmail.com', password='pass3', ewallet='WTDsd34f3f3g43f23g2'))
print(users)


@app.before_request
def before_request():
    if 'user_n' in session:
        user = [x for x in users if x.n == session['user_n']][0]
        g.user = user


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        session.pop('user_n', None)
        email = request.form['email']
        password = request.form['password']
        user = [x for x in users if x.email == email][0]
        if user and user.password == password:
            session['user_n'] = user.n
            return redirect(url_for('profile'))
        return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users.n[-1] += 1
        n = users.n
        email = request.form['email']
        ewallet = request.form['ewallet']
        password = request.form['password']
        password2 = request.form['password2']
        users.append(User(n=n, business='', email=email, password=password, ewallet=ewallet))
        print(users)
        return render_template('choice.html')
    return render_template('register.html')


@app.route('/choice', methods=['GET', 'POST'])
def choice():
    if not g.user:
        return render_template('index')
    else:
        if request.method == 'POST':
            if request.form['submit_button'] == 'buyer':
                users.business = 'buyer'
                return render_template('buyer')
            elif request.form['submit_button'] == 'seller':
                users.business = 'seller'
                return render_template('seller')
            else:
                return render_template('choice')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if not g.user:
        return render_template('index')
    return render_template('profile.html')


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
