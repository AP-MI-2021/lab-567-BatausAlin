from Domain.cheltuieli import get_data, get_suma, set_suma
from Domain.lista_undo_redo import adaugare_lista_undo_and_clear_redo, get_lista_curenta


def check_data(the_list, data):
    """
    Verifică dacă există data.
    :param the_list: lista
    :param data: data
    :return:
    """
    lista_curenta = get_lista_curenta(the_list)
    for elem in lista_curenta:
        if get_data(elem) == data:
            return elem


def adunare_valoare(the_list, data, valoarea):
    """
    Adunare suma la o dată specificată.
    :param the_list: lista
    :param data: data
    :param valoarea: suma
    :return:
    """
    if check_data(the_list, data) is None:
        raise ValueError("Data nu există!")

    adaugare_lista_undo_and_clear_redo(the_list)
    lista_curenta = get_lista_curenta(the_list)

    for elem in lista_curenta:
        if get_data(elem) == data:
            suma_noua = str(float(get_suma(elem)) + float(valoarea))
            set_suma(elem, suma_noua)
