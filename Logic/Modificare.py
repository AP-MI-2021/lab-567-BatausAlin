from Domain.cheltuieli import get_numar_apartament
from Domain.cheltuieli import set_suma, set_data, set_tip_apartament, set_id


def modificare_cheltuieli(cheltuieli, id_ul, numar_apartament, suma, data, tip):
    """ Modifică prima cheltuială pe care o găsește cu același număr de apartament. """
    for elem in cheltuieli:
        if numar_apartament == get_numar_apartament(elem):
            set_id(elem, id_ul)
            set_suma(elem, suma)
            set_data(elem, data)
            set_tip_apartament(elem, tip)

    return cheltuieli
