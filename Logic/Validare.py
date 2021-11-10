def return_type_of_room(tip):
    return tip == 'Intretinere' or tip == 'intretinere' or tip == 'canal' or tip == 'Canal' or tip == 'Alte cheltuieli' or tip == 'alte cheltuieli'


def validare_inputs(id, numar_apartament, suma, data, tip):
    """
    Validare inputs
    :param id: id
    :param numar_apartament: numar apartament
    :param suma: suma
    :param data: data
    :param tip: tip
    :return:
    """
    errors = []
    if id == '':
        errors.append('Id-ul nu poate fi vid.')
    if numar_apartament == '':
        errors.append('Numele apartamentului nu poate fi vid.')
    if suma == '':
        errors.append('Suma nu poate fi vidă.')
    if data == '':
        errors.append('Data nu poate fi vidă.')
    if tip == '':
        errors.append('Tipul nu poate fi vid.')

    try:
        numar_apartament = int(numar_apartament)
        if numar_apartament <= 0:
            errors.append('Numărul de la apartament incepe de la 1.')
    except ValueError:
        errors.append('Numărul de la apartament trebuie sa fie un numar întreg.')

    try:
        suma = float(suma)
        if suma < 0:
            errors.append('Suma trebuie sa fie un numar pozitiv.')
    except ValueError:
        errors.append('Suma trebuie sa fie un numar real pozitiv.')

    try:
        if not return_type_of_room(tip):
            errors.append('Tipul camerei poate fi ( întreținere, canal sau alte cheltuieli ).')
    except ValueError:
        errors.append('Tipul camerei trebuie sa fie un string.')

    if len(errors) != 0:
        raise ValueError(errors)

    return id, str(numar_apartament), suma, data, tip

def validare_numar_apartament(numar_apartament):
    """
    Validare număr apartament.
    :param numar_apartament: numărul de la apartament.
    :return:
    """
    errors = []
    numar_apartament = str(numar_apartament)
    if numar_apartament == '':
        errors.append('Numărul apartamentului nu poate fi vid.')

    letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
               'b', 'v', 'c', 'x', 'z', '[', '{', ']', '}', '.', ',', '/', '\\', '?', '!', '@', '#', '$', '%', '^', '&',
               '*', '(', ')', '_', '-', '+', '=', '|', '>', '<']

    for i in letters:
        if numar_apartament.find(f'{i}') != -1:
            errors.append('Numărul apartamentului trebuie sa conțină doar cifre.')
            break

    if len(errors) != 0:
        raise ValueError(errors)
