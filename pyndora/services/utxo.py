from pyndora.api.keypair import WalletKeypar
from pyndora.api import network
from pyndora.cachestore.cache import (
    CacheFactory,
)
from pyndora.cachestore.config import CacheEntries
from pyndora.services.ledger import web_ledger as ledger
from pyndora.sdk import Sdk


def decrypt_utxo_item(sid: int, wallet_info: WalletKeypar,
                      utxo: dict, memo: dict):
    """
    Decrypt UTXO item.
    ** I don't know what's happening behind in the web assembly implementation
    so I'll just parse the data received from the network.

    Parameters
        Arg1:

    Return
        Return
    """

    asset_record = ledger.ClientAssetRecord.from_json(utxo["utxo"])

    owner_memo = memo

    decrypted_asset = ledger.open_client_asset_record(
        asset_record,
        owner_memo,
        wallet_info.key_pair,
    )

    item = {
        "address": wallet_info.address,
        "sid": sid,
        "body": decrypted_asset,
        "utxo": utxo["utxo"],
        "owner_memo": owner_memo,
    }

    return item


def get_utxo_item(sid: int, wallet_info: WalletKeypar, cached_item: dict):
    """
    Get UTXO item from network.

    Parameters
        sid:int                     sid id
        wallet_info:WalletKeypar    fra wallet object
        cached_item:dict            cache item

    Return
        item:decrypted item
    """
    sdk_config = Sdk()
    sdk_environment = sdk_config.environment

    if cached_item:
        return cached_item

    net = network.Network(sdk_environment)

    print(f"Fetching sid {sid}")
    utxo_data = net.get_utxo(sid, {})
    memo_data = net.get_owner_memo(sid, {})

    item = decrypt_utxo_item(sid, wallet_info, utxo_data, memo_data)

    return item


def add_utxo(wallet_info: WalletKeypar, sids: list):
    """
    Create list of items with decrypted UTXO information

    Parameters
        wallet_info:WalletKeypar    fra wallet object
        sids:list(str)              list of sid ids

    Return
        Return
    """
    utxo_data = []
    cache_to_save = dict()
    sdk_config = Sdk()
    sdk_provider = sdk_config.environment["cache_provider"]

    entry_name = f"{CacheEntries.UTXO_DATA.value}_{wallet_info.address}"
    full_path = f"{sdk_config.environment['cache_path']}/{entry_name}.json"
    cache = CacheFactory()
    utxo_data_cache = cache.read(
        entry_name=full_path,
        provider=sdk_provider,
    )

    if not utxo_data_cache:
        utxo_data_cache = {}
        print(f"Cache data for '{full_path}' is empty.")

    for sid in sids:
        utxo_data_sid = utxo_data_cache.get(f"sid_{sid}", None)
        item = get_utxo_item(sid, wallet_info, utxo_data_sid)
        utxo_data.append(item)
        cache_to_save[f"sid_{item['sid']}"] = item

    cache.write(full_path, cache_to_save, sdk_provider)

    return utxo_data


def get_send_utxo(asset_code: str, amount: float, utxo_data: list):
    """
    Create list of utxo like objects for the send operation.

    Parameters
        asset_code:str
        amount:float
        utxo_data:list

    Return
        result:list     list of utxo data items
    """

    balance = amount

    result = []
    for item in utxo_data:
        if item["body"]["asset_type"] == asset_code:
            _amount = float(item["body"]["amount"])
            if balance < float(0):
                break
            elif _amount >= balance:
                result.append({
                        "amount": balance,
                        "origin_amount": _amount,
                        "sid": item["sid"],
                        "utxo": item["utxo"],
                        "owner_memo": item.get("owner_memo", None),
                        "memo_data": item.get("memo_data", None),
                })
            break


    return result


def add_utxo_inputs(utxo_sids: list) -> list:
    """
    Create list of inputs to be used for the transaction builder.

    Parameters
        utxo_sids:list

    Return
        result:list
    """

    input_amount = float(0)
    input_parameters_list = []
    for utxo in utxo_sids:
        input_amount += float(utxo["origin_amount"])
        # TODO: don't know how to generate a ClientAssetRecord object
        asset_record = ledger.ClientAssetRecord.from_json(utxo["utxo"])
        # TODO: don't know how to generate this TxoRef works
        txo_ref = ledger.TxoRef.absolute()

        params = {
            "txo_ref": txo_ref,
            "asset_record": asset_record,
            "owner_memo": utxo.get("owner_memo", None),
            "amount": utxo["amount"],
            "memo_data": utxo.get("memo_data", None),
            "sid": utxo["sid"],
        }
        input_parameters_list.append(params)

    result = {
        "input_parameters_list": input_parameters_list,
        "input_amount": input_amount,
    }

    return result
