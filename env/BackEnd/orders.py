class UsersData(object):
    def __init__(self,
                 seller,
                 buyer,
                 seller_wallet,
                 buyer_wallet,
                 item,
                 quantity,
                 price,
                 date):
        self.seller = seller
        self.buyer = buyer
        self.seller_wallet = seller_wallet
        self.buyer_wallet = buyer_wallet
        self.item = item
        self.quantity = int(quantity)
        self.price = int(price)
        self.date = date

    def __repr__(self):  # delete when finished to hide the data
        return f'{self.seller} {self.buyer} {self.item} {self.quantity} {self.price} {self.date}'
