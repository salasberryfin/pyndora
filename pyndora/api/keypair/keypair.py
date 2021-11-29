from pyndora.utils.crypto import wallet
from pyndora.utils.crypto.xfr import (
    XfrKeyPair,
    to_base64,
    from_base64,
)
from pyndora.services.ledger import web_ledger


class LightWalletKeypar:
    """
    A `light` version of the WalletKeypar,
    containing only address and publickey
    """

    def __init__(self, address: str, public_key: str):
        """
        :param  addres:str FRA wallet address
        :param  public_key:str base64 encoded bytes FRA pub key
        """
        self.address = address
        self.public_key = public_key


class WalletKeypar(LightWalletKeypar):
    """
    A `full` version of the WalletKeypar.
    Adds private key to what's already in a LightWalletKeypar.
    """

    def __init__(self, address: str, public_key: str,
                 key_store, key_pair: XfrKeyPair, private_str: str):
        """
        :param  key_store: encrypted key store
        :param  key_pair:XfrKeyPair
        :param  private_str:str base64 encoded bytes FRA priv key

        -> To keep private keys secure, the key store is encrypted under 
        a user-provided password.
        
        -> The key store contains an encrypted seed that deterministically 
        generates new key pairs.
        
        Because key generation is deterministic, the key store only 
        needs to encrypt one element of data, the seed!
        
        The seed is encrypted under a master key (PBKDF2 key) 
        derived from the user-provided password. Because generating the master
        key is expensive, KeyStore exposes a utility for deriving it.
        
        Applications can derive the master key once on load and cache it for
        the duration of their lifetime.
        """
        LightWalletKeypar.__init__(self, address, public_key)
        self.key_store = key_store
        self.key_pair = key_pair
        self.private_str = private_str


def create_keypair(password: str) -> WalletKeypar:
    """
    Create new key pair wallet

    Parameters
        password:str    user password for protecting the key store object

    Return
        new_wallet:WalletKeypar     new wallet object
    """
    keypair = XfrKeyPair()
    keypair.generate()
    public_key_b64 = to_base64(keypair.pub_key_raw)
    private_key_b64 = to_base64(keypair.priv_key_raw)
    address = wallet.public_key_to_bech32(keypair)

    # TODO: get keypair_str -> encrypt and passed as key_store
    # encrypted = ledger.encryption_pbkdf2_aes256gcm(keypair_str, password)
    encrypted = "pbkdf2_aes256gcm encrypted value"

    new_wallet = WalletKeypar(
        address=address,
        public_key=public_key_b64,
        key_store=encrypted,
        key_pair="TODO",
        private_str=private_key_b64,
    )

    print(f"Created keypair data: {new_wallet}")

    return new_wallet


def create_ligth_keypair(address: str) -> LightWalletKeypar:
    """
    Convert address to public key and create light wallet from address/pub_key.
    :param  address:str wallet bech32 address
    :return light_wallet:LightWalletKeypar
    """
    # TODO
    # implement Bech32 -> Public Key converter
    # public_key = wallet.bech32_to_public_key(address)
    light_wallet = LightWalletKeypar(
        address=address,
    )
    return light_wallet


def get_mnemonic(length, lang="english"):
    """
    :param length:int number of words
    :param lang:str
    :return mnemonic:str
    """
    mnemonic = wallet.generate_mnemonic_custom(length, lang)

    return mnemonic


def restore_from_mnemonic(mnemonic: list, password: str) -> WalletKeypar:
    """
    Restore keypair from mnemonic phrase.

    Args
        mnemonic:str    mnemonic phrase
        password:str    user password for key pair encryption

    Return
        WalletKeypar    fra wallet object
    """

    keypair = wallet.restore_keypair_from_mnemonic_default(
        mnemonic)
    public_key_b64 = to_base64(keypair.pub_key_raw)
    private_key_b64 = to_base64(keypair.priv_key_raw)
    address = wallet.public_key_to_bech32(keypair)

    # TODO: get keypair_str -> encrypt and passed as key_store
    # encrypted = ledger.encryption_pbkdf2_aes256gcm(keypair_str, password)
    encrypted = "pbkdf2_aes256gcm encrypted value"

    restored_wallet = WalletKeypar(
        address=address,
        public_key=public_key_b64,
        key_store=encrypted,
        key_pair=keypair,
        private_str=private_key_b64,
    )

    return restored_wallet


def restore_from_private_key(priv_str: str, passwor: str) -> WalletKeypar:
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


def restore_from_key_store(key_store, password: str) -> WalletKeypar:
    """
    Decrypt key store, get keys and create new WalletKeypar
    :param  key_store:      uint8array
    :param  password:str    encrypting password
    :return new_wallet:WalletKeypar
    """
    # TODO: check uint8array
    new_wallet = WalletKeypar()
    return new_wallet
