from Domain.cheltuieli import *
from Domain.lista_undo_redo import adaugare_lista_undo_and_clear_redo, get_lista_curenta


def ordonare_cheltuieli_desc(lista):
    """ Ordonează lista în ordine descrescătoare după sumă. """

    adaugare_lista_undo_and_clear_redo(lista)
    lista_curenta = get_lista_curenta(lista)

    for i in range(0, len(lista_curenta)):
        for j in range(i + 1, len(lista_curenta)):
            if float(get_suma(lista_curenta[i])) < float(get_suma(lista_curenta[j])):
                lista_curenta[i], lista_curenta[j] = lista_curenta[j], lista_curenta[i]

    return lista_curenta