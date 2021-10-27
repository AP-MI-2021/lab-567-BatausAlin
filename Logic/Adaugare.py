from Domain.cheltuieli import creare_cheltuiala


def adaugare_cheltuieli(cheltuieli, nr_apartament, suma, data, tip):
    """
    Adaugăm în memorie proprietari
    :param cheltuieli: lista de proprietari
    :param nr_apartament: string
    :param suma: float
    :param data: string
    :param tip: string
    :return:
    """
    cheltuiala = creare_cheltuiala(nr_apartament, suma, data, tip)
    cheltuieli.append(cheltuiala)
    return cheltuieli
