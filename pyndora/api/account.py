from pyndora.api import (
    network,
    asset,
)
from pyndora.api.keypair import WalletKeypar

from pyndora.services.utxo import add_utxo
from pyndora.services import conversion

from pyndora.sdk import Sdk


def get_asset_balance(wallet_info: WalletKeypar, asset_code: str,
                      sids: list) -> float:
    """
    Get balance for the given asset and user.

    Parameters
        wallet_info:WalletKeypar    fra wallet object
        asset_code:str              fra/custom asset code
        sids:list                   list of owned sids

    Return
        balance:float       balance for given asset and user
    """

    balance = 0
    utxo_data_list = add_utxo(wallet_info, sids)

    if not utxo_data_list:
        return balance

    filtered_utxo_data_list = []
    for utxo_item in utxo_data_list:
        if utxo_item["body"]["asset_type"] == asset_code:
            filtered_utxo_data_list.append(utxo_item)

    if not filtered_utxo_data_list:
        return balance

    # TODO: sum amounts from all retrieved sids for given address?
    for filtered_utxo_item in filtered_utxo_data_list:
        balance = balance + float(filtered_utxo_item["body"]["amount"])

    return balance


def get_wei_balance(wallet_keypair: WalletKeypar, asset_code: str) -> float:
    """
    Get wei balance from owned sids.

    Parameters
        wallet_keypair:WalletKeypar   wallet key pair
        asset_code:str                asset code

    Return
        wei_balance:float   wallet balance in wei
    """

    net = network.Network(Sdk().environment)
    sids = net.get_owned_sids(wallet_keypair.public_key, {})
    if not sids:
        print(f"No FRA balance retrieved for {wallet_keypair.address}")
        wei_balance = 0
    else:
        wei_balance = get_asset_balance(wallet_keypair, asset_code, sids)

    return wei_balance


def get_balance(wallet_keypair: WalletKeypar, asset_code: str = None) -> str:
    """
    Get the balance of the specific asset for the given user.
    Can be either a FRA or a custom asset.

    Parameters
        wallet_keypair:WalletKeypar   fra wallet object

    Return
        balance:str
    """

    if not asset_code:
        asset_code = asset.get_fra_asset_code()
    wei_balance = get_wei_balance(wallet_keypair, asset_code)
    balance = conversion.from_wei(wei_balance, 6)

    return balance
