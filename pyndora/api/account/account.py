from pyndora.utils.crypto.xfr import XfrKeyPair

from pyndora.api.asset import asset
from pyndora.api.keypair.keypair import WalletKeypar
from pyndora.api.network import network

from pyndora.services.utxo import add_utxo

from pyndora.sdk import Sdk


def get_asset_balance(wallet_info: WalletKeypar, asset_code: str, sids: list):
    """
    Method description

    Parameters
        Arg1:

    Return
        Return
    """
    
    utxo_data_list = add_utxo(wallet_info, sids)
    # import pdb; pdb.set_trace()

    pass


def get_wei_balance(wallet_keypair: WalletKeypar, asset_code: str) -> int:
    """
    Get wei balance from owend sids

    Parameters
        wallet_keypair:WalletKeypar   wallet key pair
        asset_code:str  asset code

    Return
        wei_balance:int wallet balance in wei
    """
    net = network.Network(Sdk().environment)
    sids = net.get_owned_sids(wallet_keypair.public_key, {})
    if not sids:
        print(f"No FRA balance retrieved for {wallet_keypair.public_key}")
        wei_balance = 0
    else:
        # TODO: get_asset_balance -> utxos
        wei_balance = get_asset_balance(wallet_keypair, asset_code, sids)

    return wei_balance


def get_fra_balance(wallet_keypair: WalletKeypar) -> str:
    """
    Method description

    Parameters
        wallet_keypair:WalletKeypar   wallet key pair

    Return
        balance:str
    """
    asset_code = asset.get_fra_asset_code()
    wei_balance = get_wei_balance(wallet_keypair, asset_code)
    # balance = convert_wei(wei_balance, 6).
