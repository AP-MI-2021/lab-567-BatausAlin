from Domain.cheltuieli import *


def afisare_sume_lunare(listele):
    """
    Afisează sumele anuale pe luni.
    :param listele: lista
    :return:
    """
    dictionary = {}

    for elem in listele:
        data = str(get_data(elem))
        data_split = data.split('.')
        # print(data_split[1])
        if f"Apartamentul {get_numar_apartament(elem)} luna {data_split[1]} suma este:" in dictionary:
            dictionary[f"Apartamentul {get_numar_apartament(elem)} luna {data_split[1]} suma este:"] += float(
                get_suma(elem))
        else:
            dictionary[f"Apartamentul {get_numar_apartament(elem)} luna {data_split[1]} suma este:"] = float(
                get_suma(elem))

    return dictionary
