from pyndora.cachestore.cache import (
    CacheItem,
    CacheFactory,
    CacheProvider,
)

from pyndora.cachestore.config import CacheEntries

default_env = {
    "host_url": 'https://dev-evm.dev.findora.org',
    "query_port": '8667',
    "ledger_port": '8668',
    "submission_port": '8669',
    "explorer_api_port": '26657',
    "cache_provider": CacheProvider(),
    "cache_path": './cache',
}


class Sdk:
    """
    Holds the SDK session configuration.

    """
    __instance = None

    def __new__(cls):
        """
        Only one instance of the Sdk class is allowed per session.
        This instance can later be modified.
        """
        if cls.__instance is None:
            print("Initializing Sdk environment.")
            cls.__instance = super(Sdk, cls).__new__(cls)

        return cls.__instance

    def init(self, sdk_env: dict):
        """
        Initialize SDK environment with default values if
        not specified.

        Parameters
            sdk_env:dict    SDK configuration
        """
        self.environment = {**default_env, **sdk_env}

    def reset(self):
        """
        Reset SDK environment to default values.
        """
        self.environment = default_env

    def set_utxo_data(self, wallet_addr: str, utxo_cache: dict):
        """

        Parameters
            wallet_addr:str  address of the Findora wallet
            utxo_cache:[]CacheItem list of CacheItems
        """

        cache_data_to_save = CacheItem()
        for item in utxo_cache:
            cache_data_to_save[f"sid_{item.sid}"] = item

        CacheFactory.write(
            f"{CacheEntries.UTXO_DATA.value}_{wallet_addr}",
            cache_data_to_save,
            self.environment.cache_provider,
        )

        return True
