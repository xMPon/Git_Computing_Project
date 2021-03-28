from env.BackEnd.block import Block


class Chain:
    difficulty = 20
    maxN = 2**32
    goal = 2**(256-difficulty)

    def __init__(self):
        self.chain = []
        self.current_data = [], [], []
        self.genesis()

    def genesis(self):  # create first block in the chain
        self.build(nonce=0, previous_hash=0)

    def build(self, nonce, previous_hash):  # establish block content
        block = Block(
            index=len(self.chain),
            nonce=nonce,
            previous_hash=previous_hash,
            data=self.current_data)
        self.current_data = [], [], []
        self.chain.append(block)
        return block

    @staticmethod
    def validate(block, previous_block):
        if previous_block.index + 1 != block.index:  # validation by previous block
            return False
        elif previous_block.hash != block.previous_hash:  # if the previous block is different
            return False
        elif block.timestamp <= previous_block.timestamp:  # validation by timestamp
            return False
        return True

    def get_data(self, users, items, orders):  # change this format to match the supply chain information
        self.current_data = users, items, orders
        return True

    @staticmethod
    def proof(self):
        pass

    @property
    def latest_block(self):  # Retrieve the last block
        return self.chain[-1]

    def mining(self):
        last_block = self.latest_block
        last_proof = last_block.nonce
        nonce = self.proof(last_proof)
        last_hash = last_block.previous_hash
        block = self.build(nonce, last_hash)
        return vars(block)

    @staticmethod
    def get_block(block_data):
        return Block(
            block_data['index'],
            block_data['nonce'],
            block_data['previous_hash'],
            block_data['data'],
            timestamp=block_data['timestamp'])
