from pyndora.utils.crypto import wallet

class LightWalletKeypair:
    """
    A `light` version of the WalletKeypar, containing only address and publickey
    """

    def __init__(self, address: str, public_key: str):
        """
        :param  addres:str FRA wallet address
        :param  public_key:str FRA
        """
        self.address = address
        self.public_key = public_key
    

class WalletKeypair:
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


def get_mnemonic(length, lang="english"):
    """
    :param length:int number of words
    :param lang:str
    :return str
    """
    ledger_mnemonic = wallet.generate_mnemonic_custom(length, lang)

    return ledger_mnemonic

def restore_from_mnemonic(mnemonic:[], password:str):
    """
    :param  mnemonic:[]str
    :param  password:str
    """
    ledger = get_ledger()
    keypair = ledge.restore_keypar_from_mnemonic_default(mnemonic.join(" "))
    keypair_str = get_private_key_str(keypair)
    encrypted = ledger.encryption_pbkdf2_aes256gcm(keypair_str, password)

    public_key = get_public_key_str(keypair)
    address = get_address(keypair)

    return {
        "key_store": encrypted,
        "public_key": public_key,
        "addres": address,
        "keypair": keypair,
        "private_str": keypair_str,
    }

def create_keypair(password: str):
    """
    :param  password:str user password that protects the key store object
    """
    ledger = get_ledger()

    try:
        keypair = ledger.new_keypair()
        keypair_str = ledger.keypair_to_str(keypair)
        encrypted = ledger.encryption_pbkdf2_aes256gcm(keypair_str, password)

        private_str = get_private_key_str(keypair)
        public_key = get_public_key_str(keypair)
        address = get_address(keypair)

        return {
            "key_store": encrypted,
            "public_key": public_key,
            "addres": address,
            "keypair": keypair,
            "private_str": keypair_str,
        }
    except:
        print("Could not create a WalletKeypair")

