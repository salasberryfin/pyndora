from mnemonic import Mnemonic
from pyndora.utils.crypto.xfr import XfrKeyPair


def new_keypair():
    """
    :return     XfrKeyPair
    """
    xfr_key_pair = XfrKeyPair()
    xfr_key_pair.generate()

    return xfr_key_pair

def generate_mnemonic_default():
    mnemo = Mnemonic("english")
    phrase = mnemo(strength=128)

    return phrase

def generate_mnemonic_custom(length, lang="english"):
    accepted = [12, 15, 18, 21, 24]
    if length not in accepted:
        raise ValueError(
            f"Length {length} is not in the list of supported values {accepted}."
        )
    strength = length * 8
    mnemo = Mnemonic(lang)
    phrase = mnemo.generate(strength=strength)

    return phrase

