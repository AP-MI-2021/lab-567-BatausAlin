from Domain.cheltuieli import get_tip_apartament, get_suma
from Domain.lista_undo_redo import adaugare_lista_undo_and_clear_redo, get_lista_curenta


def determinare_max_cheltuieli_pentru_fiecare_tip_de_cheltuieli(cheltuieli):
    """
        Determină maximul cheltuielilor pe fiecare tip de de cheltuială.
        :return: o lista cu valorile
    """
    max_canal = 0
    max_intretinere = 0
    max_alte_cheltuieli = 0

    adaugare_lista_undo_and_clear_redo(cheltuieli)
    lista_curenta = get_lista_curenta(cheltuieli)

    for elem in lista_curenta:
        if get_tip_apartament(elem) == "Intretinere" or get_tip_apartament(elem) == "intretinere":
            if float(get_suma(elem)) > max_intretinere:
                max_intretinere = float(get_suma(elem))
        elif get_tip_apartament(elem) == "Canal" or get_tip_apartament(elem) == "canal":
            if float(get_suma(elem)) > max_canal:
                max_canal = float(get_suma(elem))
        elif get_tip_apartament(elem) == "Alte cheltuieli" or get_tip_apartament(elem) == "alte cheltuieli":
            if float(get_suma(elem)) > max_alte_cheltuieli:
                max_alte_cheltuieli = float(get_suma(elem))

    return [max_intretinere, max_canal, max_alte_cheltuieli]
