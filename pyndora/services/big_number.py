ETH_TO_WEI = 1e18


def eth_to_wei(value: float, precision: int = 6) -> str:
    """
    Converts ETH to WEI.

    Parameters
        value:int   eth value to convert
        precision:int   precision digits

    Return
        wei:str     wei conversion
    """

    wei_scientific = value * ETH_TO_WEI
    wei = format(wei_scientific, f".{precision}f")

    return wei


def wei_to_eth(value: float, precision: int = 6) -> str:
    """
    Converts WEI to ETH.

    Parameters
        value:int   eth value to convert
        precision:int   precision digits

    Return
        eth:str     eth conversion
    """

    eth_scientific = value / ETH_TO_WEI
    eth = format(eth_scientific, f".{precision}f")

    return eth
