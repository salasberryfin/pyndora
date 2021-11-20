"""
Some test methods I use for development.

THESE ARE NOT FORMAL TESTS, just a playground exceution to
detect errors and check progress
"""

from pyndora import session
from pyndora.cachestore import memory_cache as memcache
from pyndora.api.keypair import keypair
from pyndora.utils.crypto import wallet


def create_session(env):
    print(f"Environment configuration is: {env}")
    sdk_session = session.Session(
        host_url=env["host_url"],
        cache_provider=env["cache_provider"],
        cache_path=env["cache_path"],
    )

    return sdk_session

def create_memcache_provider():
    cache = memcache.memory_cache_provider

    return cache

def create_wallet_key_pair():
    password = "123"
    mnemonic = keypair.get_mnemonic(length=24, lang="english")
    # TODO
    wallet_info = keypair.restore_from_mnemonic(mnemonic, password)

    return wallet_info

if __name__ == "__main__":
    memory_cache_provider = create_memcache_provider()

    new_session = create_session({
        "host_url": "https://prod-forge.prod.findora.org",
        "cache_provider": memory_cache_provider,
        "cache_path": "./cache",
    })

    new_key_pair = wallet.new_keypair()

    wallet_info = create_wallet_key_pair()

