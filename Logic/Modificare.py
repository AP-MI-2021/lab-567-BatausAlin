from Domain.cheltuieli import get_numar_apartament
from Domain.cheltuieli import set_suma, set_data, set_tip_apartament

def modificare_cheltuieli(cheltuieli, numar_apartament, suma, data, tip):
    """ Modifică prima cheltuială pe care o găsește cu același număr de apartament. """
    for elem in cheltuieli:
        if numar_apartament == get_numar_apartament(elem):
            set_suma(elem, suma)
            set_data(elem, data)
            set_tip_apartament(elem, tip)

    return cheltuieli
