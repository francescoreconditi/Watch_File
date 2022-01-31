from dataclasses import dataclass
from decimal import Decimal

from .const import SEP_DECIMALI, SEP_DECIMALI_STR


@dataclass()
class Distinta():
    esercizio: str
    cod_grp_tipo_pag: str
    n_distinta: str
    cod_banca: str
    des_banca: str
    cod_fornitore: str
    des_fornitore: str
    imp_distinta: str

    # ! Campi decimal
    imp_distinta_dec: Decimal = Decimal("0")

    def __post_init__(self) -> None:
        """Metodo chiamato DOPO l' "__init__" (autodichiarato)
        """
        # ! Converto le variabili "stringhe" in "Decimal"
        self.imp_distinta_dec = Distinta.string2dec(self.imp_distinta)

    @ staticmethod
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

    @staticmethod
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
