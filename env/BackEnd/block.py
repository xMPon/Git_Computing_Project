import time
import hashlib


class Block:  # declare individual blocks
    def __init__(self, index, nonce, previous_hash, data, timestamp=None):
        self.index = index
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()

    @property
    def hash(self):
        str_block = "{}{}{}{}{}".format(str(self.index),
                                        str(self.nonce),
                                        str(self.previous_hash),
                                        str(self.data),
                                        str(self.timestamp))
        return hashlib.sha256(str_block.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(str(self.index),
                                               str(self.nonce),
                                               str(self.previous_hash),
                                               str(self.data),
                                               str(self.timestamp))
