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