import time
from env.BackEnd.chain import Chain
from env.FrontEnd.connector import users, items, orders

Blockchain = Chain()
# while True:  loop doesn't finish so the web app won't work
# https://stackoverflow.com/questions/38254172/infinite-while-true-loop-in-the-background-python
while True:
    last_block = Blockchain.latest_block
    last_proof = last_block.nonce
    nonce = Blockchain.proof(last_proof)
    Blockchain.get_data(
        users=users,  # this means that this node has constructed another block
        items=items,
        orders=orders)  # building a new block (or figuring out the proof number) is awarded with 1
    last_hash = last_block.hash
    block = Blockchain.build(nonce, last_hash)
    print(Blockchain.chain)
    time.sleep(5)
