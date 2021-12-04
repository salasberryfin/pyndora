TO_WEI = 1e6


def to_wei(value: float, precision: int = 6) -> str:
    """
    Converts to WEI.

    Parameters
        value:int       value to convert
        precision:int   precision digits

    Return
        wei:str     wei conversion
    """

    wei_scientific = value * TO_WEI
    wei = format(wei_scientific, f".{precision}f")

    return wei


def from_wei(value: float, precision: int = 6) -> str:
    """
    Converts WEI.

    Parameters
        value:int       value to convert
        precision:int   precision digits

    Return
        eth:str     eth conversion
    """

    eth_scientific = value / TO_WEI
    eth = format(eth_scientific, f".{precision}f")

    return eth
