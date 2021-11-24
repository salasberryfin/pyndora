class MemoryCache():

    @classmethod
    def data(self):
        return CacheItem()


class CacheItem:
    """
    """

    def __init__(self, value: str):
        self.value = {
            "key": value,
        }


class CacheProvider():
    """
    """

    def read(self, entry_name: str) -> CacheItem:
        cache_data = MemoryCache.data().value[entry_name]

        return cache_data

    def write(self, entry_name: str, data: CacheItem):
        """
        :param  entry_name:str    key id of CacheItem
        :param  data:CacheItem  new value for the CacheItem

        :return bool    True after updating value
        """

        MemoryCache.data().value[entry_name] = data

        return True


class CacheFactory(CacheProvider):
    """
    Inherits from CacheProvider
    """

    def __init__(self, entry_name: str, provider: CacheProvider):
        self.entry_name = entry_name
        self.provider = provider

    def read(self, entry_name: str, provider: CacheProvider) -> CacheItem:
        return provider.read(entry_name)

    def write(self, entry_name: str, data: CacheItem, provider: CacheProvider):
        """
        :param  entry_name:str    key id of CacheItem
        :param  data:CacheItem  new value for the CacheItem

        :return bool    True after updating value
        """
        provider.write(entry_name, data)

        return True


# Memory Cache Provider
memory_cache_provider = CacheProvider(
    entry_name="test",
)
