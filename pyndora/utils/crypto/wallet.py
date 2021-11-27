import binascii
from enum import Enum
from ctypes import c_uint32
# from mnemonic import Mnemonic
from bip_utils import (
    Bip39MnemonicGenerator, Bip39WordsNum, Bip39Languages, Bip39SeedGenerator,
    Bip44, Bip44Coins,
    SegwitBech32Encoder, SegwitBech32Decoder
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

    def __init__(self, coin: c_uint32, account: c_uint32,
                 change: c_uint32, address: c_uint32):
        self.coin = coin
        self.account = account
        self.change = change
        self.address = address


def new_keypair():
    """
    :return     XfrKeyPair
    """
    xfr_key_pair = XfrKeyPair()
    xfr_key_pair.generate()

    return xfr_key_pair


def generate_mnemonic_default():
    """
    Generate a mnemonic phrase with default values.
    English, 12 words.

    :return mnemonic
    """
    phrase = Bip39MnemonicGenerator(Bip39Languages.ENGLISH).FromWordsNumber(
        Bip39WordsNum.WORDS_NUM_12)

    return phrase


def generate_mnemonic_custom(length, lang="english"):
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


def restore_keypair_from_mnemonic(phrase, lang, path, bip):
    """
    """
    # TODO

    mnemo_list = [x for x in phrase.split(" ")]
    if len(mnemo_list) not in SET_LENGTH.keys():
        raise ValueError(
            f"Length {len(mnemo_list)} is not supported: {SET_LENGTH.keys()}."
        )
    if lang not in SET_LANG.keys():
        raise ValueError(
            f"Language {lang} is not supported."
        )
    seed_bytes = Bip39SeedGenerator(phrase).Generate()
    bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.FINDORA)
    # Test prints
    print(f"Master key (bytes): {bip44_mst_ctx.PrivateKey().Raw().ToHex()}")
    print(f"Master key (extended): {bip44_mst_ctx.PrivateKey().ToExtended()}")
    print(f"Master key (WIF): {bip44_mst_ctx.PrivateKey().ToWif()}")
    extended_secret_key = bip44_mst_ctx.PrivateKey().ToExtended()
    # bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(path["account"])

    return bip44_mst_ctx


# Restore the XfrKeyPair from a mnemonic with a default bip44-path,
# that is "m/44'/917'/0'/0/0" ("m/44'/coin'/account'/change/address").
def restore_keypair_from_mnemonic_default(phrase):
    """
    """
    # TODO
    fra = c_uint32(917)
    xfr_key_pair = XfrKeyPair()
    bip_path = BipPath(fra,
                       c_uint32(0),
                       c_uint32(0),
                       c_uint32(0))
    bip44 = ""
    restore_keypair_from_mnemonic(phrase,
                                  "english",
                                  bip_path,
                                  bip44)

    return xfr_key_pair


# Generate Segwit Bech32 address from public key
def public_key_to_bech32(keypair: XfrKeyPair) -> str:
    addr = SegwitBech32Encoder.Encode(Hrp.Testnet.value,
                                      0,
                                      keypair.pub_key_raw)

    return addr
