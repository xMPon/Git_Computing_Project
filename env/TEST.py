
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'loggedin' in session:
        return redirect(url_for('index'))
    if request.method == 'POST' and 'uname' in request.form and 'psw' in request.form:
        username = request.form['uname']
        password = request.form['psw']
        sql = """
            SELECT username, password FROM db.users
            WHERE username = '{username}'
        """.format(username=username)
        conn.ping(reconnect=True)
        cursor.execute(sql)
        account = cursor.fetchone()
        if len(account) != 0:
            password_db = account[1].encode('ascii')
            password_match = decrypt(password_db, password)
            if password_match:
                session['loggedin'] = True
                session['username'] = account[0]
                session['current_page'] = 'index'
                return redirect(url_for('index'))
            else:
                return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'uname' in request.form and 'psw' in request.form:
        username = request.form['uname']
        raw_password = request.form['psw']
        # encrypt the password first
        password = encrypt(raw_password).decode('ascii')
        sql = """
            INSERT INTO users (username, password)
            VALUES ('{username}', '{password}')
        """.format(username=username, password=password)
        password = encrypt(raw_password).decode('ascii')
        cursor.execute(sql)
        conn.commit()

    return redirect(url_for('index'))


@app.route('/validate_user_name', methods=['POST'])
def validate_user_name():
    user_name = request.form['username']
    sql = """
        select username 
        from users 
        where username = '{user_name}'
    """.format(user_name=user_name)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        flash("Username is not available!")
        return 'Username is not available'
    else:
        return '1'


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    if 'current_page' in session:
        current_page = session['current_page']
        topic_id = session['topic_id']
        claim_id = session['claim_id']
        session.pop('current_page', None)
        session.pop('topic_id', None)
        if current_page == 'topic':
            return redirect(url_for('topic', topic_id=topic_id))
        if current_page == 'claim':
            return redirect(url_for('claim', claim_id=claim_id))
    return redirect(url_for('index'))



    # def get_user(self, emails, passwords):
    #    email = print("What is your email")
    #    password = print("What is your password")
    #    e_wallet = print("What is your e_wallet")




@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'loggedin' in session:
        return redirect(url_for('index'))
    if request.method == 'POST' and 'uname' in request.form and 'psw' in request.form:
        username = request.form['uname']
        password = request.form['psw']
    else:
        return redirect(url_for('index'))






@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'mail' in request.form and 'psw' in request.form:
        email = request.form['mail']
        password = request.form['psw']
        e_wallet = request.form['wallet']
    return redirect(url_for('index'))


def validate_email(self):
    while True:
        email = input("Enter your email: ")
        if email in self:
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
            self.append(email)
            return True

def validate_password(passwords):
    while True:
        password = input("Enter a password: ")
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
    while True:
        e_wallet = input("Enter your e_wallet: ")
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

