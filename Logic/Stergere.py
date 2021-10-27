from Domain.cheltuieli import get_numar_apartament


def stergere_cheltuieli(cheltuieli, numar_apartament):
    """ Șterge prima cheltuială pe care o gasește. """
    index = 0
    for elem in cheltuieli:
        if numar_apartament == get_numar_apartament(elem):
            cheltuieli.pop(index)
            break
        index += 1

    return cheltuieli


def stergere_totala_cheltuieli_camera(cheltuieli, numar_apartament):
    """ Șterge toate cheltuielile pe care le găsește cu același număr de apartament. """
    for elem in cheltuieli:
        if numar_apartament == get_numar_apartament(elem):
            stergere_cheltuieli(cheltuieli, numar_apartament)
            stergere_totala_cheltuieli_camera(cheltuieli, numar_apartament)

    return cheltuieli
