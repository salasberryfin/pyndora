from pyndora.api.keypair.keypair import WalletKeypar
from pyndora.api.network import network
from pyndora.api.asset import asset
from pyndora.services.utxo import (
    add_utxo,
    get_send_utxo,
    add_utxo_inputs,
)

from pyndora.sdk import Sdk


def get_transfer_operation():
    """
    """

    pass


def build_transfer_operation_with_fee(wallet_info: WalletKeypar):
    """

    """

    net = network.Network(Sdk().environment)
    sids = net.get_owned_sids(wallet_info.public_key, {})

    if not sids:
        print(f"Not sids were fecthed for address: {wallet_info.address}")

    utxo_data_list = add_utxo(wallet_info, sids)
    minimal_fee = asset.get_minimal_fee()
    fra_asset_code = asset.get_fra_asset_code()
    send_utxo_list = get_send_utxo(
        fra_asset_code,
        minimal_fee,
        utxo_data_list,
    )
    utxo_inputs_info = add_utxo_inputs(send_utxo_list)
    fra_pub_key = asset.get_fra_public_key()

    receiver_info = {
        "utxo_numbers": minimal_fee,
        "to_public_key": fra_pub_key,
    }

    transfer_operation = get_transfer_operation(
        wallet_info,
        utxo_inputs_info,
        [receiver_info],
        fra_asset_code,
    )

    pass
