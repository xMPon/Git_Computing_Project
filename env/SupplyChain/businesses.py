class User:
    def __init__(self, n, business, email, password, ewallet):
        self.users = []
        self.n = n
        self.business = business
        self.email = email
        self.password = password
        self.ewallet = ewallet
        self.users = [[n], [business], [email], [password], [ewallet]]

    def __repr__(self):
        return f'<User:{self.email}>'
