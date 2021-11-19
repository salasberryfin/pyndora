class CacheItem:
    """
    """

    def __init__(self):
        self.value = {
            "key": "value",
        }


class CacheProvider():
    """
    """

    def __init__(self, entry_name, read, write):
        self.name = entry_name 
        self.read = read
        self.write = write


class CacheFactory(CacheProvider):
    """
    """

    def __init__(self, entry_name):
        self.name = entry_name 

    def read(self):
        super().read()
        return self.name

    def write(self):
        super().write()
        return self.name

    def prune(self):
        super().prune()
        return self.name

