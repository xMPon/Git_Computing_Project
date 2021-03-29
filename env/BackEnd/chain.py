from env.BackEnd.block import Block


class Chain:
    def __init__(self):
        self.chain = []
        self.current_data = [], [], []
        self.genesis()

    def genesis(self):  # create first block in the chain
        self.build(block=Block(index=len(self.chain),
                               nonce=0,
                               previous_hash=0x0,
                               data=self.current_data))

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
        max_nonce = 2 ** 32
        difficulty = 0
        goal = 2 ** (256 - difficulty)
        nonce = self.latest_block.nonce
        for n in range(max_nonce):
            last_hash = int(str(self.latest_block.hash), 16)
            if last_hash <= goal:
                block = Block(index=len(self.chain),
                              nonce=nonce,
                              previous_hash=last_hash,
                              data=self.current_data)
                return block
            else:
                nonce += 1
                print(nonce)

    def build(self, block):  # establish block content
        self.chain.append(block)
        return block

    @staticmethod
    def get_block(block_data):
        return Block(
            block_data['index'],
            block_data['nonce'],
            block_data['previous_hash'],
            block_data['data'],
            timestamp=block_data['timestamp'])
