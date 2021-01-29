

class Users(object):
    def __init__(self, email, password, e_wallet):
        super().__init__()
        self.email = email
        self.password = password
        self.e_wallet = e_wallet


    def __repr__(self):
        return f"<User: {self.emails}>"


users = []
users.append(Users(email="firstonem@gmail.com", password="asdafwef", e_wallet="34tg453534g5"))
users.append(Users(email="newemail@gmail.com", password="passwordsasd", e_wallet="2g52gt24g5"))
print(users)
