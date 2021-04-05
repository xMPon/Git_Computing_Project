from env.BackEnd.block import Block                                 # Import block structure
import secrets                                                      # Import of hex n. generator


class Chain:
    def __init__(self):
        self.chain = []                                             # Create empty chain list
        self.current_data = [], [], []                              # Create empty data lists
        self.genesis()                                              # Create first block in the chain

    def genesis(self):                                              # First block function
        self.build(block=Block(index=len(self.chain),               # Index number in the chain
                               nonce=0,                             # First nonce set to 0
                               previous_hash=0x0,                   # There is no previous block
                               data=self.current_data))             # Set empty lists

    @staticmethod
    def validate(block, previous_block):
        if previous_block.index + 1 != block.index:                 # Validation by previous block
            return False
        elif previous_block.hash != block.previous_hash:            # If the previous block is different
            return False
        elif block.timestamp <= previous_block.timestamp:           # Validation by timestamp
            return False
        return True

    def get_data(self, users, items, orders):                       # Change this format to match the supply chain information
        self.current_data = users, items, orders                    # Append lists into current data
        return True

    @property
    def last_block(self):
        return self.chain[-1]                                       # Retrieve the last block in the list 'chain'

    ###################################################################################################################
    # The mining process has been interpreted from Tracey (2021), article on 'Building a Blockchain in Python'
    # Available at: "https://medium.datadriveninvestor.com/building-a-blockchain-in-python-f194a26530fd"
    # Accessed: 04 April 2021
    def mining(self, max_nonce=2 ** 256):
        nonce = 0
        for n in range(max_nonce):                                  # Max Nonce = the largest possible number
            difficulty = secrets.token_hex(2)                       # Random hex generator (max 3**35)
            if self.last_block.hash.startswith(difficulty):
                # Compares if the first 3 characters from the last hashed block are equal to the difficulty
                block = Block(index=len(self.chain),
                              nonce=nonce,
                              previous_hash=self.last_block.hash,
                              data=self.current_data)
                return block
            else:
                nonce += 1                                          # Nonce counter used for the block nonce difficulty
    ###################################################################################################################

    def build(self, block):
        self.chain.append(block)                                    # Adds the 'block' to the list 'chain'
        return block
