class User:
    def __init__(self,
                 business,
                 email,
                 password,
                 ewallet):
        self.business = business
        self.email = email
        self.password = password
        self.ewallet = ewallet

    def __repr__(self):
        return f'<User:{self.email}>'
