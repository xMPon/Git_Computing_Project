from env.FrontEnd.connector import users, items, orders
from env.BackEnd.chain import Chain

Blockchain = Chain()
for n in range(10):
    last_block = Blockchain.latest_block
    last_hash = last_block.hash
    Blockchain.get_data(users=users,
                        items=items,
                        orders=orders)
    nonce = Blockchain.mining()
    block = Blockchain.build(nonce)
    print(Blockchain.chain)
    n += 1  # Create 10 blocks
