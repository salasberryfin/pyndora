class MemoryCache():

    @classmethod
    def data(self):
        return CacheItem()


class CacheItem:
    """
    Cache Item
    """

    def __init__(self, item: dict):
        self.value = item


class CacheProvider():
    """
    """

    def read(self, entry_name: str) -> CacheItem:
        cache_data = MemoryCache.data().value[entry_name]

        return cache_data

    def write(self, data: CacheItem):
        """
        :param  entry_name:str    key id of CacheItem
        :param  data:CacheItem  new value for the CacheItem

        :return bool    True after updating value
        """

        MemoryCache.data().value[self._entry_name] = data

        return True


class CacheFactory():
    """
    """

    def read(self, entry_name: str, provider: CacheProvider) -> CacheItem:
        """
        Read given entry with provider.

        Parameters
            entry_name:str          key id of CacheItem
            provider:CacheProvider  cache provider object

        Return
            item:CacheItem      read cache item
        """
        # import pdb;pdb.set_trace()
        item = provider.read(entry_name)

        return item

    def write(self, data: CacheItem, provider: CacheProvider):
        """
        :param  entry_name:str    key id of CacheItem
        :param  data:CacheItem  new value for the CacheItem

        :return bool    True after updating value
        """
        provider.write(self._entry_name, data)

        return True


# # Memory Cache Provider
# memory_cache_provider = CacheProvider()
