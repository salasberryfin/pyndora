from mnemonic import Mnemonic
from pyndora.utils.crypto import xfr

def new_keypair():
    """
    :return     XfrKeyPair
    """
    xfr_key_pair = XfrKeyPair()
    xfr_key_pair.generate()

    return xfr_key_pair

def generate_mnemonic_default():
    """
    :return str:mnemonic phrase
    """
    mnemo = Mnemonic("english")
    phrase = mnemo.generate(strength=128)

    return phrase

def generate_mnemonic_custom(length, language):
    """
    :param length:int number of words
    :param language:str
    :return str:mnemonic phrase
    """
    strength = length * 8
    accepted = [128, 160, 192, 224, 256]
    if strength not in accepted:
        raise ValueError(
            f"Strength should be one of the following {accepted}, but it is not {strength}."
        )
    mnemo = Mnemonic(language)
    phrase = mnemo.generate(strength=strength)

    return phrase

