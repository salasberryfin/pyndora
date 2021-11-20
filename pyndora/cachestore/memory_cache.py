from pyndora.cachestore.cache import CacheItem, CacheProvider

class MemoryCache():

    @classmethod
    def data(self):
        return CacheItem()

def read_cache(filename):
    cache_data = MemoryCache.data().value[filename]

    return cache_data

def write_cache(filename, data):
    """
    :param  filename:str    key id of CacheItem
    :param  data:CacheItem  new value for the CacheItem

    :return bool    True after updating value
    """

    MemoryCache.data().value[filename] = data

    return True

# Memory Cache Provider
memory_cache_provider = CacheProvider(
    entry_name = "test",
    read = read_cache,
    write = write_cache,
)

