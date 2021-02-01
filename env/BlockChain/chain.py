from env.BlockChain.block import Block


class Chain(object):  # declare the
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.genesis()

    def genesis(self):  # create first block in the chain
        self.build_block(proof_number=0, previous_hash=0)

    def build_block(self, proof_number, previous_hash):  # establish block content
        block = Block(
            index=len(self.chain),
            proof_number=proof_number,
            previous_hash=previous_hash,
            data=self.current_data)
        self.current_data = []
        self.chain.append(block)
        return block

    @staticmethod
    def confirm_validity(block, previous_block):
        if previous_block.index + 1 != block.index:  # validation by previous block
            return False
        elif previous_block.compute_hash != block.previous_hash:  #
            return False
        elif block.timestamp <= previous_block.timestamp:  # validation by timestamp
            return False
        return True

    def get_data(self, sender, receiver, amount):  # change this format to match the supply chain information
        self.current_data.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount})
        return True

    @staticmethod
    def proof(last):
        pass

    @property
    def latest_block(self):
        return self.chain[-1]

    def chain_validity(self):
        pass

    def block_mining(self, miner):
        self.get_data(
            sender="0",  # it implies that this node has created a new block
            receiver=miner,
            quantity=1,  # creating a new block (or identifying the proof number) is awarded with 1
        )
        last_block = self.latest_block
        last_proof = last_block.proof_number
        proof_number = self.proof(last_proof)
        last_hash = last_block.compute_hash
        block = self.build_block(proof_number, last_hash)
        return vars(block)

    def create_node(self, address):
        self.nodes.add(address)
        return True

    @staticmethod
    def get_block_object(block_data):
        return Block(
            block_data['index'],
            block_data['proof_number'],
            block_data['previous_hash'],
            block_data['data'],
            timestamp=block_data['timestamp'])
