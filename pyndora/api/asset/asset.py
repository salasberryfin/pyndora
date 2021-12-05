from pyndora.sdk import Sdk
from pyndora.api.network import network


def get_fra_asset_code() -> str:
    """
    Returns FRA asset code

    Parameters
        No input parameters

    Return
        asset_code:str
    """
    # TODO: don't know how this is generated (wasm)
    # so, for now, I hardcode it to only allow FRA assets
    asset_code = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="

    return asset_code


def get_asset_details(asset_code: str):
    """
    Return details for given asset code

    Parameters
        asset_code:str  asset code

    Return
        Return
    """

    # TODO: add support for different assets
    net = network.Network(Sdk().environment)
    details = net.get_asset_token(asset_code)

    pass


def get_minimal_fee():
    """
    Get minimal fee for transaction.

    Parameters
        No input parameters

    Return
        Return
    """

    pass


def get_fra_public_key():
    """
    Get FRA public key.

    Parameters
        No input parameters

    Return
        Return
    """

    pass
