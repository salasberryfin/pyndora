"""
Some test methods I use for development.

THESE ARE NOT FORMAL TESTS, just a playground exceution to
detect errors and check progress
"""

from pyndora import session
from pyndora.cachestore import memory_cache as memcache


def create_session(env):
    print(f"Environment configuration is: {env}")
    print(f"Host url: {env['host_url']}")
    sdk_session = session.Session(
        host_url=env["host_url"],
        cache_provider=env["cache_provider"],
        cache_path=env["cache_path"],
    )

    return sdk_session

def create_memcache_provider():
    cache = memcache.memory_cache_provider

    return cache

if __name__ == "__main__":
    memory_cache_provider = create_memcache_provider()

    new_session = create_session({
        "host_url": "https://prod-forge.prod.findora.org",
        "cache_provider": memory_cache_provider,
        "cache_path": "./cache",
    })
