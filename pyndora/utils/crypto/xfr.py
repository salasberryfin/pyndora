import nacl.utils
from nacl.public import PrivateKey


class XfrKeyPair:
    """
    XfrKeyPair {
        pub_key: pynacl.PublicKey object
    }
    """

    @property
    def pub_key(self):
        return bytes(self._pub_key).hex()

    def __init__(self):
        self._pub_key = None

    def generate(self):
        """
        Create new key pair
        """
        self.priv_key = PrivateKey.generate()
        self._pub_key = self.priv_key.public_key

    def from_priv_key(self, secret):
        """
        Create key pair from private key
        """
        self.priv_key = secret
        self._pub_key = secret.public_key

    def destroy_into_raw(self):
        pass

    def free(self):
        pass

