import hashlib
import time


class Block(object):  # declare individual blocks
    def __init__(self, index, nonce, previous_hash, data, timestamp=None):
        self.index = index
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()

    @property
    def hash(self):
        str_block = "{}{}{}{}{}".format(self.index,
                                           self.nonce,
                                           self.previous_hash,
                                           self.data,
                                           self.timestamp)
        return hashlib.sha256(str_block.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index,
                                               self.nonce,
                                               self.previous_hash,
                                               self.data,
                                               self.timestamp)
