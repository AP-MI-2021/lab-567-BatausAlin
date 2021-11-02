from Domain.cheltuieli import *


def ordonare_cheltuieli_desc(lista):
    """ Ordonează lista în ordine descrescătoare după sumă. """
    for i in range(0, len(lista)):
        for j in range(i + 1, len(lista)):
            if float(get_suma(lista[i])) < float(get_suma(lista[j])):
                lista[i], lista[j] = lista[j], lista[i]

    return lista
