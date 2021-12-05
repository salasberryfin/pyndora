from pyndora.api.keypair.keypair import WalletKeypar
from pyndora.api.keypair.keypair import address_to_public_key
from pyndora.services.big_number import to_wei
from pyndora.api.asset import asset


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
        utxo_numbers = to_wei(float(rec["amount"]))
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

    # import pdb;pdb.set_trace()

    # TODO: transfer operation builder

    pass


def send_to_address(wallet_info: WalletKeypar, to_addr: str,
                    amount: str, asset_code: str = None):
    """
    Generate a transaction builder to send amount to given address.

    Parameters
        wallet_info:
        to_addr:
        amount:
        asset_code:

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
