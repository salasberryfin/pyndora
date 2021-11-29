from pyndora.api.keypair.keypair import WalletKeypar
from pyndora.cachestore.cache import (
    CacheItem,
    CacheFactory,
)
from pyndora.api.network.network import Network

from pyndora.sdk import Sdk


def get_utxo_item(sid: int, wallet_info: WalletKeypar, cached_item):
    """
    Method description

    Parameters
        Arg1:

    Return
        Return
    """
    if cached_item:
        return cached_item
    net = Network(Sdk().environment)

    print(f"Fetching sid {sid}")
    utxo_data_result = net.get_utxo(sid)

    pass


def add_utxo(wallet_info: WalletKeypar, sids):
    """
    Method description

    Parameters
        Arg1:

    Return
        Return
    """
    sdk_config = Sdk()
    cache_data_to_save = CacheItem({})

    # TODO: cache_entries.utxo_data
    cache_entry_name = f"cache_entries.utxo_data_{wallet_info.address}"
    full_path = f"{sdk_config.environment['cache_path']}/{cache_entry_name}.json"
    # import pdb; pdb.set_trace()
    try:
        utxo_data_cache = CacheFactory.read(
            entry_name=full_path,
            provider=sdk_config.environment["provider"],
        )
    except:
        print("Error reading the cache.")

    # for sid in sids:
    #     item = get_utxo_item(sid, wallet_info, utxo_data_cache[f"sid_{sid}"])

    pass
