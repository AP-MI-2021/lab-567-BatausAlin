from Domain.cheltuieli import creare_cheltuiala, get_id
from Domain.lista_undo_redo import get_lista_undo, get_lista_redo, get_lista_curenta, adaugare_lista_undo_and_clear_redo
from Logic.Validare import validare_inputs


def find_id(cheltuieli, id_ul):
    """
    Caută id-ul.
    :param cheltuieli: lista
    :param id_ul: id-ul
    :return:
    """
    for cheltuiala in cheltuieli:
        if get_id(cheltuiala) == id_ul:
            return cheltuiala
        return None


def adaugare_cheltuieli(cheltuieli, id_ul, nr_apartament, suma, data, tip):
    """
    Adaugăm în memorie proprietari
    :param id_ul: id-ul
    :param cheltuieli: lista de proprietari
    :param nr_apartament: string
    :param suma: float
    :param data: string
    :param tip: string
    :return:
    """
    adaugare_lista_undo_and_clear_redo(cheltuieli)
    get_cheltuieli_lista = get_lista_curenta(cheltuieli)

    if find_id(get_cheltuieli_lista, id_ul) is not None:
        raise ValueError("ID-ul exista!")

    id_ul, nr_apartament, suna, data, tip = validare_inputs(id_ul, nr_apartament, suma, data, tip)

    cheltuiala = creare_cheltuiala(id_ul, nr_apartament, suma, data, tip)
    get_cheltuieli_lista.append(cheltuiala)
