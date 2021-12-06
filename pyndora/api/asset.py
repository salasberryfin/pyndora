from pyndora.sdk import Sdk
from pyndora.api import network
from pyndora.services import conversion


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
    # import pdb;pdb.set_trace()

    pass


def get_minimal_fee() -> float:
    """
    Get minimal fee for transaction.

    Parameters
        No input parameters

    Return
        Return
    """

    # TODO: this is retrieved from js-wasm
    # hardcode it for now

    default_value = float("0.01")
    fee = conversion.to_wei(default_value)

    return fee


def get_fra_public_key():
    """
    Get FRA public key.

    Parameters
        No input parameters

    Return
        Return
    """

    # TODO: this is retrieved from js-wasm
    # hardcode it for now
    pub_key = ""

    return pub_key
