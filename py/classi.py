#
# fff Import
#

from dataclasses import dataclass
from decimal import Decimal

from .libfunz import string2dec

#
# fff Classi
#


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
        self.imp_distinta_dec = string2dec(self.imp_distinta)
