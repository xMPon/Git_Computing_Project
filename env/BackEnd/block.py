import time                 # Import time
import hashlib              # Import SHA256


class Block:                # Block blueprint
    def __init__(self, index, nonce, previous_hash, data, timestamp=None):
        self.index = index
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()

    @property
    def hash(self):
        encrypted = "{}{}{}{}{}".format(self.index,
                                        self.nonce,
                                        self.previous_hash,
                                        self.data,
                                        self.timestamp)
        return hashlib.sha256(encrypted.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index,
                                               self.nonce,
                                               self.previous_hash,
                                               self.data,
                                               self.timestamp)
