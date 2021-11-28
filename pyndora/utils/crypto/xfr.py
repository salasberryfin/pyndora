import base64

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519


class XfrKeyPair:
    """
    XfrKeyPair {
        pub_key: raw bytes public key
        priv_key: raw bytes private key
    }
    """

    @property
    def pub_key(self):
        return self._pub_key

    @property
    def pub_key_raw(self):
        return self._pub_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )

    @property
    def pub_key_base64(self):
        b64 = base64.b64encode(self._pub_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        ))
        return b64

    @property
    def priv_key(self):
        return self.__priv_key

    @property
    def priv_key_raw(self):
        return self.__priv_key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption(),
        )

    def generate(self):
        """
        Create new key pair
        """
        self.__priv_key = ed25519.Ed25519PrivateKey.generate()
        self._pub_key = self.__priv_key.public_key()

    def from_priv_key(self, private: str):
        """
        Create key pair from private key
        :param  private:str 64 hex characters private key
        """
        private_bytes = bytes(private)
        self.__priv_key = ed25519.Ed25519PrivateKey.from_private_bytes(
            data=private_bytes,
        )
        self._pub_key = self.__priv_key.public_key()

    def destroy_into_raw(self):
        pass

    def free(self):
        pass


def to_base64(key: bytes) -> bytes:
    """
    Encode key string to base64

    Parameters
        key:bytes     raw bytes to encode

    Return
        encoded:bytes encoded bytes object
    """
    try:
        encoded = base64.urlsafe_b64encode(key)
    except TypeError as error:
        raise TypeError(f"Invalid value for encoding: {error}.")

    return encoded


def from_base64(key: bytes) -> bytes:
    """
    Decode key string to base64

    Parameters
        key:bytes     base64 bytes to decode

    Return
        decoded:bytes decoded bytes object
    """
    try:
        decoded = base64.urlsafe_b64decode(key)
    except TypeError as error:
        raise TypeError(f"Invalid value for encoding: {error}.")

    return decoded
