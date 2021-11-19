from pyndora.cachestore.cache import CacheItem, CacheProvider

class Factory:

    def read(entry_name: str, provider: CacheProvider):
        """
        """
        return provider.read(entry_name)

    def write(entry_name: str, data: CacheItem, provider: CacheProvider):
        """
        """
        provider.write(entry_name, data)

    def prune(provider: CacheProvider):
        """
        """
        provider.prune()

        return True
