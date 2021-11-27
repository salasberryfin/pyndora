from pyndora.utils.crypto.xfr import XfrKeyPair
from pyndora.utils.crypto.wallet import wallet

from pyndora.api.asset import asset

from pyndora.api.network import network

from pyndora.session import Session


def get_wei_balance(wallet_keypair: XfrKeyPair, asset_code: str) -> str:
    """
    Method description

    Parameters
        walleT_keypair:XfrKeyPair   wallet key pair
        asset_code:str  asset code

    Return
        wei_balance:str wallet balance in wei
    """
    wei_balance = ""
    # TODO: for now, use default SDK environment configuration
    net_connect = network.Network(Session({}).environment)
    print(f"Network configuration environment: {net_connect}")

    return wei_balance


def get_fra_balance(walleT_keypair: XfrKeyPair) -> str:
    """
    Method description

    Parameters
        wallet_keypair:XfrKeyPair   wallet key pair

    Return
        balance:str
    """
    asset_code = asset.get_fra_asset_code()
    wei_balance = get_wei_balance(walleT_keypair, asset_code)
    # balance = convert_wei(wei_balance, 6).
