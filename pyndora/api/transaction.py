from pyndora.api.keypair import (
    WalletKeypar,
    address_to_public_key,
)
from pyndora.services import (
    conversion,
    fee,
)
from pyndora.api import asset


def send_to_many(wallet_info: WalletKeypar, receivers: list,
                 asset_code: str):
    """
    Send to multiple addresses.

    Parameters
        wallet_info:
        receivers:
        amount:
        asset_code:

    Return
        Return
    """

    receivers_info = []
    for rec in receivers:
        to_pub_key = rec["receiver_wallet_info"].public_key.decode("utf-8")
        utxo_numbers = conversion.to_wei(float(rec["amount"]))
        rec_info = {
            "to_public_key": to_pub_key,
            "utxo_numbers": utxo_numbers,
        }
        receivers_info.append(rec_info)

    fra_asset_code = asset.get_fra_asset_code()
    if asset_code == fra_asset_code:
        minimal_fee = asset.get_minimal_fee()
        fra_pub_key = asset.get_fra_public_key()
        fee_rec_info = {
            "to_public_key": fra_pub_key,
            "utxo_numbers": minimal_fee,
        }
        receivers_info.append(fee_rec_info)

    # TODO: transfer operation builder
    tx_operation_builder = fee.build_transfer_operation(
        wallet_info,
        receivers_info,
        asset_code,
    )

    # import pdb;pdb.set_trace()

    pass


def send_to_address(wallet_info: WalletKeypar, to_addr: str,
                    amount: str, asset_code: str = None):
    """
    Generate a transaction builder to send amount to given address.

    Parameters
        wallet_info:WalletKeypar    fra wallet object
        to_addr:str                 destination fra address
        amount:str                  amount to send
        asset_code:str              asset to send: defaults to FRA if None

    Return
        transaction builder
    """
    if not asset_code:
        asset_code = asset.get_fra_asset_code()

    light_wallet_info = address_to_public_key(to_addr)
    receiver_info = {
           "receiver_wallet_info": light_wallet_info,
           "amount": amount,
    }

    return send_to_many(
        wallet_info,
        [receiver_info],
        asset_code,
    )


def submit_transaction():
    """
    Submit transaction to the ledger.
    """

    pass
