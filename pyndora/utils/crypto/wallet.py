from enum import Enum
from bip_utils import (
    Bip39MnemonicGenerator,
    Bip39WordsNum,
    Bip39Languages,
    Bip39SeedGenerator,
    Bip39MnemonicValidator,
    Bip32Ed25519Slip,
    Bech32Encoder,
    Bech32Decoder,
    Bech32FormatError,
)
from pyndora.utils.crypto.xfr import XfrKeyPair


SET_LANG = {
    "english": Bip39Languages.ENGLISH,
}
SET_LENGTH = {
    12: Bip39WordsNum.WORDS_NUM_12,
    15: Bip39WordsNum.WORDS_NUM_15,
    18: Bip39WordsNum.WORDS_NUM_18,
    21: Bip39WordsNum.WORDS_NUM_21,
    24: Bip39WordsNum.WORDS_NUM_24,
}
DERIVATION = {
    "bip32": ""
}


class Hrp(Enum):
    Mainnet = "framain",
    Testnet = "fra"


class BipPath:
    """
    Bip44/Bip49 path
    """

    def __init__(self, coin: int, account: int,
                 change: int, address: int):
        self.coin = coin
        self.account = account
        self.change = change
        self.address = address


def generate_mnemonic_default():
    """
    Generate a mnemonic phrase with default values.
    English, 12 words.

    Parameters
        No input parameters

    Return
        phrase:str  mnemonic phrase
    """
    lang = Bip39Languages.ENGLISH
    length = Bip39WordsNum.WORDS_NUM_12
    phrase = Bip39MnemonicGenerator(lang).FromWordsNumber(length)

    return phrase


def generate_mnemonic_custom(length: int, lang="english") -> str:
    """
    Generate custom mnemonic for given length, language

    Parameters
        length:int  number of words of the mnemonic: check valid lengths
        lang:str    language of the mnemonic words -> defaults to english

    Return
        phrase:str  mnemonic phrase
    """

    if length not in SET_LENGTH.keys():
        raise ValueError(
            f"Length {length} is not in supported {SET_LENGTH.keys()}."
        )
    if lang not in SET_LANG.keys():
        raise ValueError(
            f"Language {lang} is not supported."
        )
    phrase = Bip39MnemonicGenerator(SET_LANG[lang]).FromWordsNumber(
        SET_LENGTH[length])

    return phrase


def restore_keypair_from_mnemonic(phrase, lang, path, bip) -> XfrKeyPair:
    """
    Restore XfrKeyPair from mnemonic phrase.

    Args:
        phrase:str  mnemonic phrase
        lang:str    mnemonic phrase language
        path:Bip44  Bip44 object
        bip:str     bip format

    Return
        keypair:XfrKeyPair  fra key pair object
    """

    if not Bip39MnemonicValidator().IsValid(phrase):
        raise ValueError(f"{phrase} is not a valid mnemonic.")

    mnemo_list = [x for x in phrase.split(" ")]
    if len(mnemo_list) not in SET_LENGTH.keys():
        raise ValueError(
            f"Length {len(mnemo_list)} is not supported: {SET_LENGTH.keys()}."
        )
    if lang not in SET_LANG.keys():
        raise ValueError(
            f"Language {lang} is not supported."
        )

    seed = Bip39SeedGenerator(phrase, SET_LANG[lang]).Generate()
    bip_path = f"m/44'/{path.coin}'/{path.account}'/{path.change}/{path.address}"
    bip32_ctx = Bip32Ed25519Slip.FromSeedAndPath(seed, bip_path)
    private = bip32_ctx.PrivateKey().Raw().ToBytes()

    keypair = XfrKeyPair()
    keypair.from_priv_key(private)

    return keypair


def restore_keypair_from_mnemonic_default(phrase) -> XfrKeyPair:
    """
    Restore XfrKeyPair from a mnemonic with a default bip44-path,
    that is "m/44'/917'/0'/0/0" ("m/44'/coin'/account'/change/address").

    Params
        phrase:str  mnemonic phrase


    Return
        restored:XfrKeyPair     key pair
    """
    fra = 917
    bip_path = BipPath(fra,
                       0,
                       0,
                       0)
    bip44 = ""
    restored = restore_keypair_from_mnemonic(phrase,
                                             "english",
                                             bip_path,
                                             bip44)

    return restored


def public_key_to_bech32(keypair: XfrKeyPair) -> str:
    """
    Generate Bech32 from public key.

    Parameters
        keypair:XfrKeyPair  wallet key pair

    Return
        addr:str    Bech32 address
    """

    try:
        addr = Bech32Encoder.Encode(Hrp.Testnet.value,
                                    keypair.pub_key_raw)
    except Bech32FormatError as err:
        raise Bech32FormatError(f"Failed to generate bech32 address: {err}")

    return addr


def bech32_to_public_key(address: str) -> str:
    """
    Generate public key from Bech32.

    Parameters
        address:str    Bech32 address

    Return
        pub_key:str    wallet key pair public key
    """

    try:
        pub_key = Bech32Decoder.Decode(Hrp.Testnet.value,
                                       address)
    except Bech32FormatError as err:
        raise Bech32FormatError(f"Failed to decode bech32 address: {err}")

    return pub_key
