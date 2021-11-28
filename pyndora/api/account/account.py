from pyndora.utils.crypto.xfr import XfrKeyPair
from pyndora.utils.crypto.wallet import wallet

from pyndora.api.asset import asset

from pyndora.api.network import network

from pyndora.session import Session


def get_wei_balance(wallet_keypair: XfrKeyPair, asset_code: str) -> int:
    """
    Get wei balance from owend sids

    Parameters
        wallet_keypair:XfrKeyPair   wallet key pair
        asset_code:str  asset code

    Return
        wei_balance:int wallet balance in wei
    """
    # TODO: for now, use default SDK environment configuration
    net = network.Network(Session({}).environment)
    print(f"Network configuration environment: {net}")
    wei_balance = net.get_owned_sids(wallet_keypair.public_key, {})

    return wei_balance


def get_fra_balance(wallet_keypair: XfrKeyPair) -> str:
    """
    Method description

    Parameters
        wallet_keypair:XfrKeyPair   wallet key pair

    Return
        balance:str
    """
    asset_code = asset.get_fra_asset_code()
    wei_balance = get_wei_balance(wallet_keypair, asset_code)
    # balance = convert_wei(wei_balance, 6).
