"""
Some methods that can be used for testing and development.
"""

from pyndora.sdk import Sdk
from pyndora.cachestore.cache import (
    CacheProvider
)
from pyndora.api import (
    keypair,
    account,
    transaction,
)


def create_session(env):
    print(f"Environment configuration is: {env}")
    sdk = Sdk()
    sdk.init(env)

    return sdk


def create_memcache_provider():
    cache = CacheProvider()

    return cache


def send_fra():
    """
    Send to FRA account

    Parameters
        No input parameters

    Return
        No return
    """

    source_account_mnemonic = ""
    to_addr = "fra1c834rhrxsc659s44gjewu6uxyt0qfmy94a70ef5083uyzxftxjtstqvdf3"

    password = "123"
    wallet_info = keypair.restore_from_mnemonic(
        mnemonic=source_account_mnemonic,
        password=password,
    )

    print(f"""Restored Wallet:\n
          address: {wallet_info.address}
          public_key: {wallet_info.public_key.decode("utf-8")}
          key_store: {wallet_info.key_store}
          key_pair: {wallet_info.key_pair}
          private_str: {wallet_info.private_str.decode("utf-8")}
          """)

    transaction.send_to_address(wallet_info, to_addr, "0.01")

    pass


def get_fra_balance():
    """
    Get FRA balance for wallet restored from mnemonic phrase.

    Parameters
        No input parameters

    Return
        No return
    """
    password = "123"
    mnemonic = ""
    wallet_info = keypair.restore_from_mnemonic(
        mnemonic=mnemonic,
        password=password,
    )

    print(f"""Restored Wallet:\n
          address: {wallet_info.address}
          public_key: {wallet_info.public_key.decode("utf-8")}
          key_store: {wallet_info.key_store}
          key_pair: {wallet_info.key_pair}
          private_str: {wallet_info.private_str.decode("utf-8")}
          """)

    balance = account.get_balance(wallet_info)

    print(f"The balance for address {wallet_info.address} is: {balance}")

    return balance


def create_fra_key_pair_from_mnemonic():
    password = "123"
    mnemonic = keypair.get_mnemonic(length=24, lang="english")
    print(f"Mnemonic phrase: {mnemonic.ToStr()}")
    wallet_info = keypair.restore_from_mnemonic(
        mnemonic=mnemonic.ToStr(),
        password=password,
    )
    print(f"""Wallet:\n
          address: {wallet_info.address}
          public_key: {wallet_info.public_key.decode("utf-8")}
          key_store: {wallet_info.key_store}
          key_pair: {wallet_info.key_pair}
          private_str: {wallet_info.private_str.decode("utf-8")}
          """)

    return wallet_info


def create_fra_key_pair():
    """
    Create new key pair wallet

    Parameters
        No parameters

    Return
        WalletKeypar:   wallet information
    """

    password = "123"
    wallet_info = keypair.create_keypair(password)

    print(f"""Wallet:\n
          address: {wallet_info.address}
          public_key: {wallet_info.public_key.decode("utf-8")}
          key_store: {wallet_info.key_store}
          key_pair: {wallet_info.key_pair}
          private_str: {wallet_info.private_str.decode("utf-8")}
          """)

    return wallet_info


if __name__ == "__main__":
    memory_cache_provider = create_memcache_provider()

    new_session = create_session({
        "host_url": "https://prod-forge.prod.findora.org",
        "cache_provider": memory_cache_provider,
        "cache_path": "./cache",
    })

    # from_mnemonic = create_fra_key_pair_from_mnemonic()
    # wallet_info = create_fra_key_pair()
    get_fra_balance()
    # send_fra()
