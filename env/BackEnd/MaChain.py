from env.FrontEnd.connector import users, items, orders     # Import the lists
from env.BackEnd.chain import Chain                         # Import the blockchain architecture


Blockchain = Chain()                                        # Start the blockchain
print("Blockchain:")
while True:                                                 # Continuous loop to create new blocks
    Blockchain.get_data(users=users,
                        items=items,
                        orders=orders)                      # Import lists
    block = Blockchain.mining()                             # Start mining process
    Blockchain.build(block)                                 # Pass the created block
    print(Blockchain.chain)                                 # Display blockchain
