import xml.etree.ElementTree as ET

from .classi import Distinta

# ! Campi dalla Testata
key_testa = {"EseCont/CodEsercizioContabile": "",
             "TabGrpTipoPag/CodGruppoTipologiePagamento": "",
             "NumeroDistinta": "",
             "CodiceContobanca/CodContoContabile": "",
             "CodiceContobanca/Descrizione1": "",
             }

# ! Campi dalle righe
key_righe = {"ContoContabile/CodContoContabile": [],
             "ContoContabile/Descrizione1": [],
             "ImportoBonifico": []
             }

# ! "relazioni" campi
dict_campi = {"esercizio": "EseCont/CodEsercizioContabile",
              "cod_grp_tipo_pag": "TabGrpTipoPag/CodGruppoTipologiePagamento",
              "n_distinta": "NumeroDistinta",
              "cod_banca": "CodiceContobanca/CodContoContabile",
              "des_banca": "CodiceContobanca/Descrizione1",
              "cod_fornitore": "ContoContabile/CodContoContabile",
              "des_fornitore": "ContoContabile/Descrizione1",
              "imp_distinta": "ImportoBonifico"
              }


def check_xml_distinta(path_file: str):

    # ! "albero" XML ...
    tree = ET.parse(path_file)

    # ! ... e tag "root"
    tag_root = tree.getroot()

    # ! Tag Principale
    tag_stampa = tag_root.find("StampaDistintaBonifici/StrutturaDistintaBonifici")

    # ! Lista Distinte
    distinte = []

    for distinta in tag_stampa.findall("TestaDistintaBonifici"):

        # ! Nuova distinta

        # ! Campi della Testa
        for key_t in key_testa:
            key_testa[key_t] = distinta.find(key_t).text

        # ! Scorro le righe
        for riga in distinta.findall("RighiDistinta/RigoDistintaBonifici"):
            for key_r in key_righe:
                key_righe[key_r].append(riga.find(key_r).text)

        # ! Distinta scorsa, "riscorro" le righe (la testata e' 1, le righe da 1 a N)
        # : sotto uso "range(0,len(...))", l' indice inizia da 0 e appena arriva a "len" esce
        for n_riga in range(0, len(key_righe[dict_campi["cod_fornitore"]])):
            distinte.append(Distinta(key_testa[dict_campi["esercizio"]],
                                     key_testa[dict_campi["cod_grp_tipo_pag"]],
                                     key_testa[dict_campi["n_distinta"]],
                                     key_testa[dict_campi["cod_banca"]],
                                     key_testa[dict_campi["des_banca"]],
                                     key_righe[dict_campi["cod_fornitore"]][n_riga],
                                     key_righe[dict_campi["des_fornitore"]][n_riga],
                                     key_righe[dict_campi["imp_distinta"]][n_riga]
                                     ))


if __name__ == '__main__':
    check_xml_distinta("c:\\temp\\origine\\xml\\g.luglioli_05806_772.xml")
