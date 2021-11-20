import nacl.utils
from nacl.public import PrivateKey

class XfrPublicKey:

    def __init__(self):
        pass

    def clone(self):
        pass

    def copy(self):
        pass

    def debug(self):
        pass

    def default(self):
        pass


class XfrSecretKey:

    def __init__(self):
        pass

    def debug(self):
        pass


class XfrKeyPair:

    def generate(self):
        self.sk = PrivateKey.generate()
        self.pk = self.sk.public_key

    def clone(self):
        pass

    def debug(self):
        pass

    def serialize(self):
        pass

    def deserialize(self):
        pass

