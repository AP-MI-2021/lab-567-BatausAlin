from copy import deepcopy


def create_cheltuieli():
    return {
        'listaCurenta': [],
        'listaUndo': [[]],
        'listaRedo': []
    }


def get_lista_curenta(cheltuieli):
    return cheltuieli['listaCurenta']


def get_lista_undo(cheltuieli):
    return cheltuieli['listaUndo']


def get_lista_redo(cheltuieli):
    return cheltuieli['listaRedo']


def set_lista_curenta(cheltuieli, newCurrentList):
    cheltuieli['listaCurenta'] = newCurrentList


def adaugare_lista_undo(cheltuieli):
    listaCurenta = get_lista_curenta(cheltuieli)
    get_lista_undo(cheltuieli).append(deepcopy(listaCurenta))


# functia se va apela pentru operatiile care modifica listaCurenta
def adaugare_lista_undo_and_clear_redo(cheltuieli):
    adaugare_lista_undo(cheltuieli)
    clear_redo(cheltuieli)


def adaugare_lista_redo(cheltuieli):
    listaCurenta = get_lista_curenta(cheltuieli)
    get_lista_redo(cheltuieli).append(deepcopy(listaCurenta))


def clear_redo(cheltuieli):
    get_lista_redo(cheltuieli).clear()
