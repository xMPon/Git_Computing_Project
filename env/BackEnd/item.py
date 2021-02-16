class Item(object):
    def __init__(self,
                 item_id,
                 seller,
                 description,
                 quantity,
                 price,
                 date):
        self.item_id = int(item_id)
        self.seller = seller
        self.description = description
        self.quantity = int(quantity)
        self.price = int(price)
        self.date = date

    def __repr__(self):
        return f'{self.item_id} {self.seller} {self.description} {self.quantity} {self.price} {self.date}'
