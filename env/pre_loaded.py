users = []
users.append(User(business='seller', email='a@a', password='a', ewallet='WTDsdg43f23g2'))
users.append(User(business='seller', email='b@b', password='b', ewallet='f343f34f34f'))
users.append(User(business='buyer', email='o@o', password='o', ewallet='3f4d3d33f3f'))
users.append(User(business='buyer', email='two@gmail.com', password='pass3', ewallet='WTDsd34f3f3g43f23g2'))
items = []
items.append(Item(item_id='1', seller='a@a', description='Metal', quantity=20, price=300, date='02/12/21'))
items.append(Item(item_id='2', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='3', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='4', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='5', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='6', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='7', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='8', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='9', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='10', seller='a@a', description='Sand', quantity=20, price=100, date='02/12/21'))
items.append(Item(item_id='11', seller='b@b', description='Coal', quantity=10, price=199, date='02/12/21'))
items.append(Item(item_id='12', seller='b@b', description='Iron', quantity=1000, price=50, date='02/12/21'))
orders = []
orders.append(
    UsersData(seller='a@a', buyer='o@o', seller_wallet='WTDsdg43f23g2',
              buyer_wallet='3f4d3d33f3f', item='Metal', quantity=20, price=300, date='02/12/21'))
orders.append(
    UsersData(seller='a@a', buyer='two@gmail.com', seller_wallet='WTDsdg43f23g2',
              buyer_wallet='WTDsd34f3f3g43f23g2', item='Metal', quantity=20, price=300, date='02/12/21'))
orders.append(
    UsersData(seller='b@b', buyer='o@o', seller_wallet='f343f34f34f',
              buyer_wallet='3f4d3d33f3f', item='Metal', quantity=20, price=300, date='02/12/21'))
