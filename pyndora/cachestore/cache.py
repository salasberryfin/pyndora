class CacheItem:
    """
    Basic cache object: key/value dictionary.
    """
    data = dict()


class CacheProvider(CacheItem):
    """
    Provider for Cache interaction: read/write
    Each CacheProvider object inherits from CacheItem
    for key:value cache storage.
    """

    def read(self, entry_name: str):
        """
        Read cache item identified by dictionary key.

        Params
            entry_name:str  dictionary key

        Return
            cache_data:cache_item value
        """

        cache_data = self.data.get(entry_name, None)

        return cache_data

    def write(self, entry_name: str, data) -> bool:
        """
        Write cache item to the specified dictionary key.

        Params
            entry_name:str  dictionary key
            data:any        item value

        Return
            bool    True if data was added
        """

        self.data[entry_name] = data

        return True


class CacheFactory:
    """
    Wrapper for a cache interaction with the given CacheProvider.
    """

    def read(self, entry_name: str,
             provider: CacheProvider) -> dict:
        """
        Read cache item identified by dictionary key with given provider.

        Params
            entry_name:str          dictionary key
            provider:CacheProvider

        Return
            cache_data:cache_item value
        """

        cache_data = provider.read(entry_name)

        return cache_data

    def write(self, entry_name: str, data: dict,
              provider: CacheProvider) -> bool:
        """
        Write cache item to the specified dictionary key with given provider.

        Params
            entry_name:str  dictionary key
            data:any        item value
            provider:CacheProvider

        Return
            bool    True if data was added
        """

        provider.write(entry_name, data)

        return True
