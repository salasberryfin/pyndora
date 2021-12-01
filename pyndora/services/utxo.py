from pyndora.api.keypair.keypair import WalletKeypar
from pyndora.api.network.network import Network

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

    Parameters
        Arg1:

    Return
        Return
    """

    asset_record = ledger.ClientAssetRecord.from_json(utxo["utxo"])

    owner_memo = memo
    # owner_memo = {}

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
        sid:int     sid id
        wallet_info:WalletKeypar    fra wallet object
        cached_item:dict    cache item

    Return
        item:decrypted item
    """
    sdk_config = Sdk()
    sdk_environment = sdk_config.environment

    if cached_item:
        return cached_item

    net = Network(sdk_environment)

    print(f"Fetching sid {sid}")
    utxo_data = net.get_utxo(sid, {})
    memo_data = net.get_owner_memo(sid, {})

    # import pdb;pdb.set_trace()

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
        print(f"Cache data for '{full_path}' is empty.")

    for sid in sids:
        # TODO: utxo_data_cache.get when no cache entries are found
        # import pdb; pdb.set_trace()
        # utxo_data_sid = utxo_data_cache.get(f"sid_{sid}", None)
        # item = get_utxo_item(sid, wallet_info, utxo_data_sid)
        item = get_utxo_item(sid, wallet_info, {})
        utxo_data.append(item)
        cache_to_save[f"sid_{item['sid']}"] = item

    cache.write(full_path, cache_to_save, sdk_provider)

    # import pdb; pdb.set_trace()

    return utxo_data
