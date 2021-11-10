from Domain.cheltuieli import get_numar_apartament
from Domain.cheltuieli import set_suma, set_data, set_tip_apartament, set_id
from Domain.lista_undo_redo import adaugare_lista_undo_and_clear_redo, get_lista_curenta
from Logic.Validare import validare_inputs


def modificare_cheltuieli(cheltuieli, id_ul, numar_apartament, suma, data, tip):
    """ Modifică prima cheltuială pe care o găsește cu același număr de apartament. """

    adaugare_lista_undo_and_clear_redo(cheltuieli)
    id_ul, nr_apartament, suna, data, tip = validare_inputs(id_ul, numar_apartament, suma, data, tip)

    lista_curenta = get_lista_curenta(cheltuieli)

    for elem in lista_curenta:
        if numar_apartament == get_numar_apartament(elem):
            set_id(elem, id_ul)
            set_suma(elem, suma)
            set_data(elem, data)
            set_tip_apartament(elem, tip)

