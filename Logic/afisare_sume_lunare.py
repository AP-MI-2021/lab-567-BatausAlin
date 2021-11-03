from Domain.cheltuieli import *


def afisare_sume_lunare(listele):
    dictionary = {}

    for elem in listele:
        data = str(get_data(elem))
        data_split = data.split('.')
        if data_split[1] in dictionary:
            dictionary[data_split[1]] += float(get_suma(elem))
        else:
            dictionary[data_split[1]] = float(get_suma(elem))

    return dictionary


lista = [{"id": '1', 'numar_apartament': '12', 'suma': '1', 'data': '11.5.2002', 'tip': 'canal'},
         {"id": '2', 'numar_apartament': '7', 'suma': '1', 'data': '11.1.2002', 'tip': 'intretinere'},
         {"id": '3', 'numar_apartament': '12', 'suma': '1', 'data': '11.7.2002', 'tip': 'alte cheltuieli'},
         {"id": '4', 'numar_apartament': '8', 'suma': '1', 'data': '11.2.2002', 'tip': 'canal'},
         {"id": '5', 'numar_apartament': '12', 'suma': '1', 'data': '11.3.2002', 'tip': 'alte cheltuieli'}]

print(afisare_sume_lunare(lista))
