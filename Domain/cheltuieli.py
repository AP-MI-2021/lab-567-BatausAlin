def creare_cheltuiala(numar_apartament, suma, data, tip):
    return {
        "numar_apartament": numar_apartament,
        "suma": suma,
        "data": data,
        "tip": tip
    }


def get_numar_apartament(cheltuiala):
    return cheltuiala['numar_apartament']


def get_suma(cheltuiala):
    return cheltuiala['suma']


def get_data(cheltuiala):
    return cheltuiala['data']


def get_tip_apartament(cheltuiala):
    return cheltuiala['tip']


def set_numar_apartament(lista, numar_apartament):
    lista['numar_apartament'] = numar_apartament


def set_suma(lista, suma):
    lista['suma'] = suma


def set_data(lista, data):
    lista['data'] = data


def set_tip_apartament(lista, tip_apartament):
    lista['tip'] = tip_apartament


def to_string(cheltuiala):
    return f'Numar apartament = {get_numar_apartament(cheltuiala)}, Suma = {get_suma(cheltuiala)}, Data = {get_data(cheltuiala)}, Tip apartament = {get_tip_apartament(cheltuiala)}'
