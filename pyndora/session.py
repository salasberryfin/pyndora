from pyndora.cachestore import memory_cache as memcache
from pyndora.cachestore.cache import CacheItem

default_environment = {
    "host_url": 'https://dev-evm.dev.findora.org',
    "query_port": '8667',
    "ledger_port": '8668',
    "submission_port": '8669',
    "explorer_api_port": '26657',
    # "cache_provider": MemoryCacheProvider,
    "cache_path": './cache',
}

class Session(object):
    """
    Session holds the SDK configuration.

    """


    def __init__(self, host_url='https://dev-evm.dev.findora.org', query_port=8667,
                 ledger_port=8668, submission_port=8669,
                 cache_provider=memcache.memory_cache_provider, cache_path="./cache"):
        """
        Initialize SDK environment with default values if
        not specified.
        """

        self.environment = {
            "host_url": host_url,
            "query_port": query_port,
            "ledger_port": ledger_port,
            "submission_port": submission_port,
            "cache_provider": cache_provider,
            "cache_path": cache_path,
        }

    def reset(self):
        """
        Reset SDK environment to default values.
        """
        self.environment = default_environment 

    def set_utxo_data(self, wallet_adr, utxo_cache):
        """
        :param  wallet_addr:str address of the Findora wallet
        :param  utxo_cache:[]CacheItem lister of CacheItems
        """

        ### TODO
        cache_data_to_save = CacheItem()
        for item in utxo_cache:
            print("do stuff..")


        return True


