from pyndora.cachestore.factory import Factory
from pyndora.cachestore.cache import CacheItem
from pyndora.cachestore import memory_cache as memcache

default_env = {
    "host_url": 'https://dev-evm.dev.findora.org',
    "query_port": '8667',
    "ledger_port": '8668',
    "submission_port": '8669',
    "explorer_api_port": '26657',
    "cache_provider": memcache.memory_cache_provider,
    "cache_path": './cache',
}


class Session:
    """
    Session holds the SDK configuration.

    """

    def __init__(self, sdk_env):
        """
        Initialize SDK environment with default values if
        not specified.
        """
        self.environment = {**default_env, **sdk_env}

    def reset(self):
        """
        Reset SDK environment to default values.
        """
        self.environment = default_env

    def set_utxo_data(self, wallet_addr: str, utxo_cache: CacheItem):
        """
        :param  wallet_addr:str address of the Findora wallet
        :param  utxo_cache:[]CacheItem list of CacheItems
        """

        cache_data_to_save = CacheItem()
        for item in utxo_cache:
            cache_data_to_save[f"sid_{item.sid}"] = item

        # TODO: define cache_entries? /src/config/cache.ts
        cache_entries = {
            "utxo_data": "utxo_data_cache",
        }
        Factory.write(
            f"{cache_entries.utxo_data}_{wallet_addr}",
            cache_data_to_save,
            self.environment.cache_provider,
        )

        return True
