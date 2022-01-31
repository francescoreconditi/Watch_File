#
# fff Import
#

from decimal import Decimal

from .const import SEP_DECIMALI, SEP_DECIMALI_STR

#
# fff Funzioni
#


def string2dec(stringa: str) -> Decimal:
    """Conversione da Stringa a Decimal

    Args:
        stringa (str): Stringa da convertire

    Returns:
        Decimal: Decimal convertito
    """
    # ! Per il momento prendo per buono, come separatore dei decimali, SEP_DECIMALI
    stringa = stringa.replace(SEP_DECIMALI_STR, SEP_DECIMALI)

    wk_stringa: str = ""

    for char in stringa:
        if char in "-0123456789" + SEP_DECIMALI:
            wk_stringa = wk_stringa + char

    # ! Converto e ritorno la stringa
    return Decimal(wk_stringa if wk_stringa else "0")


def dec2string(numero: Decimal) -> str:
    """Converte un "Decimal" in una stringa

    Args:
        numero (Decimal): Valore da convertire

    Returns:
        str: Valore convertito
    """

    # ! Formatto con due decimali
    stringa = f"{numero:>.2f}"

    # ! Sistemo il separatore
    stringa = stringa.replace(SEP_DECIMALI, SEP_DECIMALI_STR)

    return stringa
