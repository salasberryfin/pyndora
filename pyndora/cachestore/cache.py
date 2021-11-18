""" Original SDK

    export interface CacheItem {
      [key: string]: any;
    }

    export interface CacheFactory {
      read<T extends CacheProvider>(entryName: string, provider: T): Promise<CacheItem>;
      write<T extends CacheProvider>(entryName: string, data: CacheItem, provider: T): Promise<boolean>;
      prune<T extends CacheProvider>(provider: T): Promise<boolean>;
    }

"""

class CacheItem:

    def __init__(self):
        self.value = {
            "key": "value",
        } 


class CacheProvider():
    """
    export interface CacheProvider {
      read(entryName: string): Promise<CacheItem>;
      write(entryName: string, data: CacheItem): Promise<boolean>;
      prune?(): Promise<boolean>;
    }
    """

    def __init__(self, read, write):
        # self.name = entry_name 
        self.read = read
        self.write = write


class CacheFactory(CacheProvider):

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

