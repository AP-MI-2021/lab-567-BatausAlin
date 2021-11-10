from Domain.lista_undo_redo import get_lista_redo, get_lista_undo, adaugare_lista_redo, \
    set_lista_curenta, adaugare_lista_undo


def apply_undo(cheltuieli):
    """
    Aici aplicăm undo-ul
    :param cheltuieli: cheltuieli
    :return:
    undo: []
    curenta: []
    undo: 1, 2, 3
    curenta: 1
    """
    lista_undo = get_lista_undo(cheltuieli)
    if len(lista_undo) > 1:
        adaugare_lista_redo(cheltuieli)
        prior_lista_curenta = lista_undo.pop()
        set_lista_curenta(cheltuieli, prior_lista_curenta)
    else:
        set_lista_curenta(cheltuieli, [])


def apply_redo(cheltuieli):
    """
    Aici aplicam redo-ul
    :param cheltuieli:
    :return:
    """
    lista_redo = get_lista_redo(cheltuieli)
    if len(lista_redo) > 0:
        adaugare_lista_undo(cheltuieli)
        new_current_list = lista_redo.pop()
        set_lista_curenta(cheltuieli, new_current_list)
