class UsersData(object):
    def __init__(self,
                 transaction_id,
                 seller,
                 buyer,
                 seller_wallet,
                 buyer_wallet,
                 item,
                 quantity,
                 price,
                 date):
        self.transaction_id = transaction_id
        self.seller = seller
        self.buyer = buyer
        self.seller_wallet = seller_wallet
        self.buyer_wallet = buyer_wallet
        self.item = item
        self.quantity = quantity
        self.price = price
        self.date = date

    def __repr__(self):
        return f'<UsersData:{self.transaction_id}>'
