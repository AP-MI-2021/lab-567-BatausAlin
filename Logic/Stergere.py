from Domain.cheltuieli import get_numar_apartament
from Domain.lista_undo_redo import adaugare_lista_undo_and_clear_redo

from Domain.lista_undo_redo import get_lista_curenta

def find_prajitura(cheltuieli, numar_apartament):
    '''
    Find prajitura in prajituri with id
    If not found, we return None
    :param prajituri:
    :param id:
    :return:
    '''
    for elem in cheltuieli:
        if get_numar_apartament(elem) == numar_apartament:
            return elem
    return None

def stergere_cheltuieli_v2(cheltuieli, numar_apartament):
    """ Șterge prima cheltuială pe care o gasește. """
    index = 0
    for elem in cheltuieli:
        if get_numar_apartament(elem) == numar_apartament:
            cheltuieli.pop(index)
            break
        index += 1



def stergere_cheltuieli(cheltuieli, numar_apartament):
    """ Șterge prima cheltuială pe care o gasește. """

    adaugare_lista_undo_and_clear_redo(cheltuieli)

    get_lista = get_lista_curenta(cheltuieli)

    index = 0
    for elem in get_lista:
        if get_numar_apartament(elem) == numar_apartament:
            get_lista.pop(index)
            break
        index += 1



def stergere_totala_cheltuieli_camera(cheltuieli, numar_apartament):
    """ Șterge toate cheltuielile pe care le găsește cu același număr de apartament. """

    adaugare_lista_undo_and_clear_redo(cheltuieli)
    get_lista = get_lista_curenta(cheltuieli)


    stop = True

    while stop:
        stop = False
        for elem in get_lista:
            if numar_apartament == get_numar_apartament(elem):
                stergere_cheltuieli_v2(get_lista, numar_apartament)
                stop = True
                # stergere_totala_cheltuieli_camera(cheltuieli, numar_apartament)

