from bs4 import BeautifulSoup


def read_xml(xml_file: str):

    with open(xml_file, 'r') as f:
        data = f.read()

    # ! Passo il contenuto del file al parser "beautifulsoup"
    Bs_data = BeautifulSoup(data, "xml")

    # ! Trovo i tag con il nome "nomi", il metodo sotto arriva
    # ! anche ai sotto-livelli
    b_nomi = Bs_data.find_all('nomi')

    for nome in b_nomi:
        print(nome)

    # print(b_nomi)

    # ! Cerco un tag che si chiama "nome" e che ha un attributo
    # ! che si chiama "soprannome" e il cui valore e' "Frank"
    b_name = Bs_data.find('nome', {'soprannome': 'Frank'})

    if b_name is not None:
        # ! Se ho trovato il tag prendo il valore di un altro attributo (eta)
        # ! e lo stampo
        value = b_name.get('eta')
        print(value)


if __name__ == '__main__':
    read_xml("test.xml")
