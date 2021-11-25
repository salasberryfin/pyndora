from pyndora.utils.crypto import wallet
from pyndora.utils.crypto.xfr import XfrKeyPair
from pyndora.services.ledger import web_ledger


class LightWalletKeypar:
    """
    A `light` version of the WalletKeypar,
    containing only address and publickey
    """

    def __init__(self, address: str, public_key: str):
        """
        :param  addres:str FRA wallet address
        :param  public_key:str FRA
        """
        self.address = address
        self.public_key = public_key


class WalletKeypar:
    """
    A `full` version of the WalletKeypar, containing only address and publickey
    """

    def __init__(self, key_store, key_pair, private_str):
        """
        :param  key_store: encrypted key store
        :param  key_pair: instance of XfrKeyPair
        :param  private_str:str
        """
        self.key_store = key_store
        self.key_pair = key_pair
        self.private_str = private_str


def create_keypair(password: str):
    """
    :param  password:str user password that protects the key store object
    """
    keypair = XfrKeyPair()
    keypair.generate()
    public_key_str = keypair.pub_key_raw.hex()
    private_key_str = keypair.priv_key_raw.hex()
    address = wallet.public_key_to_bech32(keypair)

    # TODO: get keypair_str -> encrypt and passed as key_store
    # encrypted = ledger.encryption_pbkdf2_aes256gcm(keypair_str, password)
    encrypted = "pbkdf2_aes256gcm encrypted value"

    created = {
        "key_store": encrypted,
        "public_key": public_key_str,
        "address": address,
        "private_str": private_key_str,
    }

    print(f"Created keypair data: {created}")

    return created


def get_mnemonic(length, lang="english"):
    """
    :param length:int number of words
    :param lang:str
    :return mnemonic:str
    """
    mnemonic = wallet.generate_mnemonic_custom(length, lang)

    return mnemonic


def restore_from_mnemonic(mnemonic: [], password: str):
    """
    :param  mnemonic:[]str
    :param  password:str
    """
    keypair = wallet.restore_keypair_from_mnemonic_default(
        mnemonic.ToStr())
    public_key_str = keypair.pub_key_raw.hex()
    private_key_str = keypair.priv_key_raw.hex()
    address = wallet.public_key_to_bech32(keypair)

    # TODO: get keypair_str -> encrypt and passed as key_store
    # encrypted = ledger.encryption_pbkdf2_aes256gcm(keypair_str, password)
    encrypted = "pbkdf2_aes256gcm encrypted value"

    restored = {
        "key_store": encrypted,
        "public_key": public_key_str,
        "addres": address,
        "keypair": keypair,
        "private_str": private_key_str,
    }

    print(f"Restored keypair data: {restored}")

    return restored


def restore_from_keypair(priv_str: str, passwor: str) -> WalletKeypar:
    """
    Create instance of WalletKeypar using given private key and password

    Used to restore a wallet key pair

    The Keypair contains:
    - address
    - public key
    - key store

    :param  priv_str:str    private key
    :param  password:str    password used to generate encrypted Keystore
    :return wallet_info:WalletKeypar
    """
    keypair = web_ledger.create_keypair_from_secret(priv_str)
    pass


def restore_from_private_key(private, password) -> XfrKeyPair:
    """
    """
    # TODO: support password protected private keys
    keypair = XfrKeyPair()
    try:
        keypair.from_priv_key(
            private_bytes=private,
        )
    except:
        raise("error when restoring from private key")

    return keypair
