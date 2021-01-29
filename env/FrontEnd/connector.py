# import all flask libraries
from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   url_for,
                   session)
from datetime import datetime
# from env.SupplyChain.businesses import Users

app = Flask(__name__)

# lists for users information
emails = []
passwords = []
ewallets = []
users = []
users.append(emails, passwords, ewallets)

@app.route('/')
@app.route('/index')
def index():
    if 'loggedin' in session:
        return render_template('index.html', login_status='1')
    else:
        return render_template('index.html', login_status='0')


@app.route('/register', methods=['GET', 'POST'])
def register(Form):
    if request.method == 'POST' and 'mail' in request.form \
                                and 'psw' in request.form \
                                and 'wallet' in request.form:

        def validate_email(emails):
            email = request.form['mail']
            if email in emails:
                print("email already used")
                return False
            elif not len(email) < 5:
                print("Email is not valid 1")
                return False
            elif not email.search("@"):
                print("Email is not valid 2")
                return False
            elif not email.isupper():
                print("Emails is not valid 3")
                return False
            else:
                print("Your email seems fine")
                emails.append(email)
                return True

        def validate_password(passwords):
            password = request.form['psw']
            if password in passwords:
                print("Password already exist")
                return False
            elif not len(password) < 5:
                print("Make sure your password is at lest 8 letters")
                return False
            elif not password.isdigit():
                print("Make sure your password has a number in it")
                return False
            elif not password.isupper():
                print("Make sure your password has a capital letter in it")
                return False
            else:
                print("Your password seems fine")
                passwords.append(password)
                return True

        def validate_e_wallet(e_wallets):
            e_wallet = request.form['wallet']
            if e_wallet in e_wallets:
                print("email already used")
                return False
            elif not len(e_wallet) < 5:
                print("E_wallet is not valid 1")
                return False
            else:
                print("Your email seems fine")
                e_wallets.append(e_wallet)
                return True
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found_404(e):
    return render_template("404.html")


@app.errorhandler(405)
def page_not_found_405(e):
    return render_template("405.html")


@app.errorhandler(500)
def page_not_found_500(e):
    return render_template("500.html")


# delete debugging when finished
if __name__ == '__main__':
    app.run(debug=True)
